# P10 — The VolMax Verification Method

*An independent verifier's procedure for separating real signal from artifact in
measured-system ML claims. Domain-agnostic — batteries, power signals, grid, PV. This is
the method behind every finding in this portfolio.*

**VolMax Studio Lab** · power electronics + domain-grounded ML · independent verification

---

## The premise

The sensor does not lie. The physics does not lie. Everything between the raw signal and
the reported number is interpretation — and interpretation is where claims fail. The
verifier stands at that gap and checks whether the interpretation survives contact with
data it has never seen.

Independence is the product: we do not build the model under test and we do not sell a
competing one. A team that grades its own model has the same conflict of interest as a
vendor selling it.

---

## The procedure

### Stage 1 — Reduce to first principles
Identify the measured quantity, its units, instrument resolution, and the governing law
(conservation, monotonicity, causality, thermodynamic bound). Reject at this stage any
output that violates the law — a capacity that "un-ages" without rest, a predictor that
consumes future information, a metric below the sensor's noise floor. *Check the floor
before the ceiling.*

### Stage 2 — Hunt the interpretation artifacts
The recurrent mechanisms by which a pipeline manufactures a number the data doesn't
support:
- **Leakage** — train/test contamination. Split by unit (cell/asset), never by sample.
  Fit every learned transform (scaler, normalizer) *inside* the fold, never on the full
  dataset.
- **Inflation** — effect size on many small groups (η², R²) biased upward. Demand the
  unbiased estimator (ω², adjusted R², ICC).
- **Curation** — hard cases quietly dropped to match a benchmark. Demand the full-set number.
- **Concurrence-as-prediction** — a feature that *tracks* the outcome reported as if it
  *forecasts* it early enough to act.

### Stage 3 — Compare to state of the art
Verify "novel / first / beats X" against current reality. A short search refutes most
prior-art and superiority claims.

### Stage 4 — Verdict + correction
State where the claim holds, where it breaks, the corrected number, and the next step.
Every cited number regenerates from a single script. Limitations stated inline, not buried.

**Output is one of three verdicts:**
- **Supported** — survives held-out data and physical law; the number is honest.
- **Artifact** — the effect is leakage, inflation, or curation; corrected number differs.
- **Unfalsifiable-as-stated** — cannot be tested as written; specify what would make it so.

---

## The caveat theorem

The caveat is not a hedge appended to a conclusion — it is the operator that performs the
separation. "Split by unit" catches leakage; "report ω²" catches inflation; "full-set
error" catches curation; "held-out only" catches concurrence-as-prediction. Each is a
caveat in operational form. Remove the caveats to look more confident, and you remove
exactly the operators that catch the errors. A verifier optimized for "no caveats, deliver
fast" is structurally identical to the unverified claim it is meant to test.

---

## Practical checklist (run this on any SOH/RUL or signal model)

```
[ ] Split is by unit (cell/asset), not by sample/cycle
[ ] Every learned transform (scaler, PCA, feature selection) fit inside the CV fold
[ ] No batch/campaign signature standing in for prediction (check group structure)
[ ] Headline metric computed on the FULL test set — no dropped hard cases
[ ] Effect sizes reported with unbiased correction (ω², adjusted R²), not raw η²/R²
[ ] Feature that "tracks" vs "predicts early" distinguished explicitly
[ ] Outputs respect physics: monotonicity, conservation, no impossible recovery
[ ] Model reports calibrated uncertainty, not a bare point estimate
[ ] Every reported number regenerates from one script into a results file
[ ] Limitations stated per finding, leading — not buried in a footnote
```

---

## Worked example — this portfolio, audited against itself

The strongest test of a verifier is whether it catches itself. Applied to our own
Battery_Health_Portfolio (NASA PCoE + Severson/Attia), the method caught:

| Claim as first stated | Stage-2 mechanism | Corrected verdict |
|---|---|---|
| Protocol explains η²=77% of cycle life | inflation (~2 cells/group) | ω²-corrected 66%; rate knobs <5% each |
| Discharge model reproduces paper at ~9% | curation (one fast-failing cell dropped) | full-set 18.3%; cell kept in |
| "OOD" partition shows distribution shift | fabricated (renamed duplicate of test set) | removed; real shift built and labeled |
| R_ct strongly predicts SOH | concurrence-as-prediction | concurrent tracking only, not early-predictive |

Five claims entered; none survived unchanged. Each correction came from a Stage-2
caveat-operator applied to our own work first. That is the method's signature.

---

## What this is and is not

**Is:** a procedure that converts an asserted number into a verified, corrected, or
rejected one — across batteries, power signals, grid, PV.

**Is not:** a guarantee of accuracy. The method makes no "95%" promise — that is the
vendor claim it exists to test. A verifier that guarantees a flattering result has
reacquired the conflict of interest it was built to remove.

*Physics doesn't lie. Sensors don't lie. The method stands at the gap and checks the rest.*
