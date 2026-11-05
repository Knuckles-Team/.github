# ORG-AUTH — Implementation tasks

Governing spec: [spec.md](spec.md). Design: [plan.md](plan.md). Rows: [requirements.md](requirements.md).

Each task line reads `- [ ] T001 [P] [US1] <ID>-R012.4 description`. The task number and the row ID are required.

- [ ] T001 [US1] ORG-AUTH-R001 Add `scripts/authority_register.py` with `validate_register` and the schema and enumeration checks.
- [ ] T002 [P] [US1] ORG-AUTH-R002 Add `check_single_authority` so a decided capability has exactly one authority.
- [ ] T003 [P] [US1] ORG-AUTH-R003 Add `check_linked_specs` so a decided entry links its owner and consumer specs.
- [ ] T004 [P] [US3] ORG-AUTH-R004 Add `check_public_urls` and the closed-entry receipt checks.
- [ ] T005 [US2] ORG-AUTH-R005 Accept a proposed entry with no owner and list it as unresolved in `render`.
- [ ] T006 [US1] ORG-AUTH-R001 Add public duplicate-authority entries, one capability per entry, with owner-native spec links and merged receipts before any entry closes.
