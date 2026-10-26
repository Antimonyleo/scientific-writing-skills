---
name: literature-review
description: Find, verify, and synthesize scholarly evidence for STEM questions, manuscripts, grants, and research gaps. Use for citation checks, related work, narrative reviews, and planned systematic or scoping reviews; report search and evidence limits.
license: MIT
metadata:
  version: "1.1.0"
---

# Literature Review

Produce a traceable answer to the research question, with evidence strength and search limitations visible.

## Set the review depth

Infer the question, field, comparison, time window, and intended use from the request. A citation check or short background paragraph does not require a systematic-review protocol. For a formal systematic or scoping review, read [Formal reviews](references/formal-reviews.md). For thematic synthesis, conflicting findings, or a research-gap claim, read [Evidence synthesis](references/evidence-synthesis.md). For a substantial search, a search log, or reference checking, read [Search and verification](references/search-and-verification.md).

Use supplied papers, bibliography, and library context first. Search primary studies and official methodological guidance through available databases, publisher sites, repositories, or connected libraries. No particular search provider, paid API, citation manager, or output format is required.

## Search and verify

1. Translate the question into concepts, synonyms, relevant systems, methods, and outcomes. Include competing terminology and adjacent approaches. For broad research, use complementary sources and citation chaining; test that the search finds known relevant work.
2. For a substantial search, test it against a few known relevant papers and keep a log of sources, exact queries, filters, dates, and results. Report an exploratory web search as such. Do not manufacture database counts or imply access to unavailable full text.
3. Verify each included reference's identity and the proposition it supports at the publisher, DOI record, repository, or supplied full text. A remembered reference is a lead until resolved. Check publication status, related versions, and correction or retraction notices. When Python and network access are available, run [the bundled verifier](scripts/verify_refs.py) on the references to be delivered, fix each flagged entry, and rerun until every flag is explained; otherwise check the records manually and report what remains unverified. A valid DOI establishes identity, not claim support.
4. Extract the relevant system, method, independent unit, conditions, finding, uncertainty, limitation, and source locator. Record how deeply each source was read: full text, targeted passages (noting whether the supplement was read), abstract, or metadata only. Report details beyond that depth as not examined rather than inferring them. A bibliography or generated summary is a discovery lead.
5. Synthesize agreements, disagreements, and explanatory differences. Link claims to exact sources; retain evidence that challenges the favored account.

## Keep evidence boundaries clear

- Do not fabricate sources, identifiers, quotations, metadata, study counts, missing findings, or citations. Preserve existing citation keys unless a change is requested.
- Use primary studies for specific empirical claims and reviews for orientation or synthesis claims. Label preprints and link related journal versions without double-counting the same underlying study.
- Separate established observations, source authors' interpretations, your inferences, and proposed hypotheses. Bound comparisons by materials, sequences, conditions, assays, populations, and model regimes.
- “No direct evidence located in the searched sources” is justified by a bounded search; “no one has studied this” usually is not. Distinguish a knowledge gap from a search, access, reporting, or methodological gap.
- Apply reporting guidelines to the review type and research question. PRISMA is reporting guidance; following a checklist alone does not establish an exhaustive search or a valid synthesis.

## Deliver reusable evidence

Lead with the answer and what supports or limits it. Organize by scientific theme rather than one paragraph per paper unless annotations were requested. Use a claim/evidence/conditions/limitation/source table when it makes comparison easier. Attach locators or citation keys that the user can reuse.

For an incomplete search, give the supported synthesis, the specific coverage limitation, and the next source or query likely to resolve it. For a review intended for publication, report the methods actually used and unresolved methodological decisions; do not claim a systematic review from a few ranked search results.
