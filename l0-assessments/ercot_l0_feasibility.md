# ERCOT ESR — L0 Admissibility Feasibility Assessment
**Status:** Pre-registration research — no data downloaded.
**Author:** Ivan Nestorov, VolMax Studio Lab
**Date assessed:** 2026-07-08
**Criterion 4 (License):** ✅ Cleared — verbatim citation below.
**Data Access Path:** Free account registration at apiexplorer.ercot.com required for API; bulk ZIP download from MIS portal (np3-965-er) does not require login.

> [!IMPORTANT]
> Before any download: open https://www.ercot.com/legal/terms in a browser, copy
> the full text verbatim into the audit manifest with the access timestamp.
> archive.org does not have a confirmed snapshot of this page — live pin only.

---

## L0 Criterion 4: License — Verbatim Citation

**Source:** ERCOT Website Terms of Use, https://www.ercot.com/legal/terms
**Accessed:** 2026-07-08 (direct URL 403; text recovered via indexed cache of ercot.com)
**Action required before download:** Verify live text at https://www.ercot.com/legal/terms
and record the exact page version/date in the audit manifest.

### Relevant clauses (verbatim from ERCOT Terms of Use):

> "Publicly available contents of the ERCOT website may be used, reproduced, and
> redistributed, provided that the contents are not modified and that you maintain
> all copyright and other notices contained in the original content."

> "Notwithstanding the foregoing, raw data provided in public portions of this
> website may be used, reproduced, and redistributed in compilations, charts, and
> analyses without maintaining such notices. ERCOT does not guarantee the accuracy
> of any such compilations, charts, or analyses."

### License ruling for this audit:

The 60-Day SCED Disclosure ZIP/CSV files are **raw data provided in a public
portion of the website** (no login required, no click-agreement for the bulk
download files). The raw data exception clause explicitly permits:
- Use, reproduction, and redistribution
- In compilations, charts, and analyses
- **Without** the requirement to maintain copyright notices

**Redistribution decision:** Raw SCED CSV files **may be committed to the public
audit repo** — same practice as GB (Elexon) and AU (AEMO). SHA-256 hash is pinned
on arrival as immutability proof regardless.

**Not covered:** ERCOT API access (separate terms, requires registration). This
audit uses direct ZIP download from public website — no API, no registration.

**Caveat:** Terms of Use may be updated. The manifest records the ToU URL and
access date. If live text at time of download differs materially from the above,
the ruling is re-evaluated before any data enters the repo.

---

## L0 Criterion 1: Subject & Claim

**Selection rule (a priori, not by media prominence):**
Largest registered ESR by nameplate MW that:
1. Has been operational through the full post-RTC+B window (from 2025-12-05 onward)
2. Has a publicly pinned nameplate (MW + MWh) in an operator press release or
   official registration document — not inferred from SCED data
3. Appears by resource name in ERCOT SCED 60-day ESR CSV files

This rule selects by registry, not by headline. Asset identity determined after
applying the rule — not before.

**Decomposed claims (template — asset name and numbers filled after scouting):**

- **US-TX-ESR-001a:** "[Asset operator] states that [Asset name] has a nameplate
  AC power capacity of X MW."
  *Source: [operator press release URL, date, archive snapshot]*

- **US-TX-ESR-001b:** "[Asset operator] states that [Asset name] has a nameplate
  energy capacity of Y MWh ([Z]h duration at rated power)."
  *Source: [same or separate operator press release URL, date, archive snapshot]*

---

## L0 Criterion 2: Ground Truth Anchor

**Primary anchor:** ERCOT 60-Day SCED Disclosure — ESR Data in SCED
- Product ID: NP3-965-ER
- Format: ZIP containing CSV files, one per operating day
- Granularity: 5-minute intervals, per-resource
- Fields relevant to this audit:
  - `RESOURCE_NAME` — identifies the asset
  - `TELEMETERED_NET_OUTPUT` — measured AC power (MW), 5-min average
  - `BASE_POINT` — SCED dispatch instruction (MW)
  - `SOC` or equivalent field — operator-reported state of charge (post RTC+B)
- Access: Public, no registration, direct ZIP download from ercot.com
- Lag: 60-day rolling delay

**Anchor quality: Class A** — ERCOT is the market operator; SCED dispatch records
are settlement-grade by definition (used for real-time market clearing).

**SoC column caveat (Criterion 4 of audit, not L0 Criterion 4):**
The SoC field is **operator-reported state estimation from the BMS**, not an
independent physical measurement. It is the operator's own telemetry submitted
to ERCOT for RTC+B dispatch optimization. The SoC-based finding therefore
verifies **internal consistency of the operator's own SoC accounting**: whether
the reported SoC delta and the metered MWh throughput are self-consistent under
the declared nameplate energy. This is a novel finding class relative to prior
audits (which had no SoC signal at all) — but the caveat goes into the ledger
from day one and into the report's Limitations section, not discovered in L3.

**Correction notice protocol:**
ERCOT issued correction notice M-B020626-01 for ESR SoC columns in early 2026.
Before finalizing any analysis window, check ercot.com for correction ZIP packages
covering the target dates. Both the original and correction ZIPs are downloaded
and hashed; the correction ZIP supersedes for analysis, both hashes enter the
manifest.

