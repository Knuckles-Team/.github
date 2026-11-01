# Work items

- [x] Audit `profile/README.md` against the shipped repositories and correct any stale name,
      responsibility, or dependency-direction description, keeping the five-core-repository
      framing consistent with the component cards (ORG-FRONT-R001).
- [x] Audit `site/index.html` and `site/skills.html` against `profile/README.md` for the same
      component set, names, and responsibilities, and reconcile any mismatch (ORG-FRONT-R001).
- [x] Build or run a link checker against every `http(s)://` and relative link in
      `profile/README.md`, `site/index.html`, and `site/skills.html`; fix or remove any link
      that does not resolve (ORG-FRONT-R001).
- [x] Render `profile/README.md` through a GitHub-compatible Markdown renderer and confirm the
      component table, architecture image, and badges display correctly (ORG-FRONT-R001).
- [x] Run this repository's test suite (`pytest`) and applicable language linters against any
      changed script, and record the exact commit, check output, and pass/fail result in
      `status.json` before marking ORG-FRONT-R001 delivered.

Audit source: `5e674839fb10e1aea4e3f11468fe804636fdd8b6`. See [complete evidence](evidence/audit.json), [test output](evidence/pytest.txt), and [independent review](evidence/independent-review.json).

- [ ] ORG-FRONT-R002.1: add `SPEC_DELIVERY_PAGES` to `scripts/public_spec_report.py`.
- [ ] ORG-FRONT-R002.2: add `scripts/spec_delivery_links.py` and the marker block in `profile/README.md`.
- [ ] ORG-FRONT-R002.3: add `test_readme_spec_delivery_links_match_the_single_list` to `tests/test_front_door.py`.
- [ ] ORG-FRONT-R002.4: add a "Spec delivery" link to each per-repository block in `profile/README.md`.
- [ ] ORG-FRONT-R003.1: build the explorer in `spec-status-pages.yml` on a 30-minute schedule and on dispatch.
- [ ] ORG-FRONT-R003.2: point the profile's specification-status links and the runtime diagram at the explorer.
- [ ] ORG-FRONT-R003.3: regenerate `evidence/links.json` with the explorer URL passing.
- [ ] ORG-FRONT-R004: the status report reads schema version 2 natively.
- [ ] ORG-FRONT-R005: the status page shows the state breakdown.
- [ ] ORG-FRONT-R006: a root agents.md is the agent front door.
- [ ] ORG-FRONT-R007: agent entry points are wired in.
- [ ] ORG-FRONT-R008: a plain-text pointer serves agents.

- [ ] T001 [P] [US1] ORG-FRONT-R009.1 Model. Add `read_status_documents(repo, head)` to `scripts/public_spec_report.py`. Bound to tests/test_public_spec_report.py::test_status_documents_are_generated_from_the_head_commit.
- [ ] T002 [P] [US1] ORG-FRONT-R009.2 Behavior. Replace the manifest lookup in `committed_specs`. Bound to tests/test_public_spec_report.py::test_spec_without_a_committed_manifest_is_evaluated_from_generated_status.
- [ ] T003 [P] [US1] ORG-FRONT-R009.3 Wiring. Move the `Checkout architecture explorer generator` step before `Render from public committed specs` in the site workflow. Bound to tests/test_architecture_explorer_site.py::test_render_step_follows_the_generator_checkout_and_sets_pythonpath.
- [ ] T004 [P] [US1] ORG-FRONT-R009.4 Refusal. When the generator cannot run for a repository, the render fails with the typed finding `status-uncomputable` and the repository name. Bound to tests/test_public_spec_report.py::test_a_shallow_checkout_fails_the_render_with_status_uncomputable.
- [ ] T005 [P] [US1] ORG-FRONT-R009.5 Evidence. Each repository block states the head commit it computed and the generator commit it used. Bound to tests/test_public_spec_report.py::test_page_states_computed_head_and_generator_commit_and_no_missing_manifest_text.
- [ ] T006 [P] [US1] ORG-FRONT-R009.6 Hot-path proof. Use entry point `python scripts/public_spec_report.py --repo X=<fixture> --output <file>` on a real temporary Git repository. Bound to tests/test_public_spec_report.py::test_cli_renders_landed_state_for_a_repository_without_committed_status.
- [ ] T007 [P] [US1] ORG-FRONT-R010.1 Wiring. Add `releases` to the sparse checkout of the generator in the site workflow. Bound to tests/test_architecture_explorer_site.py::test_workflow_checks_out_releases_for_the_explorer.
- [ ] T008 [P] [US1] ORG-FRONT-R010.2 Evidence. The upload step publishes `architecture/export/rows.json` and `architecture/export/rows.md` with the page. Bound to tests/test_architecture_explorer_site.py::test_workflow_verifies_the_export_files_before_upload.
- [ ] T009 [P] [US1] ORG-FRONT-R010.3 Behavior. `site/llms.txt` names the export URLs and the Canopy hash forms `#row=`, `#part=`, `#mode=`, `#filter=` and `#release=`. Bound to tests/test_front_door.py::test_site_llms_txt_names_the_canopy_export_and_hash_forms.
