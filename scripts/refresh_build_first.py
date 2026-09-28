#!/usr/bin/env python3
"""Refresh public spec links in the committed build-first queue.

The queue's 182 program IDs and provisional partitions are checked-in data.
Only public committed status manifests are read when refreshing links.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .public_spec_report import REPOS, git
except ImportError:  # direct script invocation from the workflow
    from public_spec_report import REPOS, git


def public_spec_links(paths: dict[str, Path]) -> tuple[dict[str, str], dict[str, list[dict[str, str]]]]:
    revisions: dict[str, str] = {}
    links: dict[str, list[dict[str, str]]] = {}
    for repo in REPOS:
        path = paths[repo]
        if not (path / ".git").exists():
            raise ValueError(f"missing public Git checkout: {repo}")
        revision = git(path, "rev-parse", "HEAD").strip()
        revisions[repo] = revision
        tracked = set(git(path, "ls-tree", "-r", "--name-only", "HEAD", "--", "specs").splitlines())
        for status_path in sorted(p for p in tracked if p.endswith("/status.json") and p.count("/") == 2):
            spec_path = status_path.removesuffix("status.json") + "spec.md"
            if spec_path not in tracked:
                continue
            try:
                manifest = json.loads(git(path, "show", f"HEAD:{status_path}"))
            except json.JSONDecodeError:
                continue
            if not isinstance(manifest, dict) or manifest.get("owner_repo") != repo:
                continue
            for ident in manifest.get("requirement_ids", []):
                if not isinstance(ident, str):
                    continue
                links.setdefault(ident, []).append(
                    {
                        "repo": repo,
                        "url": f"https://github.com/Knuckles-Team/{repo}/blob/{revision}/{spec_path}",
                    }
                )
    return revisions, links


def refresh(queue: dict, revisions: dict[str, str], links: dict[str, list[dict[str, str]]]) -> dict:
    if queue.get("schema_version") != 1 or not isinstance(queue.get("items"), list):
        raise ValueError("unsupported build-first queue")
    for row in queue["items"]:
        refs = links.get(row["id"], [])
        owner = [ref for ref in refs if ref["repo"] == row["provisional_owner"]]
        previous = row.get("owner_spec_url") or ""
        owner.sort(key=lambda ref: (ref["url"].split("/specs/")[-1] not in previous, ref["url"]))
        primary = owner[0] if owner else None
        row["owner_spec_url"] = primary["url"] if primary else None
        row["related_spec_urls"] = [ref["url"] for ref in refs if ref is not primary]
        row["needs_spec"] = primary is None
        # A matching ID is only a pointer. Design and test completeness needs review.
        row["needs_design_review"] = True
    queue["source_revisions"] = revisions
    return queue


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkouts-root", type=Path, required=True)
    parser.add_argument("--repo", action="append", default=[], metavar="NAME=PATH")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    paths = {repo: args.checkouts_root / repo for repo in REPOS}
    for item in args.repo:
        if "=" not in item:
            parser.error("--repo must be NAME=PATH")
        repo, raw_path = item.split("=", 1)
        if repo not in REPOS:
            parser.error(f"unknown repository {repo}")
        paths[repo] = Path(raw_path)
    try:
        revisions, links = public_spec_links(paths)
        queue = refresh(json.loads(args.input.read_text(encoding="utf-8")), revisions, links)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Refreshed {len(queue['items'])} active IDs from {len(revisions)} public checkouts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
