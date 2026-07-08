# P10 Design Principles
**Status:** Normative for all VolMax audits. Changes require a versioned amendment
with rationale — principles are never edited silently.

P10 is a claim-verification protocol. It does not audit companies, datasets, or
technologies. It audits **claims** — public, attributable, quantitative or binary
statements — against independently observable evidence.

## The six principles

**1. Claims precede evidence.**
An audit begins with a pinned claim (verbatim text, source URL, publication date,
archive snapshot), never with an interesting dataset. The claim determines which
data is needed — not the reverse.

**2. Verification criteria are frozen before data acquisition.**
Falsification rules, verdict grammar, selection rules, and analysis windows are
committed and timestamped before unseen data is downloaded. If any data was seen
before the freeze, that exposure is disclosed and the affected window is
demoted to secondary evidence. The commit history is part of the proof.

**3. Claims are decomposed into independently falsifiable sub-claims.**
Marketing prefers one sentence; verification requires parts. A composite claim
("exceeded expectations") is either decomposed into numeric sub-claims from the
claimant's own published figures, or recorded as Unfalsifiable-as-Stated.

**4. Evidence is evaluated only within observable measurement boundaries.**
Every finding carries its resolution floor and measurement boundary inline
(e.g., "0 violations at 15-minute resolution"). What the chosen source cannot
show is stated as untestable — never filled in by assumption. Capability claims
are Demonstrated, Bounded, or Not Exercised; they are refuted only by evidence,
not by absence of evidence. Physics violations are a separate finding class.

**5. Every verdict is reproducible and attributable.**
One entry-point script regenerates every published number from hash-pinned data
into machine-readable metrics; reports render from those metrics, never by hand.
Identity fields (author, affiliation, ORCID) are copied verbatim from a pinned
identity block, never composed. Claims about public state (a page updated, a
record live) are accepted only after the live URL is independently loaded.

**6. Limitations are part of the verdict, not an appendix.**
Reports lead with where findings break before where they hold. A verdict without
its boundaries is a different — and weaker — claim than the one the audit earned.

## Verdict vocabulary

- **Verified** — the data supports the claim as stated.
- **Verified with Limitations** — the claim holds within stated boundaries
  (resolution floors, descriptive bands, provenance caveats, observed bounds).
- **Not Verified** — the data does not support the claim. This applies with
  equal force to our own hypotheses, and a rejected own hypothesis is published
  with the same prominence as any other finding.
- **Unfalsifiable-as-Stated** — the claim cannot be independently tested from
  publicly available data as currently published. This is a neutral statement
  about testability, not an accusation. L0 applies per claim: a claim halted at
  L0 is recorded in the final ledger with this disposition alongside the L5
  verdicts of admissible claims.

## The pipeline

Claim → decomposition → pre-registration (frozen, committed) → data acquisition
(license verified before download; hashes pinned on arrival) → L1 integrity →
L2 physics → L3 statistics → L4 reproducibility → L5 verdict per claim →
immutable audit package (report, metrics, decision log, manifest, checksums) →
DOI.

## What P10 is not

- It is not a domain method. It does not tell you how to design an experiment,
  choose a statistical test, or estimate SoC. It sits above domain methods and
  asks one question: *show that the rules did not move after the results arrived.*
- It does not certify quality, endorse operators, or predict future performance.
  It attests that a stated claim was tested against stated evidence under
  pre-stated rules. A verifier who needs a particular outcome — favorable or
  unfavorable — has reacquired the claimant's conflict of interest.
- It is not a standard. It is a protocol. If others adopt it, they may call it
  what they wish; we do not.
- It claims no domain beyond its case studies. Demonstrated scope today:
  operational claims of grid-scale energy storage from public market and
  settlement data. Whether the principles transfer elsewhere is decided by
  audits that exist, not by this document.
