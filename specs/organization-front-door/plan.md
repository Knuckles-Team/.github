# ORG-FRONT — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

The public status page shows `No committed status.json` and UNKNOWN for every family. Spec status is computed at read time, so no repository commits a `status.json`. The page reads that file in `committed_specs`, so each family fails. The fix computes status from the default-branch head with the pipelines generator, as the Canopy explorer already does. The same workflow also needs the release manifests and must publish the Canopy export files. Rows ORG-FRONT-R009 and ORG-FRONT-R010 hold the work. They serve the Canopy rows in the pipelines repository.

## Technical Context

- **Language/Version**: Python 3.14 for scripts; GitHub Actions workflow YAML
- **Primary Dependencies**: `pipelines_hooks.specs.generator.generate_at` from the pipelines generator checkout
- **Storage**: N/A
- **Testing**: pytest in `tests/`; no network call
- **Target Platform**: GitHub Pages built by one workflow
- **Project Type**: static site scripts
- **Performance Goals**: the workflow stays under 15 minutes
- **Constraints**: full Git history for each source checkout; no hand-edited generated page
- **Scale/Scope**: 14 repositories, about 9800 rows

## Constitution Check

The organization constitution is the one in the pipelines repository. This repository has no copy.

- I. One owner per concept: pass. The generator owns status computation; this repository only calls it.
- II. Extend before you create: pass. Rows extend ORG-FRONT-R004 and ORG-FRONT-R003.1.
- III. Specs describe the current state only: pass.
- V. Hard cutover, no legacy path: pass. The committed `status.json` read and the files are deleted in one change.
- XXI. Public files stay portable and neutral: pass.
- XXIV. Specifications are complete enough to implement without assumptions: pass. Every task below names files, function, test and tier.

## Project Structure

```
scripts/public_spec_report.py                          existing: read_status_documents (new function), committed_specs, render
.github/workflows/spec-status-pages.yml                existing: step order, PYTHONPATH, sparse list, export check
site/llms.txt                                          existing: export and hash forms
specs/README.md                                        existing: drop the status.json sentence
specs/*/status.json                                    existing: deleted
tests/test_public_spec_report.py                       existing
tests/test_architecture_explorer_site.py               existing
tests/test_front_door.py                               existing
```

## Phase 0: Research

- **Cause.** `committed_specs` at `scripts/public_spec_report.py:104` looks for `specs/<dir>/status.json` in `git ls-tree`. Repositories no longer commit it, so every family gets the problem text `No committed status.json` (line 129) and the state UNKNOWN. The live page shows 78 such rows.
- **Why Canopy is fine.** `GitReader.statuses` and `GitHubReader.statuses` in `scripts/architecture_explorer/sources.py` call `generate_at`, which clones at the head and computes status.
- **Generator access.** The workflow already checks out `pipelines_hooks/specs` from pipelines main in sparse cone mode, so `generator.py` is present. The generator needs full history; the source checkouts already use `fetch-depth: 0`.
- **Missing release manifests.** The same checkout omits `releases/`, so the live Canopy shows an empty release list.

The findings are in [research.md](research.md).

## Phase 1: Design

Data flow: `main` (line 450) loops over `REPOS`. For each, `committed_specs` calls `read_status_documents(repo, head)`, which calls `generate_at(str(repo), head)`. It passes each document to `evaluate_status`. `render` prints the head and the generator commit. A failure raises `StatusUncomputable`, `main` exits 1, and the deploy step does not run, so the last page stays.

The workflow runs the generator checkout first, then the render with `PYTHONPATH=generator`, then the Canopy build, then a verify step for the export, then the upload.

### Front-door rollout

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

### Spec-delivery links (ORG-FRONT-R002)

The row is the owner-side counterpart of the spec-delivery drill-down row in `Knuckles-Team/pipelines`.

- Data flow: `SPEC_DELIVERY_PAGES` (`scripts/public_spec_report.py:27`) feeds `render()` in
  `scripts/spec_delivery_links.py`. `--write` replaces the marker block in `profile/README.md`.
- Attach point: the block follows the navigation line at `profile/README.md:10`.
- Single list: the repository tuple `REPOS` and `SPEC_DELIVERY_PAGES` live in one module.
  The latter should hold only repositories whose page returns HTTP 200.

### Canonical architecture explorer (ORG-FRONT-R003)

The row is the owner-side counterpart of the architecture explorer row in `Knuckles-Team/pipelines`.

- Build: `spec-status-pages.yml` sparse-checks out `scripts/architecture_explorer` from pipelines
  `main` and runs `build.py --mode github --page hub/site/architecture/index.html` before upload.
- Currency: the cron `7,37 * * * *` rebuilds every 30 minutes; `repository_dispatch:
  specs-changed` rebuilds sooner when the shared Pages workflow holds a dispatch token. The
  concurrency group cancels a superseded build.
