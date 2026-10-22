#!/usr/bin/env python3
"""Per-requirement delivery derived from committed public status manifests.

A status manifest may carry a ``requirements`` array with one entry per
requirement ID. Each entry is validated on its own, with the same evidence
rules the specification-level claim uses, so a percentage is never larger
than the public proof behind it.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Any, Callable

DELIVERED = frozenset({"LANDED", "VERIFIED", "CLOSED"})
IN_PROGRESS = frozenset({"BUILDING", "BUILT"})
RETIRED = frozenset({"RETIRED"})
V1_STATES = frozenset({"LANDED", "CLOSED"}) | IN_PROGRESS | {"UNKNOWN", "SPECIFIED"}
V2_STATES = frozenset({"SPECIFIED", "LANDED", "VERIFIED", "RETIRED"})
COMMIT = re.compile(r"[0-9a-f]{7,40}\Z")


def _passed(entry: dict[str, Any], valid: Callable[[Any], bool]) -> list[dict]:
    evidence = entry.get("evidence")
    if not isinstance(evidence, list) or not all(valid(item) for item in evidence):
        return []
    return [item for item in evidence if item["result"] == "passed"]


def _proven_state_v2(entry: dict[str, Any], on_main) -> tuple[str, str]:
    """Schema version 2: landed_in short SHAs and verified_by test ids."""
    state = entry.get("delivery_state")
    if state not in V2_STATES:
        return "UNKNOWN", "Unsupported requirement state"
    if state in {"LANDED", "VERIFIED"}:
        landed = entry.get("landed_in")
        shas = [v for v in landed if isinstance(v, str) and COMMIT.fullmatch(v)] if isinstance(landed, list) else []
        if not shas:
            return "UNKNOWN", "Delivered claim lacks a landed_in commit"
        if not any(on_main(sha) for sha in shas):
            return "UNKNOWN", "landed_in commit is not on the default branch"
    if state == "VERIFIED":
        tests = entry.get("verified_by")
        if not isinstance(tests, list) or not any(isinstance(t, str) and t.strip() for t in tests):
            return "UNKNOWN", "VERIFIED claim lacks verified_by test ids"
    return state, ""


def _proven_state(
    repo: str, entry: dict[str, Any], valid: Callable[[Any], bool], on_main
) -> tuple[str, str]:
    """Return the state the public evidence supports and why a claim fell."""
    state = entry.get("delivery_state")
    if state not in V1_STATES:
        return "UNKNOWN", "Unsupported requirement state"
    passed = _passed(entry, valid)
    if state in DELIVERED:
        merged = [
            item["commit"]
            for item in passed
            if item["kind"] == "merged_head"
            and item["url"]
            == f"https://github.com/Knuckles-Team/{repo}/commit/{item['commit']}"
        ]
        if not merged:
            return "UNKNOWN", "Delivered claim lacks a merged-head commit"
        if not any(on_main(commit) for commit in merged):
            return "UNKNOWN", "Claimed commit is not on the default branch"
    if state in IN_PROGRESS and not passed:
        return "UNKNOWN", "Build claim lacks public implementation evidence"
    return state, ""


def requirement_rows(
    repo: str,
    manifest: dict[str, Any] | None,
    valid: Callable[[Any], bool],
    on_main: Callable[[str], bool],
) -> list[dict[str, str]]:
    """One row per requirement ID; IDs without an entry are SPECIFIED."""
    if not isinstance(manifest, dict):
        return []
    ids = manifest.get("requirement_ids")
    if not isinstance(ids, list):
        return []
    entries = manifest.get("requirements")
    known = {
        entry["id"]: entry
        for entry in (entries if isinstance(entries, list) else [])
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    }
    rows = []
    for ident in (value for value in ids if isinstance(value, str)):
        entry = known.get(ident)
        if not entry:
            state, problem = "SPECIFIED", ""
        elif manifest.get("schema_version") == 2:
            state, problem = _proven_state_v2(entry, on_main)
        else:
            state, problem = _proven_state(repo, entry, valid, on_main)
        title = entry.get("title") if entry else ""
        rows.append(
            {
                "id": ident,
                "title": title if isinstance(title, str) else "",
                "state": state,
                "problem": problem,
            }
        )
    return rows


def progress(rows: list[dict[str, str]]) -> dict[str, int]:
    """State breakdown, delivered count and floor percentage of active rows.

    RETIRED rows are closed: they are reported but leave the denominator.
    """
    counts = Counter(row["state"] for row in rows)
    retired = sum(counts[state] for state in RETIRED)
    total = len(rows) - retired
    delivered = sum(counts[state] for state in DELIVERED)
    return {
        "total": total,
        "delivered": delivered,
        "in_progress": sum(counts[state] for state in IN_PROGRESS),
        "specified": counts["SPECIFIED"],
        "landed": counts["LANDED"] + counts["CLOSED"],
        "verified": counts["VERIFIED"],
        "retired": retired,
        "unknown": counts["UNKNOWN"],
        "percent": delivered * 100 // total if total else 0,
    }
