# Validation record

This file records completed checks and their limits. Structural validation and behavioral evaluation are reported separately. Synthetic scenarios contain no user research data.

## Package checks

Completed locally on October 22, 2026 (America/Phoenix; October 23 UTC):

- The bundled standard-library validator passed for all three entrypoints, local Markdown references, self-contained skill links, and JSON records.
- The installed Skill Creator's `quick_validate.py` passed each skill using an existing Python environment with PyYAML. That external validator is a development check, not a runtime dependency of these skills.
- All added Python scripts compiled successfully.
- Four installer tests passed: copy fidelity, identical-rerun idempotence and backup preservation in one test; top-level symlink refusal before mutation; nested-symlink refusal; and rejection of repository-overlapping targets.
- An independent reviewer also exercised fresh installation, identical rerun, backup preservation, and nested-symlink refusal in temporary fixtures.
- The publication file set contains only reusable text assets. Checks found no user research documents or known machine-specific identifiers in the package.

The installer checks establish the exercised file-preservation behavior. They do not prove behavior under every filesystem failure or activate a live host installation.

## Behavioral forward test

A fresh evaluation agent received the candidate paths and six synthetic user requests without the authoring conversation, intended answers, or scoring rubric. It read the three entrypoints and seven relevant references, used no web search, and saved its actual outputs. The author then inspected those outputs against the predefined scenarios.

| Scenario | Observed outcome |
| --- | --- |
| A1: scientific review and polish | Preserved all reported quantities and identified unsupported robustness, optical, and kinetic claims; proposed bounded prose |
| A2: foundation grant fit | Followed the supplied call, used prospective wording, and identified the assay dependency and unresolved fallback without inventing results |
| A3: reviewer responses | Answered all concerns, verified only the supplied excerpt, kept kinetic work pending, and invented no manuscript edits or locators |
| A4: light polish | Returned one grammatical correction with the numerical facts intact and no added review workflow |
| L1: evidence synthesis | Recognized duplicate reports of one experiment, abstract-only access, sequence/salt confounding, and limits on kinetics-gap claims |
| R1: research ideation | Proposed assembly and reporter mechanisms, discriminating controls and structural readouts, and an informative pilot without invented sample size, cost, or outcome |

See [scenario prompts and assessment criteria](../evals/scenarios.md) and the [actual fresh-pass outputs](../evals/observed.md). The light-polish output changed `MgCl2` to typographic `MgCl₂` without changing the chemical identity.

Earlier development evaluations exposed one wording ambiguity: editing authority had been conflated with the ability to verify an already supplied revision. The instruction was corrected to make verification depend on available evidence and to state the limits of excerpt-only checking. The fresh six-task pass used the corrected wording and exposed no further concrete defect.

## Limits

This is a small synthetic forward test of the updated skills, not a statistical benchmark. There was no comparison against the original July skills, no independent human scientific panel, no empirical grant or publication outcome measurement, and no automatic-discovery test in Claude Code or other hosts. The evaluators were separate agents in the same Codex environment; this does not establish performance across models.

The GitHub Actions workflow repeats package and installer checks. A local pass is recorded above; remote CI results must be checked separately after publication.

## Academic-writing v1.1.0 expansion: October 23, 2026

The entrypoint grew from 631 to 644 whitespace-separated words, including metadata. Three conditional references were added: supplementary information (510 words), academic applications (818 words), and peer review (641 words). The other two skill packages were unchanged. Reference detail is loaded only when relevant, rather than adding all of it to every writing task.

### Research and test setup

The [research review](research.md#academic-writing-expansion-october-23-2026) documents nine inspected skill entrypoints across six repositories, official skill-authoring guidance, and primary genre guidance. It distinguishes selected-section inspection from full-package execution, records source-access limits, and states the adopted design rules.

Ten [synthetic prompts](../evals/expansion-prompts.json) and [criteria](../evals/expansion-criteria.md) were fixed before changing the skill. A frozen copy was checked byte-for-byte against the published v1.0.0 files in commit `c3d1b01c110966d22e22903c110c7df42451f2e7`. Separate fresh agents executed the baseline and revised skill with the same prompts, without criteria, authoring context, or each other's outputs. A third fresh agent assessed both outputs against the fixed criteria and verified the requested counts with Python. The assessment was not blinded to version labels.

### Observed results

| Scenario | Baseline | Revised skill |
| --- | --- | --- |
| S1: main/SI evidence conflicts, methods, labels, and availability | Meets criteria | Meets criteria |
| A1: award contribution, impact limits, and publication status | Meets criteria | Meets criteria |
| A2: fellowship development/research separation and host commitments | Meets criteria | Meets criteria |
| A3: conference abstract/travel fields, status, need, and word limits | Meets criteria | Meets criteria |
| A4: academic job package and truthful teaching evidence | Meets criteria | Meets criteria |
| P1: soundness-based referee report and advisory recommendation | Meets criteria | Meets criteria |
| P2: prospective proposal review under the supplied rubric | Meets criteria | Meets criteria |
| E1: light award polish preserves factual status | Meets criteria | Meets criteria |
| R1: reviewer response keeps unperformed kinetics pending | Meets criteria | Meets criteria |
| E2: light reviewer-report polish preserves the judgment | Meets criteria | Meets criteria |

Actual outputs: [baseline](../evals/expansion-baseline.md), [revised](../evals/expansion-candidate.md), and [independent assessment](../evals/expansion-assessment.md). Task outputs are preserved; execution-record paths were normalized for portability. Independently verified counts were 34 versus 23 words for the award statement, 52 versus 52 for the conference abstract, and 39 versus 31 for the travel statement. All met the supplied limits under Python `len(text.split())`; shorter output alone is not a quality improvement.

Both versions disclosed missing impact and financial-need evidence rather than inventing it. No material unsupported claim or scope failure was identified in either execution. These cases demonstrate explicit supported coverage and regression behavior; they do not demonstrate candidate superiority. The new references make the intended genre decisions available and maintainable even though the capable baseline already handled these examples.

### Package checks and limits

The bundled validator and the installed Skill Creator validator passed, as did all four installer tests using temporary fixtures. No new runtime script, paid service, required companion skill, or automatic delegation was added. User research documents and machine-specific identifiers were excluded from publication files.

This is one execution per version per synthetic task, in the same Codex environment. There was no independent human panel, multi-model study, full-document rendering, actual applicant-record verification, or measurement of successful submissions. Automatic skill discovery in any host remains untested. These limits are separate from passing package checks and remote CI.
