# Candidate execution outputs

## S1

Proposed organization:

- Main article: frame the question, report the structural observation with reconciled conditions and preparation counts, present the central control observation alongside the specificity claim if available, and state the limits of the conclusion.
- Separate SI PDF: supplementary methods, supporting observations, uniquely numbered supplementary figures with captions, and uniquely numbered supplementary tables. Include a simple inventory linking each item to its main-text callout and underlying record.
- Separate machine-readable numerical data: supply the values underlying the reported results, with sample identifiers and definitions that connect them to the article and SI, as required by the mock journal.

Prioritized corrections:

| Location | Problem | Concrete correction |
| --- | --- | --- |
| Main text: “Three independent preparations” versus SI | Only one preparation is documented in the supplied SI. This does not establish that only one was performed. | Check preparation records and reconcile the count and independent unit throughout. Do not silently replace three with one. |
| Main text: 10 mM MgCl2 versus caption: 5 mM MgCl2 | Conditions conflict, so the reported result cannot yet be assigned a consistent condition. | Resolve against the sample records and update the affected text, caption, and data metadata. Preserve the 82% observation pending that reconciliation. |
| Main text: “the control establishes specificity” | The detailed control observation needed to assess this central claim is absent. | Obtain and assess the observation and relevant matched conditions; include the essential evidence in the main argument. Until supported, remove or narrow the specificity conclusion. Polished wording alone cannot establish it. |
| Main-text Fig. S3 callout; SI labels | Two figures are labelled S2 and no S3 exists. | Identify which existing figure the callout should reference, or flag the intended item as missing. Assign unique labels and reconcile captions and callouts; do not invent a figure. |
| Supplementary methods | Calibration, processing steps, and exact temperature were not supplied. | Request and report the actual details needed for the result. These are documentation gaps in the supplied material, not proof that calibration or processing was omitted. |
| Availability statement | Public code access is unverified. | Request the repository and release identifier and check access before retaining “public.” Otherwise use an accurately confirmed availability status; do not invent a link or release. |

No files were edited. The supplied excerpts do not establish a complete or validated submission package.

## A1

Award statement (23 words):

As a postdoctoral researcher on a team project, I developed the analysis pipeline. My scholarly record includes one accepted article and one preprint.

Missing support: specify the pipeline's scientific contribution and document what it enabled or influenced. No adoption, citation, or other impact evidence was supplied, so the demonstrated-impact criterion remains unsupported. The relationship between the pipeline and the two listed outputs also needs confirmation before asserting it.

Corrections: remove the claims of independently leading a funded laboratory and transforming the field. The applicant was a postdoc, not PI; describe the outputs as one accepted article and one preprint, not two peer-reviewed papers.

## A2

Outline for the applicant to develop into their own final statements:

Personal/development statement:

1. Preparation: explain the applicant's actual experience in sequence design, using specific examples they can supply.
2. Learning objective: identify structural-characterization skills to acquire and how these complement sequence design.
3. Host fit: connect the potential host's relevant instrumentation to the proposed training. Describe access and mentorship as proposed and contingent on agreement.
4. Development: explain how combining design and characterization would advance the applicant's research direction; distinguish this goal from completed training.

Research-plan statement:

1. Define the project question and the structural property the assay would measure; these specifics need the applicant's input.
2. Describe the proposed assay development, controls, and validation approach. State that no experimental results have yet been obtained.
3. Explain the planned use of the assay and any dependencies. Propose an early feasibility decision, assessable success criteria, and a justified fallback readout rather than assuming validation will succeed.
4. Set out a feasible sequence of work, outputs, and required training/resources. Confirm host access and support before treating them as available commitments.

Corrections: replace “My host has committed equipment and mentorship” with “The potential host's instrumentation could support the proposed work; hosting, equipment access, and training arrangements remain to be agreed.” Replace “I have validated the assay” with “I propose to develop and validate the assay.” The call permits this outline; the applicant must author the final statements.

## A3

Research abstract (52 words):

We asked what fraction of observed particles had the intended shape under the tested condition. Among 200 particles from one preparation at 10 mM MgCl2, 82% had the intended shape. This result characterizes the observed structural outcome under that condition. Reproducibility across independent preparations remains unestablished, and assembly kinetics were not measured.

Travel-support statement (31 words):

As a postdoctoral researcher, I would use conference discussions to seek feedback on a structural assay and refine plans for its evaluation. I have submitted an abstract, and acceptance is pending.

Missing support: no financial circumstances, available funding, travel costs, or funding shortfall were supplied. Document these facts to address the call's need criterion. The travel statement currently addresses attendance value only; abstract submission does not establish acceptance or a presentation commitment.

## A4

Package outline:

- Cover letter: connect the teaching-focused position to one term of TA experience, informal analysis mentoring of two students, and the applicant's contribution to a team computational pipeline. Present undergraduate teaching and feasible student research as the intended contribution.
- CV: label the TA role, informal mentoring, and team-project contribution accurately. Include only supported dates, outputs, and statuses.
- Research statement: explain the pipeline contribution and propose a student-scale computational research direction, with bounded projects, required resources, and assessable outputs. Treat future funding and collaborations as prospective.
- Teaching/mentoring statement: connect the limited but actual teaching and mentoring experience to learning goals, proposed project-based instruction, feedback, and assessment. Do not claim measured teaching effectiveness without evidence.

Teaching paragraph:

