# Architecture and rollout

1. Treat `profile/README.md`, `site/index.html`, and `site/skills.html` as one coordinated
   surface: a change to a component's name, repository, or responsibility updates all three
   together, plus this repository's `README.md` and `CONTRIBUTING.md` wherever they restate
   the same component list or contribution path.
2. Keep the five-core-repository framing — Graph OS, Agent Web UI, Agent Utilities, Epistemic
   Graph, and Agent Connector SDK — and its dependency direction explicit on the profile page:
   runtime gateway, browser surface, control plane, durable knowledge engine, and
   source-integration boundary. Document Agent Terminal UI and GeniusBot as additional operator
   surfaces on the same Graph OS boundary, never folded into the "five core projects" count.
3. Run a link check against every `http(s)://` and relative link on the three front-door pages
   before publishing; a badge, documentation link, or Pages cross-link that returns a
   non-success status, or a relative path with no matching file, fails the check.
4. Verify the profile page renders correctly on the GitHub organization page (the two-column
   component table, the architecture image, and the badge row) after any structural edit, since
   GitHub's Markdown renderer treats raw HTML tables and badges differently from a generic
   Markdown viewer.

No step requires a live platform deployment; the front door describes publicly released
repositories and their relationships, verifiable from the public checkouts alone.

## Spec-delivery links (ORG-FRONT-R002)

The row is the owner-side counterpart of `PIPE-PAGES-R014.5` in `Knuckles-Team/pipelines`.

- Data flow: `SPEC_DELIVERY_PAGES` (`scripts/public_spec_report.py:27`) feeds `render()` in
  `scripts/spec_delivery_links.py`. `--write` replaces the marker block in `profile/README.md`.
- Attach point: the block follows the navigation line at `profile/README.md:10`.
- Single list: the repository tuple `REPOS` and `SPEC_DELIVERY_PAGES` live in one module.
  The latter should hold only repositories whose page returns HTTP 200.

## Canonical architecture explorer (ORG-FRONT-R003)

The row is the owner-side counterpart of `PIPE-PAGES-R042` in `Knuckles-Team/pipelines`.

- Build: `spec-status-pages.yml` sparse-checks out `scripts/architecture_explorer` from pipelines
  `main` and runs `build.py --mode github --page hub/site/architecture/index.html` before upload.
- Currency: the cron `7,37 * * * *` rebuilds every 30 minutes; `repository_dispatch:
  specs-changed` rebuilds sooner when the shared Pages workflow holds a dispatch token. The
  concurrency group cancels a superseded build.
- Links: the profile, `README.md` and the site point to the bare explorer URL; per-repository
  pages elsewhere deep-link to their own node. `spec-status.html` keeps building for the site pages
  and `CONTRIBUTING.md` that still link it.

## 2026-10-25 display-brand amendment

The profile, agent front door and hand-authored site entry points display
the five approved product display names documented in `AGENTS.md`. Axil Desk
is the desktop GUI. The spec-delivery link generator renders those labels
with unchanged repository
URLs. Epistemic Graph and Arbora retain their names; package/import names,
repository slugs, spec prefixes and the `tuig` command remain unchanged.
The architecture explorer still comes from the canonical pipelines generator;
no generated architecture or spec-status output is hand-edited.

## 2026-10-26 canonical source-chart invocation amendment (ORG-FRONT-R003.1)

The actual organization workflow, distinct from the reusable repository Pages
workflow, must opt into the pipelines source-family configuration when building
the canonical explorer. Retain the existing read token and deployment permissions;
add the shared alias/error/trailer import closure and the same pinned networkx
3.6.1 scoring dependency as the qualified generator. Smoke-import the render path
before network capture. Missing or invalid source charts fail the build before
artifact upload; never substitute a frozen study or silently serve evidence-only
as a qualified priority/dependency release. The scoped source-family and no-activity
limitations remain those of the generator. Verify the served same-build receipt
only after successful canonical deployment; do not hand-edit generated site files.
