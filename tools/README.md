# Tools

`lint.py` is the gate every change passes before it merges: it catches the setext trap (body text directly above a dashed rule renders as a heading), overlong headings, malformed tables, forbidden characters, and broken image links, and it prints a census of the highest statement identifier per prefix so counts stated in prose can be checked against reality.

Run it from the repository root:

    python3 tools/lint.py

The repository's content files (README, TERMINOLOGY, core chapters, metrics, profiles, examples, and the single-file edition) are emitted together from one source by a build pipeline maintained alongside the repository, so no file is hand-synced against another. Continuous integration running this lint on every change is on the roadmap; until then, running it locally before a pull request is the contract.
