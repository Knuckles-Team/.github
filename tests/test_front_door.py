"""Protect the front-door contract and fail closed on broken destinations."""

import io
from pathlib import Path
import re
from urllib.error import HTTPError, URLError

import pytest

from scripts.check_front_door import PAGES, audit, check_http, check_relative, extract_links

ROOT = Path(__file__).resolve().parents[1]
CORE = {"graph-os", "agent-webui", "agent-utilities", "epistemic-graph", "agent-connector-sdk"}
ADDITIONAL = {"agent-terminal-ui", "geniusbot"}


def repositories(text):
    return set(re.findall(r'https://github.com/Knuckles-Team/([\w-]+)(?=["\)])', text))


@pytest.mark.parametrize("name", PAGES)
def test_component_roles_and_navigation_remain_consistent(name):
    text = (ROOT / name).read_text()
    core = text.split("Five core projects", 1)[1].split("Additional operator surfaces", 1)[0]
    additional = text.split("Additional operator surfaces", 1)[1]
    if name.endswith(".html"):
        additional = additional.split("Related contributor repositories", 1)[0]
    else:
        additional = additional.split("## Start at the runtime door", 1)[0]
    assert repositories(core) == CORE
    assert repositories(additional) == ADDITIONAL
    assert "Graph OS REST interface" in additional
    assert "spec-status.html" in text
    assert "CONTRIBUTING.md" in text


def test_nested_badge_html_and_markdown_references_are_all_checked():
    text = '''[![Build](https://badge.example/build.svg)](https://repo.example/project)
<img src="assets/diagram.svg"><a href="next.html?mode=1&amp;view=2">Next</a>
[guide](../CONTRIBUTING.md) [details][ref]
[ref]: <docs/details.md>
'''
    assert set(extract_links(text)) == {
        "https://badge.example/build.svg", "https://repo.example/project",
        "assets/diagram.svg", "next.html?mode=1&view=2", "../CONTRIBUTING.md", "docs/details.md",
    }


def test_missing_images_and_escaping_paths_fail(tmp_path):
    (tmp_path / "site").mkdir()
    (tmp_path / "site/index.html").write_text("<h1>Home</h1>")
    assert check_relative(tmp_path, "site/index.html", "#home")["result"] == "passed"
    assert check_relative(tmp_path, "site/index.html", "missing.png")["result"] == "failed"
    assert check_relative(tmp_path, "site/index.html", "../../outside.html")["result"] == "failed"


@pytest.mark.parametrize("error", [
    HTTPError("https://example.org", 404, "Not Found", {}, None),
    URLError("unavailable"), TimeoutError("timed out"),
])
def test_unavailable_http_is_a_failure(error):
    def opener(request, timeout):
        raise error
    assert check_http("https://example.org", opener=opener)["result"] == "failed"


@pytest.mark.parametrize("status,expected", [(200, "passed"), (204, "failed"), (503, "failed")])
def test_only_final_http_200_passes(status, expected):
    response = io.BytesIO(b"ok")
    response.status = status
    response.url = "https://example.org/redirected"
    response.headers = {"Content-Type": "text/html"}
    result = check_http("https://example.org", opener=lambda request, timeout: response)
    assert result["result"] == expected
    assert result["final_url"] == "https://example.org/redirected"


def test_audit_never_hides_a_broken_destination(tmp_path):
    for name in PAGES:
        file = tmp_path / name
        file.parent.mkdir(exist_ok=True)
        file.write_text('[link](https://example.org) <img src="missing.svg">')
    result = audit(tmp_path, checker=lambda url: {"url": url, "result": "failed", "status": 404})
    assert result["result"] == "failed"
    assert result["summary"] == {"http": 1, "relative": 3, "failed": 4}
