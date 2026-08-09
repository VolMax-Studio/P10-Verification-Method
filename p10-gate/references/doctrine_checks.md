# P10 Doctrine — Non-Negotiable Rules

These are the standing rules the gate enforces. They do not depend on which model or agent is doing the work.

## Pre-registration and freezing
- The pre-registration commit (rules frozen) must precede any data download. No exceptions.
- Post-hoc findings cannot modify formal verdicts and must be labeled "exploratory, not pre-registered."
- A finding that surfaced *because of* a correction or a data inspection is post-hoc by construction.

## Reproducibility and provenance
- Every finding regenerates from source. If it cannot be regenerated, it is not a result.
- Every number is attributed (cited) or computed (regenerated from one script into a results file). No illustrative numbers presented as measured.
- Every cited URL is live-fetched with title and fetch date logged at the time of citation. Agent self-reports on public state have been wrong repeatedly.
- Raw data provenance (source URL, acquisition timestamp, SHA-256, byte count) is pinned in a manifest. No silent cache fallbacks.

## Licensing (L0)
- Data licenses are verified before any download; verbatim permission text, URL, and access date pinned as L0 artifacts.
- "Free access / downloadable" ≠ "may be re-distributed." Publishing derived analytics is re-distribution.
- Absence of an item from a free-re-use list is not permission. Presence must be shown verbatim, not assumed.
- Unresolved license → status PENDING or HALTED, never "confirmed." When an authority declines to advise, that is not a yes.

## Identity and metadata
- Identity fields (creator name, affiliation, ORCID) are copied verbatim from the pinned block:
  `Nestorov, Ivan / VolMax Studio Lab / ORCID 0009-0006-7940-9539`
  — never agent-composed, never abbreviated to "ORCID Verified" or retitled ("Lead Auditor") unless that is what the pinned block says.
- Verdict language in archived metadata (e.g. Zenodo) must match the report ledger byte-for-byte.

## Repository and registry hygiene
- Force-push on public repos is prohibited without exception. `.gitignore` files are never emptied wholesale.
- Internal strategy documents live in a private repo/folder entirely separate from public working trees.
- A registry (STATUS.md) is a single source of truth: an error in it propagates to every future session, so it is held to a *higher* bar than any single artifact, not a lower one.
- The maximum status an agent may self-assign is "ready for gate." Only the human's explicit chat phrases ratify.

## Claim scope
- Notes are descriptive measurements of public markets. They pass **no verdict** on any operator or asset.
- Audits render verdicts only in the controlled vocabulary; "Reclassify" and "Unfalsifiable-as-Stated" are dispositions, not parallel verdicts.
- A Deferred verdict covers pipeline termination at L1–L4, not a fixed level.
- Claim scope governs everything: do not claim what the data does not distinguish. (Example: 80 PLUS certification data distinguishes efficiency tiers, not the underlying transistor technology — so a tier claim is admissible, a GaN-vs-silicon claim is not.)

## The Caveat Theorem
Caveats are not disclaimers appended to soften a result. They are the active operators that detect and bound anomalies. A verifier that drops caveats has discarded its own instrument. When reviewing, treat a removed or weakened caveat as a substantive change, not an editorial one.

## Comparability discipline
- A rule amended mid-work is admissible only if proven invariant on prior datasets (it must not change earlier verdicts).
- Thresholds carried across audits must state the direction of conservatism they introduce.
- Metrics from markets under different rules (e.g. $100/MWh ERCOT vs $300/MWh NEM scarcity thresholds; single- vs dual-pricing imbalance zones) are not directly comparable — say so explicitly, in the artifact.

---

## Canonical n=1 downgrades (Check 3 in practice)

When any of these framings appear, downgrade them:

| Inflated framing | Correct framing |
|---|---|
| "This is a new category of work / already a methodology" | "The workflow executed once; repeatability is earned across several instances." |
| "A confirmed geographic gradient (A > B > C)" from one time window | "Observed variation over this window, unadjusted for regime differences." |
| "A verified pattern across n jurisdictions" where most instances are a different class (never-public, or asset-identification, not contraction) | Count only the instances of the *specific* claim; report the real n and reclassify the rest. |
| "Our method works" (from a proof-of-concept that mapped where it fails) | "We mapped where the method stops being reliable" — the boundary is the finding. |

The last row is the identity of the whole practice: *if VolMax says something works, it is very likely that it first tried to prove it does not.*
