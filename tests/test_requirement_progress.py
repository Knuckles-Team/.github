"""A requirement counts only when its own public evidence proves it."""

from scripts.public_spec_report import evaluate_status, render, valid_evidence
from scripts.requirement_progress import progress, requirement_rows

SHA = "b" * 40
REPO = "arbora"


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
    assert progress(found)["total"] == 1 and progress(found)["delivered"] == 0 and progress(found)["percent"] == 0


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


def v2(*entries, on_main=lambda sha: True):
    data = {
        "schema_version": 2,
        "requirement_ids": [e["id"] for e in entries],
        "requirements": list(entries),
    }
    return requirement_rows(REPO, data, valid_evidence, on_main)


def entry(ident, state, landed=("abc1234",), tests=("t::a",)):
    return {"id": ident, "title": ident, "delivery_state": state,
            "landed_in": list(landed), "verified_by": list(tests)}


def test_v2_verified_and_landed_count_as_delivered():
    found = v2(entry("X-R1", "VERIFIED"), entry("X-R2", "LANDED", tests=()),
               entry("X-R3", "SPECIFIED", landed=(), tests=()))
    assert [r["state"] for r in found] == ["VERIFIED", "LANDED", "SPECIFIED"]
    done = progress(found)
    assert (done["verified"], done["landed"], done["specified"]) == (1, 1, 1)
    assert (done["delivered"], done["total"], done["percent"]) == (2, 3, 66)


def test_v2_sha_off_main_or_missing_demotes_with_a_reason():
    off = v2(entry("X-R1", "LANDED"), on_main=lambda sha: False)[0]
    assert off["state"] == "UNKNOWN" and "default branch" in off["problem"]
    none = v2(entry("X-R1", "LANDED", landed=()))[0]
    assert none["state"] == "UNKNOWN" and "landed_in" in none["problem"]
    bad = v2(entry("X-R1", "LANDED", landed=("not-a-sha",)))[0]
    assert bad["state"] == "UNKNOWN"


def test_v2_verified_needs_tests_and_unknown_states_are_rejected():
    assert v2(entry("X-R1", "VERIFIED", tests=()))[0]["state"] == "UNKNOWN"
    assert v2(entry("X-R1", "BUILT"))[0]["state"] == "UNKNOWN"


def test_v2_retired_is_closed_and_leaves_the_denominator():
    found = v2(entry("X-R1", "RETIRED", landed=(), tests=()), entry("X-R2", "VERIFIED"))
    done = progress(found)
    assert (done["retired"], done["total"], done["delivered"], done["percent"]) == (1, 1, 1, 100)
