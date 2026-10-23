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
