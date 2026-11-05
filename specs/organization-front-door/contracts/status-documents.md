# Status documents seam

Provider: pipelines PIPE-GATES-R027
Consumer: .github ORG-FRONT-R009.1

## Wire shape

`generate_at(source, commit)` in the pipelines repository (`pipelines_hooks/specs/generator.py:168`) returns a map from each `specs/<dir>/status.json` path to its schema version 2 document, computed from the rows, trailers and bindings at one commit. `read_status_documents(repo, head)` in `scripts/public_spec_report.py` (planned) calls it on a local clone and keeps the map unchanged. A path with no spec directory is absent from the map.

## Refusal codes

The generator raises no stable codes of its own. A commit it cannot read fails the call, and the report builder treats that repository as having no status documents instead of inventing states.

## Authoritative types

The schema version 2 status document written by the pipelines generator. This repository holds no copy of the schema.

## Test vectors

Planned `tests/test_public_spec_report.py::test_status_documents_are_generated_from_the_head_commit` builds a fixture repository and compares the map with the generator output.
