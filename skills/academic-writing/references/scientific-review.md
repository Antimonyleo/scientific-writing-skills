# Scientific review before polishing

Use this reference for an explicit scientific critique or substantive editing that includes scientific thinking. Review the evidence made available; do not assume a complete dataset, supplement, or protocol exists in the current context.

## Map the important claims

Prioritize claims central to the contribution and claims about causation, mechanism, novelty, performance, or generality. For several claims, use:

| Claim and location | Evidence and locator | Inferential limit or competing explanation | Consequence and remedy |
| --- | --- | --- | --- |

Separate an observed result, a model prediction, a literature-supported premise, and a proposed outcome. State whether an issue can be fixed by wording, needs a clearer report of existing work, requires reanalysis, or requires new evidence. Do not edit one category into another.

## Ask questions that could change the conclusion

- Does the design measure the claimed property? What does the assay or model actually observe, and what additional assumptions connect that observation to the claim?
- What is the independent experimental unit? Distinguish independent preparations, specimens, sequences, simulation runs, images, and repeated measurements. Many measurements from one preparation do not by themselves establish between-preparation reproducibility.
- Are controls and baselines matched for relevant conditions? Could concentration, ionic conditions, temperature, processing, acquisition settings, batch, or selection of examples explain the comparison?
- Do effect sizes, uncertainty, sample sizes, missing observations, and analysis populations match across text and figures? Are exploratory choices, multiple comparisons, and dependencies reported? Do not prescribe a statistical test without the design and data needed to justify it.
- For computational work, are objectives separated from evaluation metrics? Check training/test leakage, held-out evaluation, baseline tuning, seeds, convergence, parameter sensitivity, units, and the physical regime in which the model is valid.
- For molecular engineering, distinguish thermodynamic favorability from kinetics, predicted structure from observed structure, and structural organization from functional performance. A structural assay alone may not establish an optical, mechanical, or biological function.
- Which alternative mechanism fits the same evidence? What observation would distinguish it from the preferred interpretation? Identifiability and optimizer convergence are different questions.
- Is the claim bounded by the tested material, sequences, design family, conditions, scale, time range, and readout? Do not generalize from a successful example to universal programmability or robustness.

Apply only relevant checks. Clinical or randomized-trial appraisal tools should not be imposed on a materials simulation or molecular assembly experiment. A reporting checklist measures reporting coverage; it does not certify validity or supply a numerical scientific-quality score.

## Give an actionable assessment

For each material concern, provide a source location, what is observable, why it affects the claim, and a bounded remedy. Classify missing information as unresolved rather than asserting misconduct or experimental omission. Recognize evidence that withstands the critique.

Prioritize concerns that could change the main conclusion, then concerns that affect interpretation or reproducibility, then clarity. Propose the smallest sufficient action: narrow the claim, report an existing detail, reanalyze an appropriate unit, add a discriminating control, or test a new condition. Describe additional studies as proposals until performed.

## Verification boundary

If supplied only prose, assess the argument and reported design. If supplied numerical data or code, report any actual calculations or reproductions separately. Reading methods, running a linter, and independently reproducing a result are distinct evidence levels.

## Further reading

NIH [rigor and reproducibility guidance](https://www.grants.nih.gov/policy-and-compliance/policy-topics/reproducibility/guidance) motivates attention to prior evidence and experimental design. Its agency-specific application requirements apply only when governing the task.
