# ORG-FRONT — Research

## Resolved unknowns

- **Cause of UNKNOWN.** `committed_specs` at `scripts/public_spec_report.py:104` looks for `specs/<dir>/status.json` in `git ls-tree`. Repositories compute status at read time and commit no such file. Every family gets `No committed status.json` (line 129) and the state UNKNOWN. The live page shows 78 such rows.
- **Why Canopy is fine.** `GitReader.statuses` and `GitHubReader.statuses` in the pipelines `scripts/architecture_explorer/sources.py` call `generate_at`, which clones at the head and computes status.
- **Generator access.** The workflow already checks out `pipelines_hooks/specs` in sparse cone mode, so `generator.py` is present. The generator needs full history.
- **Missing release manifests.** The same checkout omits `releases/`, so the live Canopy lists no release bundles and marks every row unscheduled.

## Open questions

none
