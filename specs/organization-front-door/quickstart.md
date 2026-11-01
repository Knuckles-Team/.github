# ORG-FRONT — Quickstart

Prove the status fix with `pytest tests/test_public_spec_report.py::test_cli_renders_landed_state_for_a_repository_without_committed_status`.
The test builds a temporary Git repository with a landing trailer and no `status.json`, runs `python scripts/public_spec_report.py`, and checks that the page shows LANDED and omits `No committed status.json`.
