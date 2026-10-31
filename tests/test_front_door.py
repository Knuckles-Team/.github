"""Protect the front-door contract and fail closed on broken destinations."""

import io
from pathlib import Path
import re
from urllib.error import HTTPError, URLError

import pytest

from scripts.check_front_door import PAGES, SELF_BLOB, audit, check_http, check_relative, extract_links

ROOT = Path(__file__).resolve().parents[1]
EXPLORER = "https://knuckles-team.github.io/.github/architecture/"
CORE = {"arbora", "overstory", "meristem", "medulla", "scion-sdk", "tuig", "axil"}


def repositories(text):
    return set(re.findall(r'https://github.com/Knuckles-Team/([\w-]+)(?=["\)])', text))


@pytest.mark.parametrize("name", PAGES)
def test_component_roles_and_navigation_remain_consistent(name):
    text = (ROOT / name).read_text()
    marker = "Core projects"
    core = text.split(marker, 1)[1]
    if name.endswith(".html"):
        core = core.split("Related contributor repositories", 1)[0]
    else:
        core = core.split("## Start at the runtime door", 1)[0]
    assert repositories(core) == CORE
    assert "Arbora REST interface" in core
    if not name.endswith(".html"):
        assert len(re.findall(r"<tr>", core)) == 4 and core.count('<td width="50%"') == 7
    assert EXPLORER in text
    if name.endswith(".html"):
        assert "spec-status.html" in text
    assert "CONTRIBUTING.md" in text


def test_front_door_links_the_explorer_at_the_top_level():
    """ORG-FRONT-R003.2: the profile sends visitors to the bare explorer URL, never spec-status.html."""
    profile = (ROOT / "profile/README.md").read_text()
    assert "spec-status.html" not in profile
    assert profile.count(EXPLORER + ")") >= 4
    assert re.search(r"github\.io/\.github/architecture/#", profile) is None
    assert "Explore the live architecture" in profile
    assert "`SPECIFIED` rows are open work" in profile
    diagram = 'src="https://raw.githubusercontent.com/Knuckles-Team/medulla/main/docs/assets/runtime-architecture.svg"'
    assert f'<a href="{EXPLORER}"><img {diagram}' in profile
    readme = (ROOT / "README.md").read_text()
    assert f"[Explore the live architecture]({EXPLORER})" in readme


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


# Verifies ORG-FRONT-R002.3.
def test_readme_spec_delivery_links_match_the_single_list():
    from scripts import spec_delivery_links
    from scripts.public_spec_report import SPEC_DELIVERY_PAGES

    text = (ROOT / "profile/README.md").read_text()
    found = re.findall(r"\]\((https://knuckles-team\.github\.io/[^)/]+/spec-delivery/?[^)]*)\)", text)
    expected = {f"https://knuckles-team.github.io/{r}/spec-delivery/" for r in SPEC_DELIVERY_PAGES}
    assert set(found) == expected
    assert all(re.fullmatch(r"https://knuckles-team\.github\.io/[\w-]+/spec-delivery/", u) for u in found)
    assert spec_delivery_links.render() in text
    for repo, brand in spec_delivery_links.DISPLAY_NAMES.items():
        assert f"**[{brand}]({spec_delivery_links.url(repo)})**" in spec_delivery_links.render()


# Verifies ORG-FRONT-R006.
def test_agents_md_is_the_agent_front_door():
    text = (ROOT / "AGENTS.md").read_text()
    for repo in CORE:
        assert f"github.com/Knuckles-Team/{repo})" in text
    for needle in (
        "reference/ecosystem-boundaries.md", "reference/spec-standard.md", "spec-status.html",
        "/architecture/", "scripts/bootstrap.sh", "Spec: none (docs)", "Smallest contribution",
        "SPECIFIED", "LANDED", "VERIFIED", "-R[0-9]{3}", "sdd-full-lifecycle", "speckit-specify",
    ):
        assert needle in text, needle
    assert len(re.findall(r"^\d+\. ", text.split("## Contribution path", 1)[1].split("##", 1)[0], re.M)) == 10
    for link in re.findall(r"\]\((?!https?://|#)([^)]+)\)", text):
        assert (ROOT / link).exists(), link


# Verifies ORG-FRONT-R007.
def test_agent_entry_points_point_at_agents_md():
    assert (ROOT / "CLAUDE.md").read_text().strip() == "@AGENTS.md"
    assert "AGENTS.md" in (ROOT / "CONTRIBUTING.md").read_text()[:300]
    assert "AGENTS.md" in (ROOT / "profile/README.md").read_text()[:300]


# Verifies ORG-FRONT-R008.
def test_site_llms_txt_points_agents_at_the_front_door_and_contribution_path():
    text = (ROOT / "site" / "llms.txt").read_text()
    front_door = "https://knuckles-team.github.io/.github/"
    for needle in (
        front_door, EXPLORER, f"{SELF_BLOB}CONTRIBUTING.md",
        "https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills",
        f"{EXPLORER}spec-details/<repo>/<family>.json", "arbora-development", "Spec: trailer",
    ):
        assert needle in text, needle
    assert len(re.findall(r"^\d+\. ", text, re.M)) == 10
    assert (ROOT / "CONTRIBUTING.md").is_file()


# Verifies ORG-FRONT-R002 and ORG-FRONT-R006.
@pytest.mark.parametrize("name", [*PAGES, "AGENTS.md"])
def test_product_display_names_keep_repository_links(name):
    text = (ROOT / name).read_text()
    brands = {
        "medulla": "Medulla",
        "overstory": "Overstory",
        "tuig": "Tuig",
        "scion-sdk": "Scion SDK",
        "meristem": "Meristem",
        "axil": "Axil",
    }
    for repo, brand in brands.items():
        url = f"https://github.com/Knuckles-Team/{repo}"
        if name.endswith(".html"):
            assert f'<a href="{url}">{brand}</a>' in text
        else:
            assert f"[{brand}]({url})" in text
    assert "Medulla" in text or "medulla" in text
    assert "Arbora" in text or "arbora" in text


def test_hub_readme_introduces_the_display_brand_family():
    text = (ROOT / "README.md").read_text()
    for brand in ("Overstory", "Tuig", "Scion SDK", "Meristem", "Axil", "Arbora", "Medulla"):
        assert f"**{brand}**" in text
    assert "`tuig`" in text
    assert "package/import identifiers" in text


# Verifies ORG-FRONT-R002 and ORG-FRONT-R006.
@pytest.mark.parametrize("name", [*PAGES, "README.md", "AGENTS.md"])
def test_front_doors_use_canonical_repository_and_pages_urls(name):
    text = (ROOT / name).read_text()
    retired = (
        "epistemic-graph", "agent-utilities", "agent-connector-sdk",
        "agent-webui", "agent-terminal-ui", "geniusbot",
    )
    for host in ("github.com/Knuckles-Team", "raw.githubusercontent.com/Knuckles-Team", "knuckles-team.github.io"):
        for slug in retired:
            assert f"https://{host}/{slug}" not in text
