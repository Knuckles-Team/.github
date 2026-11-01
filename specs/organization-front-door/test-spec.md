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
check output, and pass/fail result in the evidence directory. ORG-FRONT-R001 is accepted only when both
checks pass against the same merged commit; publishing this spec is not itself acceptance.

## Spec-delivery links (ORG-FRONT-R002)

- R002.1 to R002.4: `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list`
  must pass. It makes no network call. The test compares the README links with `SPEC_DELIVERY_PAGES`.
- `tests/test_front_door.py::test_front_doors_use_canonical_repository_and_pages_urls`
  rejects retired repository and Pages URLs after repository renames without changing package names.

## Canonical architecture explorer (ORG-FRONT-R003)

- R003.1: `tests/test_architecture_explorer_site.py::test_site_workflow_builds_the_explorer_on_a_schedule`
  reads the workflow and makes no network call.
- R003.2: `tests/test_front_door.py::test_front_door_links_the_explorer_at_the_top_level` reads the
  profile and README.
- R003.3: `python scripts/check_front_door.py` checks the live explorer URL; the recorded result is
  `evidence/links.json`.

## Agent contributability (ORG-FRONT-R004 to R007)

- ORG-FRONT-R004: `tests/test_requirement_progress.py::test_v2_verified_and_landed_count_as_delivered`, `::test_v2_sha_off_main_or_missing_demotes_with_a_reason`, `::test_v2_verified_needs_tests_and_unknown_states_are_rejected`, `::test_v2_retired_is_closed_and_leaves_the_denominator`; `tests/test_public_spec_report.py::test_v2_committed_specs_counts_verified_and_demotes_off_main`. No network call.
- ORG-FRONT-R005: `tests/test_public_spec_report.py::test_v2_committed_specs_counts_verified_and_demotes_off_main` (rendered page); `tests/test_public_spec_report.py::test_every_reported_repo_is_checked_out_by_the_pages_workflow` (every reported repository, including Axil, is checked out). No network call.
- ORG-FRONT-R005: `tests/test_public_spec_report.py::test_renamed_repositories_keep_the_workflow_checkout_paths` checks canonical report owners and their explicit existing checkout paths. No network call.
- ORG-FRONT-R006: `tests/test_front_door.py::test_agents_md_is_the_agent_front_door`. No network call.
- ORG-FRONT-R007: `tests/test_front_door.py::test_agent_entry_points_point_at_agents_md`. No network call.
- ORG-FRONT-R008: `tests/test_front_door.py::test_site_llms_txt_points_agents_at_the_front_door_and_contribution_path`. No network call.

## Canopy status and publishing (ORG-FRONT-R009, ORG-FRONT-R010)

- T-ORG-FRONT-R009: ORG-FRONT-R009 | The rollup is the minimum state of its children.
- T-ORG-FRONT-R009.1: ORG-FRONT-R009.1 | Test: `tests/test_public_spec_report.py::test_status_documents_are_generated_from_the_head_commit`. Add `read_status_documents(repo, head)` to `scripts/public_spec_report.py`.
- T-ORG-FRONT-R009.2: ORG-FRONT-R009.2 | Test: `tests/test_public_spec_report.py::test_spec_without_a_committed_manifest_is_evaluated_from_generated_status`. Replace the manifest lookup in `committed_specs`.
- T-ORG-FRONT-R009.3: ORG-FRONT-R009.3 | Test: `tests/test_architecture_explorer_site.py::test_render_step_follows_the_generator_checkout_and_sets_pythonpath`. Move the `Checkout architecture explorer generator` step before `Render from public committed specs` in the site workflow.
- T-ORG-FRONT-R009.4: ORG-FRONT-R009.4 | Test: `tests/test_public_spec_report.py::test_a_shallow_checkout_fails_the_render_with_status_uncomputable`. When the generator cannot run for a repository, the render fails with the typed finding `status-uncomputable` and the repository name.
- T-ORG-FRONT-R009.5: ORG-FRONT-R009.5 | Test: `tests/test_public_spec_report.py::test_page_states_computed_head_and_generator_commit_and_no_missing_manifest_text`. Each repository block states the head commit it computed and the generator commit it used.
- T-ORG-FRONT-R009.6: ORG-FRONT-R009.6 | Test: `tests/test_public_spec_report.py::test_cli_renders_landed_state_for_a_repository_without_committed_status`. Use entry point `python scripts/public_spec_report.py --repo X=<fixture> --output <file>` on a real temporary Git repository.
- T-ORG-FRONT-R010: ORG-FRONT-R010 | The rollup is the minimum state of its children.
- T-ORG-FRONT-R010.1: ORG-FRONT-R010.1 | Test: `tests/test_architecture_explorer_site.py::test_workflow_checks_out_releases_for_the_explorer`. Add `releases` to the sparse checkout of the generator in the site workflow.
- T-ORG-FRONT-R010.2: ORG-FRONT-R010.2 | Test: `tests/test_architecture_explorer_site.py::test_workflow_verifies_the_export_files_before_upload`. The upload step publishes `architecture/export/rows.json` and `architecture/export/rows.md` with the page.
- T-ORG-FRONT-R010.3: ORG-FRONT-R010.3 | Test: `tests/test_front_door.py::test_site_llms_txt_names_the_canopy_export_and_hash_forms`. `site/llms.txt` names the export URLs and the Canopy hash forms `#row=`, `#part=`, `#mode=`, `#filter=` and `#release=`.

## Row entries for the earlier children

- T-ORG-FRONT-R002.1: ORG-FRONT-R002.1 | Test: `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list`.
- T-ORG-FRONT-R002.2: ORG-FRONT-R002.2 | Test: `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list`.
- T-ORG-FRONT-R002.3: ORG-FRONT-R002.3 | Test: `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list`.
- T-ORG-FRONT-R002.4: ORG-FRONT-R002.4 | Test: `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list`.
- T-ORG-FRONT-R003.1: ORG-FRONT-R003.1 | Test: `tests/test_architecture_explorer_site.py::test_site_workflow_builds_the_explorer_on_a_schedule`.
- T-ORG-FRONT-R003.2: ORG-FRONT-R003.2 | Test: `tests/test_front_door.py::test_front_door_links_the_explorer_at_the_top_level`.
- T-ORG-FRONT-R003.3: ORG-FRONT-R003.3 | Test: `tests/test_front_door.py::test_audit_never_hides_a_broken_destination`.
- T-ORG-FRONT-R011: ORG-FRONT-R011 | Test: `tests/test_front_door.py::test_tests_workflow_emits_the_single_required_check`. The `ci-required` job is named `CI required`, runs always and needs `pytest`.
