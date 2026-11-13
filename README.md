# PMO First Principles

**Project management fundamentals for everyone who leads projects—even when their job title isn't “Project Manager.”**

A public, independent learning toolkit with ten concise lessons, real-world-style fictional examples, a knowledge check, downloadable practice templates, and a lightweight self-assessment. Open the [learning academy](https://dietricheubank.github.io/pmo-first-principles/) after site publication, or run locally with `python -m http.server 8000` and visit `http://localhost:8000`.

## Purpose

Create a practical, accessible path from vague request to well-governed, measurable outcome. No PMI certification or formal PM role is required.

The project is informed by the author's experience developing broad project management enablement resources at The Ohio State University. **This is newly written educational material**, not a reproduction of university-owned courses, slides, graphics, files, or official standards. No endorsement or affiliation is implied.

## Modules

1. Projects and outcomes
2. The sponsor and the charter
3. Stakeholders and communication
4. Scope and deliverables
5. Schedule and dependencies
6. Capacity and resources
7. Risks, issues, assumptions, decisions
8. Execution and transparent status
9. Change control and governance
10. Transition, closure and benefits

## Use

1. Read the lesson and fictional scenario.
2. Work through the exercise using the corresponding [templates](templates/).
3. Answer the knowledge check and review your results.
4. Run the [maturity self-assessment](assess.py) for a quick improvement conversation, not an audit or certification.

The web course persists progress only in browser local storage. Use Reset to clear it. No accounts, server or analytics.

## Command-line maturity assessment

```bash
python assess.py examples/team-assessment.json
python -m unittest discover -s tests -v
```

## Quality and safeguards

- Ten lessons stored as versionable JSON; validated by Python tests.
- HTML web academy uses vanilla JavaScript and responsive CSS.
- Synthetic case studies, invented examples and no employer-specific data.
- Completion badge is **informal**, not a professional credential.
- MIT-licensed original content and code; third-party trademarks excluded.

## Roadmap

Add instructor guides, optional group exercises, deeper scenario simulations, accessible downloadable worksheets, expanded question bank, original instructional video narration and printable study packets.

## Original OSU documentation

The author led development of an OSU PM Resource Center. The original training decks and job aids were **not available** when this public repository was initially authored; module titles and content are new, not claimed to match the historical course. University-owned material should be referenced or adapted only with appropriate authorization.
