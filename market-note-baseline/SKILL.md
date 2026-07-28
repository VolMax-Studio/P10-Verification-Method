---
name: market-note-baseline
version: 1.4.0
description: Standardization factory protocol for creating VolMax Open Market Notes (#001–#010+). Ensures every market baseline follows identical L0–L3 pipeline structure, frozen PARAMS templates, and reproducible deterministic execution.
---

# Market Note Baseline — Factory Protocol (`market-note-baseline` v1.4.0)

> **"One methodology, multiple markets. Every Open Market Note measures the market with identical discipline, deterministic pipeline execution, and zero normative overreach."**

This skill codifies the **Open Market Note Factory Standard**. It provides the mandatory structure and execution lifecycle for all VolMax telemetry and duration baselines across NEM, ERCOT, ENTSO-E, GB, and future power markets.

---

## 1. Mandatory Core Principles

### Principle 1 — One Note = One Primary Metric ($M_1$)
- **Rule:** A Note measures **EXACTLY ONE** primary metric ($M_1$).
- **Metric Creep Prohibition:** If exploratory data processing uncovers secondary phenomena, **DO NOT ADD THEM TO THE NOTE**. Relegate secondary discoveries to an appendix or spin them off into a separate Note (#006, #007, etc.).

### Principle 2 — Append-Only Decision Ledger (`DECISIONS.md`) & Impact Matrix
- Every Note MUST log design decisions prior to data download u an immutable, append-only `DECISIONS.md` file.
- **Decision Lifecycle Status:** Every decision block MUST specify an explicit lifecycle status (`Status: Active` or `Status: Superseded by D-00X`). Decisions are **NEVER deleted or silently overwritten**.
- **Evidence Required Block:** Every decision MUST specify testable evidence requirements (e.g., API field references, documentation links, mathematical conditions).
- **Decision Impact Matrix:** Every `DECISIONS.md` MUST include a dependency graph matrix mapping each Decision ID to affected downstream artifacts (`M1 calculation`, `summary.json`, `figures`, `README`, `LinkedIn`, `audit hash`).
- **Ledger vs Changelog Distinction:**
  - *Decision Ledger (`DECISIONS.md`):* Answers "Why did we choose these rules BEFORE downloading data?"
  - *Parametric Changelog (`PARAMS.md`):* Answers "What parametric values changed during post-release maintenance and why?"

### Principle 3 — Deterministic Pipeline Execution (Single Entry Point)
- **Single Entry Point Rule:** The entire end-to-end execution MUST run deterministically via a single entry point command (e.g. `python run_pipeline.py` or `./run.sh`) that regenerates `summary.json` with 0 numeric diff.

### Principle 4 — Cryptographically Locked Protocol Stack Metadata (`methodology_sha256`)
- Every computational JSON output (`summary.json`, `input_manifest.json`) MUST include an embedded `protocol_stack` metadata block containing the SHA-256 hash of the methodology parameters:
  ```json
  "protocol_stack": {
    "market-note-baseline": "1.4.0",
    "p10-gate": "1.1.0",
    "p10-client-audit": "1.0.0",
    "methodology_sha256": "<SHA256 of frozen PARAMS.md + DECISIONS.md>"
  }
  ```

### Principle 5 — Scope Exit vs Empirical Limitations
- Every `PARAMS.md` MUST maintain a clear separation between:
  - *Out of Scope (Methodological Scope Exit):* Questions intentionally left unanswered (e.g., operator evaluation, investment advice).
  - *Known Empirical Limitations (Data & Physical Bounds):* Operational constraints of data sources (e.g., publication delays, telemetry resolution, API outages).

---

## 2. Mandatory PARAMS Architecture

Every Open Market Note MUST contain a frozen `PARAMS.md` matching this exact skeleton:

```markdown
# PARAMS — Open Market Note #<ID> (<Market> <Metric> Baseline)

> **Document Status:** Frozen for L0 Release  
> **Version:** v1.0.0  
> **Date Frozen:** <ISO-8601 Timestamp>  
> **Licensing Anchor:** <License Name & Citation>  
> **Protocol Stack:**  
> - market-note-baseline v1.4.0  
> - p10-gate v1.1.0  
> - p10-client-audit v1.0.0

## 1. Scope Classification, Scope Exit & Empirical Limitations
Type: Descriptive Market Measurement

Out of Scope (Intentionally Unanswered Questions):
- Operator performance evaluation
- Market design quality assessment
- Investment recommendations
- Dispatch optimization modeling
- Causal attribution of physical bottlenecks

Known Empirical Limitations (Data & Physical System Bounds):
- Operational limitations of data source and telemetry resolution

## 2. Decision Impact Matrix
| Decision ID | Target Area | Affected Downstream Artifacts |
| :---: | :--- | :--- |
| `D-001` | M1 Threshold | M1 computation, summary.json, figures, README |
| `D-002` | Spatial Scope | Corridor loop, dataset manifest, summary.json |
| `D-003` | Denominator Hierarchy | Capacity parser, exclusion filter, summary.json |
| `D-004` | Directional Handling | Power flow sign logic, figures, README |
| `D-005` | Normalization | Time-weighting calculator, event duration |

## 3. Core Metric Definition (M1)
* Decision Source: D-001
[Mathematical expression, threshold definition, and event boundary]

## 4. Mandatory Metric Rules
* Rule A: Denominator Hierarchy (Decision Source: D-003)
* Rule B: Sub-Hourly Normalization (Decision Source: D-005)
* Rule C: Directional / Polar Neutrality (Decision Source: D-004)

## 5. Evaluated Corridors / Zones
* Decision Source: D-002
[Explicit list of bidding zones, nodes, or interconnections]

## 6. Primary Data Source & Provenance
[API endpoint / raw disclosure, resolution, license anchor URL]

## 7. Parametric Changelog
| Version | Date | Change Description | Empirical Justification |
```

---

## 3. Note Production Lifecycle (L0–L3 Workflow)

```
L0: FREEZE & PRE-CHECK  →  L1: DETERMINISTIC PIPELINE  →  L2: REGENERATE & CHARTS  →  L3: P10-GATE & PUBLISH
```

### L0 — Licensing & Pre-Check
- Verify CC BY or public domain license verbatim.
- Conduct Pre-L0 5-Question Audit (CC BY, Deterministic Pipeline, 1 Metric, BESS/EMS Relevance, Descriptive vs Normative).
- Log pre-registration choices with Status, Evidence Required, and Impact Matrix in append-only `DECISIONS.md`.
- Compute `methodology_sha256` hash over `PARAMS.md` and `DECISIONS.md`.
- Freeze `PARAMS.md` (v1.0.0).

### L1 — Deterministic Pipeline & Data Freeze
- Run end-to-end pipeline via single entry point command (`python run_pipeline.py`).
- Generate `input_manifest.json` containing endpoint parameters, query hashes, `protocol_stack`, and `methodology_sha256`.
- Raw payloads frozen u `data/` with SHA-256 manifest (`data_manifest.json`).

### L2 — Analytical Pipeline & Artifact Generation
- Compute metric $M_1$ $\to$ output `summary.json` (embedded with `protocol_stack` and `methodology_sha256`).
- Generate figures $\to$ output `./figures/`.
- Assemble `README.md` containing Executive Summary, Metric Table, ASCII Distribution, Scope Exit, Known Limitations, Decision Impact Matrix, and References.

### L3 — Governance & Gate Review
- Update master `STATUS.md` status to `Under Review`.
- Execute **`p10-gate`** audit on Note package.
- Draft LinkedIn announcement (placing errors/changelogs BEFORE findings).

---
*VolMax Studio Lab · Open Market Note Factory Standard (v1.4.0)*