---

## L0 Criterion 3: Falsification Criterion

Rules written from DESIGN_PRINCIPLES.md §4 ("Evidence is evaluated only within
observable measurement boundaries") and the Demonstrated/Bounded/Not Exercised
verdict grammar. Capability claims are not refuted by absence of exercise.

**001a — Power Capacity (X MW):**
- *Demonstrated:* Max observed `TELEMETERED_NET_OUTPUT` ≥ X MW at any 5-min
  interval across the audit window.
- *Bounded:* Max observed output < X MW but no dispatch instruction (BASE_POINT)
  ≥ X MW was ever issued. The asset was never called to nameplate — claim is
  bounded, not refuted.
- *Not Exercised:* Nameplate-level dispatch never requested in the window.
- *Physics/Registration Anomaly (separate finding class):* If
  `TELEMETERED_NET_OUTPUT` > X MW at any interval — this is a separate L2 finding,
  not a refutation of the power claim.
- *Not Verified:* If `TELEMETERED_NET_OUTPUT` falls materially short of BASE_POINT
  at dispatch instructions that reached or approached X MW — the asset failed to
  follow instructions at rated capacity.

**001b — Energy Capacity (Y MWh):**
- *Demonstrated:* A continuous discharge block ≥ Y MWh is observed (integrated
  from TELEMETERED_NET_OUTPUT across a contiguous dispatch window).
- *Bounded:* Largest observed discharge block < Y MWh, and no single dispatch
  event requested a full Y MWh depletion. SoC-enhanced bound: if reported SoC
  at discharge start × nameplate Y ≥ observed block, the shortfall is consistent
  with partial state-of-charge dispatch, not capacity limitation.
- *Not Exercised:* No dispatch event approached full duration discharge.
- *SoC consistency check (new finding class, internal only):*
  For each discharge event: verify that (SoC_start − SoC_end) × Y MWh ≈
  integrated TELEMETERED_NET_OUTPUT (within round-trip efficiency bounds).
  Systematic divergence = operator's SoC accounting is internally inconsistent.
  This finding is labeled: "SoC telemetry self-consistency: [Consistent /
  Inconsistent within X% at 5-min resolution]" — never confused with nameplate
  energy falsification.

---

## L0 Criterion 5: Physical Constraints

- AC power output bounded by nameplate MW (L2 physics check)
- AC-AC RTE bounded by thermodynamic limits (0.60 < η ≤ 1.0, same as GB audits)
- SoC bounded [0%, 100%] — values outside this range are a telemetry anomaly finding
- Energy conservation: integrated charge ≥ integrated discharge × (1/η_min)

---

## L0 Verdict

| Criterion | Status | Note |
|-----------|--------|------|
| 1. Subject & Claim | ⏳ | Asset and numbers pending scouting |
| 2. Ground Truth Anchor | ✅ | ERCOT SCED NP3-965-ER, Class A |
| 3. Falsification Criterion | ✅ | Rules written per DESIGN_PRINCIPLES.md §4 |
| 4. Reproducible Inputs | ✅ | Bulk ZIP download (MIS portal, no login); API requires free registration |
| 4b. License | ✅ | Raw data exception permits redistribution — verbatim citation above |
| 4c. ToU live pin | ⏳ | Must be done manually in browser before first download; archive.org has no snapshot |
| 5. Physical Constraints | ✅ | Standard energy conservation + SoC bounds |

**Overall: PROCEED TO ASSET SCOUTING** — Criterion 1 pending asset name and numbers.

---

## Next Action

1. Query ERCOT ESR registry (or ERCOT MIS public list) for largest MW ESR
   operational post 2025-12-05 with public nameplate objava.
2. Pin nameplate + COD from operator press release (URL + archive).
3. Confirm resource name appears in SCED ESR CSV sample.
4. Write audit_prep.md with filled-in 001a/001b claims.
5. Commit audit_prep.md (pre-registration freeze).
6. Download SCED ZIP for target window. Hash on arrival.

---

## Outcome Note (2026-07-09)

**Implementation vs. Pre-registration Deviation Report:**
1. **Data Access & Anchor Quality:** The planned direct download of primary ERCOT `NP3-965-ER` ZIPs from the MIS portal was blocked by ERCOT's Web Application Firewall (WAF) returning `HTTP 403` for non-US residential traffic. A probe run on a public US-region GitHub Actions runner (run ID 29116383279) was also blocked, indicating ERCOT blocks datacenter IP ranges. 
2. **Anchor Downgrade:** The audit anchor was downgraded to **Class B (Third-Party Rendering)**. Telemetry was retrieved via `gridstatus.io` REST API.
3. **Redistribution Decision:** Because the data source shifted from public ERCOT ZIPs to `gridstatus.io` API, the `gridstatus.io` Terms of Use (prohibiting substantial redistribution of exports) became the governing license. Consequently, raw CSV data was **not** committed to the repository. Integrity is preserved via SHA-256 hashes inside `data_manifest.json`.
4. **ToU Live Pin:** The live pin of `https://www.ercot.com/legal/terms` was not executable from the Serbian residential location due to geo-blocking, and datacenter-based automated retrievals were blocked by the WAF. The citation remains pinned to the public indexed cache, supplemented by a GHA probe step.

