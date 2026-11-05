# ORG-AUTH — Cross-repository authority governance

**Spec ID:** ORG-AUTH. **Requirements:** ORG-AUTH-R001, ORG-AUTH-R002, ORG-AUTH-R003,
ORG-AUTH-R004, ORG-AUTH-R005. **Delivery:** specified. **Acceptance:** not audited.

## Outcome

Maintain one public register for duplicate-authority decisions that cross
repository boundaries. Each register entry identifies the one component that
owns a durable fact or behavior, the components that consume it, the migration
path away from competing writers or implementations, and the public evidence
needed to close the decision. The register is a governance index; the actual
design and implementation remain in owner-native specs.

## User Scenarios and Testing

### User Story 1 - Record one authority per capability (Priority: P1)

A maintainer adds a register entry for a capability that two repositories both implement, so that one owner is named and the others migrate to it.

**Independent Test**: Run `python -m pytest -q tests/test_authority_register.py` (planned) against a fixture register.

**Acceptance scenarios**

1. Given an entry in `DECIDED` with one `authority_repo`, When the validator runs, Then it passes.
2. Given two entries for one capability that name different authorities once either is `DECIDED`, When the validator runs, Then it fails and names both entries.
3. Given a `CLOSED` entry with no merged implementation receipt, When the validator runs, Then it fails.

### User Story 2 - Keep unresolved ownership visible (Priority: P2)

A reviewer sees every known cross-repository obligation, including those with no owner yet.

**Independent Test**: Render the organization status page from a fixture register that holds a `PROPOSED` entry.

**Acceptance scenarios**

1. Given a `PROPOSED` entry with no owner, When the validator runs, Then it accepts the entry.
2. Given the same entry, When the status page renders, Then the entry shows as unresolved and never as accepted.

### User Story 3 - Keep the register public (Priority: P3)

A contributor builds and tests a public change from the public repositories alone.

**Acceptance scenarios**

1. Given an entry that names a non-public host or a short commit SHA, When the validator runs, Then it fails.
2. Given a public contribution, When the contributor follows the baseline instructions, Then the build and tests run without non-public deployment configuration.

### Edge Cases

- An entry with a duplicate ID, a duplicate consumer name or an unknown `decision_state` fails.
- A `MIGRATING` entry with no linked work for an affected writer or consumer fails.
- A `PROPOSED` entry may leave `owner_spec_url` empty; a `DECIDED` entry may not.
- A register with an empty `entries` array is valid and shows no decisions.

### Assumptions

- Owner repositories publish their own specs and receipts; this register only links to them and never replaces them.
- Repository names and URLs point to public GitHub resources of this organization.
- The validator runs in the existing hub test job, so no new CI job is needed.

## Requirements

- **FR-001**: The register file has a version and an `entries` array whose entries carry the documented fields. Rows: `ORG-AUTH-R001`.
- **FR-002**: Each tracked capability has exactly one authority once decided. Rows: `ORG-AUTH-R002`.
- **FR-003**: Owners and consumers publish their own contracts and tests, and a change reuses established wiring. Rows: `ORG-AUTH-R003`.
- **FR-004**: The register holds public architecture decisions only. Rows: `ORG-AUTH-R004`.
- **FR-005**: An obligation with no owner stays visible as `PROPOSED`. Rows: `ORG-AUTH-R005`.

## Success Criteria

- **SC-001**: A fixture register with one violation of each rule fails with one finding per violation. Rows: `ORG-AUTH-R001`, `ORG-AUTH-R002`.
- **SC-002**: A register with only `PROPOSED` entries validates and renders as unresolved. Rows: `ORG-AUTH-R005`.

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
