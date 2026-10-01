#!/usr/bin/env python3
"""Per-requirement delivery derived from committed public status manifests.

A status manifest may carry a ``requirements`` array with one entry per
requirement ID. Each entry is validated on its own, with the same evidence
rules the specification-level claim uses, so a percentage is never larger
than the public proof behind it.
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Callable

DELIVERED = frozenset({"LANDED", "CLOSED"})
IN_PROGRESS = frozenset({"BUILDING", "BUILT"})
STATES = DELIVERED | IN_PROGRESS | {"UNKNOWN", "SPECIFIED"}


def _passed(entry: dict[str, Any], valid: Callable[[Any], bool]) -> list[dict]:
    evidence = entry.get("evidence")
    if not isinstance(evidence, list) or not all(valid(item) for item in evidence):
        return []
    return [item for item in evidence if item["result"] == "passed"]


def _proven_state(
    repo: str, entry: dict[str, Any], valid: Callable[[Any], bool], on_main
) -> tuple[str, str]:
    """Return the state the public evidence supports and why a claim fell."""
    state = entry.get("delivery_state")
    if state not in STATES:
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
        state, problem = (
            _proven_state(repo, entry, valid, on_main) if entry else ("SPECIFIED", "")
        )
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
    """Delivered, in-progress and total counts with a floor percentage."""
    counts = Counter(row["state"] for row in rows)
    total = len(rows)
    delivered = sum(counts[state] for state in DELIVERED)
    return {
        "total": total,
        "delivered": delivered,
        "in_progress": sum(counts[state] for state in IN_PROGRESS),
        "percent": delivered * 100 // total if total else 0,
    }
