# Synthetic task outputs

## S1

Proposed package organization:

- Main manuscript: introduce the question; report the supported structural result and its conditions; present the control evidence needed for specificity; discuss the limits of the tested preparations and conditions. Keep essential evidence for the central claim assessable in the main argument, even if detailed control data appear in SI.
- Separate SI PDF: supplementary methods, supplementary results and controls, then individually labelled supplementary figures and tables. Provide captions that state conditions, preparation counts, analysis populations, and what each panel shows.
- Separate machine-readable numerical data, with identifiers linking records to the corresponding figures and analyses. Provide a data dictionary where needed.

Corrections and unresolved facts:

| Location | Issue | Concrete action |
| --- | --- | --- |
| Main result versus SI | Three independent preparations are claimed, but only one is documented. | Reconcile the preparation records and identify what the 82% summarizes, including its denominator and treatment of individual preparations. One documented preparation does not establish that only one was performed. Retain three only if supporting records exist; otherwise revise to the supported count. |
| Main result versus SI caption | 10 mM and 5 mM MgCl2 conflict. | Check experimental records and correct every affected description; do not select a value by inference. |
| Figures and main callout | Two figures are labelled S2; Fig. S3 is absent. | Inventory figures, assign unique sequential labels, then reconcile captions and every callout. Determine which figure the S3 citation intended; do not silently assign it to either S2. |
| Specificity claim | The detailed control observation is unavailable. | Supply the actual control design, conditions, observation, and analysis if available. Until assessed, remove or qualify “the control establishes specificity”; the supplied record does not substantiate it. |
| Methods | Calibration, processing, and exact temperature are unreported here. | Add the actual records or explicitly identify what cannot be recovered. These are reporting gaps, not proof that the procedures were omitted. |
| Code availability | Public availability is claimed without a repository or release. | Verify a working repository and identifiable release before retaining the claim. Pending that check, use an internal placeholder: “Code availability: [repository, release, and access details to be confirmed].” |

No files were edited. The supplied material cannot establish the correct MgCl2 concentration, actual preparation count, specificity, or public code availability. The proposed package follows the supplied mock journal's separation of SI and numerical data.

## A1

Award statement (34 words):

As a postdoctoral researcher, I developed the analysis pipeline for a team research project. This is my identifiable technical contribution to the team's work. My publication record includes one accepted article and one preprint.

Missing support: demonstrated impact remains unsupported. Supply documented uptake, a concrete change enabled by the pipeline, or another award-relevant impact with evidence; citation or adoption counts are not the only possible evidence. Clarify the applicant's specific role if more detail is available. Remove the claims of independent laboratory leadership and funding unless supported. An accepted article and a preprint must not be described as two peer-reviewed publications. “Transformed the field” is unsupported. No research proposal is required by this award.

## A2

Personal/development statement outline:

1. Preparation: describe actual sequence-design experience and the applicant's own contributions.
2. Development need: explain the transition to structural characterization and identify the skills to learn.
3. Proposed learning: outline training activities and how progress would be demonstrated; retain these as proposed until arrangements exist.
4. Host fit: connect the potential host's relevant instrumentation to the learning needs. Identify equipment access, mentorship, and training arrangements as unconfirmed.
5. Longer-term development: explain how the new training would complement sequence design, using the applicant's own goals.

Research-plan statement outline:

1. Define the question and objective, distinguishing the proposed project from completed work.
2. Describe the planned structural assay, comparison, controls, readouts, and analysis.
3. Establish feasibility through the relevant existing expertise and proposed facilities, with access still to be confirmed.
4. Include an early assay-feasibility decision, a feasible alternative if the assay fails, a realistic timeline, and assessable outputs. Specific success criteria need justification rather than invented thresholds.

Corrected factual framing: “I bring experience in sequence design and seek training in structural characterization. The proposed project has no experimental results yet. A potential host has relevant instrumentation; hosting, equipment access, mentorship, and training arrangements remain to be confirmed.”

Delete “My host has committed equipment and mentorship” and “I have validated the assay.” The first lacks an agreement and the second misstates proposed work as completed evidence. This is an outline within the supplied call's permitted assistance; the applicant must author the final statements.

## A3

Research abstract (52 words):

Can the assembly produce the intended shapes under the tested condition? Structural assessment of one preparation at 10 mM MgCl2 found intended shapes in 82% of 200 particles. This observation supports formation of the target morphology in that preparation. Independent preparations and kinetic measurements are needed to assess reproducibility and assembly dynamics.

Travel-support statement (39 words):

As a postdoctoral researcher, I have submitted an abstract and seek feedback on a structural assay. Attending would let me discuss assay interpretation and possible validation approaches with other researchers. This feedback would help guide my next research steps.

Missing support: financial circumstances, available institutional or other support, and realistic attendance cost estimates are needed to document need. The travel statement therefore addresses attendance value but cannot yet satisfy the documented-need criterion. The abstract is submitted, not accepted. The assay modality and further methodological detail were not supplied; no particular imaging or measurement technique has been invented.

Word counts use Python `len(text.split())` on each delivered paragraph, excluding its heading and this note; punctuation attached to a token does not create another word.

## A4

Package outline:

- Cover letter: connect the applicant's molecular-science experience to undergraduate teaching and feasible student research; identify the actual pipeline contribution and teaching/mentoring experience.
- CV: distinguish one term as a teaching assistant, informal mentoring of two students, and the team-project pipeline contribution. Do not imply instructor-of-record service, independent funding, or measured student outcomes.
- Research statement: propose projects with tractable student roles, accessible methods, realistic resource needs, staged milestones, and alternatives. Describe the computational pipeline as prior team-project work, and any independent research program as a future plan.
- Teaching/mentoring statement: use the documented teaching-assistant and informal mentoring experience, then explain proposed project-based instruction, feedback, and assessment. Any assessment methods are plans, not demonstrated successes.

