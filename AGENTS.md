# Knuckles-Team organization hub: agent front door

This repository is the public front door of the Knuckles-Team agent platform. It holds
the organization profile, the Pages site, and the generated specification status report.
Humans read [CONTRIBUTING.md](CONTRIBUTING.md); agents start here.

## What the organization is

A governed runtime for building agents, connecting operational systems, and recording every
action as durable knowledge. Every requirement lives in the owning repository's `specs/` tree.

## Core repositories and ownership

| Repository | Owns |
|---|---|
| [epistemic-graph](https://github.com/Knuckles-Team/epistemic-graph) | Facts, records, storage, query, retrieval, reasoning |
| [arbora](https://github.com/Knuckles-Team/arbora) | Admission, auth, served operations, MCP and A2A serving |
| [agent-connector-sdk](https://github.com/Knuckles-Team/agent-connector-sdk) | Connector contracts, transports, client adapters |
| [agent-utilities](https://github.com/Knuckles-Team/agent-utilities) | The in-run harness: run loop, context, fan-out, sandbox |
| [agent-webui](https://github.com/Knuckles-Team/agent-webui) | The browser operator surface |
| [agent-terminal-ui](https://github.com/Knuckles-Team/agent-terminal-ui) | The terminal operator surface |
| [geniusbot](https://github.com/Knuckles-Team/geniusbot) | The desktop operator surface |

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

1. Pick a `SPECIFIED` requirement row.
2. Clone the owner repository.
3. Read its `AGENTS.md`, then its `spec.md`, `plan.md`, `test-spec.md`, `tasks.md` and `status.json`.
4. Run `scripts/bootstrap.sh` (where the repository provides it) for pinned tools and git hooks.
5. Implement the row and the test its `test-spec.md` names. Run the repository's gates.
6. Commit with a `Spec: <ROW-ID>` trailer and open a pull request. Do not edit `status.json` by hand.

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
[sdd-full-lifecycle](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development-workflows/sdd-full-lifecycle),
[spec-generator](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/spec-generator),
[sdd-implementer](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/sdd-implementer),
[spec-verifier](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/spec-verifier).

## Working in this repository

`python -m pytest -q tests` and `python scripts/check_front_door.py` are the checks.
`scripts/public_spec_report.py` generates `site/spec-status.html` in CI; do not hand-edit that file.
Spec for this repository: `specs/organization-front-door/`.
