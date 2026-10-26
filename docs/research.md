# Research and design review

Research performed October 22, 2026 (America/Phoenix); source retrieval continued into October 23 UTC. This is a targeted comparative review of scientific skill designs and primary methodological guidance, not an exhaustive survey of every published skill or an empirical comparison of model performance.

## What was examined

The starting point was three custom skills written in a Codex session on July 19, 2026. Their original file hashes are recorded in [original-skills.json](original-skills.json). All three were concise and useful but lacked detailed procedures for substantive scientific review, grant fit, comment tracking, formal-review boundaries, and discriminating validation.

The redesign compared six relevant entrypoints in [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills): scientific-writing, research-grants, peer-review, scientific-critical-thinking, scientific-brainstorming, and literature-review. The older `claude-scientific-skills` repository URL redirected to this name during inspection. [Exact file paths and inspected blob hashes](compared-skills.json) identify the compared versions. Their supporting scripts and reference libraries were not fully audited or executed, so this review makes no claim about their operational quality.

The comparison also examined [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md), Vercel's [Skills CLI](https://github.com/vercel-labs/skills) and [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md), and the [Agent Skills specification](https://agentskills.io/specification). Scientific sources below were selected for direct relevance and primary authorship or official institutional ownership.

## Decisions from the comparison

| Area | Useful design pattern | Decision for this package |
| --- | --- | --- |
| Scientific writing | Explicit provenance and consistency checks | Check central and changed claims against evidence; scale formality to the task rather than requiring a claim registry for every sentence edit |
| Grant preparation | Establish the governing opportunity and map requirements | Use a source-to-draft requirements table when checking fit; consult current rules instead of embedding volatile agency details |
| Scientific appraisal | Separate reporting gaps, validity, bias, and interpretation | Give located, proportionate concerns and distinguish wording, reporting, reanalysis, and new-evidence remedies |
| Reviewer correspondence | Connect comments, evidence, response, and revision | Track proposed, implemented, and verified states; inspect actual changes before claiming completion |
| Literature review | Reproducible searches and distinction among records, reports, and studies | Keep ordinary synthesis lightweight; load formal-review procedures only when requested |
| Ideation | Explicit assumptions, competing mechanisms, uncertainty, and decision criteria | Favor an informative next test and meaningful alternatives; use scores only when their basis is clear |
| Prose polishing | Preserve voice and remove filler without adding facts | Retain scientific terminology and necessary uncertainty; avoid blanket punctuation rules or AI-detector claims |
| Discovery | Standard metadata and progressive loading | Keep the three existing names, short entrypoints, and self-contained references; a discovery skill is optional |

These are engineering judgments informed by inspection. They are not evidence that this package outperforms the compared collections. The package extends the original local text; no third-party skill, script, reference file, or checklist has been copied into it. Source acknowledgment does not impose automatic citations in users' manuscripts.

## Scientific and methodological sources

1. Mensh B, Kording K (2017). [Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619). PLOS Computational Biology 13(9): e1005619. The publisher page, including its correction notice, was inspected. It supports reader-focused scientific organization and an explicit contribution. The package uses flexible section guidance rather than a universal article template.

