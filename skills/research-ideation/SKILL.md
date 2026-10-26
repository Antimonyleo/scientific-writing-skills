---
name: research-ideation
description: Develop and stress-test STEM research questions, mechanisms, grant aims, and experimental or computational plans. Use for brainstorming, hypothesis generation, discriminating tests, controls, feasibility, and risks, especially molecular engineering and computational biology.
license: MIT
metadata:
  version: "1.1.0"
---

# Research Ideation

Turn an objective or observation into a small set of testable research directions and a useful next decision.

## Establish the scientific problem

State the objective and distinguish supplied observations, supported prior evidence, assumptions, and design choices. Identify real constraints: time, resources, material, instrumentation, model validity, and available readouts. Infer routine details; ask only about unresolved constraints that change the direction.

Match the shape of the request before generating anything:

| Request | Approach |
| --- | --- |
| Brainstorm directions, mechanisms, aims, or designs | Generate distinct options, then discriminate (below) |
| Stress-test one idea | Rank load-bearing assumptions by how likely each is false; find the cheapest refuting observation; brief premortem |
| Validate a claim or prediction | Map each claim to an independent measurement, controls, and a falsifying result |
| Choose between candidates | Compare them on explicit criteria; name the assumption that would flip the choice |

Do not manufacture new options when the user brought one idea or fixed candidates. The validation reference details the last three shapes.

For hypotheses, mechanisms, or grant aims, read [Hypotheses and aims](references/hypotheses-and-aims.md). For experiments, simulation plans, computational comparisons, or a premortem, read [Validation and decisions](references/validation-and-decisions.md). Load both only when the task needs both.

## Generate alternatives, then discriminate

1. Offer a few meaningfully different explanations or approaches. Vary mechanism or design principle rather than merely changing labels or parameters. Include a credible competing explanation for an observation.
2. For each promising direction, explain the mechanism, key assumption, predicted observation, observation that would challenge it, and smallest discriminating test. A resource or method-development objective can use performance and validation criteria without an artificial biological hypothesis.
3. Anchor each option to the closest prior approach you have checked and state what differs; otherwise mark the anchor and novelty unverified. Never rate novelty on your own authority. A brainstorm may precede searching, but mark unchecked premises and reopen options when evidence contradicts them. An incomplete search cannot establish novelty.
4. Compare information gained, feasibility, relevance, and risk with reasons and uncertainty. Put the cheapest observation that could disqualify a direction before costly confirmation, with cost stated as relative effort or an estimate labelled as such. Avoid invented budgets, probabilities, success rates, or scores without a basis.
5. Recommend the next action and the result that would change the recommendation. Set go, pivot, and stop criteria before collecting the deciding data. Preserve scientifically useful alternatives and the value of a null or negative outcome.

## Keep ideas distinct from findings

- A plausible mechanism is a hypothesis until supported. A proposed simulation or experiment is not completed evidence.
- Identify confounding and readout limits before claiming the proposed test distinguishes mechanisms. A measurement that all alternatives predict is not discriminating.
- Distinguish thermodynamic favorability from kinetic accessibility, predicted structure from observed structure, and structure from function. State relevant physical conditions and model regimes.
- For computational design, separate the optimization objective from independent evaluation; avoid evaluating on the data used to choose the design or tune the model.
- Preserve the distinction between exploratory and confirmatory work. A hypothesis generated after seeing outcomes requires appropriately independent evidence for a confirmatory test; do not call it prospectively specified.
- Suggest success thresholds only as justified targets or explicit provisional choices. Do not fabricate power calculations or infer that a small pilot proves reproducibility.

## Deliver a decision, not a generic idea list

Match the format to the task: a short mechanism comparison, a grant-aim outline, a validation plan, or a ranked premortem. Give enough detail to execute the next benign research step and identify the most consequential unknown. Do not make access commitments, initiate purchases, contact collaborators, or submit a proposal from an ideation request alone.
