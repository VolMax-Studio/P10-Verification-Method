# P10 — The Verification Protocol
### Separating Signal from Artifact in Measured-System Claims

*A method, not an apparatus. Where a patent claims a device, this claims a procedure:
the disciplined separation of what the data supports from what the interpretation
invented. Domain-agnostic — applies to any claim built on measured signals.*

**Author:** Ivan Nestorov, VolMax Studio Lab
**Type:** Operational verification protocol (open doctrine)
**Version:** P10 v1.1
**Status:** Working protocol, validated on the author's own portfolio corpus

---

## Abstract

Most failures in data-driven engineering are not failures of measurement — the sensor
reports honestly — but failures of *interpretation* layered on top of it. This document
defines a verification protocol that locates and tests that interpretation layer through
five ordered levels, from data integrity to independent verdict. The protocol is
adversarial toward the analyst's own claims first, treats the caveat as the load-bearing
error-catching element rather than a disclaimer, and accepts a result only when it
regenerates from source.

The protocol does not *score* a model. It *explains a decision*. Every line in a P10
report traces to a specific test, every test to specific data and a specific script. Its
authority rests not on an institutional seal but on complete transparency: you do not have
to trust the verdict — you can re-run it.

---

## 1. Premise (the axiom)

> The sensor does not lie. The physics does not lie. Everything between the raw signal
> and the reported number is interpretation — and interpretation is where claims fail.

The verifier's position is the gap between measurement and claim. Independence from the
claim is not a courtesy; it is the precondition for a trustworthy verdict. An analyst
grading their own model has the same conflict of interest as a vendor selling it.

---

## 2. What P10 is — and what it deliberately is not

**P10 is a protocol that explains a decision.** It defines, in order, what is checked,
against what criterion, and what the pass/fail rule is — so that the final verdict is not
an opinion but a traceable conclusion.

**P10 is not a rating.** It produces no numeric score (no "96/100"), because a score that
does not regenerate from a formula is exactly the kind of unbacked number P10 exists to
catch in others. A verifier that assigns a flattering number has reacquired the vendor's
conflict of interest.

**P10 is not a certificate of authority.** It issues no accreditation. TÜV or DNV can
certify because an institution stands behind the seal; P10, at this stage, builds trust on
a different foundation — reproducibility. The report's weight comes from the fact that
every claim in it can be independently re-run, not from who signed it.

---

## 3. The P10 Generic Audit Workflow

To maintain complete reproducibility and eliminate hindsight bias, every P10 audit must progress through these seven ordered phases:

1.  **L0 Documentation:** Establish audit admissibility (verbatim claim, independent ground-truth anchor, resolution floor) and document data provenance and applicable licensing conditions.
    
    > [!IMPORTANT]
    > **State Gate Constraint:** No analytical computations or Level 1–4 execution steps may begin before the Data Freeze has been completed.
    
2.  **Data Freeze:** Lock a permanent dataset snapshot, calculate SHA-256 checksums, and register the input files in `data_manifest.json` to guarantee reproducibility.
3.  **Audit Preparation:** Decompose the technical claim into testable sub-claims, address resolution floor constraints, and define a-priori falsification rules before running analytics.
4.  **Execution:** Execute the predefined audit pipeline (L1–L4) against the frozen dataset. No modification of the frozen dataset is permitted, and no new hypotheses, rules, or thresholds may be introduced during this phase to prevent moving the goalposts.
5.  **Publication:** Determine the Level 5 verdict (**Verified**, **Verified with Limitations**, **Not Verified**, or **Unfalsifiable-as-Stated**) and issue the formal audit report.
6.  **Decision Log:** A mandatory registry entry tracking the audit's operational history. It must record:
    *   Claim ID
    *   Dataset version
    *   Audit version
    *   Protocol version (e.g., P10 v1.1)
    *   Verdict
    *   Confidence
    *   Known limitations & uncertainties
    *   Reviewer
    *   Date