- Links: the profile, `README.md` and the site point to the bare explorer URL; per-repository
  pages elsewhere deep-link to their own node. `spec-status.html` keeps building for the site pages
  and `CONTRIBUTING.md` that still link it.

### 2026-10-25 display-brand amendment

The profile, agent front door and hand-authored site entry points display
the five approved product display names documented in `AGENTS.md`. Axil Desk
is the desktop GUI. The spec-delivery link generator renders those labels
with unchanged repository
URLs. Epistemic Graph and Arbora retain their names; package/import names,
repository slugs, spec prefixes and the `tuig` command remain unchanged.
The architecture explorer still comes from the canonical pipelines generator;
no generated architecture or spec-status output is hand-edited.

### 2026-10-26 canonical source-chart invocation amendment (ORG-FRONT-R003.1)

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


## Phase 2: Task approach

The tasks run in order. T001 to T006 fix the status bug and are the first slice. T007 to T009 publish what Canopy needs and can run in parallel with them after T003, because they edit the same workflow file and must rebase one at a time.

Each task is one child row. A standard lane implements one task in under 30 minutes with the files, function and test named here.

| Task | Row | Files to touch | Extend this | Test | Tier |
|---|---|---|---|---|---|
| T001 | ORG-FRONT-R009.1 | scripts/public_spec_report.py; tests/test_public_spec_report.py | committed_specs at public_spec_report.py:104 | `tests/test_public_spec_report.py::test_status_documents_are_generated_from_the_head_commit` | standard |
| T002 | ORG-FRONT-R009.2 | scripts/public_spec_report.py; specs/README.md; specs/organization-front-door/status.json (delete); specs/crossrepo-authority-governance/status.json (delete) | committed_specs at public_spec_report.py:104 | `tests/test_public_spec_report.py::test_spec_without_a_committed_manifest_is_evaluated_from_generated_status` | standard |
| T003 | ORG-FRONT-R009.3 | .github/workflows/spec-status-pages.yml; tests/test_architecture_explorer_site.py | workflow step list in spec-status-pages.yml | `tests/test_architecture_explorer_site.py::test_render_step_follows_the_generator_checkout_and_sets_pythonpath` | standard |
| T004 | ORG-FRONT-R009.4 | scripts/public_spec_report.py; tests/test_public_spec_report.py | main in public_spec_report.py:450 | `tests/test_public_spec_report.py::test_a_shallow_checkout_fails_the_render_with_status_uncomputable` | standard |
| T005 | ORG-FRONT-R009.5 | scripts/public_spec_report.py; tests/test_public_spec_report.py | render in public_spec_report.py:364 | `tests/test_public_spec_report.py::test_page_states_computed_head_and_generator_commit_and_no_missing_manifest_text` | standard |
| T006 | ORG-FRONT-R009.6 | tests/test_public_spec_report.py | git fixture helpers in test_public_spec_report.py | `tests/test_public_spec_report.py::test_cli_renders_landed_state_for_a_repository_without_committed_status` | standard |
| T007 | ORG-FRONT-R010.1 | .github/workflows/spec-status-pages.yml; tests/test_architecture_explorer_site.py | sparse-checkout list in spec-status-pages.yml | `tests/test_architecture_explorer_site.py::test_workflow_checks_out_releases_for_the_explorer` | standard |
| T008 | ORG-FRONT-R010.2 | .github/workflows/spec-status-pages.yml; tests/test_architecture_explorer_site.py | step list in spec-status-pages.yml | `tests/test_architecture_explorer_site.py::test_workflow_verifies_the_export_files_before_upload` | standard |
| T009 | ORG-FRONT-R010.3 | site/llms.txt; tests/test_front_door.py | test_site_llms_txt_points_agents_at_the_front_door_and_contribution_path | `tests/test_front_door.py::test_site_llms_txt_names_the_canopy_export_and_hash_forms` | standard |

## Complexity Tracking

none

## Build contract

- Run `pytest tests/test_public_spec_report.py tests/test_architecture_explorer_site.py tests/test_front_door.py tests/test_requirement_progress.py`.
- Run pre-commit on the changed files. Add no baseline entry and no suppression.
- Do not hand-edit `site/spec-status.html`; CI generates it.
- Call `generate_at`; do not copy its logic.

## Production caller chain

- Workflow `spec-status-pages.yml` step `Render from public committed specs` (line 137) runs `scripts/public_spec_report.py` `main` (line 450).
- `main` calls `committed_specs` (line 104), then `read_status_documents`, then `pipelines_hooks.specs.generator.generate_at`, then `evaluate_status` and `render`.
- Obsolete paths to delete: the `git ls-tree` manifest lookup, the `No committed status.json` and `Invalid status.json` branches, and the tracked `specs/*/status.json` files.

## Cross-repo seams

- Release manifests and export files: PIPE-PAGES-R056.3 and PIPE-PAGES-R057.3 in the pipelines repository consume ORG-FRONT-R010.1 and ORG-FRONT-R010.2. The contract is [canopy-publishing.md](contracts/canopy-publishing.md).
