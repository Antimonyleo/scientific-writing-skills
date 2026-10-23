# Validation plans and research decisions

## Choose a test that can change the decision

Identify the most consequential assumption and a feasible observation that distinguishes the leading explanations or design options. Prefer a small informative experiment or simulation before a large optimization campaign when it can rule out an unsuitable mechanism or readout.

Specify inputs, perturbations or groups, independent experimental unit, comparator, readout, analysis, expected outcomes under the alternatives, and the resulting decision. Use negative controls, positive controls, matched baselines, ablations, and orthogonal readouts where each has a defined purpose.

Distinguish repeated measurements from independent replication. State how batches, preparations, sequences, fields of view, or simulation trajectories enter the inference. Do not select a sample size or claim adequate power without an estimand, variability assumption, meaningful effect, and justified analysis. A pilot can estimate feasibility or variability without establishing generality.

## Computational and physical validation

Separate code correctness, numerical convergence, agreement with a model, and agreement with experiment. A successful software test validates the tested behavior; it does not validate the physical assumptions.

For a computational comparison, match inputs, hardware or resource budget, stopping criteria, baseline tuning, and quality metrics. Retain relevant software versions and seeds. Separate tuning from evaluation; use independent data or held-out conditions when evaluating generalization. Check parameter sensitivity, model regime, units, boundary conditions, and the cost of uncertainty where relevant.

For molecular engineering, link the proposed structural assay and functional assay to separate claims. A structure consistent with a design is one result; optical, mechanical, kinetic, or biological performance needs an appropriate independent readout.

## Plan interpretation before collecting decisive evidence

Record the expected observation under each leading explanation, a null or ambiguous outcome, likely assay failure, and what each would imply. Separate technical failure from evidence against the mechanism. Explain when to repeat, redesign, stop, or advance.

If the hypothesis arose from an already examined dataset, identify what was seen and which data remain untouched. A later confirmatory claim needs appropriately independent evidence or a justified design; renaming the same analysis as validation does not create independence. [Center for Open Science guidance](https://www.cos.io/initiatives/prereg) explains the purpose and limits of specifying plans in advance.

## Prioritize without false precision

Compare scientific relevance, discriminatory power, feasibility, and downside with qualitative reasons. For a close decision, identify which uncertain input could reverse the ranking. If the user supplies weights and anchored scores, show their influence and sensitivity rather than treating a weighted sum as objective truth.

For a premortem, focus on a few failure modes that would change the plan. For each, give the mechanism of failure, early evidence, mitigation, residual uncertainty, and a stop or pivot criterion. End with a concrete next action and the evidence needed to reconsider it.
