# Validation plans and research decisions

## Choose a test that can change the decision

Identify the most consequential assumption and a feasible observation that distinguishes the leading explanations or design options. Prefer a small informative experiment or simulation before a large optimization campaign when it can rule out an unsuitable mechanism or readout. Order tests by the cost of reaching a disqualifying answer: a quick gel, control, or calculation that could end a direction comes before an expensive confirming measurement. Give cost as relative effort, time, or instrument and compute use; label estimates and take numbers from the user's constraints rather than inventing them.

For a validation request, map each claim to an independent observable: what the measurement can and cannot resolve, the expected effect relative to its resolution and run-to-run variation, the controls, and the result that would falsify the claim rather than merely fail to support it. Rerunning the model or design tool that produced a prediction is not independent validation.

Specify inputs, perturbations or groups, independent experimental unit, comparator, readout, analysis, expected outcomes under the alternatives, and the resulting decision. Use negative controls, positive controls, matched baselines, ablations, and orthogonal readouts where each has a defined purpose.

Distinguish repeated measurements from independent replication. State how batches, preparations, sequences, fields of view, or simulation trajectories enter the inference. Do not select a sample size or claim adequate power without an estimand, variability assumption, meaningful effect, and justified analysis. A pilot can estimate feasibility or variability without establishing generality.

## Computational and physical validation

Separate code correctness, numerical convergence, agreement with a model, and agreement with experiment. A successful software test validates the tested behavior; it does not validate the physical assumptions.

For a computational comparison, match inputs, hardware or resource budget, stopping criteria, baseline tuning, and quality metrics. Retain relevant software versions and seeds. Separate tuning from evaluation; use independent data or held-out conditions when evaluating generalization. Check parameter sensitivity, model regime, units, boundary conditions, and the cost of uncertainty where relevant.

Before trusting a model's output, state what that model does not represent, and check that the question falls inside its validity domain: the conditions it was parameterized for, the interactions it omits, and whether it speaks to equilibrium, kinetics, geometry, or yield at all. A design or simulation tool that cannot represent the deciding factor cannot answer the question, however good its score. Where a design environment differs from the intended application environment, such as buffer composition, ionic strength, temperature, degrading enzymes, or available instrument resolution, treat performance in the application environment as a separate claim needing its own measurement. Match each readout to the question: state the expected effect against the instrument's resolution and run-to-run variation, and prefer the cheapest readout that can disqualify the design.

For molecular engineering, link the proposed structural assay and functional assay to separate claims. A structure consistent with a design is one result; optical, mechanical, kinetic, or biological performance needs an appropriate independent readout.

## Plan interpretation before collecting decisive evidence

Record the expected observation under each leading explanation, a null or ambiguous outcome, likely assay failure, and what each would imply. Separate technical failure from evidence against the mechanism. Explain when to repeat, redesign, stop, or advance.

Write go, pivot, and stop criteria before collecting the deciding data: the observation, the threshold and its basis (pilot data, a physical model, measurement resolution, or the user's target), when it will be evaluated, and the action on each branch. A pivot names a different approach to the same question, not the same approach with more effort. Heilmeier's questions, including cost, duration, and mid-term and final "exams", are a quick audit for a proposed direction.

If the hypothesis arose from an already examined dataset, identify what was seen and which data remain untouched. A later confirmatory claim needs appropriately independent evidence or a justified design; renaming the same analysis as validation does not create independence. [Center for Open Science guidance](https://www.cos.io/initiatives/prereg) explains the purpose and limits of specifying plans in advance.

## Prioritize without false precision

Compare scientific relevance, discriminatory power, feasibility, and downside with qualitative reasons. When choosing between candidates, also compare the cost to the first informative result, the chance that result is interpretable, what each option unlocks or forecloses, and the cost of stopping. For a close decision, identify which uncertain input could reverse the ranking. If the user supplies weights and anchored scores, show their influence and sensitivity rather than treating a weighted sum as objective truth.

For a stress test of one idea, list its load-bearing assumptions, rank them by how likely each is false, and identify which can already be checked with existing data or tools. For a premortem, focus on a few failure modes that would change the plan. For each, give the mechanism of failure, early evidence, mitigation, residual uncertainty, and a stop or pivot criterion. End with a concrete next action and the evidence needed to reconsider it.
