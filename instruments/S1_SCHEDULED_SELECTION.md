# S₁ — Scheduled Selection

> **Document Status:** Draft — SPREMNO ZA GEJT (not frozen, not ratified)
> **Version:** v0.1.0
> **Author:** Nestorov, Ivan / VolMax Studio Lab / ORCID 0009-0006-7940-9539
> **Role:** Selection rule **S** for scheduled operation, under
> `INSTRUMENT_SPEC — Measurement Domain and Visibility Boundaries` (v0.3.0).
> **Scope:** This document defines one selection mode. Triggered selection is a
> **separate document** (`S2`) defining a **different population**, and results produced
> under S₁ and S₂ are never pooled or compared as one distribution.

---

## 1. What S determines

S does not decide what is measured (**M**) or how a result is labelled (**C**). It decides
**which windows are measured at all**, and therefore **which population every statement
about this instrument refers to**.

Under S₁ the population is: *all windows in the operating period, without exception.*

---

## 2. Selection rule

1. **Cadence.** One run per calendar month, covering the immediately preceding complete
   calendar month as W. No partial months.
2. **No manual window choice.** The window is a function of the calendar and nothing
   else. A window is never chosen, skipped, re-run for a different period, or deferred
   because its result is uninteresting or inconvenient.
3. **Publication lag.** The run executes no earlier than L days after the end of W, where
   L is frozen in `PARAMS.md`. **L is measured, not assumed** — it is derived from the
   observed availability of the designated series for the relevant markets, conforming to the same completeness floor and gap limits as M₁ §4, and the measurement is recorded at freeze time.
4. **Every window is published**, including windows classified NULL. A NULL month is a
   measurement, not a non-event; the record of NULLs is what makes any non-NULL label
   interpretable at all.
5. **Abort is not skip.** A window that aborts under the completeness floor or gap rule
   (M₁ §4) is published as *not measured*, with its completeness account. It is never
   silently omitted, and it is never retried with relaxed parameters.

---

## 3. Baseline: rolling, disjoint

B is a **rolling window ending immediately before W**, of length N calendar months, with N
frozen in `PARAMS.md`.

**3.1 Disjointness.** B ∩ W = ∅, inherited from M₁ §2.1 without modification. The rolling
rule shifts B by exactly one month per run, so disjointness holds by construction rather
than by check — but the check is still executed each run.

**3.2 Why rolling.** M₁ measures a market against **its own recent régime**, not against
an absolute level. A baseline frozen years earlier measures a relationship to a different
epoch, so the quantity drifts in meaning while keeping its name. Rolling preserves the
meaning of M₁ across time.

**3.3 What comparability means here.** Under a rolling baseline, **R differs between
runs.** Two months' M₁ values are not two readings of one instrument setting; they are
two readings of the same *rule*. Comparability is therefore a property of the procedure,
not of the threshold:

> Procedure-level comparability, not reference-level identity.
> Not the same R. The same function producing R.

Every run publishes the R it used, per market, together with the B window that produced
it. An M₁ value quoted without its R and B is not quotable.

**3.4 Seasonal composition.** A rolling B shorter than twelve months contains a different
seasonal mix each run, so R oscillates with the season rather than with the market. N is
therefore chosen so that B always spans a full annual cycle (minimum 12 calendar months). This is a consequence of the
rolling choice and belongs here, not in M₁ — M₁ imposes no minimum on B and continues to
impose none.

---

## 4. Visibility consequence of the rolling choice

The following are structural blindnesses introduced **by this selection rule**, and are
added to the instrument's visibility constraints (**V**) rather than noted as caveats:

1. **Régime Drift Blindness:** Under a rolling baseline, the instrument cannot observe slow régime change. If the entire comparison set drifts in the same direction over a period comparable to or longer than B, the reference drifts with it and M₁ returns approximately (1 − q) regardless. The instrument reports "ordinary" precisely because "ordinary" has moved.
2. **Variance Drift Blindness:** If market dispersion/volatility increases without shifting the median, the quantile $Q_q$ rises. Consequently, the instrument becomes less sensitive precisely during periods of elevated variance.
3. **The expected value is built in.** By construction approximately (1 − q) of baseline
  time sits at or above R, so an ordinary window yields M₁ ≈ (1 − q). Any elevation
  threshold in **C** is read against that expectation, never as an absolute quantity.
4. **A window enters the next run's baseline.** After W is measured, it becomes part of B
  for later windows. An extreme month therefore raises the reference for the months that
  follow it, which suppresses M₁ in those months. This is correct behaviour under a local
  reference and it is not a contamination of the run in which W was measured — but the
  effect is real and is stated in any sequence of results spanning it.

---

## 5. Parameters frozen in `PARAMS.md`

S₁ is parameter-free as a definition. Values live in `PARAMS.md`:

| Parameter | Meaning | Status |
|---|---|---|
| `L` | Publication lag in days before a run may execute | TO BE MEASURED, then frozen |
| `N` | Rolling baseline length in calendar months | TO BE FROZEN |
| Run day | Day of month on which the scheduled run executes | TO BE FROZEN |
| Operating start | First window in the scheduled series | TO BE FROZEN |

An implementation that supplies a default for any of these is non-conforming.

---

## 6. Relationship to S₂ (Triggered)

S₂ is a different selection rule producing a **different population**: windows that passed
a trigger, rather than all windows. Results are recorded under the mode that produced
them and are never merged into one series, one chart, or one summary statistic. Any
document presenting both states the mode of each result in the same breath as the result.

S₂ is not defined here and does not exist until it is written and frozen. Until then, no
run is executed under a triggered rationale. Legacy pre-registered probe runs (such as OMN-003-PROBE) carry registry designation `selection_mode: legacy_triggered_human` and exist outside S₁ and S₂.

---

## 7. What S₁ does not do

- It does not define what is measured (**M**) or how a label is assigned (**C**).
- It does not guarantee that any window will ever be non-NULL. If the scheduled series
  runs for years without a non-NULL label, that is a result about the markets, not a
  failure of the instrument.
- It does not license comparing an S₁ result to an S₂ result.

*Amendments require a version bump with stated rationale. Definitions are never edited
silently.*

*VolMax Studio Lab · P10 Verification Protocol*
