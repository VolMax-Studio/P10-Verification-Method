# P10 — The Verification Framework
### Separating Signal from Artifact in Measured-System Claims

*A method, not an apparatus. Where a patent claims a device, this claims a procedure: the disciplined separation of what the data supports from what the interpretation invented.*

**Author:** Ivan Nestorov, VolMax Studio Lab  
**Status:** Open Doctrine / Core Methodology Entry Point  
**Version:** 1.1

---

## Overview

The P10 framework is a meta-verification protocol designed to evaluate data-driven claims on physical, measured systems. Rather than assigning a rating or score, P10 defines a reproducible sequence of tests that separates physical signal from interpretation-driven artifacts. 

The framework is structured as a two-stage process: a Stage 0 admissibility gatekeeper followed by a five-level computational audit.

---

## Directory Map

### 1. [L0 — Audit Admissibility Protocol](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_Audit_Admissibility_Protocol.md)
Before beginning any analysis, the proposed audit must pass the L0 checklist. It validates if the claim is mathematically and operationally falsifiable by confirming:
*   **Subject & Claim:** A specific claimant and testable assertion.
*   **Ground Truth Anchor:** An independent reference series sufficiently independent to permit falsification.
*   **Falsification Criterion:** Predefined limits under which the claim fails.
*   **Reproducible Inputs:** Versioned and immutable raw data accessible to reviewers.
*   **Physical Constraints:** Conservation laws limiting the solution space.

*If any check fails, the audit is terminated at L0 as **Unfalsifiable-as-Stated**.*

### 2. [L1–L5 — Core Verification Protocol](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_verification_protocol_v1.md)
Once admissibility is verified, the claim enters the core five-level audit:
*   **L1 Data Integrity:** Verifies data provenance, timestamps, calibration, and temporal split integrity.
*   **L2 Physics Compliance:** Enforces physical laws, conservation limits, and resolution thresholds.
*   **L3 Statistical Integrity:** Detects data leakage, preprocessing leakage, and concurrence tracking.
*   **L4 Reproducibility:** Pin-locks code and inputs, ensuring deterministic replication.
*   **L5 Independent Verdict:** Delivers the final verdict per admissible claim: *Verified*, *Verified with Limitations*, *Not Verified*, or *Unfalsifiable-as-Stated*.

> [!NOTE]
> **Multi-claim audits:** L0 applies per claim. A claim halted at L0 is recorded in the final ledger as **Unfalsifiable-as-Stated** alongside the L5 verdicts of all admissible claims. This preserves a single coherent report structure regardless of whether individual claims are rejected at the gatekeeper or proceed through the full L1–L5 stack.

### 3. [Domain Annex: Battery Systems](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_Battery_Annex.md)
Translates the general P10 protocol into concrete, domain-specific checks for electrochemical storage assets, defining explicit tests for capacity degradation, thermal response, and dispatch conformance.

---

## The Core Philosophy

1.  **Hardest on ourselves first:** The protocol is applied adversarially to the analyst's own assumptions first (see the [Governance Rejection Notice](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/REJECTION_NOTICE_v1.1.md) as a demonstration of self-applied admissibility limits).
2.  **No institutional seals:** Trust is established through complete, local reproducibility of every test and figure.
3.  **The Caveat Theorem:** Caveats are not disclaimers; they are the active operators that detect and bound statistical anomalies. A verifier that drops caveats has discarded its own instrument.
