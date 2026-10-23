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
