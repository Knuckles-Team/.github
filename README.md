# Graph OS organization hub

The [organization profile](profile/README.md) introduces the Graph OS ecosystem.
The [build-first program](site/build-first.html) tracks provisional queued and
building obligations. The [specification status report](site/spec-status.html) is generated from committed
`specs/*/status.json` in ten public owner repositories and this organization hub. The [contribution
guide](CONTRIBUTING.md) points contributors to the owner-native design, tasks,
tests, and reusable development skills.

The [Pages workflow](.github/workflows/spec-status-pages.yml) rebuilds the report
from public `main` branches on each hub change, daily, and on manual dispatch.
The report is a snapshot with source revisions, not a live CI feed. `SPECIFIED`
is the build queue; `LANDED` and `ACCEPTED` require separate public evidence.
The build-first program marks design review pending for every item. Its owner
assignments are provisional: partition or owner-review rows expose candidate
specs but no normative owner spec until an explicit reviewed decision exists.
A linked ID alone does not make a spec complete.

To render locally, clone the ten public owner repositories under one directory and run
`python scripts/public_spec_report.py --checkouts-root <directory> --repo .github=. --output site/spec-status.html`.
See `python scripts/public_spec_report.py --help` for explicit checkout paths.
