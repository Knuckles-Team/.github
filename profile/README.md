> **For AI agents → [AGENTS.md](https://github.com/Knuckles-Team/.github/blob/main/AGENTS.md)**


<div align="center">

# Knuckles-Team agent platform

**A governed runtime for building agents, connecting operational systems, and turning every action into durable, explainable knowledge. The ecosystem develops itself inside Medulla as changesets, a code graph, and requirement records.**

[![Platform documentation](https://img.shields.io/badge/platform-documentation-6d5dfc?style=for-the-badge)](https://knuckles-team.github.io/meristem/) [![Run Arbora](https://img.shields.io/badge/start-Arbora-18a999?style=for-the-badge)](https://knuckles-team.github.io/arbora/) [![GitHub repositories](https://img.shields.io/badge/explore-repositories-111827?style=for-the-badge&logo=github)](https://github.com/orgs/Knuckles-Team/repositories)

**[Live architecture and spec status](https://knuckles-team.github.io/.github/architecture/)** · **[Repositories and skills](https://knuckles-team.github.io/.github/skills.html)** · **[Contribution guide](https://github.com/Knuckles-Team/.github/blob/main/CONTRIBUTING.md)**

<!-- spec-delivery:begin -->
Spec delivery: **[Medulla](https://knuckles-team.github.io/medulla/spec-delivery/)** · **[Scion SDK](https://knuckles-team.github.io/scion-sdk/spec-delivery/)** · **[Meristem](https://knuckles-team.github.io/meristem/spec-delivery/)** · **[arbora](https://knuckles-team.github.io/arbora/spec-delivery/)** · **[Overstory](https://knuckles-team.github.io/overstory/spec-delivery/)** · **[Tuig](https://knuckles-team.github.io/tuig/spec-delivery/)** · **[Axil](https://knuckles-team.github.io/axil/spec-delivery/)**
<!-- spec-delivery:end -->

<a href="https://knuckles-team.github.io/.github/architecture/"><img src="https://raw.githubusercontent.com/Knuckles-Team/medulla/main/docs/assets/runtime-architecture.svg" alt="Knuckles-Team platform runtime architecture" width="100%"></a>

**[Explore the live architecture](https://knuckles-team.github.io/.github/architecture/)**

</div>

## Core projects

The seven core projects are **Arbora**, **Overstory**, **Medulla**, **Meristem**, **Scion SDK**, **Tuig**, and **Axil**. **Tuig** and **Axil** are further operator surfaces on the same Arbora boundary. Overstory provides the browser operator surface through Arbora. MCP, REST, and A2A clients use the same governed **Arbora** boundary. Arbora composes the runtime and serves every operation. **Meristem** is the in-run harness. It applies decisions it receives and holds no store. **Medulla** commits durable knowledge, evidence, provenance, and reasoning results. Source systems connect through the governed **Scion SDK** contract.

<table>
<tr>
<td width="50%" valign="top">

### [Arbora](https://github.com/Knuckles-Team/arbora)

The one door to the platform (formerly graph-os): served operations, admission, authentication, MCP and A2A serving, the registry, and Overstory hosting.

**[Documentation](https://knuckles-team.github.io/arbora/)** · **[Build status](https://github.com/Knuckles-Team/arbora/actions)** · **[Spec delivery](https://knuckles-team.github.io/arbora/spec-delivery/)**

</td>
<td width="50%" valign="top">

### [Overstory](https://github.com/Knuckles-Team/overstory)

The browser operator experience (formerly agent-webui) for conversations, approvals, tool activity, and graph-backed work.

**[Documentation](https://knuckles-team.github.io/overstory/)** · **[Build status](https://github.com/Knuckles-Team/overstory/actions)** · **[Spec delivery](https://knuckles-team.github.io/overstory/spec-delivery/)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Medulla](https://github.com/Knuckles-Team/medulla)

The reasoning and durable knowledge engine (formerly epistemic-graph) for graph, RDF, SQL, vectors, time, blobs, evidence, and provenance. Writes use concurrent writers with version checks, mandatory provenance, and contradiction records. Memory decays and consolidates natively. Ships as one engine with one server executable (`medulla-server`) and the `medulla` package. Medulla keeps no synced second database. External stores stay connector sources, read as virtual graphs.

**[Documentation](https://knuckles-team.github.io/medulla/)** · **[Capability status](https://knuckles-team.github.io/medulla/status/)** · **[Spec delivery](https://knuckles-team.github.io/medulla/spec-delivery/)**

</td>
<td width="50%" valign="top">

### [Meristem](https://github.com/Knuckles-Team/meristem)

The in-run agent harness (formerly agent-utilities): run loop, context, fan-out, sandbox, replay, and trace events. It holds no store and serves no API.

**[Documentation](https://knuckles-team.github.io/meristem/)** · **[Build status](https://github.com/Knuckles-Team/meristem/actions)** · **[Spec delivery](https://knuckles-team.github.io/meristem/spec-delivery/)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Scion SDK](https://github.com/Knuckles-Team/scion-sdk)

The connector contracts and transports (formerly agent-connector-sdk) for connector identity, discovery, synchronization, replay, and write-back.

**[Documentation](https://knuckles-team.github.io/scion-sdk/)** · **[Build status](https://github.com/Knuckles-Team/scion-sdk/actions)** · **[Spec delivery](https://knuckles-team.github.io/scion-sdk/spec-delivery/)**

</td>
<td width="50%" valign="top">

### [Tuig](https://github.com/Knuckles-Team/tuig)

The terminal operator surface for the Arbora REST interface.

**[Documentation](https://knuckles-team.github.io/tuig/)** · **[Build status](https://github.com/Knuckles-Team/tuig/actions)** · **[Spec delivery](https://knuckles-team.github.io/tuig/spec-delivery/)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Axil](https://github.com/Knuckles-Team/axil)

The desktop GUI for specialist agents, embedded terminals, tool approvals, and graph-backed exploration.

**[Documentation](https://knuckles-team.github.io/axil/)** · **[Build status](https://github.com/Knuckles-Team/axil/actions)** · **[Spec delivery](https://knuckles-team.github.io/axil/spec-delivery/)**

</td>
</tr>
</table>

## Start at the runtime door

Arbora is the governed runtime entry point. With Python 3.12+ and [`uv`](https://docs.astral.sh/uv/) installed, launch the zero-infrastructure local profile:

```bash
uvx --from arbora setup-config generate --profile tiny
uvx --from arbora arbora --transport stdio
```

The generated profile starts with local, bounded defaults. Continue with the **[Arbora quick start](https://knuckles-team.github.io/arbora/)** for provider configuration, Overstory hosting, messaging, and authenticated network transports.

## Follow the flow

| If you want to… | Start here |
|---|---|
| Run the platform or connect an MCP/A2A client | [Arbora documentation](https://knuckles-team.github.io/arbora/) |
| Use the browser experience | [Overstory documentation](https://knuckles-team.github.io/overstory/) |
| Run or extend the agent harness | [Meristem documentation](https://knuckles-team.github.io/meristem/) |
| Query or operate the knowledge engine directly | [Medulla documentation](https://knuckles-team.github.io/medulla/) |
| Build or certify a source connector | [Scion SDK documentation](https://knuckles-team.github.io/scion-sdk/) |

Every repository documents its own contract and links back to this same runtime map. The boundaries are deliberate: Arbora is the door, Meristem runs agents in-run, Medulla owns durable knowledge and reasoning, Overstory presents the browser surface, and Scion SDK governs source integration.

## Project health

Build and release evidence lives with the component that owns it. Use each repository's **Actions** page for current CI and its Pages **Status** or **Capabilities** section for shipped behavior. Public issues and pull requests are tracked in the owning repository so operational and design discussions retain their architectural context.

The [Arbora Architecture Explorer](https://knuckles-team.github.io/.github/architecture/) shows every spec row of the core repositories, the connectors and the desktop client with its status, placed on the part of the architecture it builds, and is rebuilt on every merge to a core repository's main branch, and at least every 30 minutes. `SPECIFIED` rows are open work waiting to be built; delivery and acceptance are separate states. The [contribution guide](https://github.com/Knuckles-Team/.github/blob/main/CONTRIBUTING.md) links the shared `arbora-development` and spec skills.

## Delivery and development model

Concept-proof phases P1 to P5 shipped as release bundles. The architecture explorer shows the releases. Rust serde types are the source of truth for the Medulla wire format. Clients are hand-written and tested on round-trip vectors, and the repositories commit no generated API contracts. Spec status is computed at read time. Spec IDs use the prefixes MEDULLA-, ARBORA-, MERISTEM-, SCION-, OVERSTORY-, TUIG-, AXIL-, CONN-<REPO>-, and PIPE-.

## Contribute from a public spec

The path is spec-driven, from constitution to release. Each step names its skill and the files it writes:

1. **Constitution.** Read the [constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md). Every plan checks against it.
2. **Route.** Pick the owner repository with the [ecosystem boundaries](https://github.com/Knuckles-Team/pipelines/blob/main/reference/ecosystem-boundaries.md) and [`arbora-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/arbora-development). Choose an open (`SPECIFIED`) row in [Canopy](https://knuckles-team.github.io/.github/architecture/).
3. **Specify.** [`spec-intake-wizard`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/spec-intake-wizard) and [`spec-generator`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/spec-generator) write `specs/<id>/spec.md`: user stories, Given/When/Then scenarios, and `FR-` and `SC-` labels mapped to row IDs.
4. **Clarify.** Resolve every `[NEEDS CLARIFICATION]` marker in `spec.md` before you plan.
5. **Plan.** [`spec-generator`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/spec-generator) writes `plan.md`. Add `contracts/` for cross-repository seams, `data-model.md`, `quickstart.md`, and `research.md` when unknowns remain.
6. **Tasks.** [`task-planner`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/task-planner) writes `tasks.md`. Each line reads `- [ ] T001 [P] [US1] <ROW-ID>`.
7. **Analyze and checklist.** [`spec-verifier`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/spec-verifier) checks consistency and writes `checklists/requirements.md`.
8. **Implement.** [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-implementer) builds each task. Run the repository gates.
9. **Land.** Open a pull request whose commits carry a `Spec: <ROW-ID>` trailer and a bound test. Do not edit `status.json` by hand.
10. **Release.** Landed rows ship in the next release bundle.

Standards: [constitution](https://github.com/Knuckles-Team/pipelines/blob/main/.specify/memory/constitution.md), [spec standard](https://github.com/Knuckles-Team/pipelines/blob/main/reference/spec-standard.md), [spec templates](https://github.com/Knuckles-Team/pipelines/tree/main/specs/_template), and [Canopy](https://knuckles-team.github.io/.github/architecture/). Install the skills with `pip install universal-skills`, then `install-skills --all-detected --symlink`. The [step-by-step guide](https://github.com/Knuckles-Team/.github/blob/main/CONTRIBUTING.md) covers local setup, reuse, tests, and pull requests.

All seven core projects are released under the [MIT License](https://opensource.org/license/mit).