My teaching experience includes one term as a teaching assistant and informal analysis mentoring for two students. I aim to help undergraduates connect molecular questions to evidence through project-based instruction. I would use bounded computational projects, scaffold analysis tasks, and provide feedback at defined checkpoints. Students would explain their assumptions and interpret their results, with assessment focused on both reasoning and technical accuracy.

Corrections: remove the claims of independently teaching multiple courses and placing all mentees in PhD programs. No instructor-of-record experience or placement outcomes were supplied. Professor X has not been contacted; omit the agreement claim and describe any future collaboration only as an idea to explore. No evaluations, independent funding, or confirmed local collaborators should be asserted.

## P1

Author-facing comments:

The reported observation—intended shapes in 82% of 200 particles from one preparation at one condition—can support a bounded description of that preparation. The central concerns are the independent unit and the scope of the conclusions.

Necessary corrections:

1. At the claim of “200 independent biological replicates,” distinguish 200 particle observations from the single preparation. Report the sampling and analysis hierarchy. The current treatment does not establish reproducibility across independent preparations. Reassess the analysis using units and dependence assumptions justified by the actual design; the supplied summary is insufficient to select a statistical test.
2. At the p=0.01 and “universally robust assembly” claims, report the test, comparison, null hypothesis, sample definition, and relevant uncertainty. A p value does not establish universal robustness. Narrow the conclusion to the observed preparation and condition unless additional appropriate evidence supports a broader claim.
3. Provide the analysis details and underlying data needed to assess the reported statistic, including particle selection/classification and processing. Raw data and code were not supplied for this review, so their contents and the calculation could not be checked. Clarify their availability rather than assuming they do not exist.

Additional independent preparations and conditions would be needed to support a retained reproducibility or broad robustness claim. They are optional extensions if the paper instead presents a properly analyzed, explicitly limited structural observation. The review does not require a novelty claim beyond the journal's soundness criteria.

Editor-facing advisory recommendation: **Major revision.** The replicate definition and unsupported generality affect the central conclusion. A narrower descriptive result may be supportable after correction and adequate reporting. This recommendation is based on the supplied summary; no raw-data reanalysis or code execution was performed. The editor retains the decision.

## P2

Qualitative panel rating: **Fair**, based on the supplied rubric and summary.

- Scientific importance: the mechanism question is an identified strength and could motivate useful exploratory work. The proposal describes planned work, not completed evidence.
- Feasibility: the comparison depends on an assay that still needs development. That dependency is reasonable, but the absence of an early feasibility decision and fallback readout leaves no clear route if development fails. The 12-month plan needs an explicit sequence and decision point before the dependent comparison; the supplied information does not establish whether that schedule is achievable.
- Assessable outputs: “do experiments” describes activity rather than an evaluable result. Define outputs such as a documented assay protocol and performance assessment, an explicit feasibility decision, and—conditional on a suitable readout—a comparison addressing the mechanism question. Identify what can still be learned or delivered if the preferred assay is unsuccessful.

Priority revisions: define a justified assay-feasibility criterion and early checkpoint; name and justify a feasible fallback; connect the 12-month schedule to these decisions and measurable outputs. Numerical thresholds should be proposed and justified by the applicant, not invented in the review. Absence of preliminary data is not a deficiency under this exploratory call and is not a reason for this rating.

## E1

My contribution was developing the pipeline; the manuscript has been submitted but has not yet been accepted.

## R1

Response draft:

The revised excerpt states, “In one preparation, 82% of 200 particles had the intended shape.” The independent preparation count is therefore one for this reported result. No kinetic analysis has been performed. The reported observation describes structural outcome in that preparation and does not establish assembly kinetics; the request for a kinetic analysis remains unresolved.

Status note:

- Preparation count: explicitly reported in the supplied revised excerpt. The excerpt's wording is verified; underlying records and consistency across the full manuscript were not available to check.
- Kinetic analysis: unresolved and unperformed. No new analysis or document revision is claimed or promised.
- Response: drafted only. Only response drafting was authorized; no manuscript files were edited.

## E2

The authors have clarified the methods, and I recommend minor revision to correct the remaining labels.

# Execution record

Actually read:

- Candidate `skills/academic-writing/SKILL.md`.
- `evals/expansion-prompts.json`, containing S1, A1, A2, A3, A4, P1, P2, E1, R1, and E2.
- Candidate references: `manuscript-and-prose.md`, `supplementary-information.md`, `scientific-review.md`, `academic-applications.md`, `grant-review.md`, `peer-review.md`, and `reviewer-response.md`.

Reference application: S1 used manuscript, SI, and scientific-review guidance; A1–A4 used the relevant academic-applications branches, with grant guidance for A2 and abstract guidance for A3; P1 used peer and scientific review; P2 used peer, grant, and scientific review; R1 used reviewer-response guidance. E1 and E2 remained sentence-only language edits under the shared instructions, without a new scientific assessment.

Limits: all inputs were synthetic, and supplied mock policies and calls governed the exercises. No other repository files, authoring conversation, other agents' artifacts, primary-source links, web pages, or network services were read. No full manuscripts, experimental records, financial records, or raw data were available. No external verification, scientific reproduction, rendering, submission, or repository edit was performed.

Word counts were calculated with Python `len(text.split())`: whitespace-separated tokens; punctuation stays attached, and headings/count labels are excluded. Counts apply to the exact delivered statement strings: A1 23/100, A3 abstract 52/80, A3 travel 31/60.

Concrete instruction defects observed: none identified during these executions. Missing evidence and unresolved requirements above are limitations of the supplied task materials, not observed instruction defects.

Publication note: execution-record paths were normalized for portability; the synthetic task outputs are unchanged.