7.  **Mandatory Reproducibility Archive (Immutable Audit Package):** Bundle the finalized assets into a static, unchangeable directory structure containing:
    *   `report.md` (the issued audit report)
    *   `metrics.json` (generated computational metrics)
    *   `decision_log.json` (machine-readable decision metadata log)
    *   `data_manifest.json` (frozen dataset manifest with hashes)
    *   `SHA256SUMS` (checksum file for bundle assets)
    *   `LICENSE` (audit redistribution terms)
    *   `sources.md` (verifiable URL/ Wayback links)
    *   `versions.md` (environment and dependency locks)

---

## 4. The verification sequence

The protocol begins with Stage 0 (Admissibility), followed by five ordered levels (L1–L5). **A failure at any stage halts the audit** — there is no point checking data integrity if the claim is structurally unfalsifiable, running statistics on data failed integrity, or testing reproducibility on a result already shown to be a physical artifact. The report states exactly where the audit stopped and why.


### P10-L0 — Audit Admissibility (Stage 0 Gatekeeper)
*Is this technical claim even capable of being audited?*

Checks: claimant identity, ground-truth anchor independence, mathematical/physical falsification thresholds, input reproducibility, and physical bounds (see detailed protocol in [P10_Audit_Admissibility_Protocol.md](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_Audit_Admissibility_Protocol.md)).

Rule: any check failure at Stage 0 classifies the claim as **Unfalsifiable-as-Stated** or redirects to **Reclassify**, terminating the audit immediately.

### P10-L1 — Data Integrity
*Is the input trustworthy enough to audit at all?*

Checks: dataset provenance; missing values; timestamp consistency; unit consistency;
sensor-calibration plausibility; duplicate records; split integrity (how train/test was
partitioned).

Rule: any integrity failure that would invalidate every downstream result **halts the
audit** at L1. A model cannot be verified on data that cannot be trusted.

### P10-L2 — Physics Compliance
*Does the model's output respect the governing law?*

