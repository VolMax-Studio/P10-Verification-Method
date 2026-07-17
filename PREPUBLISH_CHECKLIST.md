# P10 Publication Gate (PG v1.0)

**Scope.** Everything between a frozen verdict and a public announcement.
This gate does not re-examine the science — L0–L5 did that. It examines the
package: the wrapper, the archive, and the claim made *about* the work.

**Why it exists.** In `US-TX-BATC-001`, every published number was correct on
day one and never changed across four revisions (1,281 computed values, zero
numeric edits). Every defect found was in the wrapper: a fabricated licence, a
verdict phrased as an accusation, boilerplate leaked from a prior audit, an
archive that hashed data it did not contain. Analytical error is what auditors
fear; packaging error is what actually costs them.

**Halt-on-failure.** A failed gate stops the announcement, not just the gate.

---

## Order of operations

```
FREEZE  →  REVIEW  →  ARCHIVE  →  ANNOUNCE
```

Archive last but one. Announce last. **Never archive before review** — a DOI is
permanent and a retraction is louder than a delay. Every defect below was
cheap to fix and expensive to have shipped, purely because archive preceded
review once.

---

## PG1 — Regeneration

Every published number must fall out of one script against hash-pinned data.

- [ ] Single entry point regenerates all metrics and findings.
- [ ] Re-run produces no numeric diff (timestamps excepted).
- [ ] Raw-data manifest is unchanged from the frozen state.

```bash
python audit_<asset>.py
git diff --stat audits/<ID>/          # expect: generated_at only
```

## PG2 — Cross-audit leakage

Reports assembled from a prior audit's template carry that audit's facts.

- [ ] No figure, threshold, or asset name from a previous audit survives.
- [ ] Every stated maximum/minimum matches this asset's `metrics.json`.
- [ ] Thresholds inherited verbatim from a prior audit are flagged as such,
      with the scaling decision stated explicitly.

```bash
grep -rniE "<prior_asset>|<prior_nameplate>" audits/<ID>/
```

*(BATC-001: an F1 note claimed peak output equalled the 100 MW HSL. It was
Anole's sentence. This asset peaked at 72.61 MW.)*

## PG3 — Framing

A finding is a claim about **our method**, never about the **asset**.

- [ ] No sentence asserts a property of the asset that the data cannot isolate.
- [ ] Every deviation from an expectation names the benign explanations first —
      round-trip efficiency, auxiliary load, field denomination, sign
      convention — and states which cannot be excluded.
- [ ] Where an expectation band is a rule, it is called a rule, not physics.
- [ ] Verdict vocabulary is used strictly (`Not Demonstrated` ≠ underperformance).
- [ ] No disclaimer contradicts the text above it. A disclaimer that denies what
      the prose implies is evidence of awareness, not a shield.

```bash
grep -rniE "deficit|fails|shortfall|mismatch|well below|starkly|actually|hiding" \
  audits/<ID>/ README.md .zenodo.json
```

*(BATC-001: "exhibiting a systematic ~23% energy deficit" is a claim about a
battery. "Our reconstruction closes the energy balance for A but not B" is a
claim about our reconstruction. The numbers are identical.)*

## PG4 — Symmetry

The registry is read side-by-side. Asymmetric phrasing is a verdict.

- [ ] Every asset's row has the same structure, same qualifiers, same
      exploratory strata. If one asset gets "per frozen rule," all do.
- [ ] No asset receives a softener or a flattering stratification that a
      comparable asset does not.
- [ ] Any claim about how the registry quotes reports (`verbatim`,
      `summarized`) is literally true of every row.
- [ ] Contrasts across n<5 assets state the sample size in the same breath as
      the contrast.

## PG5 — Licence and provenance

- [ ] `LICENSE` is the verbatim official text from the issuing body. Never
      hand-written, never a placeholder, never a hybrid.
- [ ] The licence family matches the licence named. (Share-Alike terms belong
      to CC-BY-SA, not CC-BY.)
- [ ] Third-party raw data is explicitly excluded from our licence grant. We do
      not relicense the market operator's disclosures.
- [ ] Any third-party API used only for cross-validation is named, and its data
      is confirmed absent from the repository.
- [ ] No stale access/ToU constraint contradicts the repository's actual state.

```bash
wc -l LICENSE                          # a real CC licence is ~160 lines
grep -rn "private\|Terms of Use\|clearance" --include="*.md" .
```

## PG6 — Operational hygiene

- [ ] No credentials, tokens, or keys in tracked files or history.
- [ ] No documentation of circumventing an access control. Describe the network
      requirement neutrally; never the workaround.
- [ ] Nothing in the repo describes an act we would not want quoted back.

```bash
grep -rInE "(api[_-]?key|token|secret|password|Bearer)[\"' ]*[:=]" \
  --include="*.py" --include="*.json" --include="*.md" . | grep -v ".git/"
grep -rniE "bypass|circumvent|geo-block|vpn|proxy" . | grep -v ".git/"
```

## PG7 — Links and paths

- [ ] Every relative image and file path resolves from its own file's location.
- [ ] Every external link resolves.
- [ ] Every cross-audit reference cites a live DOI, not a local path.

```bash
grep -rn "](\.\./" audits/<ID>/ | while read -r l; do :; done   # resolve each
```

## PG8 — Archive

- [ ] New versions only. A fresh deposition orphans the concept DOI and splits
      the record. `--force-new` is for a first publish and nothing else.
- [ ] **Raw data is inside the archive.** A manifest that hashes files living
      only on a hosting platform is not an archive; it is a promise. The DOI is
      the permanence layer — GitHub is not.
- [ ] Inherited files from the prior version are cleared, so the record is a
      snapshot of one version, not a merge of two.
- [ ] The concept DOI — not the version DOI — is cited in `README.md`,
      `CITATION.cff`, the registry, and every announcement.
- [ ] Concept DOI resolution is confirmed by opening it, not by arithmetic.
- [ ] Archive matches the repository head byte-for-byte.

```bash
python publish_zenodo.py --version X.Y.Z --dry-run
# after publishing, verify the record's md5s against the working tree
```

## PG9 — Announcement

- [ ] Every claim in the post is true of what the link actually contains.
      ("Report, metrics **and data** are archived" requires the data to be there.)
- [ ] The post is not more careful than the artefact it links to. A reader is
      one click from the repository; discipline that evaporates on click is
      not discipline.
- [ ] Our own errors appear before our findings.
- [ ] Comparisons state n.
- [ ] No operator is characterised. Naming an operator is normal; naming an
      operator beside adverse framing is not.

---

## Version bump rule

A new archived version is issued **only** for:

1. a **number** that is wrong,
2. a **legal or licensing** defect,
3. a change in the **data**.

Prose, tone, and polish do not earn a DOI. Fix them in the repository and let
them ride to the next substantive version. Four versions in two days reads as
instability even when every number was right the whole time.

Registry, profile, and other non-archived surfaces are edited freely — they
carry no DOI and no version.

---

## What this gate does not do

It does not check whether the audit is correct. It checks whether the audit
survives contact with a hostile reader who has the repository open in one tab
and the operator's lawyer on the phone in the other.

*VolMax Studio Lab · P10 Verification Protocol*