Teaching paragraph:

My teaching experience consists of one term as a teaching assistant and informal mentoring of two students in analysis. I plan to use project-based instruction to connect molecular-science concepts with data analysis. Students would practice formulating questions, examining data, and explaining conclusions, with projects scoped to available time and resources.

Corrections: replace “independently taught multiple courses” with the documented teaching-assistant experience. Remove the claim that all mentees entered PhD programs because no placement outcomes were supplied. Remove the assertion that Professor X agreed to collaborate; Professor X has not been contacted. Describe a possible collaboration only as an unconfirmed future possibility. Teaching evaluations and evidence of teaching effectiveness are unavailable; do not invent them.

## P1

Author-facing report:

The reported observation—intended shapes in 82% of 200 particles at one condition—is potentially useful as a structural result for the preparation examined. The principal concern is that the analysis treats particles from one preparation as 200 independent biological replicates and then makes a universal robustness claim. Substantial correction is needed to make the analysis and conclusions match the design.

Necessary corrections:

1. **Independent unit and statistical analysis.** Report one independent preparation and 200 particle observations. Explain particle sampling and any clustering or dependence. Revisit the inference underlying p = 0.01 using the actual design; the particle count cannot establish between-preparation reproducibility. Supply the tested hypothesis, comparison, test assumptions, effect estimate, and appropriate uncertainty. The available summary is insufficient to prescribe or reproduce a replacement test.
2. **Scope of the conclusion.** A p-value does not establish universal robustness. Bound the conclusion to the observed morphology in the single preparation and condition. If reproducibility or robustness remains a central claim, it needs independent preparations and evidence spanning the conditions to which the claim applies.
3. **Assessability and reproducibility.** Provide the detailed methods and statistics, underlying numerical observations, and relevant code or access details under the journal's applicable requirements. These materials were not supplied for this review, so their existence and adequacy remain unknown.

Optional work: broader condition testing or kinetic characterization could answer additional questions. They need not be required for a manuscript whose claims are adequately narrowed to the available structural observation. Independent replication becomes necessary if the authors retain claims that depend on it.

Editor-facing advisory recommendation: **Major revision.** The supported single-preparation observation may remain useful, but the independent-unit error and excessive inference materially affect the conclusions. Reanalysis, clearer reporting, and narrower claims could address the central problems; the supplied material does not justify judging the paper by perceived novelty. This recommendation is based on the summary, without raw-data or code verification.

## P2

Qualitative rating: **Fair**, using the supplied criteria of scientific importance, feasibility, and assessable outputs.

- **Scientific importance:** Strong. The proposal addresses an important mechanism question. The supplied summary supports the relevance of the question, while the experimental outcomes remain proposed.
- **Feasibility:** Unresolved and insufficiently planned. The comparison depends on developing the assay, but the 12-month plan lacks an early feasibility decision and fallback readout. An assay-development delay could consume the time needed for the comparison. The absence of preliminary data is not itself a deficiency under this exploratory call.
- **Assessable outputs:** Weak. “Do experiments” describes activity rather than a result that the panel can assess. Specify outputs such as an assay-performance report, a documented comparison with uncertainty if the assay is viable, and a record of limitations or failure modes if it is not.

Priority revisions: put an early assay-feasibility checkpoint into the schedule, justify the decision criteria, specify a feasible fallback readout and its limitations, and allocate time to the comparison, analysis, and reporting. A provisional sequence could reserve an initial assay-development phase, a decision before the main comparison, and a final analysis/reporting phase; actual durations require the applicant's technical justification. Explain what mechanistic knowledge remains obtainable if the assay fails or the favored explanation is unsupported.

This assessment does not impose another agency's criteria or require preliminary results. It evaluates the proposed plan, not completed experimental evidence.

## E1

My contribution was developing the pipeline; the manuscript has been submitted but has not yet been accepted.

## R1

Draft response:

The independent preparation count is one, as reported in the revised excerpt: “In one preparation, 82% of 200 particles had the intended shape.” We have not performed a kinetic analysis. The reported result describes the observed shape frequency in that preparation and does not characterize assembly kinetics.

Status note:

- Preparation count: verified in the supplied excerpt only. No page or line locator was provided, and consistency elsewhere in the manuscript has not been checked.
- Kinetic analysis: unresolved; no analysis has been performed. An author decision is needed on whether to perform it or provide a supported explanation for not doing so. This draft makes no commitment to new work and reports no new result.
- Only response drafting was authorized. No manuscript changes were made, and this response should not be described as evidence that the kinetic request has been fulfilled.

## E2

The authors have clarified the methods, and I recommend minor revision to correct the remaining labels.

## Execution record

Files read:

- `frozen-v1.0.0/academic-writing/SKILL.md`
- `frozen-v1.0.0/academic-writing/references/manuscript-and-prose.md`
- `frozen-v1.0.0/academic-writing/references/scientific-review.md`
- `frozen-v1.0.0/academic-writing/references/grant-review.md`
- `frozen-v1.0.0/academic-writing/references/reviewer-response.md`
- `evals/expansion-prompts.json`

Limits: synthetic supplied records only; no web search, network access, primary-source verification, raw-data analysis, rendered-document inspection, or other repository-file access. The mock calls and policies supplied in the tasks governed these exercises. No skill or repository files were edited. These are task outputs, without rubric scoring or comparative claims.

Publication note: execution-record paths were normalized for portability; the synthetic task outputs are unchanged.