Checks: conservation laws; monotonic degradation (no impossible "un-aging"); thermodynamic
limits; measurement resolution (no metric reported below the sensor's noise floor);
physical plausibility of the output range.

Outcome per check: **PASS / WARNING / FAIL.** A physics FAIL (e.g. a capacity estimate
that recovers spontaneously) is decisive — the floor is checked before the ceiling.

### P10-L3 — Statistical Integrity
*Is the reported number an effect of the data, or of the interpretation?*

Checks: leakage detection (train/test contamination); preprocessing leakage (transforms
fit before the split); group/batch leakage (unit or campaign signature standing in for
prediction); out-of-distribution behavior; effect-size correction (η²→ω², R²→adjusted);
confidence calibration (does the model quantify its own uncertainty, and is that
uncertainty calibrated); concurrence-vs-prediction (does a claimed predictor forecast, or
merely track).

Rule: a confirmed leakage or curation finding invalidates the reported accuracy — the
corrected number is computed and reported alongside the mechanism.

### P10-L4 — Reproducibility
*Can every number be regenerated from source?*

Requires: a reproducible script; deterministic execution (fixed seed); a version lock on
the code; a dataset identifier (hash) so the exact input is pinned; a report identifier so
the exact document is pinned.

Rule: if a headline number cannot be regenerated from the provided script, it is **FAIL**
— an unreproducible result is an assertion, not a finding.

### P10-L5 — Independent Verdict
*What is the honest conclusion, and why?*

One of three:
- **Verified** — survives held-out data and physical law; the reported number is the
  honest number.
- **Verified with Limitations** — holds under stated conditions, but with bounded
  caveats that are named explicitly (e.g. small calibration set; single operating
  condition; simulation-based ground truth).
- **Not Verified** — the reported number is an artifact of leakage, inflation, or
  curation, or cannot be reproduced; the corrected number (where one exists) is stated.

---

## 5. The output format — an audit trail, not a grade

The final decision is presented as a per-level trail. Each row carries a **status** and a
**reason** that points to a concrete test. This is not scoring; it is a documented chain
in which every decision can be checked.

**Example (an audit halted by leakage at L3):**

| Level | Status | Reason |
|---|---|---|
| L1 Data Integrity | PASS | Dataset complete; cell-level split verified |
| L2 Physics Compliance | PASS | No physical inconsistencies detected |
| L3 Statistical Integrity | FAIL | Cell-level leakage identified; accuracy invalidated |
| L4 Reproducibility | NOT EXECUTED | Audit terminated after L3 failure |
| **Final Verdict** | **Not Verified** | Leakage invalidates the reported accuracy |

Every entry answers "why" with a fact, not a number. "FAIL: cell-level leakage" leads
directly to the test that found it, which leads to the data and the script. That chain —
claim → test → data → script — is the whole product.

---

## 6. Report identity and integrity (stated for exactly what they do)

Each P10 report carries two technical elements. Their descriptions claim **exactly their
function and nothing more** — no implied accreditation, no legal weight.

- **Internal report ID** (e.g. `VM-2026-00184`): an internal document identifier for
  reference and versioning. It is not a certificate number and implies no external
  registry.
- **Document hash** (SHA-256 of the final report): allows any reader to verify that the
  report's content has not been altered after issuance. It is an integrity check on the
  file — nothing more. It does not confer legal validity or third-party certification.

Also recorded: date of issuance, protocol version (P10 v1.0), and the software/commit
version used to produce the results.

The discipline here is the same one P10 applies to numbers: **state exactly what the
element does, not a gram more.** A hash checks file integrity — so that is what is
claimed, not "guarantees validity." An ID names a document — so that is what is claimed,
not "certifies compliance."

---

## 7. The caveat theorem

**Claim:** In this protocol, the caveat is not a hedge appended to a conclusion — it is
the operator that performs the separation.

**Argument:** Every artifact in L3 is detected by a constraint that *narrows* the claim:
"split by unit" catches leakage; "report ω²" catches inflation; "full-set error" catches
curation; "held-out only" catches concurrence-as-prediction. Each is a caveat in
operational form. Removing caveats to maximize confidence or density removes exactly the
operators that catch the errors. Therefore a method optimized for "no caveats, deliver
immediately, density above all" is structurally identical to the unverified claim it is
meant to test — it has discarded its own instrument. **The caveat is the blade that
separates wheat from chaff; a verifier that drops it is winnowing with no wind.**

---

## 8. Worked example (validation on own corpus)

The protocol was applied, adversarially, to the author's *own* portfolio — the strongest
test of a verifier being whether it catches itself:

| Claim as first stated | Level / mechanism | Corrected verdict |
|---|---|---|
| Protocol explains η²=77% of cycle life | L3 inflation (~2 cells/group, null η²≈0.5) | ω²-corrected 66%; rate knobs <5% each |
| Discharge model reproduces paper at 9.97% | L3 curation (one fast-failing cell dropped) | full-set 18.3%; gap traced, cell kept |
| "OOD" partition demonstrates distribution shift | L1 fabricated artifact (renamed duplicate of test set) | removed; real shift built and labeled |
| R_ct r≈−0.95 indicates strong predictor | L3 concurrence-as-prediction | concurrent tracking only; not early-predictive |
| SOH point-estimate is safe under OOD | L3 uncertainty absent; conformal bounds bloat under shift | UQ necessary but not sufficient under shift |

Claims entered; not one survived unchanged. Each correction was produced by a caveat-
operator from a P10 level, applied to the author's own work before any external party
could. That is the portfolio's signature: hardest on its own claims first.

---

## 9. Honest status

This is a protocol, validated on the author's own corpus. It is not yet validated by
independent application to third-party claims under commercial conditions — that
validation comes only when an external client's claim is audited and the verdict holds up.
Until then it is a strong, self-consistent procedure with worked examples, not a proven
industry standard. Stated plainly, per its own rules.

---

*Physics doesn't lie. Sensors don't lie. The protocol stands at the gap, explains the
decision, and hands over the script.*
