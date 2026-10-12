"""Regenerate compatibility SVGs from the pinned Epistemic Graph authority."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

MANIFEST = Path(__file__).with_name("runtime_diagram.json")
GUIDE = "https://github.com/Knuckles-Team/.github/blob/main/docs/runtime-diagram.md"


def render(source, manifest):
    """Preserve the exact source bytes after a deterministic provenance comment."""
    if hashlib.sha256(source).hexdigest() != manifest["sha256"]:
        raise ValueError("Source SHA-256 differs from runtime_diagram.json")
    return (
        f"<!-- Generated compatibility copy; do not edit.\n"
        f"Source: {manifest['source_url']}\n"
        f"SHA-256: {manifest['sha256']}\n"
        f"Synchronize: {GUIDE}\n-->\n"
    ).encode() + source


def sync(target, content, check=False):
    """Check or replace an existing compatibility path without deleting it."""
    current = target.read_bytes()
    if current == content:
        return True
    if check:
        return False
    target.write_bytes(content)
    return True


def check_published(manifest):
    """Flag canonical drift and stale published copies; never update repositories."""
    live_url = "https://raw.githubusercontent.com/Knuckles-Team/epistemic-graph/main/docs/assets/runtime-architecture.svg"
    with urlopen(live_url, timeout=30) as response:
        source = response.read()
    expected = render(source, manifest)
    clean = True
    for name, path in manifest["copies"].items():
        url = f"https://raw.githubusercontent.com/Knuckles-Team/{name}/main/{path}"
        with urlopen(url, timeout=30) as response:
            matched = response.read() == expected
        print(f"{'OK' if matched else 'DRIFT'}: {url}")
        clean = clean and matched
    return 0 if clean else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Local canonical SVG (verified against the pinned digest)")
    parser.add_argument("--repo", action="append", metavar="NAME=CHECKOUT", help="Existing compatibility checkout; repeat for multiple repositories")
    parser.add_argument("--check", action="store_true", help="Report drift without writing")
    parser.add_argument("--check-published", action="store_true", help="Check live EG source and published compatibility copies without writing")
    args = parser.parse_args(argv)
    manifest = json.loads(MANIFEST.read_text())
    if args.check_published:
        return check_published(manifest)
    targets = []
    for value in args.repo or [f".github={MANIFEST.parent.parent}"]:
        name, separator, checkout = value.partition("=")
        if not separator or name not in manifest["copies"]:
            parser.error(f"Unknown repository mapping: {value}")
        target = Path(checkout) / manifest["copies"][name]
        if not target.is_file():
            parser.error(f"Missing existing compatibility asset: {target}")
        targets.append(target)
    if args.source:
        source = args.source.read_bytes()
    else:
        with urlopen(manifest["source_url"], timeout=30) as response:
            source = response.read()
    content = render(source, manifest)
    clean = True
    for target in targets:
        matched = sync(target, content, args.check)
        print(f"{'OK' if matched else 'DRIFT'}: {target}")
        clean = clean and matched
    return 0 if clean else 1


if __name__ == "__main__":
    raise SystemExit(main())
