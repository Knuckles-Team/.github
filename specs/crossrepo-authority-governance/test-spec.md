# Test and acceptance contract

## Register validation

- Reject duplicate entry IDs, missing fields, malformed public URLs, incomplete
  commit SHAs, unknown decision states, and duplicate consumer names.
- Reject `DECIDED` entries without exactly one owner and a public owner spec.
- Reject `MIGRATING` entries without linked work for each affected writer and
  consumer.
- Reject `CLOSED` entries if any affected repository lacks merged
  implementation, test, and consumer or release receipts or still has a
  documented competing writer.
- Accept a `PROPOSED` entry with unresolved ownership, and keep it visibly
  unresolved in the HTML report.

## Acceptance evidence

Exercise the validator against positive and negative fixtures in a clean
checkout. For a real entry, inspect public owner and consumer specs, run the
relevant component tests, and verify linked commits are reachable from the
default branches. Record exact URLs and SHAs in the register. ORG-AUTH-R001
through ORG-AUTH-R005 are each accepted only when the register is populated
for the known cross-repository cases and every closed entry satisfies the
receipts above; merely publishing this spec is not acceptance.
