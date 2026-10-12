# Runtime architecture diagram

The maintained SVG is [Epistemic Graph's runtime architecture](https://github.com/Knuckles-Team/epistemic-graph/blob/main/docs/assets/runtime-architecture.svg).
Edit that file only. README and Pages image references use its absolute raw URL:

```text
https://raw.githubusercontent.com/Knuckles-Team/epistemic-graph/main/docs/assets/runtime-architecture.svg
```

Existing SVG paths in this hub and consumer repositories remain available for old
links. They are generated compatibility copies. Each carries an immutable source
URL, SHA-256, and this guide in an XML comment; the source SVG bytes follow unchanged.

## Refresh compatibility copies

After an EG diagram change lands, update `source_url` to its immutable commit and
`sha256` in `scripts/runtime_diagram.json`. From this hub checkout, run:

```bash
python scripts/sync_runtime_diagram.py
python scripts/sync_runtime_diagram.py --repo agent-utilities=../agent-utilities
python scripts/sync_runtime_diagram.py --check
```

Repeat `--repo NAME=CHECKOUT` for any combination of repositories listed in the
manifest. Every target must already exist. `--source PATH` supplies a local
canonical SVG instead of downloading it; both modes verify the pinned digest
before writing. `--check` exits nonzero on drift and never writes.
Review and commit generated files in their owning repositories. The test suite
checks the hub copy against the manifest without network access.
