# Organization front door

**Spec ID:** ORG-FRONT-001. **Requirements:** ORG-FRONT-R001. **Delivery:** landed.
**Acceptance:** accepted.

## Outcome

A visitor who lands on the organization profile or the published Pages site understands, in
under a minute, what the platform is, which repositories compose it, and where to start. The
front door is `profile/README.md` (rendered on the GitHub organization page), `site/index.html`
and `site/skills.html` (the published ecosystem map and contributor skill guide), and this
repository's own `README.md` and `CONTRIBUTING.md`. Every claim on these pages describes the
shipped platform in present tense; no page states a future design as current behavior, and no
link points to a resource that fails to resolve.

## Content contract

The organization profile names the five core public repositories and their dependency
direction: **Graph OS** is the governed runtime gateway that people, and MCP, REST, and A2A
clients reach the platform through; Graph OS composes the runtime and delegates agent work to
the **Agent Utilities** control plane; **Epistemic Graph** commits durable knowledge, evidence,
provenance, and reasoning results; source systems connect through the governed **Agent
Connector SDK** contract; and **Agent Web UI** is the browser operator surface served through
that same Graph OS boundary. **Agent Terminal UI** and **GeniusBot** are documented as
additional operator surfaces on the same boundary — further front ends, not a sixth or seventh
core project — so the "five core projects" framing and the per-component cards stay consistent
with each other.

Every outbound link on the front-door pages — badges, component cards, navigation, and the
"Follow the flow" and "Contribute from a public spec" tables in `profile/README.md` — must
resolve: a GitHub repository, branch, or file path that exists, or a GitHub Pages documentation
URL that serves content. `site/index.html` and `site/skills.html` list the same component set
and link back to `spec-status.html` and this repository's `CONTRIBUTING.md`, so a visitor
reaches the same contribution path from any of the three entry pages.

## Architecture and contribution rules

These pages are static content with no build step of their own beyond the existing Pages
publish. A change to a component's public name, repository location, or responsibility updates
`profile/README.md`, `site/index.html`, and `site/skills.html` together, so the three surfaces
never disagree about what a repository owns. Do not add a project to the "core" framing, or
describe a capability, without a shipped, documented owner repository backing the claim.

## Evidence and completion

| Gate | State | Evidence |
|---|---|---|
| Link check across `profile/README.md`, `site/index.html`, `site/skills.html` | PASS | [Exact-source results](evidence/links.json); [merged-source CI](https://github.com/Knuckles-Team/.github/actions/runs/37174684510) |
| GitHub rendering check of the organization profile | PASS | [Live and commit-pinned render facts](evidence/render.json); [live screenshot](evidence/organization-live.png) |

Audited source: [`5e674839fb10e1aea4e3f11468fe804636fdd8b6`](https://github.com/Knuckles-Team/.github/commit/5e674839fb10e1aea4e3f11468fe804636fdd8b6). [Complete criterion evidence](evidence/audit.json), [test output](evidence/pytest.txt), and [independent review](evidence/independent-review.json) bind to that source commit. A later receipt-only commit records this audit without changing its source identity.

**LANDED** requires the exact merged front-door content. **ACCEPTED** requires both checks in
`test-spec.md` passing against that commit, linked in the evidence section above.

Requirement IDs are defined in [requirements.md](requirements.md); delivery state per ID is in `status.json`.
