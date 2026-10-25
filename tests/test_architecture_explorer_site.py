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


def test_architecture_sparse_checkout_covers_imports_before_network_build():
    """ORG-FRONT-R003.1: validate the generator's complete sparse import closure."""
    text = WORKFLOW.read_text()
    checkout = text.split("      - name: Checkout architecture explorer generator\n", 1)[1]
    sparse = checkout.split("          sparse-checkout: |\n", 1)[1].split("      - name:", 1)[0]
    assert [line.strip() for line in sparse.splitlines()] == [
        "scripts/__init__.py",
        "scripts/architecture_explorer",
        "pipelines_hooks/__init__.py",
        "pipelines_hooks/core/__init__.py",
        "pipelines_hooks/core/repositories.py",
        "pipelines_hooks/specs/__init__.py",
        "pipelines_hooks/specs/ids.py",
        "pipelines_hooks/specs/priority.py",
        "pipelines_hooks/specs/requirements_doc.py",
    ]
    smoke = "      - name: Validate architecture explorer imports\n        run: python3 generator/scripts/architecture_explorer/build.py --help\n"
    assert smoke in text
    assert text.index(smoke) < text.index("      - name: Build architecture explorer\n")
