# Test and acceptance contract

## Content checks

- Confirm `profile/README.md` names exactly the five core repositories (Graph OS, Agent Web
  UI, Agent Utilities, Epistemic Graph, Agent Connector SDK), each with its stated
  responsibility, and that the dependency direction between them (Graph OS as the entry point,
  delegating to Agent Utilities; Epistemic Graph as the durable knowledge engine; Agent
  Connector SDK governing source integration) is stated in present tense.
- Confirm Agent Terminal UI and GeniusBot appear as additional operator surfaces and are not
  counted among the "five core projects."
- Confirm `site/index.html` and `site/skills.html` list a consistent component set and both
  link to the architecture explorer, `spec-status.html` and this repository's `CONTRIBUTING.md`;
  the profile links the bare explorer URL and no longer links `spec-status.html`.

## Link check

- Reject any `http://` or `https://` link in `profile/README.md`, `site/index.html`, or
  `site/skills.html` that does not return a successful response.
- Reject any relative link or image path in those files that does not resolve to a file in
  this repository.

## Rendering check

- Render `profile/README.md` through a GitHub-compatible Markdown renderer and confirm the
  component table, architecture image, and badge row display without broken markup.

## Acceptance evidence

Run the link check and the rendering check in a clean checkout and record the exact commit,
check output, and pass/fail result in `status.json`. ORG-FRONT-R001 is accepted only when both
checks pass against the same merged commit; publishing this spec is not itself acceptance.

## Spec-delivery links (ORG-FRONT-R002)

- R002.1 to R002.4: `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list`
  must pass. It makes no network call. The test compares the README links with `SPEC_DELIVERY_PAGES`.

## Canonical architecture explorer (ORG-FRONT-R003)

- R003.1: `tests/test_architecture_explorer_site.py::test_site_workflow_builds_the_explorer_on_a_schedule`
  reads the workflow and makes no network call.
- R003.2: `tests/test_front_door.py::test_front_door_links_the_explorer_at_the_top_level` reads the
  profile and README.
- R003.3: `python scripts/check_front_door.py` checks the live explorer URL; the recorded result is
  `evidence/links.json`.

## Agent contributability (ORG-FRONT-R004 to R007)

- ORG-FRONT-R004: `tests/test_requirement_progress.py::test_v2_verified_and_landed_count_as_delivered`, `::test_v2_sha_off_main_or_missing_demotes_with_a_reason`, `::test_v2_verified_needs_tests_and_unknown_states_are_rejected`, `::test_v2_retired_is_closed_and_leaves_the_denominator`; `tests/test_public_spec_report.py::test_v2_committed_specs_counts_verified_and_demotes_off_main`. No network call.
- ORG-FRONT-R005: `tests/test_public_spec_report.py::test_v2_committed_specs_counts_verified_and_demotes_off_main` (rendered page). No network call.
- ORG-FRONT-R006: `tests/test_front_door.py::test_agents_md_is_the_agent_front_door`. No network call.
- ORG-FRONT-R007: `tests/test_front_door.py::test_agent_entry_points_point_at_agents_md`. No network call.
