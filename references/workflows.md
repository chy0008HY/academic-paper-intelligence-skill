# Analysis modes and reading workflow

Read only the mode relevant to the user's request. All modes share the evidence policy and source ledger.

## Triage

Use when the user needs to decide whether a paper deserves close reading.

Capture identity, access level, research question, claimed contribution, apparent method, relevance, obvious credibility or fit concerns, and the next reading decision. Do not produce a detailed validity judgment from the abstract alone.

## Abstract-only appraisal

Use when the abstract is the most complete material available and the user still needs an initial interpretation.

Produce a provisional appraisal containing:

- claims explicitly reported in the abstract;
- design details that are stated versus missing;
- association-versus-causation boundary;
- conclusions that require methods, results, figures, tables, or supplements;
- a prioritized full-text verification checklist.

Do not simulate a deep read, figure audit, statistical audit, or reproducibility assessment. Mark those fields `Unknown` or `Unclear from available material`. If the user asks only for a dossier outline, return the proposed sections and fields without populating unavailable evidence.

## Deep read

Use for understanding, group meetings, thesis work, or method reuse.

Perform three passes:

1. **Whole-argument pass:** abstract, introduction, contribution statements, conclusion, and limitations.
2. **Evidence pass:** methods, experiments/results, figures, tables, supplement, and ablations or robustness checks.
3. **Challenge pass:** test whether each conclusion follows from the design and displayed evidence; identify missing controls, alternative explanations, boundary conditions, and original-paper checks.

Finish with a claim-evidence matrix and implications for the user's project.

## Review

Use for an authorized peer-review draft or review preparation. Evaluate the paper actually supplied, not a different study the reviewer wishes had been conducted.

Report summary, strengths, major concerns, minor concerns, questions for authors, reproducibility, ethics where relevant, and confidence. Give locations and explain why each issue matters. Offer feasible remedies without demanding unlimited new work.

Do not reveal confidential material or search for author identity when blinded review rules prohibit it.

## Compare

Use for two to five explicitly named papers. Apply the same fields to every paper:

- question and scope;
- design/data;
- contribution;
- evidence strength;
- validity risks;
- reproducibility;
- relevance to the user's decision.

Avoid a winner-only ranking. Explain tradeoffs, non-comparable assumptions, and which paper is more informative for which purpose.

## Context map

Use when novelty, field position, or a disputed claim requires external literature.

Search narrowly around the focal claim. Prefer DOI registries, publisher or venue pages, preprint servers, official repositories, and primary research. Record search date, query or discovery route, and source role. Distinguish a targeted context map from a systematic review; do not claim exhaustiveness.

## Source acquisition order

1. User-provided full text and supplements.
2. Official publisher, venue, DOI, or preprint record.
3. Official project/repository and registered data or protocol.
4. Related primary papers.
5. Reviews or secondary commentary for orientation only.

If multiple versions exist, record the analyzed version and note meaningful version differences when known.
