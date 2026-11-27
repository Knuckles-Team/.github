"""The organization site builds the canonical architecture explorer (ORG-FRONT-R003.1)."""

from pathlib import Path

WORKFLOW = (
    Path(__file__).resolve().parents[1] / ".github/workflows/spec-status-pages.yml"
)


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
    checkout = text.split(
        "      - name: Checkout architecture explorer generator\n", 1
    )[1]
    sparse = checkout.split("          sparse-checkout: |\n", 1)[1].split(
        "      - name:", 1
    )[0]
    assert [line.strip() for line in sparse.splitlines()] == [
        "scripts/__init__.py",
        "scripts/architecture_explorer",
        "pipelines_hooks",
        "releases",
        ".specify/templates",
    ]
    smoke = "      - name: Validate architecture explorer imports\n"
    assert smoke in text
    assert (
        'PYTHONPATH=generator python3 -c "from scripts.architecture_explorer.story_render import prepare_models"'
        in text
    )
    assert (
        'PYTHONPATH=generator python3 -c "from pipelines_hooks.specs.plan_conformance import template_text"'
        in text
    )
    assert text.index(smoke) < text.index("      - name: Build architecture explorer\n")


def test_workflow_checks_out_releases_for_the_explorer():
    """ORG-FRONT-R010.1: the explorer build reads release manifests from releases/ and fails without it."""
    text = WORKFLOW.read_text()
    checkout = text.split(
        "      - name: Checkout architecture explorer generator\n", 1
    )[1]
    sparse = checkout.split("          sparse-checkout: |\n", 1)[1].split(
        "      - name:", 1
    )[0]
    entries = [line.strip() for line in sparse.splitlines()]
    assert "releases" in entries
    assert ".specify/templates" in entries


def test_canonical_build_requires_same_capture_source_chart_before_upload():
    """ORG-FRONT-R003.1: the actual canonical caller must opt in, not only reusable Pages."""
    text = WORKFLOW.read_text()
    build = text.split("      - name: Build architecture explorer\n", 1)[1].split(
        "      - name:", 1
    )[0]
    assert "GITHUB_TOKEN: ${{ github.token }}" in build
    assert "--mode github" in build
    assert (
        "--source-families generator/scripts/architecture_explorer/source-families.json"
        in build
    )
    assert "--page hub/site/architecture/index.html" in build
    assert "set -euo pipefail" in build
    assert "continue-on-error" not in build and "||" not in build
    assert "--redirect" not in build and "snapshot" not in build
    install = "python3 -m pip install --disable-pip-version-check networkx==3.6.1"
    assert install in text
    assert text.index(install) < text.index(
        "      - name: Validate architecture explorer imports\n"
    )
    assert text.index("      - name: Build architecture explorer\n") < text.index(
        "      - name: Upload Pages artifact\n"
    )
