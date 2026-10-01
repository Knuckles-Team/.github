# Architecture and rollout

1. Treat `profile/README.md`, `site/index.html`, and `site/skills.html` as one coordinated
   surface: a change to a component's name, repository, or responsibility updates all three
   together, plus this repository's `README.md` and `CONTRIBUTING.md` wherever they restate
   the same component list or contribution path.
2. Keep the five-core-repository framing — Graph OS, Agent Web UI, Agent Utilities, Epistemic
   Graph, and Agent Connector SDK — and its dependency direction explicit on the profile page:
   runtime gateway, browser surface, control plane, durable knowledge engine, and
   source-integration boundary. Document Agent Terminal UI and GeniusBot as additional operator
   surfaces on the same Graph OS boundary, never folded into the "five core projects" count.
3. Run a link check against every `http(s)://` and relative link on the three front-door pages
   before publishing; a badge, documentation link, or Pages cross-link that returns a
   non-success status, or a relative path with no matching file, fails the check.
4. Verify the profile page renders correctly on the GitHub organization page (the two-column
   component table, the architecture image, and the badge row) after any structural edit, since
   GitHub's Markdown renderer treats raw HTML tables and badges differently from a generic
   Markdown viewer.

No step requires a live platform deployment; the front door describes publicly released
repositories and their relationships, verifiable from the public checkouts alone.
