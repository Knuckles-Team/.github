"""Report claims must be derived from committed public spec metadata."""

import subprocess
from pathlib import Path

from scripts.public_spec_report import committed_specs, evaluate_status, render

SHA = "a" * 40
REPO = "arbora"


def status(**changes):
    base = {
        "schema_version": 1,
        "spec_id": "GRAPHOS-001",
        "owner_repo": REPO,
        "requirement_ids": ["GRAPHOS-R001"],
        "delivery_state": "SPECIFIED",
        "acceptance_state": "NOT_AUDITED",
        "evidence": [],
    }
    base.update(changes)
    return base


def proof(kind, commit=SHA):
    return {
        "kind": kind,
        "url": f"https://github.com/Knuckles-Team/{REPO}/commit/{commit}",
        "commit": commit,
        "result": "passed",
    }


def test_no_manifest_or_unproven_landing_is_unknown():
    row = evaluate_status(REPO, "one", "specs/one/spec.md", None)
    assert (row["delivery"], row["acceptance"]) == ("UNKNOWN", "NOT_AUDITED")
    row = evaluate_status(
        REPO, "one", "specs/one/spec.md", status(delivery_state="LANDED")
    )
    assert row["delivery"] == "UNKNOWN"
    assert "merged-head" in row["problem"]


def test_acceptance_requires_matching_merged_head_test_and_consumer_or_release():
    row = evaluate_status(
        REPO,
        "one",
        "specs/one/spec.md",
        status(
            delivery_state="LANDED",
            acceptance_state="ACCEPTED",
            evidence=[proof("merged_head"), proof("test")],
        ),
    )
    assert (row["delivery"], row["acceptance"]) == ("LANDED", "NOT_AUDITED")
    row = evaluate_status(
        REPO,
        "one",
        "specs/one/spec.md",
        status(
            delivery_state="LANDED",
            acceptance_state="ACCEPTED",
            evidence=[proof("merged_head"), proof("test"), proof("consumer")],
        ),
    )
    assert (row["delivery"], row["acceptance"]) == ("LANDED", "ACCEPTED")


def test_report_escapes_spec_metadata():
    row = evaluate_status(
        REPO, "one", "specs/one/spec.md", status(spec_id="<script>alert(1)</script>")
    )
    page = render({REPO: SHA}, [row])
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in page
    assert "<script>alert(1)</script>" not in page


def test_uncommitted_manifest_cannot_advance_status(tmp_path: Path):
    repo = tmp_path / REPO
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "config", "user.email", "test@example.com"], check=True
    )
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
    spec = repo / "specs" / "one"
    spec.mkdir(parents=True)
    (spec / "spec.md").write_text("# one\n", encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(repo), "add", "--", "specs/one/spec.md"], check=True
    )
    subprocess.run(["git", "-C", str(repo), "commit", "-qm", "add spec"], check=True)
    (spec / "status.json").write_text('{"delivery_state":"LANDED"}', encoding="utf-8")
    _, rows = committed_specs(repo, REPO)
    assert len(rows) == 1
    assert (rows[0]["delivery"], rows[0]["acceptance"]) == ("UNKNOWN", "NOT_AUDITED")


def v2_manifest(**changes):
    base = {
        "schema_version": 2, "spec_id": "S-001", "owner_repo": REPO,
        "delivery_state": "VERIFIED", "requirement_ids": ["S-R001", "S-R002"],
        "requirements": [
            {"id": "S-R001", "title": "a", "delivery_state": "VERIFIED",
             "landed_in": ["abc1234"], "verified_by": ["tests/t.py::a"]},
            {"id": "S-R002", "title": "b", "delivery_state": "RETIRED",
             "landed_in": [], "verified_by": []},
        ],
    }
    base.update(changes)
    return base


def test_v2_manifest_is_read_natively():
    row = evaluate_status(REPO, "s", "specs/s/spec.md", v2_manifest())
    assert (row["delivery"], row["problem"]) == ("VERIFIED", "")
    assert evaluate_status(REPO, "s", "specs/s/spec.md",
                           v2_manifest(delivery_state="BUILT"))["delivery"] == "UNKNOWN"


def git_repo(tmp_path: Path, manifest: dict) -> Path:
    import json
    repo = tmp_path / REPO
    (repo / "specs" / "s").mkdir(parents=True)
    run = lambda *a: subprocess.run(["git", "-C", str(repo), *a], check=True, capture_output=True)
    run("init", "-q", "-b", "main")
    run("config", "user.email", "t@example.com")
    run("config", "user.name", "Test")
    (repo / "specs/s/spec.md").write_text("# s\n")
    run("add", "--", "specs/s/spec.md")
    run("commit", "-qm", "spec")
    sha = run("rev-parse", "--short", "HEAD").stdout.decode().strip()
    for r in manifest["requirements"]:
        if r["landed_in"]:
            r["landed_in"] = [sha]
    (repo / "specs/s/status.json").write_text(json.dumps(manifest))
    run("add", "--", "specs/s/status.json")
    run("commit", "-qm", "status")
    run("update-ref", "refs/remotes/origin/main", "HEAD")
    return repo


def test_v2_committed_specs_counts_verified_and_demotes_off_main(tmp_path: Path):
    from scripts.requirement_progress import progress
    _, rows = committed_specs(git_repo(tmp_path, v2_manifest()), REPO)
    assert rows[0]["delivery"] == "VERIFIED" and rows[0]["acceptance"] == "ACCEPTED"
    done = progress(rows[0]["requirements"])
    assert (done["verified"], done["retired"], done["percent"]) == (1, 1, 100)
    page = render({REPO: SHA}, rows)
    assert "VERIFIED 1" in page and "RETIRED 1" in page and "1/1 (100%)" in page

    bad = v2_manifest()
    bad["requirements"][0]["landed_in"] = ["deadbee"]
    other = tmp_path / "other"
    other.mkdir()
    repo = git_repo(other, bad)
    import json
    m = json.loads((repo / "specs/s/status.json").read_text())
    m["requirements"][0]["landed_in"] = ["deadbee"]
    (repo / "specs/s/status.json").write_text(json.dumps(m))
    subprocess.run(["git", "-C", str(repo), "add", "--", "specs/s/status.json"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-qm", "bad"], check=True)
    subprocess.run(["git", "-C", str(repo), "update-ref", "refs/remotes/origin/main", "HEAD"], check=True)
    _, rows = committed_specs(repo, REPO)
    assert rows[0]["delivery"] == "UNKNOWN" and "default branch" in rows[0]["problem"]
