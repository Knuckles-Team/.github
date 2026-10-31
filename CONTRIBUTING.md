# Contributing to Arbora

> **For AI agents:** start at [AGENTS.md](AGENTS.md). This guide is the human path.

You can contribute using public GitHub repositories and a development environment
you control. The normal spec, build, and pull request path requires no private
service or live deployment. Start here even if you have
never worked in this ecosystem.

The [repositories and skills map](https://knuckles-team.github.io/.github/skills.html)
shows which public repository owns each kind of work and which shared skill to
use at each stage.

The contribution path is spec-driven. Each step names its skill and the files it writes:

1. **Constitution.** Read the [constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md). Every plan checks against it.
2. **Route.** Pick the owner repository with the [ecosystem boundaries](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md) and [`arbora-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/arbora-development). Choose an open (`SPECIFIED`) row in [Canopy](https://knuckles-team.github.io/.github/architecture/).
3. **Specify.** [`speckit-specify`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-specify) and [`speckit-clarify`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-clarify) write `specs/<id>/spec.md`: user stories, Given/When/Then scenarios, and `FR-` and `SC-` labels mapped to row IDs.
4. **Clarify.** Resolve every `[NEEDS CLARIFICATION]` marker in `spec.md` before you plan.
5. **Plan.** [`speckit-plan`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-plan) writes `plan.md`. Add `contracts/` for cross-repository seams, `data-model.md`, `quickstart.md`, and `research.md` when unknowns remain.
6. **Tasks.** [`speckit-tasks`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-tasks) writes `tasks.md`. Each line reads `- [ ] T001 [P] [US1] <ROW-ID>`.
7. **Analyze and checklist.** [`speckit-analyze`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-analyze) checks consistency and writes `checklists/requirements.md`.
8. **Implement.** [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-implementer) builds each task. Run the repository gates.
9. **Land.** Open a pull request whose commits carry a `Spec: <ROW-ID>` trailer and a bound test. Do not edit `status.json` by hand.
10. **Release.** Landed rows ship in the next release bundle.

Standards: [constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md), [spec standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/spec-standard.md), [spec templates](https://github.com/Knuckles-Team/pipelines/tree/main/specs/_template), and [Canopy](https://knuckles-team.github.io/.github/architecture/). Install the skills with `pip install universal-skills`, then `install-skills --all-detected --symlink`.
You may use [GitHub Spec Kit](https://github.com/github/spec-kit) for the same artifacts; review generated diffs before combining generators. Record any unavailable check as a gap; do not claim it passed.

Use the public [universal-skills kit](https://github.com/Knuckles-Team/universal-skills)
to install the same workflows used by maintainers:

- [`arbora-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/arbora-development) for ecosystem boundaries, a local development environment, and reuse of existing components;
- [`speckit-specify`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-specify) to turn a proposal into a complete owner-native spec;
- [`speckit-tasks`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-tasks) and [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-implementer) to build from the spec;
- [`speckit-analyze`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/speckit-analyze) to review its evidence and acceptance;
- [`sdd-full-lifecycle`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-full-lifecycle) to coordinate the sequence.

The canonical development skill also ships with
[Arbora](https://github.com/Knuckles-Team/arbora/tree/main/arbora/skills/arbora-development).
The [universal-skills contribution guide](https://github.com/Knuckles-Team/universal-skills/blob/main/CONTRIBUTING.md)
explains its Spec Kit integration and artifact conventions.

Use the owner repo's public interfaces and test setup. A contribution should
follow its documented CCCC, jscpd, dupehound, and KISS requirements, reuse its
existing wiring and components, and include focused tests for its acceptance
criteria. Keep the spec self-contained: all design and test decisions needed
to build the deliverable belong in the owner repository. Update `status.json`
only with public evidence. A merged change is not automatically accepted.
