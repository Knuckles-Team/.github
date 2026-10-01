# Organization-owned specifications

The organization repository owns cross-repository governance contracts and its own
public front door. Runtime, engine, connector, UI, and workspace implementation specs
remain in their owner repositories. See the [public specification status](../site/spec-status.html).

Every spec here provides `spec.md`, `plan.md`, `tasks.md`, `test-spec.md`, `requirements.md`
(the definition of every requirement ID the spec owns, one row per ID), and `status.json`
(machine-readable delivery and acceptance, including a per-requirement `requirements` array
with its own `delivery_state` and evidence for each ID; a requirement counts as delivered only
with a merged-head commit on the default branch). A cross-repository governance spec can set
rules and track owner-native receipts; it cannot declare a component accepted on its own.

## Specifications

- [`crossrepo-authority-governance`](crossrepo-authority-governance/spec.md) — ORG-AUTH-001:
  ORG-AUTH-R001–ORG-AUTH-R005, the duplicate-authority register.
- [`organization-front-door`](organization-front-door/spec.md) — ORG-FRONT-001:
  ORG-FRONT-R001, the organization README and site front door.
