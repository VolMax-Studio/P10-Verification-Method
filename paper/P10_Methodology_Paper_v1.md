---
Title: "P10 Grid-Scale Asset Verification Methodology"
Author: "Nestorov, Ivan (VolMax Studio Lab)"
ORCID: "0009-0006-7940-9539"
Date: "2026-07-12"
License: "CC BY 4.0"
Version: "v1.0 (Level 5 Verdict: Verified with Limitations; F4 Deferred pending ERCOT SCED database documentation)"
---



---

# Section 1: Introduction: The Verification Gap in Grid-Scale Assets

## 1.1 The Adversarial Audit and Data Containment
A recurring pattern observed in conventional grid asset verification is a reliance on invasive, prosecutorial audits that demand proprietary internal logs. When verification requires access to sensitive, developer-level files—such as raw battery management system (BMS) logs, private firmware databases, or proprietary SCADA histories—asset operators often respond with *data containment*. This tension is demonstrated by structural halts in public verification, where claims regarding sub-second grid-stability or virtual capacity aggregation are not published in public records due to telemetry resolution boundaries or Balancing Mechanism aggregation rules. The resulting asymmetry of information makes independent verification impossible; when auditors must rely on the claimant to provide the underlying data, the audit's independence is compromised from the outset.


## 1.2 The Flattery and Illusions of Self-Reported Metrics
In the absence of independent verification, the energy transition relies on self-reported, vendor-supplied data. This creates three distinct classes of verification risk:

1.  **Flattered Backtests:** Operational models are historically vulnerable to post-hoc optimization and parameter tuning, making it easy to flatter performance prior to live grid dispatch.
2.  **Purchased Illusions:** Without independent anchoring, asset buyers purchase capacity and degradation guarantees that exist only in contractual warranties and cannot be physically demonstrated in the field.
3.  **Idealized Datasheets:** Manufacturer specifications represent idealized laboratory behavior that systematically hides the real-world performance losses caused by auxiliary loads, degradation, and ambient environmental conditions.

When verification is based on proprietary, self-reported data, the boundary between auditing an operational claim and merely republishing a marketing document disappears.

## 1.3 The Path to Non-Invasive Falsification
The VolMax P10 Verification Protocol proposes a structural alternative: **non-invasive falsification**. Instead of demanding proprietary internal logs, P10 audits grid assets by matching their public nameplate claims against independent, public grid telemetry anchors (such as regulatory market dispatch records or public operator dashboards).

By shifting the auditor's role from an adversarial prosecutor demanding private data to a neutral scientist verifying public, reproducible traces, we bypass the data containment wall. If a claimed capability cannot be observed through the physical and regulatory trace it leaves on the public grid, the claim is not declared fraudulent; it is simply classified as *Unfalsifiable-as-Stated* and halted at Level 0. This paper details the P10 protocol—comprising an L0 admissibility gate followed by a five-level verification sequence (L1–L5)—and demonstrates its application through two real-world battery energy storage system (BESS) case studies.

---

# Section 2: The Admissibility Layer (Level 0) and the Doctrine of Falsifiability

## 2.1 The Definition of Unfalsifiable-as-Stated

A claim is *falsifiable from public data* if one can name, in advance, a specific piece of independent public evidence that would appear differently depending on whether the claim is true or false. Where such evidence exists and is accessible, the claim can be admitted to audit: the true and the false version of the world leave distinguishable traces, and the audit's job is to determine which trace the data actually shows.

A claim is classified as *Unfalsifiable-as-Stated* when no such distinguishing public evidence exists — that is, when the true and the false version of the claim would leave the same (or no) trace in any available public record. Under such conditions the claim cannot be confirmed or refuted from open data, irrespective of its actual truth value.

This classification is deliberately neutral. It is a statement about the observability of the claim, not about the honesty of the developer or the performance of the asset. A claim may be entirely true and still be Unfalsifiable-as-Stated; the disposition records only that open data cannot adjudicate it. Distinguishing "we cannot test this" from "this is false" is the central discipline the admissibility layer exists to enforce, and conflating the two is the most common error in ad-hoc verification.

## 2.2 The Anchor: What Makes Evidence Admissible

Every Level 1 (L1) audit rests on an independent evidentiary anchor. The anchor need not be of any single institutional type; across the VolMax portfolio it has taken at least two distinct forms:

- **Regulatory settlement telemetry** — the accounting record a market operator maintains for financial settlement, e.g., Elexon B1610 actual generation output (GB) or ERCOT SCED 60-Day ESR telemetry disclosure (US-TX).
- **Operator-disclosed public telemetry** — data an operator publishes on a public dashboard, e.g., the ECO STOR Bollingstedt operational export (`speicherbetrieb.eco-stor.de`).

What qualifies a source as an anchor is not its institutional origin but three properties: it must be **public** (accessible without privileged access), it must be **independent of the audit** (not produced or shaped by the verifier), and it must **expose falsifiable quantities** (values whose internal consistency or physical plausibility can be checked, such as power against a declared ceiling).

The type of anchor bounds what can be tested. The Bollingstedt dashboard export, for instance, admitted active-power and dispatch analysis but exposed no state-of-charge or round-trip-efficiency fields; the L2 physics layer for that audit was therefore recorded as *N/A - Not testable from this export*, not as a passed or failed check. The absence of a data field is itself a documented limitation, never silently filled.

The alternative to a qualifying anchor is reliance on proprietary logs, developer-supplied spreadsheets, or backcast simulations. Each of these originates with a party holding an interest in the result, which collapses the distinction between auditing a claim and reporting it. A qualifying anchor is what keeps the verifier independent rather than a conduit for the claimant's own figures.

## 2.3 The Boundary Dimensions: Resolution and Aggregation Floors

Even where a qualifying anchor exists, its granularity bounds which claims remain admissible. Two boundaries recur across the portfolio:

1. **The Resolution Floor.** Defined by the temporal and physical granularity of the anchor. Elexon B1610, for example, is reliable settlement data but resolves to 30-minute intervals; it cannot capture sub-second active-power behaviour or transient grid-forming response such as synthetic inertia. High-resolution stability claims therefore fall beneath the resolution floor and are halted at Level 0 as Unfalsifiable-as-Stated — not because they are false, but because no public record resolves them. (Case: Zenobē synthetic inertia.)

2. **The Aggregation Floor.** Defined by the boundaries of asset registration. Embedded or behind-the-meter assets may carry no standalone registration, aggregating their output under a virtual or supplier Balancing Mechanism unit. The physical asset exists and operates, but its individual per-unit behaviour cannot be isolated within the aggregate, so the claim cannot be tested at the unit level from public channels. (Case: Bramley BESS.)

Both floors produce the same disposition — Unfalsifiable-as-Stated — from opposite causes: the resolution floor is a limit of *granularity*, the aggregation floor a limit of *identifiability*. Naming which floor a claim falls beneath is part of the L0 record, so that the halt is attributable to a specific structural cause rather than to verifier discretion.

## 2.4 The Verdict Taxonomy

To ensure methodological clarity, P10 defines a strict verdict vocabulary. Verification results are reported at two levels: **Level 1–4 Findings** (evaluating individual physical or data rules) and the **Level 5 Final Verdict** (the overall audit conclusion).

### Table 2.1: Finding Dispositions (L1–L4)
| Finding Status | Meaning | Application Example |
| :--- | :--- | :--- |
| **Passed** | The dataset or physical rule satisfies the pre-registered audit criteria without exceptions. | L1 Data Integrity or L2 Physics (RTE) |
| **Demonstrated** | Telemetry proves the asset achieved or exceeded the claimed nameplate rating at the grid boundary. | Anole 240 MW export capacity (Claim 001a) |
| **Bounded** | Observed dispatch verifies performance but limits it below the nominal nameplate capacity. | Pillswood 97.78 MW peak export (nominal 98 MW) |
| **Inconsistent** | Telemetry violates pre-registered physical or logical consistency rules. | Anole SoC telemetry failing the F3 80% pass threshold |
| **Deferred** | Evaluation is postponed due to semantic ambiguity or lack of official column/schema definitions. | Anole F4 max_soc column semantics |

### Table 2.2: Final Audit Verdicts (L5)
| Final Verdict | Meaning | Mapping |
| :--- | :--- | :--- |
| **Verified** | The asset's claims are fully confirmed without material caveats, failures, or unresolved semantics. | All L1–L4 findings are `Passed` or `Demonstrated`. |
| **Verified with Limitations** | The claims hold under stated conditions, but with documented physical bounds, data gaps, or deferred sub-claims. | Active power capacity is `Bounded` or specific parameters are `Deferred`/`Inconsistent`. |
| **Not Verified** | The reported capacity is refuted by grid telemetry, cannot be reproduced, or lacks an admissible anchor. | The audit fails L1–L2 gates, or L0 admissibility is halted. |

---

# Section 3: The Failure Registry: Mapping the Boundaries of Open Data

