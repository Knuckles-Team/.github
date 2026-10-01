# Cross-repository authority governance

**Spec ID:** ORG-AUTH-001. **Requirements:** ORG-AUTH-R001, ORG-AUTH-R002, ORG-AUTH-R003,
ORG-AUTH-R004, ORG-AUTH-R005. **Delivery:** specified. **Acceptance:** not audited.

## Outcome

Maintain one public register for duplicate-authority decisions that cross
repository boundaries. Each register entry identifies the one component that
owns a durable fact or behavior, the components that consume it, the migration
path away from competing writers or implementations, and the public evidence
needed to close the decision. The register is a governance index; the actual
design and implementation remain in owner-native specs.

## Entry contract

The machine-readable register at `authority-register.json` has a version and
an `entries` array. An entry must contain a stable ID, a short capability name,
`authority_repo`, `consumer_repos`, `owner_spec_url`, `consumer_spec_urls`,
`decision_state`, and `receipts`. Repository names and URLs must point to
public GitHub resources. `decision_state` is `PROPOSED`, `DECIDED`,
`MIGRATING`, or `CLOSED`. A receipt has a repository, a full commit SHA, a
public URL, and a kind (`implementation`, `test`, `consumer`, or `release`).

`PROPOSED` entries may have an unresolved owner and no owner spec URL.
`DECIDED` requires one owner and a complete owner-native design and test spec.
`MIGRATING` additionally requires linked implementation work for every affected
writer and consumer. `CLOSED` requires public merged commit, test, and consumer
or release receipts from each affected repository, with no competing authority
left in the public implementation. This org register never substitutes for
those owner-native receipts.

## Architecture and contribution rules

The organization hub displays the decision and links to the owner and
consumers. Owner repositories publish their own API, data, migration, and
failure contracts; consumers publish integration and negative tests. A
change affecting an existing capability must reuse the established wiring
and component boundaries. Avoid a second store, writer, policy engine, or
generated client when an authoritative component already exists. Follow the
owner repos' CCCC, jscpd, dupehound, and KISS rules when implementing code.

The register contains public architecture decisions only. Environment-specific
deployment details belong to the operator's own configuration and cannot be
required to build or test a public contribution.

Requirement IDs are defined in [requirements.md](requirements.md); delivery state per ID is in `status.json`.
