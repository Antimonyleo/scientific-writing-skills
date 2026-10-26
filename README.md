# Scientific Writing Skills

Three portable Agent Skills for scientific writing, evidence synthesis, and research planning. They support manuscripts and supplements, proposals, academic applications, polishing with scientific reasoning, and giving or responding to reviews.

| Skill | Use it for |
| --- | --- |
| [academic-writing](skills/academic-writing/SKILL.md) | Manuscripts/SI, proposals, academic applications, referee reports, and reviewer responses |
| [literature-review](skills/literature-review/SKILL.md) | Verified citations, related work, evidence synthesis, reference checking, and scoped or formal reviews |
| [research-ideation](skills/research-ideation/SKILL.md) | Mechanisms, hypotheses, grant aims, stress-testing, discriminating tests, and research decisions |

Each skill works on its own. Detailed procedures live in references loaded only when needed. The skills require no paid service, API key, particular model, or automatic agent delegation. Literature searches and current venue or funder checks use whatever suitable sources the host can access.

Two skills bundle an optional standard-library script. `literature-review` checks references against public registries for identifier resolution, metadata match, retraction or correction notices, and published preprint versions. `academic-writing` compares an original and a revised text for silently changed numbers, units, citation keys, labels, cross-references, and math. Each is a run, fix, and rerun step with a documented manual fallback; neither needs an account or key, and no contact address is sent unless the user sets one.

## Writing and review coverage

`academic-writing` supports drafting, substantive revision, and light polishing at the requested depth. It routes to these procedures:

| Artifact or task | Guidance |
| --- | --- |
| Manuscripts, abstracts, and public summaries | [Manuscript and prose](skills/academic-writing/references/manuscript-and-prose.md) |
| Supplementary methods, figures, tables, and data | [Supplementary information](skills/academic-writing/references/supplementary-information.md) |
| Grants and proposals | [Grant review](skills/academic-writing/references/grant-review.md) |
| Awards, nominations, and fellowships | [Academic applications](skills/academic-writing/references/academic-applications.md) |
| Conference abstracts, participation, travel, and session proposals | [Academic applications](skills/academic-writing/references/academic-applications.md) |
| Academic job cover letters, statements, CVs, and packages | [Academic applications](skills/academic-writing/references/academic-applications.md) |
| Scientific assessment and referee/panel reports | [Scientific review](skills/academic-writing/references/scientific-review.md) and [Peer review](skills/academic-writing/references/peer-review.md) |
| Author responses and revision verification | [Reviewer responses](skills/academic-writing/references/reviewer-response.md) |
| AI-use disclosure, funder originality rules, and confidential review | [AI-use policies](skills/academic-writing/references/ai-use-policies.md) |

Actual calls and venue instructions govern requirements. This coverage describes the procedures available, not certification for every discipline, institution, or application.

## Install

Using the [Skills CLI](https://github.com/vercel-labs/skills), choose the skills, agent, and project or global scope in its interactive prompts:

```bash
npx skills add Antimonyleo/scientific-writing-skills
```

Alternatively, clone the repository and copy the desired skill directories to your host's documented skill location. For Codex, a user skill location is `~/.agents/skills`; Claude Code uses `~/.claude/skills`. Consult current host documentation if your setup differs.

The bundled local installer creates copies, preserves replaced directories in a backup folder, and skips identical installations:

```bash
python3 scripts/install.py --target ~/.agents/skills
```

Use `--target ~/.codex/skills` to update an existing legacy Codex installation, or `--target ~/.claude/skills` for Claude Code. If a destination is a symlink, inspect its owner and update that source explicitly; the installer refuses to follow or replace it. Do not install duplicate copies in several discovery locations. Newly installed skills may require a new turn or session in your host.

## Examples

```text
Use academic-writing to review this proposal's scientific argument before polishing.
Map it to the attached funding call. Propose substantive changes for review first.
```

```text
Use academic-writing to draft a point-by-point response. Track every concern,
distinguish proposed from completed changes, and verify against the revised manuscript.
```

```text
Use literature-review to compare these mechanisms. Verify the primary sources,
explain conflicting evidence, and state the search limits.
```

```text
Use research-ideation to propose competing explanations and the smallest experiment
that distinguishes them. State the independent unit, controls, and decision criteria.
```

Skill invocation syntax depends on the host. In Codex, explicit invocations can use `$academic-writing`, `$literature-review`, or `$research-ideation`. The descriptions also support automatic selection; automatic discovery must be tested in each host.

## Design and evidence

These are extensions of three custom skills first written in a Codex session on July 19, 2026. They are maintained here as their upstream source. Existing scientific skill collections and primary methodological guidance informed the redesign; no third-party skill package was vendored.

Read the [research and design review](docs/research.md) for sources and tradeoffs, and the [validation record](docs/validation.md) for what was actually checked. Package checks and synthetic examples do not establish improved publication outcomes or performance across models.

The workflows preserve author decisions and evidence boundaries. They do not invent results or citations, certify compliance, or submit documents. Applicable journal, institution, and funder rules remain controlling.

## Maintenance

```bash
python3 scripts/validate.py
python3 scripts/test_install.py
python3 -m unittest discover -s tests
```

The package checks cover structure, local links, JSON records, installation behavior, and the bundled scripts' offline behavior against synthetic fixtures and mocked registry responses.

Maintain reusable procedures in the skills and project-specific source paths, build commands, and editing conventions in the project's `AGENTS.md` or equivalent. Run relevant [original scenarios](evals/scenarios.md), [application/SI/review scenarios](evals/expansion-prompts.json), and [verification, policy, and ideation scenarios](evals/merge-prompts.json) when changing substantive workflow guidance. The [expansion criteria](evals/expansion-criteria.md) and [merge criteria](evals/merge-criteria.md) are kept separate from executor prompts. The validator checks package structure and references, not scientific judgment.

MIT licensed. Source links are attribution and verification aids; installing these skills does not require adding a software citation to every scientific document.
