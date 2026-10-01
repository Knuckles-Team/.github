# ORG-FRONT-001 requirements

| ID | Requirement | Verification |
|---|---|---|
| `ORG-FRONT-R001` | **Organization front door describes the five-repository flow.** The organization-level README presents the ecosystem's five public repositories in present tense, with an accurate description of how the web UI connects to the graph engine service, and only links that resolve successfully. | An automated link check confirms every linked URL in the front door returns HTTP 200, and a rendering check confirms the page displays correctly on GitHub. |