To demonstrate that the admissibility layer performs real exclusion rather than a rubber-stamp compliance check, we catalog nine case studies where auditing stalled, was corrected, or collapsed. 

These cases are mapped across two orthogonal axes:
1.  **The Causal Axis:** Categorized by the source of the failure: *Boundary* (data availability or licensing constraints), *Verifier* (human design or process errors), *Tooling* (automated agent-level gaps), or *Empirical* (falsification or rejection of model hypotheses by grid telemetry).
2.  **The Intervention Axis:** Categorized by the temporal phase and cost of the correction. This spans a spectrum from low-cost, upfront halts (Cases 1, 2, 4, and 5) that prevent the audit from launching, through mid-stream corrections caught during the verification process (Case 8), to high-cost retractions of published or pre-registered conclusions (Cases 3 and 7). Scope rejections (Case 6) occupy the boundary between design rules and process constraints, while Case 9 represents an empirical rejection where the data is admissible but the physical hypothesis is refuted by grid performance.

---


## 3.1 Boundary Failures (Data, License & Physics Limits)
Boundary failures occur when the physical, regulatory, or legal constraints of the open data ecosystem prevent verification. These cases define the outer limit of what can be audited from the public domain.

1.  **RTE7000 Halt:** A Level 0 Halt triggered by the complete absence of a falsifiable public telemetry anchor. This failure exposed the vulnerability of attempting to verify performance claims without a grid-tied baseline, serving as the historical catalyst for creating the L0 admissibility protocol.
2.  **BattGP L0 Halt:** A Level 0 Halt caused by data licensing restrictions. Although the physical data existed, it was restricted by a Creative Commons Attribution-NonCommercial (CC BY-NC) license, which blocked open audit execution and commercial replication.
3.  **GB RTE Withdrawal:** The retraction of a pre-registered verification threshold because the necessary certified physical curves could not be obtained from the public registry, preventing the execution of the L2 physics compliance check.
4.  **Zenobē Stability Halt (Resolution Boundary):** A Level 0 Halt on synthetic inertia and grid-stability claims. The audit was blocked because sub-second nodal voltage and frequency waveforms are proprietary and not published by the system operator (NESO), falling beneath the temporal resolution floor of public data.
5.  **Bramley BESS Halt (Aggregation Boundary):** A Level 0 Halt on the `UK-BWESS-001` capacity claim. The audit was halted because individual BM Unit telemetry could not be located in the Elexon registry, exposing how virtual aggregation hides individual asset behavior.

*What this class proves:* Boundary failures demonstrate that the protocol maps real-world data and physical constraints rather than operating in a theoretical vacuum, ensuring that audits only proceed when grounded in verifiable physical records.

---

## 3.2 Verifier Failures (Human Design & Process Errors)
Verifier failures document errors in the design and execution of the methodology itself. Acknowledging these failures enforces the self-correcting discipline of the verifier.

6.  **v1.1 Rejected:** The formal rejection of P10 version 1.1 due to domain-specific bloat and the fabrication of speculative model entities (such as Lyapunov exponents, Detrended Fluctuation Analysis [DFA], HALO parameters, and the "VolMax Engine") to protect and maintain a lean, domain-agnostic core.
7.  **L0 Admissibility Correction (Self-Failure):** The correction of a previously published `ADMISSIBLE` verdict for BW ESS. The verifier had speculatively assumed that the identifier `E_BRLE-1` existed and mapped to its T4 capacity market profile. Direct API registry queries disproved the assumption, forcing the verifier to correct the verdict to `HALTED`.

*What this class proves:* Verifier failures demonstrate the verifier's capacity for self-correction, proving that the protocol does not suffer from self-reinforcing bias and will actively retract its own errors when exposed to new registry evidence.

---

## 3.3 Tooling Failures (Machine & Agent-Level Gaps)
Tooling failures record errors introduced by automated agents, highlighting the necessity of human gating.

8.  **Model Gap-Filling Bias (AI Error):** The tendency of automated agents to fill telemetric and registry gaps with speculative physical or commercial mechanisms (e.g., asserting a confirmed ID in report headers and claiming an asset was "aggregated inside a virtual portfolio" despite having only a negative search result). This registry entry documents the verifier's vulnerability to presenting speculative explanations as verified fact.

*What this class proves:* Tooling failures highlight the necessity of a human-in-the-loop gate, showing that automated verification pipelines cannot be blindly executed without active human oversight of the qualitative claims.

---

