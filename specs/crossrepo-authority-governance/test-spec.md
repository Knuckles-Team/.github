# ORG-AUTH test specification

## Register validation

| Requirement | Layer and fixture | Expected positive result | Required negative proof |
|---|---|---|---|
| `ORG-AUTH-R001` | Unit: `tests/test_authority_register.py::test_register_schema_rejects_missing_fields_and_unknown_states` (planned), inline register dictionaries | A register with a version and valid entries passes | A missing field, a duplicate entry ID, a duplicate consumer name or an unknown `decision_state` fails |
| `ORG-AUTH-R002` | Unit: `tests/test_authority_register.py::test_one_authority_per_capability_once_decided` (planned) | A decided capability with one `authority_repo` passes | Two entries for one capability with different authorities, once either is decided, fail |
| `ORG-AUTH-R003` | Unit: `tests/test_authority_register.py::test_decided_entry_links_owner_and_consumer_specs` (planned) | A decided entry with an owner spec URL and consumer spec URLs passes | A decided entry with no owner spec, and a `MIGRATING` entry with no linked work for an affected writer or consumer, fail |
| `ORG-AUTH-R004` | Unit: `tests/test_authority_register.py::test_register_rejects_non_public_urls_and_short_shas` (planned) | Public GitHub URLs and full 40-character SHAs pass | A non-public host, a short SHA and a closed entry with no merged implementation receipt fail |
| `ORG-AUTH-R005` | Unit: `tests/test_authority_register.py::test_proposed_entry_without_owner_is_accepted_and_shown_unresolved` (planned) | A proposed entry with a capability and consumers passes and renders as unresolved | A proposed entry that renders as accepted fails |

## Acceptance evidence

Exercise the validator against positive and negative fixtures in a clean
checkout. For a real entry, inspect public owner and consumer specs, run the
relevant component tests, and verify linked commits are reachable from the
default branches. Record exact URLs and SHAs in the register. ORG-AUTH-R001
through ORG-AUTH-R005 are each accepted only when the register is populated
for the known cross-repository cases and every closed entry satisfies the
receipts above; merely publishing this spec is not acceptance.
