# ORG-FRONT-001 requirements

| ID | Requirement | Verification |
|---|---|---|
| `ORG-FRONT-R001` | **Organization front door describes the five-repository flow.** The organization-level README presents the ecosystem's five public repositories in present tense, with an accurate description of how the web UI connects to the graph engine service, and only links that resolve successfully. | An automated link check confirms every linked URL in the front door returns HTTP 200, and a rendering check confirms the page displays correctly on GitHub. |
| `ORG-FRONT-R002` | **The organisation README links every repository's spec-delivery page.** The organisation README must link each repository page at `https://knuckles-team.github.io/<repo>/spec-delivery/`. Children implement `PIPE-PAGES-R014.5` (organisation, then repository, then spec). | Children R002.1 to R002.4 pass. |
| `ORG-FRONT-R002.1` | **One list names the repositories with a page.** `SPEC_DELIVERY_PAGES` in `scripts/public_spec_report.py` must list only repositories whose page returns HTTP 200. | `tests/test_front_door.py::test_readme_spec_delivery_links_match_the_single_list` |
| `ORG-FRONT-R002.2` | **A generated block renders the section.** `scripts/spec_delivery_links.py --write` must render the block between the spec-delivery markers in `profile/README.md`. | Same test; the block equals `render()`. |
| `ORG-FRONT-R002.3` | **The README links match the list.** Every spec-delivery link in `profile/README.md` must equal the list and use the exact page form. | Same test. |
| `ORG-FRONT-R002.4` | **Each repository block links its page.** Each per-repository block in the README should carry a "Spec delivery" link when its page exists. | Same test. |
