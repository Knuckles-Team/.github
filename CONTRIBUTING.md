# Contributing to Graph OS

You can contribute using public GitHub repositories and a development environment
you control. The normal spec, build, and pull request path requires no private
service or live deployment. Start here even if you have
never worked in this ecosystem:

1. Open the [build-first program](https://knuckles-team.github.io/.github/build-first.html)
   and choose a `QUEUED` or `BUILDING` requirement. The proposed owner is
   provisional. If it says **Owner unresolved**, resolve the owner and consumer
   partition in public specs before implementing. Candidate links do not establish
   authority. If it says **Needs public spec**, contribute the missing design
   first. The [specification status report](https://knuckles-team.github.io/.github/spec-status.html)
   shows each published spec's separate delivery and acceptance states.
2. Open the **owner spec** and read `spec.md`, `plan.md`, `test-spec.md`,
   `tasks.md`, and `status.json` together. These describe the desired behavior,
   architecture, test cases, work slices, and evidence. If any part is missing,
   propose it in the owner repository before treating the spec as build-ready.
   A **related spec** in another repository describes a consumer or interface;
   it does not take ownership from the component that owns the behavior.
3. Read that repository's `AGENTS.md`, contribution guide, and local setup.
   Use [`graph-os-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/graph-os-development)
   to bootstrap a local ecosystem environment and find the established code,
   wiring, interfaces, and components to reuse.
4. Install [universal-skills](https://github.com/Knuckles-Team/universal-skills)
   (`pip install universal-skills`, then `install-skills --all-detected --symlink`)
   and make the skills available to your coding agent. Use the map below to
   choose the right skill. You may use [GitHub Spec Kit](https://github.com/github/spec-kit)
   for the same owner-native artifacts; review generated diffs before combining
   generators.
5. Implement the owner spec and its consumer contracts in their respective
   repositories. Run the repository's focused tests and configured CCCC,
   `jscpd`, Dupehound, and KISS checks. Record any unavailable check as a gap;
   do not claim it passed.
6. Open a pull request against the owner repository, link the spec and affected
   consumer specs, and provide test evidence. Update `status.json` only with
   public merged commits and test or consumer evidence. A merged pull request
   establishes delivery, while acceptance needs its own receipts.

Use the public [universal-skills kit](https://github.com/Knuckles-Team/universal-skills)
to install the same workflows used by maintainers:

- [`graph-os-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/graph-os-development) for ecosystem boundaries, a local development environment, and reuse of existing components;
- [`spec-generator`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/spec-generator) to turn a proposal into a complete owner-native spec;
- [`task-planner`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/task-planner) and [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/sdd-implementer) to build from the spec;
- [`spec-verifier`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development/spec-verifier) to review its evidence and acceptance;
- [`sdd-full-lifecycle`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/development-workflows/sdd-full-lifecycle) to coordinate the sequence.

The canonical development skill also ships with
[Graph OS](https://github.com/Knuckles-Team/graph-os/tree/main/graph_os/skills/graph-os-development).
The [universal-skills contribution guide](https://github.com/Knuckles-Team/universal-skills/blob/main/CONTRIBUTING.md)
explains its Spec Kit integration and artifact conventions.

Use the owner repo's public interfaces and test setup. A contribution should
follow its documented CCCC, jscpd, dupehound, and KISS requirements, reuse its
existing wiring and components, and include focused tests for its acceptance
criteria. Keep the spec self-contained: all design and test decisions needed
to build the deliverable belong in the owner repository. Update `status.json`
only with public evidence. A merged change is not automatically accepted.
