# Evidence and claim policy

## Evidence classes

Tag important statements by origin:

- **Author claim:** explicitly stated by the paper.
- **Direct paper evidence:** result, figure, table, equation, method, or supplement directly observed.
- **External evidence:** information from another identified source.
- **Analyst inference:** a reasoned interpretation not explicitly stated by a source.
- **Unknown:** not verifiable from the reviewed material.

Do not silently convert an author claim into a verified fact or an analyst inference into an author conclusion.

## Support labels

- **Supported:** the available evidence directly and adequately supports the claim within its stated scope.
- **Partially supported:** relevant evidence exists, but scope, design, uncertainty, assumptions, or missing checks limit the conclusion.
- **Weakly supported:** evidence is indirect, underpowered, poorly matched, or materially incomplete.
- **Contradicted:** available evidence conflicts with the claim.
- **Unclear from available material:** the necessary section, data, figure, supplement, or external verification is unavailable.

Always attach a short rationale. Labels are judgments about a specific claim, not scores for the whole paper.

### Abstract-only causal rule

An observational abstract cannot by itself establish causality. Never assign `Supported` to a causal claim from that evidence alone. Record the observed relationship as an association; mark the causal interpretation `Unclear from available material`, or use `Partially supported` only when the rationale explicitly limits support to the association.

Before evaluating a causal interpretation, look for the estimand and identification strategy, temporal ordering, confounding control, selection mechanisms, measurement validity, missingness, adjustment or collider bias, sensitivity analyses, and assumptions connecting the design to the causal claim. Missing information is a verification gap, not evidence that the design is invalid.

## Overclaim checks

Look for:

- causal language from observational or otherwise unidentified designs;
- generalization beyond the sampled population, task, benchmark, geography, or time period;
- practical importance inferred from statistical significance alone;
- “state of the art” claims without comparable baselines or current context;
- cherry-picked metrics, subgroups, thresholds, or figures;
- conclusions based on proxy outcomes that do not establish the target construct;
- absence claims based on non-significant results or incomplete search;
- robustness claims without sensitivity analysis across plausible choices;
- reproducibility claims unsupported by code, data, environment, seeds, or sufficient method detail.

## Figure and table checks

For each decisive visual, record:

- what is measured and on which population or dataset;
- axes, scale, denominator, uncertainty, and aggregation;
- comparison group or baseline;
- whether the caption and text match the displayed result;
- whether the visual supports magnitude, direction, mechanism, or only association;
- missing panels, exclusions, or transformations that affect interpretation.

## Confidence

State confidence as high, medium, or low only when useful, followed by reasons. Full-text access, transparent methods, direct evidence, convergent checks, and reproducibility assets raise confidence. Abstract-only access, ambiguous extraction, missing supplements, unsupported assumptions, or unresolved contradictions lower it.
