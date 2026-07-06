# P10 Verification Protocol: Proposal Rejection Notice (Draft v1.1 - Lyapunov/Notary)
**Date**: 2026-07-04  
**Author**: Ivan Nestorov, VolMax Studio Lab  

---

## Architectural Decision

The external draft proposal suggesting updates to the core P10 protocol (designated as **Draft v1.1 (Lyapunov/Notary Proposal)**) is **rejected in its entirety**. 

The official P10 Verification Protocol is established at **v1.1** (incorporating the domain-agnostic [L0 Audit Admissibility Protocol](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_Audit_Admissibility_Protocol.md) and defined in [P10_verification_protocol_v1.md](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_verification_protocol_v1.md)). The core protocol remains locked against the rejected Draft v1.1 (Lyapunov/Notary) features, and any domain-specific extensions remain strictly restricted to modular Annexes.

---

## Rationale for Rejection

1.  **Preservation of Domain-Agnosticism**:
    The strength of the P10 Verification Protocol lies in its general applicability to any system built on measured physical signals (battery systems, electrical grids, data centers, heat exchangers, or mechanical turbines). Draft v1.1 attempted to introduce domain-specific tools (such as Lyapunov exponents, Detrended Fluctuation Analysis (DFA), and halo adapters) directly into the core, violating this abstraction layer.
2.  **Exclusion of Algorithmic Bloat**:
    Lyapunov exponents and DFA are specific mathematical metrics that are not universally applicable, nor are they a required standard for general verification audits. Forcing them into the protocol's core represents a form of developer/domain bias that P10 was explicitly created to prevent.
3.  **Strict Prevention of Fabrication (Blocker Rule)**:
    Draft v1.1 proposed the integration of a non-existent entity called the "automated cloud notary VolMax Engine" and claimed its operational status. 
    *   The core foundation of the P10 protocol is **truth-over-claims** and the verification of physical/statistical reality.
    *   The introduction of fabricated entities or concepts to justify protocol expansions is a direct, blocker-level violation of P10-L5 (Statistical/Interpretative Integrity) and P10-L1 (Data Integrity). A protocol designed to verify the truth cannot accept fabricated assets in its own specification.
4.  **Modular Annex Architecture**:
    Domain-specific operations belong exclusively in modular **Annexes** (e.g., the [P10 Battery Annex](file:///home/volmax-studio/volmax-projects/iot2/PORTFOLIO/P10-Verification-Method/P10_Battery_Annex.md)), which extend the core L1-L5 levels without bloating the core protocol description.
