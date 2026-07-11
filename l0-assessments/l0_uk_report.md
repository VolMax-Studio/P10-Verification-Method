# P10 L0 Transparency Scouting Report: UK BESS Market (Elexon/BMRS)

**Author:** Ivan Nestorov, VolMax Studio Lab  
**ORCID:** 0009-0006-7940-9539  
**Date:** 2026-07-07  
**Scope:** L0 Admissibility Scouting ONLY (Elexon/BMRS BESS and Elia Belgium Side-Scan)  

---

## 1. License Verdicts

This section reviews the legal terms of use for data sourcing. Under P10, a license check must pass and be pinned before downloading any bulk data.

### A. Elexon BMRS / Insights Solution Data
*   **Source URL:** [Elexon BMRS Copyright Licence](https://www.elexon.co.uk/bsc/data/balancing-mechanism-reporting-agent/copyright-licence-bmrs-data/)
*   **Archive Snapshot:** [web.archive.org/web/20260220122501/https://www.elexon.co.uk/bsc/data/balancing-mechanism-reporting-agent/copyright-licence-bmrs-data/](https://web.archive.org/web/20260220122501/https://www.elexon.co.uk/bsc/data/balancing-mechanism-reporting-agent/copyright-licence-bmrs-data/)
*   **Access Date:** 2026-07-07
*   **Permitted Commercial Use:** **YES**
*   **Exact Permission Quote:**
    > *"Elexon Limited hereby grants You a worldwide, royalty-free, perpetual, non-exclusive licence to Use the BMRS Data subject to the conditions below. ... You are free to: copy, publish, distribute and transmit the BMRS Data; adapt the BMRS Data; exploit the BMRS Data commercially and non-commercially..."*
*   **Attribution Requirement:**
    > *"Contains BMRS data © Elexon Limited copyright and database right [year]. Where possible You must also contain a link to this licence."*
*   **Verdict:** **ADMISSIBLE**.

### B. NESO (National Energy System Operator) Data Portal
*   **Source URL:** [National Grid ESO Open Data Licence v1.0](https://data.nationalgrideso.com/licence)
*   **Archive Snapshot:** [web.archive.org/web/20230601123607/https://data.nationalgrideso.com/licence](https://web.archive.org/web/20230601123607/https://data.nationalgrideso.com/licence)
*   **Access Date:** 2026-07-07
*   **Permitted Commercial Use:** **YES**
*   **Relationship to OGL:** Based on version 3.0 of the Open Government Licence (OGL), with specific amendments for NGESO.
*   **Exact Permission Quote:**
    > *"You are free to: copy, publish, distribute and transmit the Information; adapt the Information; exploit the Information commercially and non-commercially..."*
*   **Attribution Requirement:**
    > *"Supported by National Grid ESO Open Data"*
*   **Verdict:** **ADMISSIBLE**.

---

## 2. Granularity & Resolution Floor

This section maps BMRS and NESO BESS datasets, defining the boundaries of what is mathematically testable.

### A. Dataset Granularity Matrix

| Dataset | Source | Granularity | Time Resolution | License | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **B1610** | Elexon | Per BM Unit | 30 minutes (Settlement Period) | Elexon BMRS Copyright Licence | Metered volume (MWh) flowing to/from the grid. Positive is discharge, negative is charge. |
| **FPN** | Elexon | Per BM Unit | 1 minute / spot profile | Elexon BMRS Copyright Licence | Final Physical Notifications (planned active power generation/demand). |
| **BOALF** | Elexon | Per BM Unit | Spot instruction timestamps | Elexon BMRS Copyright Licence | Bid-Offer Acceptance Level Flags (real-time dispatch instructions). |
| **MELS/MILS**| Elexon | Per BM Unit | 30 minutes | Elexon BMRS Copyright Licence | Maximum Export/Import Limits declared by the unit. |
| **EAC/Ancillary**| NESO | Auction level / aggregated | Hourly/daily blocks | NESO Open Data Licence v1.0 | Procurement clearing prices and total contracted capacity. |
| **Frequency Tel**| NESO | Per BM Unit | Proprietary / Not published | None | 1-second frequency response delivery. |

### B. BM Unit Naming Conventions & Data Layout
*   **Naming Convention:** Batteries appear under distinct Balancing Mechanism (BM) Unit IDs:
    *   `T_` prefix: Transmission-connected BESS (e.g., `T_BLWNB-1` - Thornton Battery).
    *   `E_` prefix: Embedded distribution-connected BESS (e.g., `E_OVRHB-1` - Overhill BESS).
    *   `2__` prefix: Virtual / supplier BESS (e.g., `2__FBPGM001` - Wormald Green BESS).
*   **Bidirectional Flow Representation:** In the B1610 dataset, bidirectional flow is mapped onto a single BM Unit. The sign convention is algebraic: positive (+) values denote export (discharging) and negative (-) values denote import (charging).
*   **Sample Data Schema (B1610):**
    ```json
    {
      "dataset": "B1610",
      "psrType": "Generation",
      "bmUnit": "2__FBPGM001",
      "nationalGridBmUnitId": "FBPG01",
      "settlementDate": "2026-06-01",
      "settlementPeriod": 3,
      "halfHourEndTime": "2026-06-01T00:30:00",
      "quantity": 0.014
    }
    ```
    *   *Sample Data File SHA-256 Hash:* `6fc637c9ad3afb7880dacd414265b2eeac22ac36d3573946250b3a9d805e5f3f` (Location: `data/raw_b1610_202606.json`, 171,002 records in our established reproduction pipeline).

### C. Resolution Floor Statement
The public resolution floor for metered energy volume is **30 minutes** (B1610), while dispatch instructions (BOALF) and physical notifications (FPN) are available at **minute-level**. 
No sub-second or 1-second telemetry of BESS response is published in open datasets. Consequently, claims regarding real-time Dynamic Containment (DC) delivery or sub-second frequency containment compliance are **Unfalsifiable-as-Stated** from open-source data alone.

---

## 3. Claim Harvesting & Registry

We harvest specific public claims by UK BESS operators, using the updated P10 Claim Registry identifier format.

### A. Harmony Energy (Pillswood BESS)
*   **Claim ID:** `UK-HARMONY-001` (Capacity & Software Claim)
*   **Verbatim Claim:**
    > *"98 / 196 (Lithium-ion)"* ... *"Tesla two-hour Megapack"* ... *"Tesla – Autobidder"*
*   **Live URL:** [Harmony Energy Case Study: Pillswood BESS](https://harmonyenergy.co.uk/case-studies/pillswood-bess/)
*   **Archive Snapshot:** [web.archive.org/web/20260707134620/https://harmonyenergy.co.uk/case-studies/pillswood-bess/](https://web.archive.org/web/20260707134620/https://harmonyenergy.co.uk/case-studies/pillswood-bess/)
*   **Access Date:** 2026-07-07
*   **Testability Class:** **TESTABLE**. The 98 MW export capacity and 196 MWh energy capacity are auditable via B1610 metered volumes.
*   **Business Impact Class:** **A** (highly relevant for lenders/insurers tracking Autobidder dispatch performance).

### B. Zenobē (Blackhillock BESS)
*   **Claim ID:** `UK-ZENOBE-001` (Stability Services Claim)
*   **Verbatim Claim:**
    > *"the first in the world to deliver Stability Services using a transmission-connected battery"* ... *"When fully built, Blackhillock will be a 300MW / 600MWh project."* ... *"Kraken and EDF to navigate the complexities and opportunities of service stacking"*
*   **Live URL:** [Zenobē News: Breaks Ground on 300MW Battery in Blackhillock](https://www.zenobe.com/news-and-events/zenobe-breaks-ground-on-pioneering-300mw-battery-in-blackhillock/)
*   **Archive Snapshot:** [web.archive.org/web/20260707140555/https://www.zenobe.com/news-and-events/zenobe-breaks-ground-on-pioneering-300mw-battery-in-blackhillock/](https://web.archive.org/web/20260707140555/https://www.zenobe.com/news-and-events/zenobe-breaks-ground-on-pioneering-300mw-battery-in-blackhillock/)
*   **Access Date:** 2026-07-07
*   **Testability Class:** **UNFALSIFIABLE from public data**. Verifying synthetic inertia or short-circuit level delivery requires sub-second nodal telemetry (e.g. voltage and frequency waveforms) which are withheld as proprietary by NESO. (Standard active power capacity is testable, but the core stability claim is unfalsifiable).
*   **Business Impact Class:** **A** (stability services represent high strategic grid value, but cannot be audited from open data).

### C. BW ESS (Bramley BESS)
*   **Claim ID:** `UK-BWESS-001` (Capacity & Hardware Claim)
*   **BM Unit ID:** None locatable (`E_BRLE-1` was the speculative identifier; not found in Elexon registry)
*   **Verbatim Claim:**
    > *"100MW / 331MWh"* ... *"deploy Sungrow’s PowerTitan 2.0 liquid cooled BESS – a system that combines a 2.5MW Power Conversion System using integrated string inverters and a 5MWh battery into a single container."*
*   **Live URL:** [BW ESS News: secures financing for Bramley](https://bw-ess.com/news/bw-ess-secures-financing-for-its-operational-331mwh-bramley-bess)
*   **Archive Snapshot:** [web.archive.org/web/20260115042230/https://bw-ess.com/news/bw-ess-secures-financing-for-its-operational-331mwh-bramley-bess](https://web.archive.org/web/20260115042230/https://bw-ess.com/news/bw-ess-secures-financing-for-its-operational-331mwh-bramley-bess)
*   **Access Date:** 2026-07-07
*   **Testability Class:** **UNFALSIFIABLE from public data**. The asset is real and has been commercially operational since February 2025 under a tolling agreement with Shell; the capacity claims are likely correct. However, no standalone BM Unit registration was locatable in Elexon's registry under any derived identifier (`E_BRLE-1`, `BRLE40`, `E_BRLE40`, `T_BRLE40`, `2__BRLE40`, `2__EBRLE40`), nor within the registered portfolio of the offtakers (Shell Energy Europe Limited / Shell Energy UK Limited). Aggregation under a virtual/supplier BM Unit is the most likely explanation but is not independently confirmed; what is established is that per-unit telemetry is not publicly locatable, rendering individual unit behavior unobservable.

*   **Business Impact Class:** **A** (verifies performance of Sungrow's PowerTitan 2.0 liquid-cooled system).

*   **Claim ID:** `UK-BWESS-002` (Tolling Agreement Claim)
*   **Verbatim Claim:**
    > *"seven-year tolling agreement with Shell Energy Europe Limited (Shell)"* ... *"fixed-price tolling agreement provides revenue certainty for BW ESS and Penso Power while Shell will trade the Bramley BESS into a range of ancillary services and wholesale markets."*
*   **Live URL:** [BW Group Newsroom: Tolling Agreement with Shell](https://bw-group.com/newsroom/articles/2024/08/bw-ess-penso-power-sign-long-term-uk-battery-energy-storage-tolling-agreement-with-shell/)
*   **Archive Snapshot:** [web.archive.org/web/20260707143132/https://bw-group.com/newsroom/articles/2024/08/bw-ess-penso-power-sign-long-term-uk-battery-energy-storage-tolling-agreement-with-shell/](https://web.archive.org/web/20260707143132/https://bw-group.com/newsroom/articles/2024/08/bw-ess-penso-power-sign-long-term-uk-battery-energy-storage-tolling-agreement-with-shell/)
*   **Access Date:** 2026-07-07
*   **Testability Class:** **UNFALSIFIABLE from public data**. Commercial pricing and revenue terms of the tolling agreement are proprietary.
*   **Business Impact Class:** **B** (highly interesting business model, but cannot be audited).


---

## 4. Claim Risk Assessment

Under P10, "Risk" represents the **computational and verification cost of falsifying the claim**.
*   **Low Risk:** Claim is validated directly from a single public database (e.g. active power dispatch conformance).
*   **Medium Risk:** Claim requires matching 2-3 public datasets or proxy indicators (e.g. capacity duration, RTE analysis).
*   **High Risk:** Claim requires high-resolution/nodal telemetry that is proprietary or withheld (e.g. synthetic inertia).
*   **Very High Risk:** Claim requires commercial or contractual records (e.g. software bidding optimization, tolling margins).

| Claim ID | Company | Claim Type | Risk Class | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **UK-HARMONY-001** | Harmony Energy | Active Power Capacity / Dispatch | **Medium** | Capacity and duration verified by analyzing B1610 metered volumes over a 30-day window. |
| **UK-BWESS-001** | BW ESS | Active Power Capacity | **Verification Risk: High** | No standalone BM Unit registration found (checked `E_BRLE-1`, `BRLE40`, `E_BRLE40`, `T_BRLE40`, `2__BRLE40`, `2__EBRLE40`), making per-unit telemetry unobservable in public data. |
| **UK-ZENOBE-001** | Zenobē | Synthetic Inertia Stability | **High** | Falsification is impossible without sub-second nodal electrical parameters withheld by NESO. |
| **UK-BWESS-002** | BW ESS | Commercial Tolling Terms | **Very High** | Requires private contract details; CAISO/Elexon registries contain no commercial tolling logs. |

---

## 5. Transparency Classes & L0 Admissibility Verdicts

### A. Operator Transparency Index
We define the **Transparency Class (T0–T5)** of data sources strictly by objective, publicly verifiable data-openness criteria (not a subjective reputational rating):
*   **T5 (Raw Telemetry Portal):** Publicly publishes raw per-unit telemetry, API access, clear open licenses, and a complete historical database.
*   **T4 (Dashboard & Statistics):** Publicly publishes detailed interactive dashboards, per-asset specs, and historical statistics.
*   **T3 (Aggregates & Whitepapers):** Publicly publishes aggregated regional reports and detailed technical whitepapers.
*   **T2 (Marketing & PR):** Publicly publishes marketing claims and PR announcements with minimal PDF datasheets.
*   **T1 (PR Only):** Basic PR/press announcements only.
*   **T0 (Closed System):** Completely closed, no public disclosures.

| Operator / Source | Transparency Class | Rationale |
| :--- | :--- | :--- |
| **Elexon Insights Solution** | **T5** | Open raw API, granular B1610/BOALF per-unit data, clear public copyright license. |
| **NESO Data Portal** | **T5** | Open API, system frequency and clearing data, open government-style license. |
| **Harmony Energy** | **T2** | Marketing case studies and PR announcements only, without live telemetry portals or detailed per-unit datasheets. |
| **BW ESS** | **T2** | Press releases and PR announcements only, without live telemetry portals or detailed per-unit datasheets. |
| **Zenobē** | **T3** | Detailed stability technical specs, but grid telemetry is withheld as proprietary. |

### B. Operator L0 Admissibility Verdicts
*   **Harmony Energy:** **ADMISSIBLE** (T2 operator, claims are Low-to-Medium risk, L0 PASS).
*   **BW ESS:** **HALTED (Unfalsifiable-as-Stated)** (T2 operator, no standalone BM Unit telemetry found under checked identifiers, claims are unfalsifiable from public data).
*   **Zenobē:** **HOLD** (T3 operator, stability claims are High risk and FAIL on L0; standard active power dispatch is admissible, but core stability claims are halted).

### C. Reclassification & Correction Note (July 11, 2026)
*   **Correction:** The initial L0 scouting report (dated July 7, 2026) incorrectly classified BW ESS as **ADMISSIBLE** based on the speculative assumption that a standalone BM Unit (`E_BRLE-1`) existed matching its T4 transparency profile. A direct API query of the Elexon Insights Solution (B1610 stream and `/reference/bmunits/all` registry) confirmed that no records or registrations exist under `E_BRLE-1` or any related identifiers. The earlier verdict is corrected here to **HALTED (Unfalsifiable-as-Stated)**. The asset itself is active and real, but its individual telemetry is not publicly locatable.


---

## 6. Recommendations for First UK Audits

1.  **Harmony Energy (Pillswood BESS):**
    *   *Target Claim:* `UK-HARMONY-001` (98 MW / 196 MWh capacity claim) over a 30-day window (June 2026).
    *   *Ready Pipeline:* The Elexon metered data pipeline and raw telemetry for June 2026 are already fully operational in our local `volmax-gb-bess-audit` repository! The Pillswood audit starts with the pipeline ready.
2.  **BW ESS (Bramley BESS):**
    *   *Target Claim:* `UK-BWESS-001` (100 MW / 331 MWh capacity).
    *   *Status:* **HALTED** at Level 0 due to the inability to locate individual per-unit telemetry in BMRS.


---

## 7. Belgium Side-Scan (Elia Open Data Portal)

*   **License Type:** Creative Commons Attribution 4.0 International (CC BY 4.0).
*   **Data Availability:** The Elia Open Data Portal does not publish per-asset or per-BMU real-time or historical dispatch telemetry for BESS. Public data is restricted to system-level aggregates (e.g., total balancing volume, system imbalance prices, fuel-type generation summaries).
*   **L0 Verdict:** **NOT ADMISSIBLE** for per-unit audits. All individual operator claims remain **Unfalsifiable-as-Stated** under open data due to the complete lack of a per-unit grid telemetry anchor.
