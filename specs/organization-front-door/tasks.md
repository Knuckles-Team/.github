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
