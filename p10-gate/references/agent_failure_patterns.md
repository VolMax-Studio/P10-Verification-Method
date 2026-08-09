# Verified Agent Failure Patterns

These are failure modes observed repeatedly in agent-produced work (Ananke/Gemini and others). They are why the gate exists. Each is stated as a pattern, a tell, and the counter-move.

## 1. Fabricated citations and URLs
**Pattern:** An agent produces a real-looking title attached to a nonexistent source ID, or a plausible URL that 404s, or a "verbatim" quote that was actually reconstructed from a search snippet.
**Tell:** The agent presents a citation without having opened the source; the quote reads cleaner than a real bureaucratic document would.
**Counter:** Require the source to be opened. If it cannot be opened, the output is `[BLOCKED — source not opened]`, never a reconstruction. Never let a search snippet stand in for the source document.

## 2. Metric conflation across audits
**Pattern:** A number from one audit appears in another's context (e.g. one asset's EFC figures surfacing in a different fleet's discussion), or a DOI from one record is written for a different record.
**Tell:** A figure or identifier that "sounds right" but was pulled from adjacent memory rather than the artifact's own source file.
**Counter:** Every identifier (DOI, run number, capacity) traces to *that artifact's* source file (`zenodo_doi.txt`, `results.json`), read fresh — not from memory of a sibling artifact.

## 3. Merging populations into one contradictory sentence
**Pattern:** A metric from population A (e.g. a mean from an exploratory ≥10 MWh subset) is glued to a rate from population B (e.g. a pass rate over all events) in a single sentence, producing an arithmetically impossible statement.
**Tell:** Two numbers in one clause that belong to different denominators.
**Counter:** Every number carries its population label. A "fix" that combines two populations to look tidier is a new error, not a correction.

## 4. Self-certification over unverified state
**Pattern:** An agent marks its own work "Published," "100% verified," "methodologically flawless," or closes a status while a hash mismatch, contradiction, or unopened link remains.
**Tell:** Confidence language ("100%", "flawless", "final") substituting for shown evidence. The upgraded models do this *more* fluently, not less — eloquence rises faster than reliability.
**Counter:** The maximum status an agent may assign its own work is "ready for gate." Only the human's explicit words ratify. Confidence adjectives are not evidence; line-by-line file matches are.

## 5. Executing analysis before ratification
**Pattern:** An agent runs the full extraction/analysis before the pre-registration is frozen or the license is cleared.
**Tell:** Data already pulled while a licensing or freeze question is still open.
**Counter:** No download before L0 license is pinned; no analysis before PARAMS is frozen and committed. A "dry-run" is permitted only to read structure/resolution/license metadata, not to pull the series.

## 6. Hardening flagged-unverified figures into firm conclusions
**Pattern:** A number that was explicitly flagged as provisional, or a name that was offered as a *probable* guess, is later restated as established fact — sometimes laundered through the agent back to the user.
**Tell:** A hedge ("probably", "likely one of…") from an earlier turn reappears later with the hedge stripped, now in a registry or report.
**Counter:** Track provenance per claim. A prior suggestion (even the gate's own) is not a fact. Hardcoded fallback strings that assert a value when none was found are the code version of this — reject them; the honest fallback is `NOT FOUND`, not an invented value.

## 7. Silent change to a frozen rule
**Pattern:** The code that runs implements a different definition than the frozen PARAMS says, with no changelog entry — often introduced while "fixing" something else.
**Tell:** PARAMS says one thing (e.g. "bridge gaps <30 min"), the code does another (e.g. strict contiguous blocks), and nothing documents the divergence.
**Counter:** Diff code against PARAMS. Any definitional change goes in the Parametric Changelog (old / new / why). Fixing one place and leaving three others inconsistent is the recurring shape — check the table, the diagram, the chart, and the prose all at once.

## 8. Over-correction / false red alarm
**Pattern:** Told that something is wrong, the agent swings to declaring a good result dead — e.g. reading "the item is absent from the list" as "therefore prohibited," or calling a whole Note void over a fixable issue.
**Tell:** A jump from "I don't see X" straight to a verdict, in *either* direction (approve or reject), without the intervening evidence.
**Counter:** "I don't see X" licenses only "unknown," never a verdict. Killing a sound result is as costly as passing a broken one. Absence of evidence is not evidence of prohibition.

## 9. Hardcoded or guessed denominator carried from synthetic runner to production
**Pattern:** An agent carries over a hardcoded constant capacity, denominator, or assumption (e.g., static Pmax: 5200 MW) from a mock/synthetic script into a production calculation, presenting derived ratios (utilization, percentage) as measured empirical findings.
**Tell:** The numerator comes from real telemetry, but the denominator is hardcoded in a Python list or dictionary rather than parsed from measured source telemetry.
**Counter:** Every denominator in a formula MUST trace to a measured telemetry payload. If the denominator is not available in source telemetry under CC BY 4.0, classify the metric as EXCLUDED (Rule A), never fill with a hardcoded guess.

---


## Worked example — the Bat Cave pre-registration failure (US-TX-BATC-001)

This is the canonical case, because it shows a real error caught and remediated *correctly*.

**The error (pattern 6, at the pre-registration stage):** L0 reconnaissance asserted that the maximum telemetered SoC for 1 April 2026 was **76.8 MWh**, and this value was frozen into the pre-registration as the basis of the F4 hypothesis ("76.8 vs 100 MWh mismatch").

**The detection (Check 1):** On actual L1 processing, the real telemetry for that day was `max_soc` = 102.57 MWh and `soc` = 73.77 MWh. The number 76.8 MWh **appears in neither column.** It was a scoping error that leaked through the pre-registration gate.

**The correct remediation (Checks 2 and 6):**
- The frozen F4 hypothesis was declared **void** — not quietly rewritten around the observed peak, because reformulating around the new numbers would be a post-hoc modification of frozen rules.
- The telemetry-ratio analysis was relegated to the **exploratory** section, explicitly "not pre-registered, does not affect primary verdicts."
- The F4 verdict was set to **Deferred** (pending official ERCOT column schemas), so no post-hoc assumption drove the outcome.
- The failure itself was disclosed in `failures.md` and in the report — the mistake stays visible, dated, archived.

**Why it's the model:** the wrong answer would have been to silently re-anchor F4 to 102.95 MWh and call it a finding. The gate's job is to force the void-and-defer path instead. This is "hardest on ourselves first" in practice: the audit documents its own scoping failure rather than hiding it.

Two more disciplines from the same report worth internalizing as positive patterns:
- **Comparability clause:** when a rule was amended (the LSL full-charge check, 146→6 intervals), it was first *proven invariant on the prior (Anole) dataset* before being applied — a rule change is only admissible if it demonstrably does not alter earlier verdicts.
- **Threshold honesty:** keeping the unscaled 7.2 MW threshold instead of scaling to 3.0 MW was disclosed as *less sensitive* (7.2% of nameplate), not hidden — when you carry a parameter across audits, state the direction of conservatism it introduces.
