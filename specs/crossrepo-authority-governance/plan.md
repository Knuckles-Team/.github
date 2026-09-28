# Architecture and rollout

1. Add the register schema and a validator in this repository. Validate the
   version, required fields, decision transitions, URL/commit format, and that
   each entry has exactly one authority once `DECIDED`.
2. Inventory competing writers and duplicated behavior from public owner
   repositories. Add one entry per capability, with unresolved ownership left
   `PROPOSED` until contributors review the public designs.
3. Publish owner-native specs for each affected implementation and consumer.
   Link them from the register before setting `DECIDED`.
4. Migrate by component, with public implementation and negative test receipts.
   Link merged receipts before setting `CLOSED`.

The register is appendable and reviewable in ordinary pull requests. Changes
to ownership or closure need review from the affected repositories. Report
renderers may summarize the register but must preserve its source links and
states. No central CI run can stand in for an owner's own acceptance evidence.
