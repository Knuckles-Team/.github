# Work items

- [ ] Audit `profile/README.md` against the shipped repositories and correct any stale name,
      responsibility, or dependency-direction description, keeping the five-core-repository
      framing consistent with the component cards (ORG-FRONT-R001).
- [ ] Audit `site/index.html` and `site/skills.html` against `profile/README.md` for the same
      component set, names, and responsibilities, and reconcile any mismatch (ORG-FRONT-R001).
- [ ] Build or run a link checker against every `http(s)://` and relative link in
      `profile/README.md`, `site/index.html`, and `site/skills.html`; fix or remove any link
      that does not resolve (ORG-FRONT-R001).
- [ ] Render `profile/README.md` through a GitHub-compatible Markdown renderer and confirm the
      component table, architecture image, and badges display correctly (ORG-FRONT-R001).
- [ ] Run this repository's test suite (`pytest`) and applicable language linters against any
      changed script, and record the exact commit, check output, and pass/fail result in
      `status.json` before marking ORG-FRONT-R001 delivered.
