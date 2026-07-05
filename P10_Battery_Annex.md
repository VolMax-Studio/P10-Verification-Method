# P10 — Battery Verification Annex (BESS-Specific Protocol)
### Operational Domain-Specific Extensions to P10 v1.0

This annex defines the necessary physical, statistical, and data-integrity operations required to audit claims involving Battery Energy Storage Systems (BESS) and Battery Machine Learning models. 

Every test defined here inherits the discipline of the core **P10 v1.0 Protocol**: it is adversarial, reproducible, and explains a decision.

---

## Part 1: Grid-Dispatch Audits (Grid-Side Telemetry)
*Applicable to datasets lacking cell-level telemetry (e.g., GB Elexon B1610, AEMO dispatch).*

### G1.1 Sign Conventions and Telemetry Seams
*   **Rule**: Active power telemetry must maintain a consistent sign convention:
    *   **Discharging (Export to Grid)**: Positive ($>0$)
    *   **Charging (Import from Grid)**: Negative ($<0$)
*   **Check**: Verify that the dataset contains both positive and negative values. If a dataset claims to capture battery operations but contains only positive values, the audit must check if charging is omitted or folded into an aggregate. If charging is omitted, the audit is halted at L1 (Incomplete Telemetry).

### G1.2 Commercial Operation Date (COD) Screening
*   **Rule**: Units whose Commercial Operation Date (COD) falls within the audit window, or which exhibit zero active generation capacity during the audit window, must be excluded from the main accepted fleet baseline.
*   **Reason**: Inclusion of commissioning units introduces severe statistical bias (unrepresentative standby states, test cycles, and high outage rates). Commissioning data must be relegated to a separate appendix, and main statistics must reflect only the stable, operational fleet.

### G1.3 Grid-Side Round-Trip Efficiency (RTE) Bounds
*   **Rule**: The AC-to-AC round-trip efficiency ($\eta_{\text{RTE, AC}}$) measured at the grid connection point (boundary of B1610 or dispatch telemetry) must respect thermodynamic limits.
*   **Check**: Compute the ratio of total discharged energy to total charged energy over a closed operational window (e.g., 30-day aggregate):
    $$\eta_{\text{RTE, AC}} = \frac{\sum E_{\text{discharge}}}{\sum E_{\text{charge}}}$$
*   **Boundaries**: 
    *   If $\eta_{\text{RTE, AC}} > 0.92$, the audit flags a **FAIL** at L2 (under-reported charging energy or auxiliary loads excluded from the metered boundary).
    *   If $\eta_{\text{RTE, AC}} < 0.60$, the audit flags a **FAIL** at L2 (excessive auxiliary load leakage, transformer losses, or cell degradation) unless auxiliary loads (HVAC, cooling) are explicitly isolated and explained.
    *   The acceptable physical band for utility-scale lithium-ion BESS is defined as $[0.60, 0.92]$.

---

## Part 2: Cell-Level & SCADA Audits (Deep Telemetry)
*Applicable to datasets containing cell-level or sub-station telemetry (e.g., ERCOT SCED ESR, internal SCADA).*

### C2.1 Long-Term Capacity Degradation Trend
*   **Rule**: Except for minor sensor noise, cell relaxation recovery, or temperature/calibration shifts, the actual capacity ($C_{\text{actual}}$) of a battery system must not exhibit a long-term increasing trend.
*   **Check**: Rather than enforcing strict step-by-step monotonicity ($C_t \leq C_{t-1}$), fit a linear or monotonic regression over monthly or quarterly intervals. The slope of the capacity trend must be non-positive:
    $$\frac{dC_{\text{actual}}}{dt} \le \epsilon_{\text{noise}}$$
    Any statistically significant positive capacity slope exceeding the measurement noise threshold $\epsilon_{\text{noise}}$ (typically $>1.5\%$ of nominal capacity) without a cell replacement or chemistry change flags a **FAIL** at L2.

### C2.2 State of Charge (SoC) Continuity
*   **Rule**: The State of Charge ($SoC$) must satisfy the conservation of energy:
    $$SoC_{t} = SoC_{t-1} + \frac{\eta_{\text{charge}} \cdot P_{\text{charge}, t} \cdot \Delta t - P_{\text{discharge}, t} \cdot \Delta t / \eta_{\text{discharge}}}{C_{\text{nominal}}}$$
*   **Check**: If telemetry reports both SoC and active power, the final SoC of period $t$ must align with the initial SoC of period $t+1$. Discrepancies exceeding sensor noise limits ($>3\%$) trigger an L2 warning.

### C2.3 Conformal Prediction for State of Health (SOH)
*   **Rule**: Point predictions of SOH are rejected for Level 5 verification under Out-of-Distribution (OOD) operations. SOH models must feature calibrated uncertainty bounds.
*   **Check**: Implement **Split Conformal Prediction** to map prediction intervals with a guaranteed coverage probability ($1 - \alpha$):
    $$I(x_{\text{test}}) = [\hat{\mu}(x_{\text{test}}) - q_{1-\alpha}, \hat{\mu}(x_{\text{test}}) + q_{1-\alpha}]$$
    If the prediction intervals bloat excessively under OOD inputs, the model is classified as **Verified with Limitations**, and the operational boundaries are explicitly defined.

### C2.4 Internal Resistance Concurrence-vs-Prediction
*   **Rule**: Claims of early prediction based on internal resistance ($R_{\text{int}}$ or $R_{\text{ct}}$) must be tested for concurrence-as-prediction.
*   **Check**: Verify that the correlation is forecasting future failure rather than merely tracking current operational temperature and load variations. If $R_{\text{int}}$ tracks temperature concurrently, it is a tracking metric, not an early predictor.

---

## Part 3: Reproducibility & Data Pinning

### R3.1 Metadata and Hash Pinning
*   **Rule**: BESS audits must pin the exact data manifest containing SHA-256 hashes of all raw telemetry files, including the active power registry, SoC curves, and auxiliary load records.
*   **Elexon Specific Rule**: Because Elexon BMRS metered volumes are subject to subsequent settlement runs (II, SF, R1, R2, R3, RF, DF) over a multi-year timeline, live API endpoints do not guarantee static data. Audits must freeze raw API pulls into static local archives, calculate their SHA-256 hashes, and use these frozen files as the sole inputs for the verification pipeline (`reproduce.py`).
