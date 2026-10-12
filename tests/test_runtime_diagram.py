"""Keep compatibility assets reproducible and preserve old links."""

import hashlib
import json
from pathlib import Path

import pytest

from scripts.sync_runtime_diagram import MANIFEST, main, render, sync

ROOT = Path(__file__).resolve().parents[1]


def test_committed_copy_matches_pinned_source_and_provenance():
    manifest = json.loads(MANIFEST.read_text())
    committed = (ROOT / manifest["copies"][".github"]).read_bytes()
    source = committed.split(b"-->\n", 1)[1]
    assert committed == render(source, manifest)


def test_wrong_source_is_refused_before_copying():
    with pytest.raises(ValueError, match="SHA-256"):
        render(b"wrong source", json.loads(MANIFEST.read_text()))


def test_check_detects_drift_without_writing_and_sync_is_repeatable(tmp_path):
    target = tmp_path / "diagram.svg"
    target.write_bytes(b"old")
    source = b'<svg xmlns="http://www.w3.org/2000/svg"/>'
    manifest = {"source_url": "https://example.org/source.svg", "sha256": hashlib.sha256(source).hexdigest()}
    expected = render(source, manifest)
    assert not sync(target, expected, check=True)
    assert target.read_bytes() == b"old"
    assert sync(target, expected)
    assert sync(target, expected, check=True)
    assert sync(target, expected)
    assert target.read_bytes() == expected


def test_unknown_repository_is_refused_before_network_access():
    with pytest.raises(SystemExit) as error:
        main(["--repo", "unknown=."])
    assert error.value.code == 2


def test_profile_uses_the_live_canonical_image():
    text = (ROOT / "profile/README.md").read_text()
    assert 'src="https://raw.githubusercontent.com/Knuckles-Team/epistemic-graph/main/docs/assets/runtime-architecture.svg"' in text
    assert 'src="https://raw.githubusercontent.com/Knuckles-Team/.github/main/profile/assets/runtime-architecture.svg"' not in text
