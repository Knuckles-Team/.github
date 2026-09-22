
<div align="center">

# Knuckles-Team agent platform

**A governed runtime for building agents, connecting operational systems, and turning every action into durable, explainable knowledge.**

[![Platform documentation](https://img.shields.io/badge/platform-documentation-6d5dfc?style=for-the-badge)](https://knuckles-team.github.io/agent-utilities/) [![Run GraphOS](https://img.shields.io/badge/start-GraphOS-18a999?style=for-the-badge)](https://knuckles-team.github.io/graph-os/) [![GitHub repositories](https://img.shields.io/badge/explore-repositories-111827?style=for-the-badge&logo=github)](https://github.com/orgs/Knuckles-Team/repositories)

<img src="./assets/runtime-architecture.svg" alt="Knuckles platform runtime architecture" width="100%">

</div>

## One platform, five clear responsibilities

People and MCP/A2A clients enter through **Agent WebUI** or **GraphOS**. GraphOS applies the runtime boundary and delegates agent work to the **Agent Utilities** control plane. **Epistemic Graph** commits durable knowledge, evidence, provenance, and reasoning results. Source systems connect through the governed **Agent Connector SDK** contract.

<table>
<tr>
<td width="50%" valign="top">

### [GraphOS](https://github.com/Knuckles-Team/graph-os)

The public runtime gateway: MCP, REST, A2A, identity, policy, fleet composition, and WebUI hosting.

**[Documentation](https://knuckles-team.github.io/graph-os/)** · **[Build status](https://github.com/Knuckles-Team/graph-os/actions)**

</td>
<td width="50%" valign="top">

### [Agent WebUI](https://github.com/Knuckles-Team/agent-webui)

The operator experience for conversations, approvals, tool activity, and graph-backed work.

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

GraphOS is the single public entry point. With Python 3.12+ and [`uv`](https://docs.astral.sh/uv/) installed, launch the zero-infrastructure local profile:

```bash
uvx --from graph-os setup-config generate --profile tiny
uvx --from graph-os graph-os --transport stdio
```

The generated profile starts with local, bounded defaults. Continue with the **[GraphOS quick start](https://knuckles-team.github.io/graph-os/)** for provider configuration, WebUI hosting, and authenticated network transports.

## Follow the flow

| If you want to… | Start here |
|---|---|
| Run the platform or connect an MCP/A2A client | [GraphOS documentation](https://knuckles-team.github.io/graph-os/) |
| Use the browser experience | [Agent WebUI documentation](https://knuckles-team.github.io/agent-webui/) |
| Build agents, workflows, evaluations, or skills | [agent-utilities documentation](https://knuckles-team.github.io/agent-utilities/) |
| Query or operate the knowledge engine directly | [epistemic-graph documentation](https://knuckles-team.github.io/epistemic-graph/) |
| Build or certify a source connector | [agent-connector-sdk documentation](https://knuckles-team.github.io/agent-connector-sdk/) |

Every repository documents its own contract and links back to this same runtime map. The boundaries are deliberate: GraphOS is the door, agent-utilities controls agent behavior, epistemic-graph owns durable knowledge and reasoning, Agent WebUI presents the operator surface, and agent-connector-sdk governs source integration.

## Project health

Build and release evidence lives with the component that owns it. Use each repository's **Actions** page for current CI and its Pages **Status** or **Capabilities** section for shipped behavior. Public issues and pull requests are tracked in the owning repository so operational and design discussions retain their architectural context.

All five core projects are released under the [MIT License](https://opensource.org/license/mit).
