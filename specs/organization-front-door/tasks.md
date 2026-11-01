# Work items

- [x] T101 [P] [US1] ORG-FRONT-R001 Audit `profile/README.md`, `site/index.html` and `site/skills.html` against the shipped repositories. Reconcile every name, responsibility and link, and keep the five-core-repository framing consistent. Bound to tests/test_front_door.py::test_component_roles_and_navigation_remain_consistent.

Audit source: `5e674839fb10e1aea4e3f11468fe804636fdd8b6`. See [complete evidence](evidence/audit.json), [test output](evidence/pytest.txt), and [independent review](evidence/independent-review.json).

- [x] T010 [P] [US1] ORG-FRONT-R002.1 Model. Add `SPEC_DELIVERY_PAGES` to `scripts/public_spec_report.py`. Bound to tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list.
- [x] T011 [P] [US1] ORG-FRONT-R002.2 Wiring. Add `scripts/spec_delivery_links.py` and the marker block in `profile/README.md`. Bound to tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list.
- [x] T012 [P] [US1] ORG-FRONT-R002.3 Behavior. Add `test_readme_spec_delivery_links_match_the_single_list` to `tests/test_front_door.py`. Bound to tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list.
- [x] T013 [P] [US1] ORG-FRONT-R002.4 Behavior. Add a "Spec delivery" link to each per-repository block in `profile/README.md`. Bound to tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list.
- [x] T014 [P] [US1] ORG-FRONT-R003.1 Wiring. Build the explorer in `spec-status-pages.yml` on a 30-minute schedule and on dispatch. Bound to tests/test_architecture_explorer_site.py::test_site_workflow_builds_the_explorer_on_a_schedule.
- [x] T015 [P] [US1] ORG-FRONT-R003.2 Behavior. Point the profile's specification-status links and the runtime diagram at the explorer. Bound to tests/test_front_door.py::test_front_door_links_the_explorer_at_the_top_level.
- [x] T016 [P] [US1] ORG-FRONT-R003.3 Evidence. Regenerate `evidence/links.json` with the explorer URL passing. Bound to scripts/check_front_door.py::main.
- [x] T017 [P] [US1] ORG-FRONT-R004 Behavior. The status report reads schema version 2 natively. Bound to tests/test_requirement_progress.py::test_v2_verified_and_landed_count_as_delivered.
- [x] T018 [P] [US1] ORG-FRONT-R005 Behavior. The status page shows the state breakdown. Bound to tests/test_public_spec_report.py::test_v2_committed_specs_counts_verified_and_demotes_off_main.
- [x] T019 [P] [US1] ORG-FRONT-R006 Behavior. A root `AGENTS.md` is the agent front door. Bound to tests/test_front_door.py::test_agents_md_is_the_agent_front_door.
- [x] T020 [P] [US1] ORG-FRONT-R007 Wiring. Agent entry points are wired in. Bound to tests/test_front_door.py::test_agent_entry_points_point_at_agents_md.
- [x] T021 [P] [US1] ORG-FRONT-R008 Behavior. A plain-text pointer serves agents. Bound to tests/test_front_door.py::test_site_llms_txt_points_agents_at_the_front_door_and_contribution_path.

- [ ] T001 [P] [US1] ORG-FRONT-R009.1 Model. Add `read_status_documents(repo, head)` to `scripts/public_spec_report.py`. Bound to tests/test_public_spec_report.py::test_status_documents_are_generated_from_the_head_commit.
- [ ] T002 [P] [US1] ORG-FRONT-R009.2 Behavior. Replace the manifest lookup in `committed_specs`. Bound to tests/test_public_spec_report.py::test_spec_without_a_committed_manifest_is_evaluated_from_generated_status.
- [ ] T003 [P] [US1] ORG-FRONT-R009.3 Wiring. Move the `Checkout architecture explorer generator` step before `Render from public committed specs` in the site workflow. Bound to tests/test_architecture_explorer_site.py::test_render_step_follows_the_generator_checkout_and_sets_pythonpath.
- [ ] T004 [P] [US1] ORG-FRONT-R009.4 Refusal. When the generator cannot run for a repository, the render fails with the typed finding `status-uncomputable` and the repository name. Bound to tests/test_public_spec_report.py::test_a_shallow_checkout_fails_the_render_with_status_uncomputable.
- [ ] T005 [P] [US1] ORG-FRONT-R009.5 Evidence. Each repository block states the head commit it computed and the generator commit it used. Bound to tests/test_public_spec_report.py::test_page_states_computed_head_and_generator_commit_and_no_missing_manifest_text.
- [ ] T006 [P] [US1] ORG-FRONT-R009.6 Hot-path proof. Use entry point `python scripts/public_spec_report.py --repo X=<fixture> --output <file>` on a real temporary Git repository. Bound to tests/test_public_spec_report.py::test_cli_renders_landed_state_for_a_repository_without_committed_status.
- [ ] T007 [P] [US1] ORG-FRONT-R010.1 Wiring. Add `releases` to the sparse checkout of the generator in the site workflow. Bound to tests/test_architecture_explorer_site.py::test_workflow_checks_out_releases_for_the_explorer.
- [ ] T008 [P] [US1] ORG-FRONT-R010.2 Evidence. The upload step publishes `architecture/export/rows.json` and `architecture/export/rows.md` with the page. Bound to tests/test_architecture_explorer_site.py::test_workflow_verifies_the_export_files_before_upload.
- [ ] T009 [P] [US1] ORG-FRONT-R010.3 Behavior. `site/llms.txt` names the export URLs and the Canopy hash forms `#row=`, `#part=`, `#mode=`, `#filter=` and `#release=`. Bound to tests/test_front_door.py::test_site_llms_txt_names_the_canopy_export_and_hash_forms.
