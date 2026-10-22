"""The organization site builds the canonical architecture explorer (ORG-FRONT-R003.1)."""

from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/spec-status-pages.yml"


def test_site_workflow_builds_the_explorer_on_a_schedule():
    text = WORKFLOW.read_text()
    assert "cron: '7,37 * * * *'" in text
    assert "repository_dispatch:\n    types: [specs-changed]" in text
    assert "repository: Knuckles-Team/pipelines\n          ref: main" in text
    assert "scripts/architecture_explorer\n" in text
    build = text.index("architecture_explorer/build.py --mode github")
    assert "--page hub/site/architecture/index.html" in text[build:]
    assert build < text.index("Upload Pages artifact")
    assert "--output hub/site/spec-status.html" in text
