# Knuckles-Team organization hub: agent front door

This repository is the public front door of the Knuckles-Team agent platform. It holds
the organization profile, the Pages site, and the generated specification status report.
Humans read [CONTRIBUTING.md](CONTRIBUTING.md); agents start here.

## What the organization is

A governed runtime for building agents, connecting operational systems, and recording every
action as durable knowledge. Every requirement lives in the owning repository's `specs/` tree.

## Core repositories and ownership

Links below use the canonical repository names; packages, imports and spec prefixes remain unchanged.
Tuig runs as `tuig`; Axil is the desktop GUI.

| Repository | Owns |
|---|---|
| [Medulla](https://github.com/Knuckles-Team/medulla) | Facts, records, storage, query, retrieval, reasoning |
| [arbora](https://github.com/Knuckles-Team/arbora) | Admission, auth, served operations, MCP and A2A serving |
| [Scion SDK](https://github.com/Knuckles-Team/scion-sdk) | Connector contracts, transports, client adapters |
| [Meristem](https://github.com/Knuckles-Team/meristem) | The in-run harness: run loop, context, fan-out, sandbox |
| [Overstory](https://github.com/Knuckles-Team/overstory) | The browser operator surface |
| [Tuig](https://github.com/Knuckles-Team/tuig) | The terminal operator surface |
| [Axil](https://github.com/Knuckles-Team/axil) | The desktop operator surface |

Supporting repositories: [pipelines](https://github.com/Knuckles-Team/pipelines) (gates, spec
standard), [universal-skills](https://github.com/Knuckles-Team/universal-skills) (skills), and
one connector repository per external system. The one authoritative boundary table, with worked
examples, is [ecosystem-boundaries.md](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md).
File each part of a feature in its owner's `specs/`; never in a repository that merely uses it.

## How to pick work

1. Open the [specification status report](https://knuckles-team.github.io/.github/spec-status.html)
   and expand a spec's open requirements. Pick a row in state `SPECIFIED`.
2. Use the [architecture explorer](https://knuckles-team.github.io/.github/architecture/) to
   see which repository owns the area.
3. The owner named on the row is the authority. Its `requirements.md` defines the ID.

## Contribution path

The path is spec-driven. Skills come from [universal-skills](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/).

1. **Constitution.** Read the [constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md). Every plan checks against it.
2. **Route.** Pick the owner repository with the [ecosystem boundaries](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md) and [`arbora-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/arbora-development). Choose an open (`SPECIFIED`) row in [Canopy](https://knuckles-team.github.io/.github/architecture/).
3. **Specify.** [`speckit-specify`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-specify) and [`speckit-clarify`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-clarify) write `specs/<id>/spec.md`: user stories, Given/When/Then scenarios, and `FR-` and `SC-` labels mapped to row IDs.
4. **Clarify.** Resolve every `[NEEDS CLARIFICATION]` marker in `spec.md` before you plan.
5. **Plan.** [`speckit-plan`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-plan) writes `plan.md`. Add `contracts/` for cross-repository seams, `data-model.md`, `quickstart.md`, and `research.md` when unknowns remain.
6. **Tasks.** [`speckit-tasks`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-tasks) writes `tasks.md`. Each line reads `- [ ] T001 [P] [US1] <ROW-ID>`.
7. **Analyze and checklist.** [`speckit-analyze`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-analyze) checks consistency and writes `checklists/requirements.md`.
8. **Implement.** Run `scripts/bootstrap.sh` (where the repository provides it) for pinned tools and git hooks. [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-implementer) builds each task. Run the repository gates.
9. **Land.** Open a pull request whose commits carry a `Spec: <ROW-ID>` trailer and a bound test. Do not edit `status.json` by hand.
10. **Release.** Landed rows ship in the next release bundle.

Standards: [constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md), [spec standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/spec-standard.md), [spec templates](https://github.com/Knuckles-Team/pipelines/tree/main/.specify/templates), and [Canopy](https://knuckles-team.github.io/.github/architecture/). Install the skills with `pip install universal-skills`, then `install-skills --all-detected --symlink`.

## Smallest contribution

A documentation fix or small bug needs no new spec. Branch, fix, add or adjust a test when
behavior changes, and commit with the trailer `Spec: none (docs)` (or `Spec: none (<reason>)`).
Run the repository's pre-commit hooks and its test command, then open a pull request. If the fix
changes documented behavior of an existing row, use that row's ID instead.

## Spec standard cheat sheet

Full text: [spec-standard.md](https://github.com/Knuckles-Team/pipelines/blob/main/reference/spec-standard.md).

- States: `SPECIFIED` (written, not on main), `LANDED` (a commit with the ID in a `Spec:` trailer
  is on main), `VERIFIED` (landed and a test is bound to the ID). A generator owns them; `RETIRED` rows are closed.
- Trailer: `Spec: <ROW-ID>` on every commit, or `Spec: none (<reason>)` when no row applies.
- Row ID pattern: `^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-R[0-9]{3}(\.[0-9]+)*$`, for example `ORG-FRONT-R003`.
- Current state only: specs describe what is true now; git holds the past.
- Never stage with `git add -A` or `git add .`; list explicit paths.

## Skills

The [universal-skills](https://github.com/Knuckles-Team/universal-skills) spec-driven development skills:
[sdd-full-lifecycle](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-full-lifecycle),
[speckit-specify](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-specify),
[sdd-implementer](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-implementer),
[speckit-analyze](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-analyze).

## Working in this repository

`python -m pytest -q tests` and `python scripts/check_front_door.py` are the checks.
`scripts/public_spec_report.py` generates `site/spec-status.html` in CI; do not hand-edit that file.
Spec for this repository: `specs/organization-front-door/`.
