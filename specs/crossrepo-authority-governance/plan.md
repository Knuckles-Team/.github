# ORG-AUTH — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

The organization hub validates one public register of duplicate-authority decisions and shows unresolved entries on its status page. The live caller is the `Hub script tests` step (.github/workflows/tests.yml:24), which runs every test under `tests/`. The reuse candidates are `scripts/check_front_door.py` (`main` at line 108) for the command shape and `render` in `scripts/public_spec_report.py` (line 364) for the summary; no second validator framework or store is added.

## Technical Context

- **Language/Version**: Python 3.12 (the version pinned in .github/workflows/tests.yml)
- **Primary Dependencies**: the standard library only; pytest for tests
- **Storage**: N/A (one JSON file in the spec directory)
- **Testing**: pytest through `python -m pytest -q tests`; fixtures are inline dictionaries
- **Target Platform**: GitHub Actions runner and a local checkout
- **Project Type**: CLI scripts for a documentation and governance repository
- **Performance Goals**: N/A
- **Constraints**: public GitHub resources only; no network access during validation
- **Scale/Scope**: one register file and 5 rows

## Constitution Check

- I One owner per concept: pass. The register links to owner specs and never copies their receipts.
- II Extend before you create: pass. The validator follows `scripts/check_front_door.py` and the report reuses `render`.
- XXIV Complete rows: pass. Each row holds a caller chain, a shape and a planned test path.
- XXI Public files stay portable: pass. The register holds public URLs only.

## Project Structure

```text
scripts/authority_register.py                                  new       validate_register and its checks
tests/test_authority_register.py                               new       validator tests with inline fixtures
scripts/public_spec_report.py                                  existing  render lists unresolved entries
specs/crossrepo-authority-governance/authority-register.json   existing  the register, empty today
```

## Phase 0: Research

No unknowns. Every row names an existing caller and a new file at an exact path, so this spec adds no research.md.

## Phase 1: Design

The register is appendable and reviewable in ordinary pull requests. Changes to ownership or closure need review from the affected repositories. Report renderers may summarize the register but must preserve its source links and states. No central CI run can stand in for an owner's own acceptance evidence.

### Rollout

1. Add the register schema and a validator in this repository. Validate the
   version, required fields, decision transitions, URL and commit format, and that
   each entry has exactly one authority once `DECIDED`.
2. Inventory competing writers and duplicated behavior from public owner
   repositories. Add one entry per capability, with unresolved ownership left
   `PROPOSED` until contributors review the public designs.
3. Publish owner-native specs for each affected implementation and consumer.
   Link them from the register before setting `DECIDED`.
4. Migrate by component, with public implementation and negative test receipts.
   Link merged receipts before setting `CLOSED`.

## Phase 2: Task approach

Order the work producer first: the validator and its schema checks (R001), then the authority and link checks (R002, R003, R004), then the report summary (R005). Tasks on different checks run in parallel. Each task line in tasks.md names one row.

## Complexity Tracking

None. The constitution check passed with no violation.

## Build contract

The change must meet these gate thresholds from the organization constitution table.

- Cyclomatic complexity 10 and cognitive complexity 15 per function.
- Words per sentence 20 (`ste`).
- Clone similarity 0.85 blocking at 40 tokens (`dupehound`).

Repository commands: `python -m pytest -q tests` and `python scripts/check_front_door.py` from .github/workflows/tests.yml. No scanner gaming and no duplicate implementation: a check reuses the helper named in its `Shape:` sentence.

## Production caller chain

Entry point: the `Hub script tests` step (.github/workflows/tests.yml:24) runs `tests/test_authority_register.py` (planned), which calls `validate_register` in `scripts/authority_register.py` (planned) on the register file. The status page reaches the register through `main` (scripts/public_spec_report.py:450) and `render` (scripts/public_spec_report.py:364). Obsolete paths to delete: none.

## Cross-repo seams

None. The register links to owner and consumer specs by public URL and holds no wire contract with another repository.
