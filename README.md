# Academic Paper Intelligence Skill

A unified Codex skill for turning selected academic literature into traceable research intelligence.

It combines paper triage, deep reading, claim-evidence analysis, method and figure auditing, targeted literature context, comparison, and peer-review preparation in one workflow. It is designed for direct reuse whenever you provide a PDF, DOI, arXiv ID, title, or paper URL.

## Install

```text
$skill-installer install https://github.com/chy0008HY/academic-paper-intelligence-skill
```

Start a new Codex turn after installation. Automatic invocation is enabled, or invoke it explicitly as `$academic-paper-intelligence`.

## Example requests

- `用 $academic-paper-intelligence 解析這篇 PDF，建立 claim-evidence matrix。`
- `比較這三篇論文的方法、證據強度與可重現性。`
- `分析這篇研究是否足以支持作者的因果結論。`
- `整理成組會可用的文獻 intelligence dossier。`

## Outputs

Short tasks return a calibrated chat analysis. Full analyses can produce a reusable dossier containing a report, claim-evidence matrix, and source ledger. See `references/output-contract.md`.

## Validation

```text
python C:/Users/minks/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python -m unittest discover -s tests -v
```

## Provenance

This is a clean-room synthesis informed by four public projects. Their revisions, license status, and high-level design influence are documented in `references/provenance.md`; their source code and prompts are not bundled here.
