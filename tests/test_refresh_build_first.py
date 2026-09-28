"""The build queue treats cross-repository mentions as links, not ownership."""

from scripts.refresh_build_first import refresh


def test_owner_and_related_links_remain_distinct():
    row = {
        "id": "EH-1",
        "provisional_owner": "graph-os",
        "owner_spec_url": None,
        "related_spec_urls": [],
        "needs_spec": True,
        "needs_design_review": True,
    }
    queue = {"schema_version": 1, "items": [row]}
    links = {
        "EH-1": [
            {"repo": "epistemic-graph", "url": "https://github.com/Knuckles-Team/epistemic-graph/blob/a/specs/engine/spec.md"},
            {"repo": "graph-os", "url": "https://github.com/Knuckles-Team/graph-os/blob/b/specs/facade/spec.md"},
        ]
    }
    result = refresh(queue, {"graph-os": "b"}, links)["items"][0]
    assert result["needs_spec"] is False
    assert result["owner_spec_url"] == links["EH-1"][1]["url"]
    assert result["related_spec_urls"] == [links["EH-1"][0]["url"]]
    assert result["needs_design_review"] is True


def test_partition_review_never_promotes_provisional_consumer_to_owner():
    row = {
        "id": "EH-592",
        "provisional_owner": "graph-os",
        "needs_partition_review": True,
        "needs_owner_review": False,
        "owner_spec_url": "https://github.com/Knuckles-Team/graph-os/blob/main/specs/hosted-api-operations/spec.md",
        "related_spec_urls": [],
        "needs_spec": False,
    }
    refs = [
        {"repo": "epistemic-graph", "url": "https://github.com/Knuckles-Team/epistemic-graph/blob/a/specs/error-code/spec.md"},
        {"repo": "graph-os", "url": "https://github.com/Knuckles-Team/graph-os/blob/b/specs/hosted-api-operations/spec.md"},
    ]
    result = refresh({"schema_version": 1, "items": [row]}, {"graph-os": "b"}, {"EH-592": refs})["items"][0]
    assert result["owner_unresolved"] is True
    assert result["owner_spec_url"] is None
    assert result["related_spec_urls"] == [ref["url"] for ref in refs]
    assert result["needs_spec"] is False


def test_reviewed_owner_requires_matching_public_spec():
    url = "https://github.com/Knuckles-Team/.github/blob/main/specs/crossrepo-authority-governance/spec.md"
    row = {
        "id": "RF-024",
        "provisional_owner": ".github",
        "needs_owner_review": True,
        "reviewed_owner_repo": ".github",
        "reviewed_owner_evidence_url": url,
    }
    ref = {"repo": ".github", "url": url.replace("/main/", "/abc/")}
    result = refresh({"schema_version": 1, "items": [row]}, {".github": "abc"}, {"RF-024": [ref]})["items"][0]
    assert result["owner_unresolved"] is False
    assert result["owner_spec_url"] == ref["url"]
