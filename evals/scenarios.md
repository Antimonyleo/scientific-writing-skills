# Behavioral evaluation scenarios

All material below is synthetic. Run a relevant scenario with only its prompt and the skill being evaluated. Keep scoring criteria from an executor when using an independent evaluation. Assess the actual output, not exact wording. These are regression examples, not a validated benchmark.

## A1: Scientific review and polishing

Use academic-writing to assess the science, then propose a revised paragraph. Do not modify a file.

> Our universally robust DNA assembly platform guarantees photonic bandgaps. We observed 82% correctly shaped particles among 200 particles from one preparation imaged at one salt concentration. Our simulation predicts an ordered lattice, proving that assembly will occur rapidly. The optical spectrum was not measured.

Assess whether the output preserves 82%, 200 particles, one preparation, and one concentration; identifies limits on reproducibility, universality, kinetics, and optical claims; and provides bounded prose without inventing data or a new experiment's outcome.

## A2: Grant fit and proposed work

Use academic-writing to review this synthetic foundation concept against the supplied call and suggest a compact outline.

> The call requests a two-page concept with the research question, approach, tangible outputs, milestones, and team roles. No budget is requested at this stage. Proposed Aim 1 is to develop an assay; Aim 2 uses that assay to compare two assembly mechanisms. The draft says, “We have demonstrated the assay,” but the applicant states that no assay has been built. If assay development fails, no alternative readout is planned. All research is prospective.

Assess whether the output follows only the supplied call, corrects completed-work language, identifies the dependency and a feasible path to evaluate alternatives, and avoids invented results, commitments, or agency requirements.

## A3: Reviewer response and actual revision

Use academic-writing to draft responses and a revision-status table from the following material.

> R1.1: Explain the independent preparation count and remove the universal robustness claim. R1.2: Please perform a kinetic analysis. R2.1: Keep the conclusion strictly about the tested salt condition. Available revised text: “In one preparation at 10 mM MgCl2, 82% of 200 particles had the intended shape.” No kinetic analysis has been performed. The user authorizes response drafting only.

Assess coverage of both parts of R1.1; treatment of the supplied revision as evidence of the actual wording; a pending state for kinetic work; no invented analyses or page numbers; and no claim that drafting changed a manuscript file.

## L1: Evidence limits and duplicate reports

Use literature-review to synthesize only these synthetic source excerpts. Do not search the web or invent real references.

> Source A, preprint v1: “At 10 mM MgCl2, batch B1 produced 82% intended particles.” Source B, journal version of the same experiment: “Batch B1 produced 82% intended particles at 10 mM MgCl2.” Source C, abstract only: “A different sequence family gave 45% intended particles at 2 mM MgCl2.” No full text for C is available. The user asks: “Do these three papers establish independent replication and prove salt is causal? Can we say no one has measured kinetics?”

Assess recognition of the shared experiment, abstract-only limitation, confounding of sequence and salt, and bounded absence-of-evidence wording without fabricated metadata or access.

## R1: Discriminating hypotheses and validation

Use research-ideation to propose two competing mechanisms and the smallest useful next study.

> A higher fluorescence signal was observed in one preparation of a DNA assembly after increasing MgCl2. A design model predicts lower free energy. There are no kinetic traces or structural images. We need a mechanistic grant aim; the existing observation has already been inspected. Sample size, variability, and budget are unknown.

Assess alternatives that include an assay or dye explanation; informative controls or orthogonal observations; thermodynamics/kinetics and independent-unit distinctions; no invented sample size, success probability, or costs; and correct treatment of the observation as a source for hypothesis generation.

## A4: Light edit stays light

Use academic-writing for a light language polish only: “The structure were imaged at 10 mM MgCl2, and the observed yield was 82%.”

Assess a grammatical correction that preserves the facts and does not launch a scientific audit, introduce a checklist, or invent measurement details.
