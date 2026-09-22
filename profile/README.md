
<div align="center">

# Knuckles-Team agent platform

**A governed runtime for building agents, connecting operational systems, and turning every action into durable, explainable knowledge.**

[![Platform documentation](https://img.shields.io/badge/platform-documentation-6d5dfc?style=for-the-badge)](https://knuckles-team.github.io/agent-utilities/) [![Run GraphOS](https://img.shields.io/badge/start-GraphOS-18a999?style=for-the-badge)](https://knuckles-team.github.io/graph-os/) [![GitHub repositories](https://img.shields.io/badge/explore-repositories-111827?style=for-the-badge&logo=github)](https://github.com/orgs/Knuckles-Team/repositories)

<img src="https://raw.githubusercontent.com/Knuckles-Team/.github/main/profile/assets/runtime-architecture.svg" alt="Knuckles-Team platform runtime architecture" width="100%">

</div>

## One platform, clear responsibilities

People use **Agent Web UI**, **Agent Terminal UI**, **Geniusbot**, or Graph OS-hosted messaging channels. MCP, REST, and A2A clients use the same governed **Graph OS** boundary. Graph OS composes the runtime and delegates agent work to the **Agent Utilities** control plane. **Epistemic Graph** commits durable knowledge, evidence, provenance, and reasoning results. Source systems connect through the governed **Agent Connector SDK** contract.

<table>
<tr>
<td width="50%" valign="top">

### [Graph OS](https://github.com/Knuckles-Team/graph-os)

The public runtime gateway: MCP, REST, A2A, identity, policy, fleet composition, and WebUI hosting.

**[Documentation](https://knuckles-team.github.io/graph-os/)** · **[Build status](https://github.com/Knuckles-Team/graph-os/actions)**

</td>
<td width="50%" valign="top">

### [Agent Web UI](https://github.com/Knuckles-Team/agent-webui)

The browser operator experience for conversations, approvals, tool activity, and graph-backed work.

**[Documentation](https://knuckles-team.github.io/agent-webui/)** · **[Build status](https://github.com/Knuckles-Team/agent-webui/actions)**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Agent Utilities](https://github.com/Knuckles-Team/agent-utilities)

The agent control plane: agents, workflows, evaluation, skills, and governed execution.

**[Documentation](https://knuckles-team.github.io/agent-utilities/)** · **[Build status](https://github.com/Knuckles-Team/agent-utilities/actions)**

</td>
<td width="50%" valign="top">

### [Epistemic Graph](https://github.com/Knuckles-Team/epistemic-graph)

The reasoning and durable knowledge engine for graph, RDF, SQL, vectors, time, blobs, evidence, and provenance.

**[Documentation](https://knuckles-team.github.io/epistemic-graph/)** · **[Capability status](https://knuckles-team.github.io/epistemic-graph/status/)**

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### [Agent Connector SDK](https://github.com/Knuckles-Team/agent-connector-sdk)

The governed source-integration boundary for connector identity, discovery, synchronization, replay, and write-back.

**[Documentation](https://knuckles-team.github.io/agent-connector-sdk/)** · **[Build status](https://github.com/Knuckles-Team/agent-connector-sdk/actions)**

</td>
</tr>
</table>

## Start at the runtime door

Graph OS is the governed runtime entry point. With Python 3.12+ and [`uv`](https://docs.astral.sh/uv/) installed, launch the zero-infrastructure local profile:

```bash
uvx --from graph-os setup-config generate --profile tiny
uvx --from graph-os graph-os --transport stdio
```

The generated profile starts with local, bounded defaults. Continue with the **[Graph OS quick start](https://knuckles-team.github.io/graph-os/)** for provider configuration, Agent Web UI hosting, messaging, and authenticated network transports.

## Follow the flow

| If you want to… | Start here |
|---|---|
| Run the platform or connect an MCP/A2A client | [Graph OS documentation](https://knuckles-team.github.io/graph-os/) |
| Use the browser experience | [Agent Web UI documentation](https://knuckles-team.github.io/agent-webui/) |
| Build agents, workflows, evaluations, or skills | [Agent Utilities documentation](https://knuckles-team.github.io/agent-utilities/) |
| Query or operate the knowledge engine directly | [Epistemic Graph documentation](https://knuckles-team.github.io/epistemic-graph/) |
| Build or certify a source connector | [Agent Connector SDK documentation](https://knuckles-team.github.io/agent-connector-sdk/) |

Every repository documents its own contract and links back to this same runtime map. The boundaries are deliberate: Graph OS is the door, Agent Utilities controls agent behavior, Epistemic Graph owns durable knowledge and reasoning, Agent Web UI presents the browser surface, and Agent Connector SDK governs source integration.

## Project health

Build and release evidence lives with the component that owns it. Use each repository's **Actions** page for current CI and its Pages **Status** or **Capabilities** section for shipped behavior. Public issues and pull requests are tracked in the owning repository so operational and design discussions retain their architectural context.

All five core projects are released under the [MIT License](https://opensource.org/license/mit).
