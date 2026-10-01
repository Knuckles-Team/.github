"""A requirement counts only when its own public evidence proves it."""

from scripts.public_spec_report import evaluate_status, render, valid_evidence
from scripts.requirement_progress import progress, requirement_rows

SHA = "b" * 40
REPO = "graph-os"


def proof(kind, commit=SHA):
    return {
        "kind": kind,
        "url": f"https://github.com/Knuckles-Team/{REPO}/commit/{commit}",
        "commit": commit,
        "result": "passed",
    }


def manifest(*entries):
    return {
        "requirement_ids": [entry["id"] for entry in entries] + ["GRAPHOS-R009"],
        "requirements": list(entries),
    }


def rows(*entries, on_main=lambda sha: True):
    return requirement_rows(REPO, manifest(*entries), valid_evidence, on_main)


def test_ids_without_an_entry_are_specified_and_open():
    found = rows()
    assert [(row["id"], row["state"]) for row in found] == [("GRAPHOS-R009", "SPECIFIED")]
    assert progress(found) == {"total": 1, "delivered": 0, "in_progress": 0, "percent": 0}


def test_landed_needs_a_merged_commit_on_the_default_branch():
    landed = {"id": "GRAPHOS-R001", "delivery_state": "LANDED", "evidence": []}
    assert rows(landed)[0]["state"] == "UNKNOWN"
    landed["evidence"] = [proof("merged_head")]
    assert rows(landed, on_main=lambda sha: False)[0]["state"] == "UNKNOWN"
    found = rows(landed)
    assert found[0]["state"] == "LANDED"
    assert progress(found)["percent"] == 50


def test_build_claims_need_public_implementation_evidence():
    built = {"id": "GRAPHOS-R002", "delivery_state": "BUILT", "evidence": []}
    assert rows(built)[0]["state"] == "UNKNOWN"
    built["evidence"] = [proof("branch")]
    found = rows(built)
    assert found[0]["state"] == "BUILT"
    assert progress(found)["in_progress"] == 1


def test_malformed_or_unsupported_entries_never_count():
    bad_state = {"id": "GRAPHOS-R003", "delivery_state": "DONE", "evidence": []}
    bad_proof = {
        "id": "GRAPHOS-R004",
        "delivery_state": "LANDED",
        "evidence": [{"kind": "merged_head", "result": "passed"}],
    }
    assert [row["state"] for row in rows(bad_state, bad_proof)][:2] == ["UNKNOWN"] * 2
    assert requirement_rows(REPO, None, valid_evidence, lambda sha: True) == []


def test_report_shows_delivered_share_and_open_requirements():
    row = evaluate_status(REPO, "one", "specs/one/spec.md", None)
    landed = {
        "id": "GRAPHOS-R001",
        "title": "Served <b>route</b>",
        "delivery_state": "LANDED",
        "evidence": [proof("merged_head")],
    }
    row["requirements"] = rows(landed)
    page = render({REPO: SHA}, [row])
    assert "1/2 (50%)" in page
    assert "GRAPHOS-R009" in page
    assert "<b>route</b>" not in page
