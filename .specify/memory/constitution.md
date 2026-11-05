# Organization hub constitution

This repository inherits the [organization constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md) version 1.7.0. Every article of that constitution applies here. This file adds only the rules and limits of this repository. `.specify/templates/` is vended by pipelines; do not edit it.

**Inherits**: organization constitution v1.7.0 | **Version**: 1.0.0 | **Ratified**: 2026-11-05 | **Last amended**: 2026-11-05

## Organization standards

- [Spec standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/spec-standard.md): one owning spec per capability, computed states, `Spec:` trailers.
- [Ecosystem boundaries](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md): which repository owns which requirement.
- [Wording standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ste.md): sentences of 20 words or fewer, with `must`, `should`, or `may`.

## Repository articles

### R-I. The front door states only public, shipped facts

Every page of the organization front door describes the shipped platform in present tense and links only to public resources that resolve. It names no private host, domain or tool.

**Enforced by:** `python scripts/check_front_door.py` and `tests/test_front_door.py`.

**Plan check:** Does every new claim and link on a front-door page describe a public, shipped resource?

### R-II. Owner specs hold the requirements

This repository owns only the front door and cross-repository governance. A requirement for a component stays in the owning repository's `specs/`; the hub links to it and never copies its state.

**Enforced by:** [Ecosystem boundaries](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md) and the computed status report.

**Plan check:** Does the change file each requirement in its owner's `specs/` and only link to it here?

## Repository limits

This repository sets no numeric limit of its own. It follows the organization limits table.

Amend this file in a reviewed change. State the impact in the pull request. When the organization constitution changes its version, update the **Inherits** line in the same change.
