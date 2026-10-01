# Graph OS organization hub

The [organization profile](profile/README.md) introduces the Graph OS ecosystem.
The [repositories and skills map](site/skills.html) links the public owners,
universal-skills kit, and canonical `graph-os-development` instructions.
The [specification status report](site/spec-status.html) is generated from committed
`specs/*/status.json` in the public owner repositories and this organization hub. It shows, per
repository and per specification, how many requirements are delivered and which are still open. The [contribution
guide](CONTRIBUTING.md) points contributors to the owner-native design, tasks,
tests, and reusable development skills.

The [Pages workflow](.github/workflows/spec-status-pages.yml) rebuilds the report
from public `main` branches on each hub change, daily, and on manual dispatch.
The report is a snapshot with source revisions, not a live CI feed. `SPECIFIED`
is the build queue; `LANDED` and `ACCEPTED` require separate public evidence.
Each requirement ID is defined in its owner spec's `requirements.md` and carries its own
delivery state in `status.json`. A requirement counts toward the completion percentage only
when its entry cites an implementing commit on the owner repository's default branch.

To render locally, clone the public owner repositories under one directory and run
`python scripts/public_spec_report.py --checkouts-root <directory> --repo .github=. --output site/spec-status.html`.
See `python scripts/public_spec_report.py --help` for explicit checkout paths.