## 3.4 Empirical Rejections (Hypothesis Falsification)
Empirical rejections occur when the open data and telemetry are fully available and admissible, but the physical hypothesis or transferability assumption being tested is refuted by the evidence.

9.  **EFC-Signatures-Not-Carried:** A cross-jurisdictional verification failure where operational signatures (specifically Equivalent Full Cycles and standby ratios) derived from one market baseline (ECO STOR Bollingstedt) did not generalize or transfer to assets operating under different market volatility and dispatch rules (AEMO NEM BESS fleet).

*What this class proves:* Empirical rejections prove that the protocol is capable of genuine falsification, demonstrating that it does not merely check data compliance but actively tests and rejects incorrect physical hypotheses against real-world grid performance.

---

# Section 4: Case Studies: Pillswood BESS and esVolta Anole BESS

To demonstrate the P10 protocol in operation, we present two grid-scale battery energy storage system (BESS) audits. These cases contrast an audit bounded by missing telemetry fields (Pillswood) with an audit that utilizes newly available State of Charge (SoC) telemetry but faces semantic ambiguity (Anole).

---

## 4.1 Case Study 1: Pillswood BESS Grid-Dispatch Audit (UK-HARMONY-001)

### 4.1.1 Audit Setup and Anchor
- **Asset Details:** Pillswood BESS (98 MW / 196 MWh nominal, 2-hour duration), registered under Balancing Mechanism Units `E_PILLB-1` and `E_PILLB-2`.
- **Pre-Registration:** Falsification and verification rules were frozen in commit `d6458e5` before acquiring the 11-month unseen window telemetry.
- **Anchor Source:** Elexon BMRS B1610 metered volumes (half-hourly billing telemetry).
- **Physical Boundaries:** The anchor lacks State of Charge (SoC) data, cell-level telemetry, and sub-minute active power records. Net active power (MW) is computed as a 30-minute average: $\text{Average Power (MW)} = \text{Metered Volume (MWh)} \times 2$.

### 4.1.2 Verification Results
1.  **L1 Data Integrity:** Passed. The dataset matches the hash in `data_manifest.json`, with documented gaps (a 24-hour gap on 2026-06-27 and query boundary anomalies).
2.  **L2 Physics Compliance (RTE Gate):** Passed. The combined AC-to-AC Round-Trip Efficiency (RTE) was verified at **86.58%** over the 12-month period, well within expected thermodynamic bounds.
3.  **Active Power Capacity (98 MW Export):** *Verified with Limitations (Bounded).* The maximum observed 30-minute average export power was **97.78 MW** (2026-03-31 Settlement Period 35). Because it did not strictly meet the 98.0 MW threshold, the capability is classified as *Bounded* by observed dispatch.
4.  **Energy Capacity (196 MWh Export):** *Verified with Limitations (Bounded).* The maximum continuous discharge block was **183.67 MWh** over 4.5 hours (2026-03-31 SP 33–41) at partial power (averaging approximately 40.8 MW, compared to the 98 MW peak capacity).
5.  **Level 5 Verdict:** **Verified with Limitations**. Both capacity claims are verified as *Bounded* below the nominal nameplate capacity. The absence of SoC telemetry prevents direct DC-side physical validation.

---

## 4.2 Case Study 2: esVolta Anole BESS Telemetry Audit (US-TX-ANOL-001)

### 4.2.1 Audit Setup and Anchor
- **Asset Details:** esVolta Anole BESS (240 MW / 480 MWh nominal), registered in ERCOT as Resource ID `ANOL_ESS_ESR1`.
- **Anchor Source:** ERCOT SCED 60-Day ESR telemetry disclosure, acquired via `gridstatus.io` (Class B third-party rendering due to ERCOT WAF geo-blocking).
- **Physical Boundaries:** The anchor includes SCED execution telemetry (5-minute average intervals) and DC-side State of Charge (SoC) telemetry, enabling L2 physical consistency checks.