2. Noble WS (2017). [Ten simple rules for writing a response to reviewers](https://doi.org/10.1371/journal.pcbi.1005730). PLOS Computational Biology 13(10): e1005730. The full publisher text was inspected. It supports answering each concern, giving direct explanations, and making revisions easy to locate. The package adds implementation states and source verification as its own workflow decisions.

3. NIH. [Advice on Application Sections](https://www.grants.nih.gov/grants-process/write-application/advice-on-application-sections). The official page emphasizes the opportunity's instructions, goals, expected outcomes, and informative aims. The package uses these principles while leaving section requirements and limits to the governing call.

4. NIH. [Guidance: Rigor and Reproducibility in Grant Applications](https://www.grants.nih.gov/policy-and-compliance/policy-topics/reproducibility/guidance). The official guidance addresses the strength of prior research and rigorous experimental design. It informs attention to controls and assumptions, without making NIH-specific requirements universal across STEM.

5. NSF. [How We Make Funding Decisions](https://www.nsf.gov/funding/merit-review). The official page identifies intellectual merit and broader impacts and notes that solicitations may add criteria. The package therefore distinguishes sponsor requirements from general writing advice. It does not freeze a PAPPG edition, page count, or weighting rule into reusable instructions.

6. Alfred P. Sloan Foundation. [Apply](https://sloan.org/grants/apply). The official page was inspected for program-specific application stages, tangible outputs, management, and milestones. This is a useful counterexample to imposing one federal-agency template on foundation proposals. Live program instructions remain controlling.

7. PRISMA Executive. [PRISMA 2020](https://www.prisma-statement.org/prisma-2020) and [PRISMA overview](https://www.prisma-statement.org/). The official pages describe reporting guidance and extensions for other evidence syntheses. The package distinguishes reporting from methodology and ordinary narrative research from a documented formal review. A review label or completed checklist does not establish comprehensive retrieval.

8. Center for Open Science. [Preregistration](https://www.cos.io/initiatives/prereg). The official guidance explains recording a plan and distinguishing planned from unplanned work. The package uses this to prevent hypotheses generated from inspected outcomes being described as prospectively specified. It does not claim that registration alone validates a hypothesis or automatically makes an analysis confirmatory.

## Packaging and host guidance

- [Agent Skills specification](https://agentskills.io/specification): name and description metadata, optional resources, self-contained directories, and progressive loading inform package structure.
- [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills): metadata supports discovery, while references provide conditional detail; user installation and host configuration remain separate from skill content.
- [Vercel Skills README](https://github.com/vercel-labs/skills): repository installation and discovery support the optional `npx skills add` route. The core package also supports direct copying without the CLI.

Web retrieval of one Nature Portfolio reporting-policy page encountered an authentication redirect. Its search excerpt was not used as a governing source. A guessed PRISMA scoping-review URL returned 404; the package links the verified official overview instead. Neither failure is evidence about the scientific content of those resources.

## Scope and maintenance limits

These procedures support expert work; they do not certify scientific validity, publication acceptance, grant success, or policy compliance. Policies, database coverage, reporting guidance, and host discovery can change. Runtime instructions therefore call for checking the actual current source when it governs the requested task.

The release includes synthetic behavioral scenarios and package checks. Their observed results and limitations belong in [validation.md](validation.md). A later comparative effectiveness claim would require a fixed baseline, representative documents, blinded assessment, and results across the actual target models and hosts.

## Academic-writing expansion: October 23, 2026

The next review addressed explicit gaps in supplementary-information preparation, awards and fellowships, conference/travel applications, academic job packages, and giving formal paper/proposal reviews. It retained the three skills and expanded only `academic-writing`. Source access dates below are UTC. This remains a targeted deep comparison, not a census or ranking of the skill ecosystem.

### Similar skills inspected

Exact entrypoint paths and blob hashes are recorded in [compared-skills.json](compared-skills.json). Entrypoints were inspected for instructions and routing; their supporting libraries and execution quality were not audited. Selected sections of the unusually long pre-submission orchestrator were inspected, rather than treating its full package as reviewed.

| Source | Lesson used | Boundary retained here |
| --- | --- | --- |
| [Career Document Architect](https://github.com/lyndonkl/claude/blob/main/skills/career-document-architect/SKILL.md) | Link a coherent application narrative to evidence and institutional fit | Do not import fixed page counts, legacy biosketch formats, numeric quality cutoffs, or generic achievement examples as applicant facts |
| [Career Development](https://github.com/jjfroehlich/agent-handbook-for-life-science-research/blob/main/skills/career-development/SKILL.md) | Tailor to the requested artifact, actual contribution, and current role; preserve publication and commitment status | Keep broader career choices and negotiation outside this writing workflow |
| [Publishing and Peer Review](https://github.com/jjfroehlich/agent-handbook-for-life-science-research/blob/main/skills/publishing-and-peer-review/SKILL.md) | Distinguish author, reviewer, and editor-facing actions; make requested work proportional to the retained claim | Do not turn an editing request into publication strategy or an unsolicited review |
| [Scientific Writing](https://github.com/jjfroehlich/agent-handbook-for-life-science-research/blob/main/skills/scientific-writing/SKILL.md) | Choose structure, rhetoric, or sentence intervention according to the user's actual request | Avoid mandatory whole-paper diagnosis for local polishing |
| [Paper Review](https://github.com/WenyuChiou/academic-writing-skills/blob/main/skills/paper-review/SKILL.md) | Load the smallest relevant modules; distinguish verified requirements, scientific concerns, and preferences | Avoid adopting named reviewer personas or domain-specific overlays as general STEM rules |
| K-Dense [Scientific Writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md) and [Peer Review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md) | Trace claims and displays to evidence and distinguish reported detail from independently checked results | Do not impose per-claim registries or elaborate intake machinery on ordinary writing; allow a requested advisory recommendation under the actual review form |
| [Pre-submission Reviewer](https://github.com/mdenolle/academic-practice-agents/blob/main/pre-submission-agent/skills/pre-submission-reviewer/SKILL.md) | Keep review provenance and reconcile prior comments against revisions | Do not require a large agent team, author examination, lab rubric, or suppression of newly found validity issues in unchanged text |

The formerly linked `jjfroehlich/agent-skills-for-academic-research` repository redirected to `agent-handbook-for-life-science-research`; the inspected source uses the latter name. Similar skills supply design examples, not proof of effectiveness or authority over a user's institution. No source file or code was copied into this package.

### Authoring guidance and operating rules

The review read official [OpenAI guidance on concise skills](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), [OpenAI skill evaluations](https://developers.openai.com/blog/eval-skills), [Anthropic skill-authoring practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), the [Agent Skills specification](https://agentskills.io/specification), and the [Anthropic Skill Creator implementation](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md). The local Codex Skill Creator also governed implementation. Source instructions were compared rather than blindly merged: broad, emphatic trigger language in one implementation conflicts with the goal of precise selection across a large installed skill set.

The resulting rules for this expansion are:

1. Keep the description short but name the actual document families, including supplements, applications, and reports. Keep detailed trigger distinctions in a small routing table.
2. Add reusable decisions that change the output. Preserve light editing, author voice, and task scope; avoid a fixed itinerary for every request.
3. Link conditional detail directly from the entrypoint. Add three references instead of more globally discoverable skills or a nested routing framework.
4. Separate evidence, claimed status, proposed actions, and actual verification. In applications this includes personal contribution, acceptance, funding, teaching, and host agreement.
5. Let actual venue/call requirements govern. Page limits, criteria, required statements, comment channels, and permitted assistance vary; examples remain examples.
6. Match checks to observable outcomes. Fix scenarios and criteria before editing, run the old and revised skill independently, inspect outputs and counts, and separate structural checks from scientific judgment.
7. Keep models and harnesses out of the core procedure. Add no paid API, mandatory delegation, authoring-time tool name, or new script when prose guidance suffices.

These rules operationalize the sources; they are not claims of universally optimal prompt length or measured effectiveness. Explicit invocation is tested here. Automatic skill selection and performance in other hosts require separate evidence.

### Genre-specific primary guidance

| Verified source | Implication for the expansion |
| --- | --- |
| [PLOS supporting information](https://journals.plos.org/plosone/s/supporting-information) | Check item names, captions, files, and packaging against the target venue. Supporting files need their own quality checks; publisher-specific conventions are not universal. |
| MIT Communication Lab [research statements](https://mitcommlab.mit.edu/aeroastro/commkit/faculty-applications-research-statement/) | Connect an applicant's research direction and evidence to the actual department and role, including feasible student research where relevant. |
| MIT/Broad Communication Lab [faculty cover letters](https://mitcommlab.mit.edu/broad/commkit/cover-letter-for-a-faculty-position/) | Give a cover letter a distinct role connecting the application; avoid duplicating the CV or importing generic page conventions. |
| MIT CAPD [teaching philosophy overview](https://capd.mit.edu/resources/teaching-philosophy-statements/) | Relate teaching beliefs to genuine examples. Expanded teaching guidance also draws on the inspected career skills and the supplied applicant evidence, rather than requiring invented outcomes. |
| [ACS nomination requirements](https://www.acs.org/funding/awards/national/nominations/requirements-and-timeline.html) | Address the award's purpose with attributable accomplishments and complementary support materials. Nominee and nominator roles differ. |
| [NSF fellowship application guidance](https://www.nsf.gov/funding/initiatives/grfp/applicants/application-help-videos) | Distinguish applicant preparation/development from the research plan, retain authenticity, and follow the governing opportunity and assistance rules. |
| [Biophysical Society travel awards](https://www.biophysics.org/2027meeting/awards-competitions/travel-awards) | Conference science, participation value, applicant role, and travel support can be distinct requested fields. This inspected call was already closed; it is not evidence of a live opportunity. |
| [COPE reviewer guidelines](https://doi.org/10.24318/cope.2019.1.9), inspected through the [official PDF](https://members.publicationethics.org/sites/default/files/cope-ethical-guidelines-peer-reviewers-v2_0.pdf) | Make reviews accountable and appropriate to their role, expertise, and process. These ethics principles do not require a permission ceremony for an already authorized public-paper critique. |
| [PLOS reviewer guidance](https://journals.plos.org/plosone/s/reviewer-guidelines) | Use actual assessment criteria and permitted author/editor channels. Not every journal accepts an unrestricted confidential recommendation section. |

Retrieval limits: the MIT faculty-materials landing page returned HTTP 429, the full MIT teaching-philosophy page returned HTTP 502, and Nature's SI page redirected to authentication. Indexed text from those pages was used only for discovery, not as the sole verification of a new rule. Successful primary sources above establish the retained guidance. Two inspected ACS pages showed different cycle dates, reinforcing the need to resolve governing-source conflicts; no deadline or award amount was embedded in the skill.

### Implementation and evaluation contract

The expansion adds `supplementary-information.md`, `academic-applications.md`, and `peer-review.md`, with direct routing from a compact entrypoint. Existing manuscript, grant, scientific-appraisal, and response guidance remains available. Research and comparisons live in this document, outside the skill's routine context.

Ten synthetic prompts and [assessment criteria](../evals/expansion-criteria.md) were fixed before changing instructions. An unchanged v1.0.0 snapshot supplied the baseline, and separate agents executed the same prompts without criteria or authoring context. Review the resulting artifacts and [validation record](validation.md) before drawing any performance conclusion. Small synthetic tests can demonstrate behaviors and expose defects; they do not establish overall superiority, real application success, or expertise across every discipline.

## Review-improvement merge: October 26, 2026

Three independent reviews of the earlier July copies of these skills proposed scripts, references, and workflow changes. Those reviews targeted older text, so each finding was compared with the current package and ported only when it added a capability this package lacked. Reviewer claims were re-checked against primary sources on October 26, 2026 (America/Phoenix) before inclusion; several were corrected or dropped, as recorded below. The reviews themselves are not part of this repository.

### AI-use policies

Runtime guidance in `academic-writing/references/ai-use-policies.md` gives a procedure and source links; the dated observations below are not runtime rules. Pages were retrieved directly. Quotations are short excerpts.

| Source (retrieved October 26, 2026) | Observed rule | Decision |
| --- | --- | --- |
| [NIH NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html), released July 17, 2025 | "NIH will not consider applications that are either substantially developed by AI, or contain sections substantially developed by AI, to be original ideas of applicants." NIH states it uses AI-content detection; post-award detection may be referred to the Office of Research Integrity. Six applications per PI per calendar year, excluding T activity codes and R13; effective for the September 25, 2025 receipt date onward. | Cite the originality principle as an example; leave the application cap and dates out of runtime text |
| [NIH NOT-OD-23-149](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html), June 23, 2023 | Peer reviewers are prohibited from using generative AI "for analyzing and formulating peer review critiques"; uploading application content to online generative AI tools violates confidentiality. Accessibility exceptions require prior notice. | Supports the confidential-review procedure |
| [NSF merit review and AI](https://www.nsf.gov/policies/ai/merit-review) (redirect from the December 14, 2023 notice; page updated May 21, 2026) | Reviewers "are prohibited from uploading any content from proposals, review information and related records to non-approved generative AI tools"; proposers "are encouraged to indicate in the project description" whether and how generative AI was used. | Example of a non-approved-tool rule and an encouraged proposer disclosure |
| [ICMJE Recommendations](https://www.icmje.org/recommendations/), updated January 2026 | A separate section covers AI use. Authors describe use "in both the cover letter and the submitted work"; writing assistance belongs in acknowledgments, and data, analysis, or figure use in methods. AI tools are not authors, and AI-generated material is not an acceptable primary source. Reviewers follow the journal's policy or request permission. | Supports the disclosure and no-AI-authorship guidance |
| [ACS AI policy](https://researcher-resources.acs.org/publish/aipolicy), updated December 13, 2024 | "All use of AI tools should be disclosed within the submission," in Acknowledgments, with substantial uses in Methods; no language-editing exemption appears on the page. Disclosing a submission to a text-generation service breaches reviewer confidentiality. ToC graphics may not use AI-generated images. | Example of broad disclosure; not generalized |
| [Springer Nature/Nature Portfolio](https://www.nature.com/nature-portfolio/editorial-policies/ai) and linked [manuscript-preparation](https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation) and [peer-review](https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-peer-review) pages | A tiered risk framework. Language polishing is permitted; the linked page asks authors to describe its use. Confidential material "must not be uploaded to unsecured or public AI systems"; reviewers should disclose AI use. | A reviewer's claim that Nature exempts copy editing from disclosure was **not confirmed** on the current pages and was dropped |
| [Elsevier](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals), updated June 2026 | A separate AI declaration statement; "Basic checks of grammar, spelling and punctuation do not need a declaration statement." Reviewers should not upload a submitted manuscript to an AI tool; private tools may support the language of a review, with disclosure. | Example of an exemption and of a qualified reviewer rule |
| [Wiley AI guidelines](https://www.wiley.com/publishing/article/ai-guidelines) (no date shown) | Authors must disclose AI use; simple grammar correction "typically" does not require disclosure. Reviewers should not upload any portion of submitted manuscripts. | Example only |

The COPE position statement on authorship and AI tools returned HTTP 403 and was not used. The differences above are the reason runtime text requires checking the governing page rather than listing per-publisher rules.
