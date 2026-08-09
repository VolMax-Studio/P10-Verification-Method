---
name: p10-client-audit
version: 1.0.0
description: Operational execution protocol for conducting a formal VolMax P10 Verification Audit (L0–L5) on third-party technical claims, measured grid datasets, and BESS performance metrics. Use this skill whenever executing, drafting, or structuring a P10 audit report, admissibility check, or findings ledger.
---

# P10 Client Audit — Operational Execution Protocol (`p10-client-audit`)

> **"A method, not an apparatus. We do not score a model; we explain a decision. Every claim traces to a test, every test to data, every data point to a script."**

This skill codifies the **P10 Verification Protocol (v1.1)**, **L0 Audit Admissibility Protocol (v1.1)**, and **Battery Verification Annex**. It guides the agent step-by-step through evaluating third-party technical claims, executing L0–L5 checks, and producing an immutable, reproducible audit package.

---

## 1. Operational Execution Sequence (7-Phase Workflow)

```
L0 ADMISSIBILITY  →  DATA FREEZE  →  AUDIT PREP  →  L1–L4 EXECUTION  →  L5 VERDICT  →  DECISION LOG  →  REPRODUCIBILITY ARCHIVE
```

### Phase 1 — L0 Admissibility Assessment (Stage 0 Gatekeeper)
Before downloading data or writing code, evaluate the 5 Admissibility Criteria:
1. **Subject & Claim ($S \rightarrow C$):** Is there an explicit claimant making a checkable assertion?
2. **Ground Truth Anchor ($T$):** Does an independent reference exist to permit falsification?
3. **Falsification Criterion ($E$):** Is there a predefined threshold where the claim fails?
4. **Reproducible Inputs ($I$):** Are inputs versioned, immutable, and accessible?
5. **Physical/System Constraints ($P$):** Do physical laws constrain the feasible solution space?

*If ANY criterion fails $\rightarrow$ HALT AUDIT immediately. Issue Rejection Notice with disposition `Unfalsifiable-as-Stated` or `Reclassify`.*

### Phase 2 — Data Freeze & Provenance
Lock dataset into static archive. Compute SHA-256 hashes for all raw files and record in `data_manifest.json`.

### Phase 3 — Audit Preparation & Decomposing Claims
Decompose main claim into testable sub-hypotheses ($F_1, F_2, \dots, F_n$). Define a-priori pass/fail bounds before running analytics.

### Phase 4 — Execution (L1–L4 Pipeline)
Run analytics sequentially. **A failure at any level halts execution**:
- **L1 Data Integrity:** Missing values, timestamp gaps, sign conventions (Discharge $>0$, Charge $<0$), sensor noise floor.
- **L2 Physics Compliance:** Conservation of energy, monotonic degradation slope ($\frac{dC}{dt} \le \epsilon$), thermodynamic RTE bounds ($0.60 \le \eta_{\text{RTE, AC}} \le 0.92$).
- **L3 Statistical Integrity:** Train/test leakage, preprocessing leakage, effect-size correction ($\eta^2 \to \omega^2$), concurrence-vs-prediction, conformal uncertainty calibration.
- **L4 Reproducibility:** Single entry point script (`python audit_<asset>.py`) produces 0 numeric diff against `metrics.json`.

### Phase 5 — L5 Verdict Determination
Assign verdict from controlled vocabulary:
- **Verified:** Claim holds under pre-registered rules; numbers match ground truth.
- **Verified with Limitations:** Holds under bounded conditions; caveats explicitly named.
- **Not Verified:** Failed integrity, physics, leakage, or reproducibility tests.
- **Unfalsifiable-as-Stated:** Terminated at L0 (missing anchor, inputs, or falsification rule).

### Phase 6 — Decision Log Entry
Append immutable record to `decision_log.json` containing Claim ID, dataset hash, protocol version, verdict, reviewer, and date.

### Phase 7 — Immutable Reproducibility Archive
Build archive containing: `report.md`, `metrics.json`, `decision_log.json`, `data_manifest.json`, `SHA256SUMS`, `LICENSE`, `sources.md`, `versions.md`.

---

## 2. Domain Annexes (BESS Extensions)

- **Grid-Side Telemetry (G1.1–G1.3):** Discharge $>0$, Charge $<0$. Exclude COD/commissioning units from main baseline. Enforce AC RTE bounds $[0.60, 0.92]$.
- **Cell-Level & SCADA (C2.1–C2.4):** Monotonic capacity slope $\frac{dC}{dt} \le \epsilon$. SoC energy conservation continuity ($>3\%$ gap flags warning). Split Conformal Prediction required for SOH under OOD.
- **Electrochemical Impedance (EIS E4.1–E4.4):** Require 3-electrode disclosure for mechanism claims. Mid-frequency porosity overlap must be bounded. Residual Kramers-Kronig analysis required.

---

## 3. Output Format — Audit Trail Summary Table

Every P10 audit report MUST conclude with a per-level execution trail:

```markdown
| Level | Status | Reason / Evidence |
|:---|:---|:---|
| **L0 Admissibility** | PASS | All 5 criteria satisfied; ground truth anchor verified |
| **L1 Data Integrity** | PASS | Provenance verified; zero missing timestamps |
| **L2 Physics Compliance** | PASS | Monotonic capacity slope validated; RTE = 86.4% |
| **L3 Statistical Integrity** | FAIL / PASS | [Specific test result and leakage check] |
| **L4 Reproducibility** | PASS / NOT EXECUTED | Regenerates from source script with 0 diff |
| **Final Verdict** | **<VERDICT>** | <Summary explanation tracing to test failure/pass> |
```

---
*VolMax Studio Lab · P10 Verification Protocol Skill (v1.0.0)*
