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
  link to `spec-status.html` and this repository's `CONTRIBUTING.md`.

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
