#!/usr/bin/env python3
"""Validate an Academic Paper Intelligence dossier's traceability structure."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable


CLAIM_COLUMNS = (
    "claim_id",
    "claim",
    "claim_origin",
    "location",
    "evidence",
    "source_id",
    "support_label",
    "rationale",
    "caveat",
    "verification_needed",
)

SOURCE_COLUMNS = (
    "source_id",
    "title",
    "source_type",
    "identifier_or_url",
    "version_or_date",
    "accessed_on",
    "role",
    "access_level",
    "notes",
)

ALLOWED_ORIGINS = {
    "Author claim",
    "Direct paper evidence",
    "External evidence",
    "Analyst inference",
    "Unknown",
}

ALLOWED_SUPPORT = {
    "Supported",
    "Partially supported",
    "Weakly supported",
    "Contradicted",
    "Unclear from available material",
}


def read_csv(path: Path, required: Iterable[str]) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    if not path.is_file():
        return [], [f"missing required file: {path.name}"]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = tuple(reader.fieldnames or ())
        if headers != tuple(required):
            errors.append(
                f"{path.name}: expected columns {','.join(required)}; got {','.join(headers)}"
            )
        rows = list(reader)
    if not rows:
        errors.append(f"{path.name}: must contain at least one data row")
    return rows, errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    report = root / "paper_intelligence_report.md"
    if not report.is_file():
        errors.append("missing required file: paper_intelligence_report.md")
    elif len(report.read_text(encoding="utf-8-sig").strip()) < 200:
        errors.append("paper_intelligence_report.md: report is unexpectedly short")

    sources, source_errors = read_csv(root / "source_ledger.csv", SOURCE_COLUMNS)
    claims, claim_errors = read_csv(root / "claim_evidence_matrix.csv", CLAIM_COLUMNS)
    errors.extend(source_errors)
    errors.extend(claim_errors)

    source_ids = {row.get("source_id", "").strip() for row in sources}
    if "" in source_ids:
        errors.append("source_ledger.csv: source_id cannot be empty")
    if len(source_ids) != len(sources):
        errors.append("source_ledger.csv: source_id values must be unique")

    claim_ids: set[str] = set()
    for line, row in enumerate(claims, start=2):
        claim_id = row.get("claim_id", "").strip()
        if not claim_id:
            errors.append(f"claim_evidence_matrix.csv:{line}: claim_id cannot be empty")
        elif claim_id in claim_ids:
            errors.append(f"claim_evidence_matrix.csv:{line}: duplicate claim_id {claim_id}")
        claim_ids.add(claim_id)

        source_id = row.get("source_id", "").strip()
        if source_id and source_id not in source_ids:
            errors.append(
                f"claim_evidence_matrix.csv:{line}: unknown source_id {source_id}"
            )
        origin = row.get("claim_origin", "").strip()
        if origin not in ALLOWED_ORIGINS:
            errors.append(
                f"claim_evidence_matrix.csv:{line}: invalid claim_origin {origin!r}"
            )
        support = row.get("support_label", "").strip()
        if support not in ALLOWED_SUPPORT:
            errors.append(
                f"claim_evidence_matrix.csv:{line}: invalid support_label {support!r}"
            )
        if not row.get("rationale", "").strip():
            errors.append(f"claim_evidence_matrix.csv:{line}: rationale cannot be empty")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dossier", type=Path, help="Dossier directory to validate")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output")
    args = parser.parse_args()

    root = args.dossier.expanduser().resolve()
    errors = validate(root)
    result = {"ok": not errors, "dossier": str(root), "errors": errors}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif errors:
        print("FAIL: dossier validation failed")
        for error in errors:
            print(f"- {error}")
    else:
        print("PASS: dossier structure and traceability fields are valid")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
