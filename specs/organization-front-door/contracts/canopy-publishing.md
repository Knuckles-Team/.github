# Canopy publishing seam

Consumer: pipelines PIPE-PAGES-R056.3
Consumer: pipelines PIPE-PAGES-R057.3
Provider: .github ORG-FRONT-R010.1
Provider: .github ORG-FRONT-R010.2

## Wire shape

- The site workflow checks out `releases/` and `scripts/architecture_explorer` from the pipelines default branch.
- `build.py --mode github --page hub/site/architecture/index.html` writes `export/rows.json` and `export/rows.md` beside the page.
- `rows.json` holds `{schema, built_at, heads, view, digest, rows[]}`.

## Refusal codes

- `status-uncomputable`: the status report cannot compute a repository. The render exits 1 and the last page stays.
- `unsafe-path`, `export-row-missing`, `release-manifest-invalid`: see the pipelines contract. The build exits 1.
