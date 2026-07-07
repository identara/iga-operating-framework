# Platform Capability Checklist

*Companion worksheet, non-normative. Fifteen tool-agnostic capabilities derived from the core and the metrics specification. Any platform or combination of platforms satisfying these can run the framework; none of them names a vendor. Use it to evaluate an incumbent stack or a candidate one, and record how each capability is met or compensated.*

**Organization:** [name]  **Platform(s) evaluated:** [names]  **Date:** [date]  **Assessor:** [role]

| # | Capability | Derived from | Met / compensated / gap |
|---|---|---|---|
| 1 | Consumes lifecycle events from authoritative sources, including leave, return, rehire, and conversion signals | S4; PR1, PR8 | |
| 2 | Applies a precedence rule where identity sources conflict | S4 | |
| 3 | Reproduces the in-scope inventory per resource class on request | S2 | |
| 4 | Governs at entitlement granularity where the scope register requires it | S3 | |
| 5 | Maintains a registry of non-human identities with a human owner per entry | S7; O7 | |
| 6 | Runs the request path with an approval chain by tier and a time bound per stage | PR3; P2, C4 | |
| 7 | Detects provisioning outside the request path by reconciliation | PR3 | |
| 8 | Presents certifiers with entitlement description, last use, and recorded justification | PR4 | |
| 9 | Constrains bulk approval, and logs it where permitted | PR4 | |
| 10 | Executes revocation with verification of removal in the target system | PR5 | |
| 11 | Maintains an exception register with expiry and owner per entry | PR6 | |
| 12 | Triggers out-of-cycle review on role change, departure, incident, and organizational change | C3 | |
| 13 | Records grant, revocation, and certification decision timestamps, and campaign completion dates | MS6; part III data model | |
| 14 | Computes or exports the data for metrics over declared, constant windows | MS1 to MS4 | |
| 15 | Records delegations of approval authority as time-bounded and revocable | O6 | |

*Where a capability is met by a compensating process rather than the platform, record the process and its owner. A gap with no compensation is scope the program cannot govern yet, and it belongs in the tier-sequenced backlog (chapter 4).*

---

*Companion artifact, Open IGA Operating Framework, v0.1. Non-normative; where this worksheet and the core diverge, the core governs. Licensed under CC BY 4.0.*
