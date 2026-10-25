> **For AI agents → [AGENTS.md](https://github.com/Knuckles-Team/.github/blob/main/AGENTS.md)**


<div align="center">

# Knuckles-Team agent platform

**A governed runtime for building agents, connecting operational systems, and turning every action into durable, explainable knowledge.**

[![Platform documentation](https://img.shields.io/badge/platform-documentation-6d5dfc?style=for-the-badge)](https://knuckles-team.github.io/agent-utilities/) [![Run Arbora](https://img.shields.io/badge/start-Arbora-18a999?style=for-the-badge)](https://knuckles-team.github.io/arbora/) [![GitHub repositories](https://img.shields.io/badge/explore-repositories-111827?style=for-the-badge&logo=github)](https://github.com/orgs/Knuckles-Team/repositories)

**[Live architecture and spec status](https://knuckles-team.github.io/.github/architecture/)** · **[Repositories and skills](https://knuckles-team.github.io/.github/skills.html)** · **[Contribution guide](https://github.com/Knuckles-Team/.github/blob/main/CONTRIBUTING.md)**

<!-- spec-delivery:begin -->
Spec delivery: **[epistemic-graph](https://knuckles-team.github.io/epistemic-graph/spec-delivery/)** · **[Scion SDK](https://knuckles-team.github.io/agent-connector-sdk/spec-delivery/)** · **[Meristem](https://knuckles-team.github.io/agent-utilities/spec-delivery/)** · **[arbora](https://knuckles-team.github.io/arbora/spec-delivery/)** · **[Overstory](https://knuckles-team.github.io/agent-webui/spec-delivery/)** · **[Tuig](https://knuckles-team.github.io/agent-terminal-ui/spec-delivery/)** · **[Axil Desk](https://knuckles-team.github.io/geniusbot/spec-delivery/)**
<!-- spec-delivery:end -->

<a href="https://knuckles-team.github.io/.github/architecture/"><img src="https://raw.githubusercontent.com/Knuckles-Team/epistemic-graph/main/docs/assets/runtime-architecture.svg" alt="Knuckles-Team platform runtime architecture" width="100%"></a>

**[Explore the live architecture](https://knuckles-team.github.io/.github/architecture/)**

</div>

## Core projects

The seven core projects are **Arbora**, **Overstory**, **Epistemic Graph**, **Meristem**, **Scion SDK**, **Tuig**, and **Axil Desk**. **Tuig** and **Axil Desk** are further operator surfaces on the same Arbora boundary. Overstory provides the browser operator surface through Arbora. MCP, REST, and A2A clients use the same governed **Arbora** boundary. Arbora composes the runtime and delegates agent work to the **Meristem** control plane. **Epistemic Graph** commits durable knowledge, evidence, provenance, and reasoning results. Source systems connect through the governed **Scion SDK** contract.

<table>
<tr>
<td width="50%" valign="top">

### [Arbora](https://github.com/Knuckles-Team/arbora)

The public runtime gateway: MCP, REST, A2A, identity, policy, fleet composition, and WebUI hosting.

**[Documentation](https://knuckles-team.github.io/arbora/)** · **[Build status](https://github.com/Knuckles-Team/arbora/actions)** · **[Spec delivery](https://knuckles-team.github.io/arbora/spec-delivery/)**

</td>
<td width="50%" valign="top">

### [Overstory](https://github.com/Knuckles-Team/agent-webui)

The browser operator experience for conversations, approvals, tool activity, and graph-backed work.

**[Documentation](https://knuckles-team.github.io/agent-webui/)** · **[Build status](https://github.com/Knuckles-Team/agent-webui/actions)** · **[Spec delivery](https://knuckles-team.github.io/agent-webui/spec-delivery/)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Epistemic Graph](https://github.com/Knuckles-Team/epistemic-graph)

The reasoning and durable knowledge engine for graph, RDF, SQL, vectors, time, blobs, evidence, and provenance. Publishes `epistemic-graph` and `epistemic-graph-server` (the native server and its container image; [PyPI](https://pypi.org/project/epistemic-graph-server/)).

**[Documentation](https://knuckles-team.github.io/epistemic-graph/)** · **[Capability status](https://knuckles-team.github.io/epistemic-graph/status/)** · **[Spec delivery](https://knuckles-team.github.io/epistemic-graph/spec-delivery/)**

</td>
<td width="50%" valign="top">

### [Meristem](https://github.com/Knuckles-Team/agent-utilities)

The agent control plane: agents, workflows, evaluation, skills, and governed execution.

**[Documentation](https://knuckles-team.github.io/agent-utilities/)** · **[Build status](https://github.com/Knuckles-Team/agent-utilities/actions)** · **[Spec delivery](https://knuckles-team.github.io/agent-utilities/spec-delivery/)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Scion SDK](https://github.com/Knuckles-Team/agent-connector-sdk)

The governed source-integration boundary for connector identity, discovery, synchronization, replay, and write-back.

**[Documentation](https://knuckles-team.github.io/agent-connector-sdk/)** · **[Build status](https://github.com/Knuckles-Team/agent-connector-sdk/actions)** · **[Spec delivery](https://knuckles-team.github.io/agent-connector-sdk/spec-delivery/)**

</td>
<td width="50%" valign="top">

### [Tuig](https://github.com/Knuckles-Team/agent-terminal-ui)

The terminal operator surface for the Arbora REST interface.

**[Documentation](https://knuckles-team.github.io/agent-terminal-ui/)** · **[Build status](https://github.com/Knuckles-Team/agent-terminal-ui/actions)** · **[Spec delivery](https://knuckles-team.github.io/agent-terminal-ui/spec-delivery/)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Axil Desk](https://github.com/Knuckles-Team/geniusbot)

The desktop GUI for specialist agents, embedded terminals, tool approvals, and graph-backed exploration.

**[Documentation](https://knuckles-team.github.io/geniusbot/)** · **[Build status](https://github.com/Knuckles-Team/geniusbot/actions)** · **[Spec delivery](https://knuckles-team.github.io/geniusbot/spec-delivery/)**

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
| Use the browser experience | [Overstory documentation](https://knuckles-team.github.io/agent-webui/) |
| Build agents, workflows, evaluations, or skills | [Meristem documentation](https://knuckles-team.github.io/agent-utilities/) |
| Query or operate the knowledge engine directly | [Epistemic Graph documentation](https://knuckles-team.github.io/epistemic-graph/) |
| Build or certify a source connector | [Scion SDK documentation](https://knuckles-team.github.io/agent-connector-sdk/) |

Every repository documents its own contract and links back to this same runtime map. The boundaries are deliberate: Arbora is the door, Meristem controls agent behavior, Epistemic Graph owns durable knowledge and reasoning, Overstory presents the browser surface, and Scion SDK governs source integration.

## Project health

Build and release evidence lives with the component that owns it. Use each repository's **Actions** page for current CI and its Pages **Status** or **Capabilities** section for shipped behavior. Public issues and pull requests are tracked in the owning repository so operational and design discussions retain their architectural context.

The [Arbora Architecture Explorer](https://knuckles-team.github.io/.github/architecture/) shows every spec row of the core repositories, the connectors and the desktop client with its status, placed on the part of the architecture it builds, and is rebuilt on every merge to a core repository's main branch, and at least every 30 minutes. `SPECIFIED` rows are open work waiting to be built; delivery and acceptance are separate states. The [contribution guide](https://github.com/Knuckles-Team/.github/blob/main/CONTRIBUTING.md) links the shared `arbora-development` and spec skills.

## Contribute from a public spec

Pick a `SPECIFIED` row in the [architecture explorer](https://knuckles-team.github.io/.github/architecture/), then read its owner repository's `spec.md`, `requirements.md`, `plan.md`, `test-spec.md`, `tasks.md`, and `status.json`. The owner repo defines the implementation; related repository specs describe consumers and interfaces. Bootstrap with [`arbora-development`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/arbora-development), then use [universal-skills](https://github.com/Knuckles-Team/universal-skills): [`spec-generator`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/spec-generator), [`task-planner`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/task-planner), [`sdd-implementer`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-implementer), [`spec-verifier`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/spec-verifier), and [`sdd-full-lifecycle`](https://github.com/Knuckles-Team/universal-skills/tree/main/universal_skills/skills/sdd-full-lifecycle). The [step-by-step guide](https://github.com/Knuckles-Team/.github/blob/main/CONTRIBUTING.md) covers local setup, reuse, tests, pull requests, and public evidence.

All seven core projects are released under the [MIT License](https://opensource.org/license/mit).
