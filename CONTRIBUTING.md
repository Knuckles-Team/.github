# Contributing to Graph OS

Start with the [build-first program](https://knuckles-team.github.io/.github/build-first.html)
for queued and building requirements, then open the [public specification status report](https://knuckles-team.github.io/.github/spec-status.html)
and filter Delivery to `SPECIFIED` for published build contracts. Open the linked
spec in its owner repository. Its `spec.md`, `plan.md`, `tasks.md`, `test-spec.md`,
and `status.json` define the design, implementation slices, tests, and evidence
state. Check that repository's contribution guide and `AGENTS.md` before coding.
If a spec is incomplete, propose the missing design or test detail in that owner
repository before treating it as ready to implement.

Use the public [universal-skills kit](https://github.com/Knuckles-Team/universal-skills)
to install the same workflows used by maintainers:

- [`graph-os-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/graph-os-development) for ecosystem boundaries, a local development environment, and reuse of existing components;
- [`spec-generator`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/spec-generator) to turn a proposal into a complete owner-native spec;
- [`task-planner`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/task-planner) and [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/sdd-implementer) to build from the spec;
- [`spec-verifier`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/spec-verifier) to review its evidence and acceptance;
- [`sdd-full-lifecycle`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development-workflows/sdd-full-lifecycle) to coordinate the sequence.

Use the owner repo's public interfaces and test setup. A contribution should
follow its documented CCCC, jscpd, dupehound, and KISS requirements, reuse its
existing wiring and components, and include focused tests for its acceptance
criteria. Keep the spec self-contained: all design and test decisions needed
to build the deliverable belong in the owner repository. Update `status.json`
only with public evidence. A merged change is not automatically accepted.
