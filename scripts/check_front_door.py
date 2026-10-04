"""Check every HTTP(S) URL and relative link/image on the three front doors."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

PAGES = ("profile/README.md", "site/index.html", "site/skills.html")


class HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value is not None:
                self.links.append(value)


def extract_links(text: str) -> list[str]:
    """Inventory HTML attributes, Markdown destinations, and literal URLs.

    Raw URL scanning also includes badge images nested in Markdown links.
    Reference definitions are checked even if their label is currently unused.
    This intentionally includes URLs in examples: the contract covers every URL.
    """
    parser = HTMLLinks()
    parser.feed(text)
    markdown = re.findall(r'\]\(\s*(<[^>]*>|[^\s)]+)', text)
    references = re.findall(r'^\s*\[[^\]]+\]:\s*(<[^>]*>|\S+)', text, re.M)
    absolute = re.findall(r'https?://[^\s<>"\)]+', text)
    return sorted({html.unescape(url.strip("<>")) for url in
                   parser.links + markdown + references + absolute})


def check_relative(root: Path, source: str, url: str) -> dict:
    parts = urlsplit(url)
    target = (root / source).parent / unquote(parts.path)
    if not parts.path:
        target = root / source
    target = target.resolve()
    passed = target.is_relative_to(root.resolve()) and target.is_file()
    return {"source": source, "url": url, "result": "passed" if passed else "failed"}


def check_http(url: str, *, timeout: float = 20, opener=urlopen) -> dict:
    request = Request(url, headers={"User-Agent": "ORG-FRONT-001-link-check/1.0"})
    try:
        with opener(request, timeout=timeout) as response:
            status = response.status
            return {"url": url, "status": status, "final_url": response.url,
                    "content_type": response.headers.get("Content-Type"),
                    "result": "passed" if status == 200 else "failed"}
    except HTTPError as exc:
        return {"url": url, "status": exc.code, "result": "failed", "error": str(exc)}
    except (URLError, OSError, ValueError) as exc:
        return {"url": url, "status": None, "result": "failed", "error": str(exc)}


def audit(root: Path, *, checker=check_http) -> dict:
    sources = {name: (root / name).read_bytes() for name in PAGES}
    urls: dict[str, list[str]] = {}
    relative, unsupported = [], []
    for name, content in sources.items():
        for url in extract_links(content.decode("utf-8")):
            parts = urlsplit(url)
            if parts.scheme in {"http", "https"}:
                urls.setdefault(url, []).append(name)
            elif not parts.scheme and not parts.netloc:
                relative.append(check_relative(root, name, url))
            else:
                unsupported.append({"source": name, "url": url, "result": "failed",
                                    "error": "Unsupported URL scheme; review explicitly."})
    with ThreadPoolExecutor(max_workers=4) as pool:
        responses = list(pool.map(checker, sorted(urls)))
    for response in responses:
        response["sources"] = urls[response["url"]]
    checks = responses + relative + unsupported
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "source_sha256": {name: hashlib.sha256(data).hexdigest() for name, data in sources.items()},
        "method": "GET, follow redirects, require final HTTP 200; relative destinations must be repository files",
        "http": responses, "relative": relative, "unsupported": unsupported,
        "summary": {"http": len(responses), "relative": len(relative),
                    "failed": sum(row["result"] != "passed" for row in checks)},
        "result": "passed" if all(row["result"] == "passed" for row in checks) else "failed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(args.root)
    result["commit"] = subprocess.check_output(
        ["git", "-C", str(args.root), "rev-parse", "HEAD"], text=True
    ).strip()
    result["worktree_changes"] = subprocess.check_output(
        ["git", "-C", str(args.root), "status", "--porcelain"], text=True
    ).splitlines()
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(json.dumps(result["summary"]))
    return 0 if result["result"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
