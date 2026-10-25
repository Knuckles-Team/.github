"""Render the organization README spec-delivery section from SPEC_DELIVERY_PAGES."""

from pathlib import Path
import sys

try:
    from .public_spec_report import SPEC_DELIVERY_PAGES
except ImportError:  # direct script invocation
    from public_spec_report import SPEC_DELIVERY_PAGES

README = Path(__file__).resolve().parents[1] / "profile/README.md"
BEGIN = "<!-- spec-delivery:begin -->"
END = "<!-- spec-delivery:end -->"
DISPLAY_NAMES = {
    "agent-webui": "Overstory",
    "agent-terminal-ui": "Tuig",
    "agent-connector-sdk": "Scion SDK",
    "agent-utilities": "Meristem",
    "geniusbot": "Axil Desk",
}


def url(repo):
    return f"https://knuckles-team.github.io/{repo}/spec-delivery/"


def render():
    links = " · ".join(f"**[{DISPLAY_NAMES.get(repo, repo)}]({url(repo)})**" for repo in SPEC_DELIVERY_PAGES)
    return f"{BEGIN}\nSpec delivery: {links}\n{END}"


def main():
    text = README.read_text()
    head, rest = text.split(BEGIN, 1)
    tail = rest.split(END, 1)[1]
    new = head + render() + tail
    if "--write" in sys.argv:
        README.write_text(new)
    return 0 if new == text else 1


if __name__ == "__main__":
    raise SystemExit(main())