### 4.2.2 Verification Results
1.  **L1 Data Integrity:** Passed. Telemetry was retrieved without gaps via gridstatus.io; timestamps were successfully aligned to UTC and deduplicated.
2.  **L2 Physics Compliance:** Passed. High-level active power and energy integrals satisfy thermodynamic boundary rules, though the State of Charge telemetry fails internal consistency checks (see F3).
3.  **Power Capacity (Claim 001a: 240 MW):** *Demonstrated.* The peak telemetered net output, base point, and High Sustainable Limit (HSL) converged precisely at **240.0 MW**, demonstrating model-saturated physical capability.
4.  **Energy Capacity (Claim 001b: 480 MWh):** *Demonstrated.* The largest continuous discharge block was verified at **513.03 MWh** over 2.167 hours (2026-02-11), exceeding nameplate capacity by 6.9%. Telemetry shows this discharge block started at an SoC of **547.67 MWh** and ended at **11.89 MWh** (a delta SoC of 535.78 MWh), yielding a highly realistic one-way discharge-vs-SoC ratio of **95.8%**.
5.  **SoC Internal Consistency (F3 Rule):** *Inconsistent.* Under the pre-registered 80% pass rule for all discharge events, the asset achieved a **55.2%** consistency rate. An exploratory post-hoc analysis filtering for major discharge cycles (≥10 MWh) yielded an **81.8%** consistency rate, suggesting telemetry skew dominates micro-discharges, but because this filter was not pre-registered, the strict verdict remains *Inconsistent*.
6.  **SoC Field Interpretation (F4 Rule):** **Deferred**. The observed maximum live state of charge was 558.0 MWh (+78.0 MWh above nominal), while the maximum capacity limit parameter in the `max_soc` column reached 560.3 MWh (+80.3 MWh above nominal). Without official ERCOT database column definitions, it is impossible to determine if this represents a physical over-sizing buffer or alternative scaling math.
7.  **Level 5 Verdict:** **Verified with Limitations**. Power and energy capacities are demonstrated, but the final verdict carries limitations due to the inconsistent SoC telemetry and the deferred F4 interpretation.

### 4.2.3 Physical Consistency and Telemetry Deferral
The relationship between the demonstrated active energy capacity of 513.03 MWh (F2) and the State of Charge telemetry (F3/F4) is physically consistent at the event level. The 513.03 MWh AC export on 2026-02-11 was drawn from a telemetered SoC drop of 535.78 MWh (from 547.67 MWh down to 11.89 MWh), representing a realistic one-way discharge-vs-SoC ratio of 95.8%. Both telemetry sets confirm that the physical asset is oversized relative to its 480 MWh nameplate capacity (likely to buffer cell degradation and guarantee its 480 MWh nominal rating over time).

However, their methodological treatment under the P10 protocol differs:
- The active energy capacity is **Demonstrated** because active power (MW) is a standard, globally defined physical trace at the point of interconnection.
- The F4 SoC interpretation is **Deferred** because `max_soc` (reaching 560.3 MWh) is a scheduling database column whose exact mathematical scaling, operational buffer definitions, or DC-to-AC modeling rules are not publicly documented by ERCOT. Presenting a deferred verdict is not a failure of the audit, but a demonstration of the protocol in action: it openly declares the semantic boundaries of public disclosures.

---

# Section 5: Conclusion and Methodological Boundaries

## 5.1 The Battery Passport and Chemistry Boundary
The P10 protocol operates exclusively on public, external grid-boundary signatures—active power dispatch, integrated energy throughput, and reported state of charge. It cannot verify cell-level chemical and thermodynamic states, such as internal cell resistance shifts, electrolyte degradation mechanisms, local thermal management efficiency, or cell-level capacity mismatches. Verifying these electrochemical claims requires privileged manufacturer logs or a standardized "battery passport" disclosing cell-level laboratory testing. The protocol does not attempt to replace these internal diagnostics; instead, it enforces the boundary that electrochemical performance claims remain *Unfalsifiable-as-Stated* from open data alone.

## 5.2 The Generalization Boundary
The case studies in this paper demonstrate the operation of P10's admissibility layer and physical gates across two specific markets (Elexon in GB and ERCOT in the US). While the broader VolMax portfolio includes BESS audits across four distinct jurisdictions (DE, AU, GB, and US), the protocol's generalizability is not unlimited. Other regulatory frameworks (such as CAISO or PJM) remain to be tested, and the admissibility of claims in each new market must be evaluated against its specific local telemetry anchors.


## 5.3 Complete Audit Reproducibility
The authority of the P10 protocol rests not on institutional consensus, but on mathematical reproducibility. In alignment with this principle, all quantitative findings, capacity bounds, and telemetry metrics presented in Section 4 are backed by public, immutable audit packages. Every verification script, data manifest, and SHA-256 telemetry hash is open-source and version-controlled, allowing any independent verifier to reconstruct, verify, or falsify the conclusions of this paper. Ultimately, P10 does not attempt to verify or prove every performance claim. It defines, in advance, which claims can be independently tested from public evidence and which cannot, establishing a transparent boundary between physical grid performance and unverified interpretation.
