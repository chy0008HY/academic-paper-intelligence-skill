from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_dossier", ROOT / "scripts" / "validate_dossier.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateDossierTest(unittest.TestCase):
    def make_valid_dossier(self, root: Path) -> None:
        report = (
            "# Report\n\n"
            "This dossier records the analyzed paper, reviewed material, argument, methods, "
            "claim-evidence findings, limitations, implications, confidence, and next actions. "
            "It is deliberately long enough to represent a substantive report rather than an "
            "empty placeholder. The evidence ledger below anchors the central finding."
        )
        (root / "paper_intelligence_report.md").write_text(report, encoding="utf-8")

        with (root / "source_ledger.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=MODULE.SOURCE_COLUMNS)
            writer.writeheader()
            writer.writerow(
                {
                    "source_id": "S1",
                    "title": "Example paper",
                    "source_type": "paper",
                    "identifier_or_url": "doi:10.0000/example",
                    "version_or_date": "2026",
                    "accessed_on": "2026-10-31",
                    "role": "focal paper",
                    "access_level": "full text",
                    "notes": "",
                }
            )

        with (root / "claim_evidence_matrix.csv").open(
            "w", encoding="utf-8", newline=""
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=MODULE.CLAIM_COLUMNS)
            writer.writeheader()
            writer.writerow(
                {
                    "claim_id": "C1",
                    "claim": "The method improves the reported metric.",
                    "claim_origin": "Author claim",
                    "location": "Table 1",
                    "evidence": "Reported comparison",
                    "source_id": "S1",
                    "support_label": "Partially supported",
                    "rationale": "The table supports the direction but uncertainty is missing.",
                    "caveat": "Single benchmark",
                    "verification_needed": "Check supplement",
                }
            )

    def test_valid_dossier_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_dossier(root)
            self.assertEqual(MODULE.validate(root), [])

    def test_unknown_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_valid_dossier(root)
            path = root / "claim_evidence_matrix.csv"
            text = path.read_text(encoding="utf-8").replace(",S1,", ",S9,")
            path.write_text(text, encoding="utf-8")
            errors = MODULE.validate(root)
            self.assertTrue(any("unknown source_id S9" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
