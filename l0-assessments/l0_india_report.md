# P10 L0 Transparency Scouting Report: Indian BESS Market & Grid Portals

**Author:** Ivan Nestorov, VolMax Studio Lab  
**Date:** 2026-07-13  
**Scope:** L0 Admissibility Scouting ONLY (National Grid-India/NLDC, Maharashtra MSLDC, Gujarat GSLDC)

---

## 1. License & Accessibility Verdicts

This section reviews the legal accessibility and availability of grid and dispatch telemetry. Under P10, a license and network connectivity check must pass before a market is declared admissible.

### A. Network & Geo-Fencing Analysis
*   **Western Regional Load Despatch Centre (WRLDC):**
    *   *URL:* `https://wrldc.in`
    *   *Status:* **TIMED OUT** / Server Unreachable. Persistent `Connection timed out` errors indicate geo-fencing or highly unstable public infrastructure.
*   **Gujarat State Load Despatch Centre (GSLDC):**
    *   *URLs checked:* `sldc.gujarat.gov.in` (does not resolve), `sldcguj.com` (403 Forbidden), `sldcguj.org.in` (GEO02 Country Block on GoDaddy Firewall).
    *   *Status:* **BLOCKED**. Complete country-level geo-fencing restricts access to regional telemetry.
*   **Maharashtra State Load Despatch Centre (MSLDC):**
    *   *URL:* `https://mahasldc.in`
    *   *Status:* **ACCESSIBLE**. Publicly viewable without geographic restrictions, but limited to static formats.

### B. Legal Terms of Use
*   **MSLDC Data Policy:**
    *   *Source:* `https://mahasldc.in`
    *   *Permitted Commercial Use:* **NO EXPLICIT GRANT**. No Open Government License (OGL) framework or Creative Commons equivalent is declared.
    *   *Verdict:* **INADMISSIBLE** for public redistribution or commercial auditing pipelines due to a lack of clear open-data licenses.

---

## 2. Granularity & Resolution Floor

This section maps the telemetry resolution and access control structures in the Indian grid.

### A. Public vs. Private Data Availability

| Dataset | Source | Granularity | Time Resolution | Access Level | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **System Operations Daily Report** | MSLDC | Regional Aggregate | Daily summary | Public (PDF) | Total generation by fuel type, peak demand, major outages. |
| **MOD Stack Report** | MSLDC | Per-Unit | Monthly (PDF) | Public (PDF) | Merit Order Despatch list with variable cost rankings. |
| **RSD / Zero Schedule** | MSLDC | Per-Unit | Incident-based (PDF) | Public (PDF) | Reserve Shut Down list identifying unit-wise outages. |
| **SCADA DSM Details** | MSLDC | Per-Unit | Daily (PDF) | Public (PDF) | Daily capacity, schedule, actual, deviation, and margins. |
| **SCADA Overview Console** | MSLDC | Station Level | Real-time (JPG) | Public (Dynamic Image) | Visual screenshot console of active power outputs. |
| **Format 1D DSM Schedule vs. Actual** | SLDCs / RLDCs | Per-Unit | 15-minute blocks | **Restricted (Login Gated)** | Raw telemetry and metered data used for Deviation Settlement. |

### B. Access Control & Authorization (The Verification Halt)
Under the Indian Deviation Settlement Mechanism (DSM) regulations (specifically **Clause 5.15 of the DSM Procedures**):
*   Sirovi per-unit telemetry (15-minute time block metered values from SEM/ABT meters and MDAS) **exists** at the necessary resolution for P10 audits.
*   However, these datasets are gated behind the secure **DSM Application Login Portal** and are accessible only to registered State Entities, Power Utilities, and generating resource owners. 
*   No public API or historical CSV archive is made available for third-party auditing.

### C. Resolution Floor Statement
The public resolution floor for per-unit data is restricted to static PDF reports (monthly MOD stack, daily DSM summaries) and visual consoles (JPG screenshots). Programmatic per-unit time-series telemetry (e.g., CSV/Excel) is not publicly accessible. 

---

## 3. Claim Harvesting & Registry

We harvest specific public claims by Indian BESS operators and analysts, using the P10 Claim Registry identifier format.

### A. Gujarat Khavda BESS Event
*   **Claim ID:** `IN-KHAVDA-001` (Grid-Code Compliance Claim)
*   **Asset:** speculative BESS units charging at Khavda, Gujarat.
*   **Verbatim Claim (derived from peer discussions):**
    *   *Shubham Tyagi (SDO / Transmission):* BESS units failed to auto-disconnect during Gujarat grid frequency event (drop to 49.398 Hz) on May 13, 2026.
    *   *Ashish Kumar (VP BD):* ~650 MW of BESS units in charging mode failed to auto-disconnect, requiring manual intervention, citing ~9 GW net frequency oscillation impact.
*   **Regulatory Anchor:** **IEGC 2023 Clause 29(12)**:
    > *"All Energy Storage Systems (ESS) in charging mode shall automatically disconnect prior to the first stage of Under Frequency Relay (UFR) operation..."* (set at 49.6 Hz / 50ms, ahead of the first-stage UFR threshold of 49.4 Hz).
*   **Testability Class:** **UNFALSIFIABLE from public data**. Although the regulatory requirement (IEGC Clause 29(12)) is clear, there is no public per-unit telemetry (such as a 15-minute or sub-second trace) to verify if individual batteries auto-disconnected or remained online. The official Grid-India/NLDC root-cause report is still pending, and the GSLDC portal is geo-blocked.

---

## 4. Claim Risk Assessment

Under P10, "Risk" represents the computational and verification cost of falsifying the claim.

| Claim ID | Company / Source | Claim Type | Risk Class | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **IN-KHAVDA-001** | Ashish Kumar / Tyagi | Grid-Code / Event-Response | **Very High** | Requires either access to private DSM/SCADA accounts or the release of the official NLDC disturbance report. |

---

## 5. Transparency Classes & L0 Admissibility Verdicts

### A. Operator & Portal Transparency Index
*   **MSLDC (Maharashtra):** **T3 (Aggregates & PDFs)**. Publishes per-unit data, but locks it in non-machine-readable formats (PDF, JPG) without an open data license.
*   **GSLDC (Gujarat):** **T0 (Closed System)**. Completely geo-blocked to foreign datacenters.
*   **WRLDC / Grid-India:** **T0-T1 (Closed / Unstable)**. Return timeout errors, making systematic automation impossible.

### B. Market L0 Admissibility Verdict
*   **Verdict:** **HALTED (Unfalsifiable / Access-Restricted)**.
*   **Halt Class:** **Access-Gated (Category: Access Control)**. The primary barrier to auditing is not the non-existence of data, but rather that high-resolution data is restricted to authenticated entities via login walls and geo-blocked portals.

---

## 6. Recommendations & Future Actions

1.  **Keep India in Horizon Phase:** Do not proceed with Indian BESS audits under P10 v1.0.
2.  **Monitor the Draft National Electricity Data Sharing Framework (NEDSF):** A proposed Ministry of Power draft (July 2026) aims to establish a National Electricity Data Portal. Re-evaluate if this portal goes live with public, machine-readable per-unit APIs.
3.  **Use as Failure Case for Paper v2:** Cite this report in the next paper version to document "access control" as a distinct boundary of public grid observability.
