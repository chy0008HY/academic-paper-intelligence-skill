# Research dossier output contract

Create a dossier directory when the user asks for a reusable, file-based, or full analysis.

## Required files

```text
dossier/
├── paper_intelligence_report.md
├── claim_evidence_matrix.csv
└── source_ledger.csv
```

Optional files, created only when relevant:

```text
figure_table_audit.md
methods_reproducibility.md
comparison_matrix.csv
reviewer_questions.md
```

## Report requirements

`paper_intelligence_report.md` must state:

- the paper and version analyzed;
- the user's task;
- material reviewed and unavailable material;
- one-sentence verdict and confidence rationale;
- research question and contribution;
- argument and method summary;
- claim-evidence findings;
- validity, limitations, and unresolved checks;
- implications and prioritized next actions.

Avoid copying long passages. Use short quotations only when exact wording is analytically necessary and permitted.

## Claim-evidence matrix

Required CSV columns:

```text
claim_id,claim,claim_origin,location,evidence,source_id,support_label,rationale,caveat,verification_needed
```

Use stable IDs such as `C1`, `C2`. `source_id` must resolve to the source ledger. Leave a field empty only when it genuinely does not apply; use `Unknown` when the information should exist but is unavailable.

## Source ledger

Required CSV columns:

```text
source_id,title,source_type,identifier_or_url,version_or_date,accessed_on,role,access_level,notes
```

Roles include focal paper, supplement, metadata, repository, dataset, related primary paper, or secondary context. Access levels include full text, partial text, abstract, metadata only, or unavailable.

## Validation

Run `scripts/validate_dossier.py` on the dossier directory. Fix structural errors before delivery. Report scientific uncertainty separately; a structurally valid dossier can still contain uncertain evidence.
