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
