# Worked example: Fernway Software

*Non-normative. Fernway Software is a fictional organization; any resemblance to a real company is coincidental. Every value below is Fernway's own choice, recorded to show the framework in use. Nothing here is a benchmark (MS5).*

Fernway Software is a 300-person expense-management SaaS company. It has an HR system, a production cloud estate, a code host, a finance system, and roughly forty SaaS applications. It has never run an identity governance program: greenfield on the starting-state axis, small product organization on the archetype axis. This part walks Fernway through the six layers in build order, filling each companion as it goes. Each section ends with the split between what the framework supplied and what Fernway decided.

## Layer 1: Fernway's mandate

Fernway's charter states risk first: reduce standing privilege in production and in systems holding customer financial data. SOC 2 Type II, committed to enterprise customers by contract, is listed as an obligation the program satisfies (M2). The business driver is recorded plainly: security questionnaires are stalling enterprise deals, and access evidence is the slowest answer. The scope boundary names workforce and non-human identities across production and core business systems, and declares customer identity out, owned by the product authentication stack (M4). Authority lists three compellable actions: require reviews on the cadence table, revoke access that fails certification, block provisioning that violates policy (M5). The CTO signs as sponsor, and the program reports to the executive team quarterly (M6, M7). Being greenfield, Fernway deletes the remediation section of the charter template rather than filling it, which is the template working as designed.

**Framework supplied:** the charter structure, the risk-first ordering, the authority section most charters omit. **Fernway decided:** which risk, which obligation, which three actions, who signs.

## Layer 2: Fernway's ownership

At 300 people the map is short. Business resource access carries its A with function heads: the Controller for the finance system, the VP Engineering for production and the code host (O1). The IT team of four builds and runs the platform; the Head of Security, a team of one, governs. That leaves one overlap: the IT lead also certifies tier-3 collaboration tools, recorded as accepted risk, accepted by the CTO, reviewed annually (O2). Escalation is one line: disputes go to the CTO, decided within five business days (O3). Every service account maps to an engineering team lead, and ownership transfers on departure (O7). The interfaces table names five counterparts: the HR system feed for lifecycle events, IT intake for requests, application owners for revocation execution, finance operations for contractor end dates, and the on-call security rotation for incident triggers (O8).

**Framework supplied:** the decision classes, the one-A rule, the self-certification check, the interface list. **Fernway decided:** the names, the overlap it could live with, the five-day bound.

## Layer 3: Fernway's scope

The scope register declares four populations: employees in, sourced from the HR system; contractors in, sourced from the HR system's contingent records; non-human identities in, with the unknown portion recorded as discovery debt owned by the Head of Security with a sixty-day bound (S1, S4, S7); customer identity declared out, with the exclusion written down and a revisit date one year on (S6). Resource classes: the production cloud and the finance system are governed at entitlement level, the code host at repository-role level, collaboration SaaS at group level, each granularity recorded with its reason (S3). The onboarding gate runs from day one, so every system entering scope arrives with an owner and a tier already attached (S5), which is the greenfield advantage the modulation section describes: the gate costs little now and prevents the debt other programs spend years discovering.

**Framework supplied:** the population list, the gate, the rule that silence is a defect. **Fernway decided:** where entitlement depth was worth it and what could wait at group level.

## Layer 4: Fernway's priorities

Fernway writes four criteria and three tiers (P1):

| Criterion | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Customer financial data exposure | Direct access | Indirect or derived | None |
| Production blast radius | Can alter or delete customer-facing systems | Internal systems only | Neither |
| SOC 2 materiality | In audit scope | Supports in-scope systems | Out of scope |
| External exposure | Internet-facing admin surface | Authenticated internal | Internal only |

The production cloud, the customer database, the finance system, and the code host land in tier 1; the code host is there on blast radius, since the deploy pipeline is a production-altering surface. Privileged access and non-human identities sit in tier 1 by default, and Fernway keeps the default (P4). The intensity mapping ties tier to certification frequency and approval depth (P2), and the sequencing rule is one sentence: tier decides order, and within a tier, the system with the larger identity population goes first (P3). The on-ramp selector answers greenfield, and the recorded first move follows section 4.4: the HR feed and lifecycle spine first, privileged access second, then tier-1 systems through the gate (P6).

**Framework supplied:** the criteria prompts, the top-tier defaults, the on-ramp. **Fernway decided:** every cell in the table above.

## Layer 5: Fernway's processes

The lifecycle checklist fills in as follows. A joiner event from the HR system grants birthright access defined by written policy: email, single sign-on, collaboration suite, team group (PR1, PR2). A mover event fires on role or department change and re-evaluates existing access; a manager change alone does not, a local call Fernway records (PR1). Leavers split into two paths: voluntary departures revoke within one business day, involuntary departures the same day (PR8), both verified in target systems (PR5). Leave of absence suspends access within one day of the HR event, return requires verification before restore, a rehire is treated as a joiner with history, and a contractor converting to employee has the contractor profile replaced rather than added to (PR8). Requests run through one intake with approval depth by tier and a bound per stage, and a weekly reconciliation looks for side-door grants (PR3). Certifications start manual and light, which is the greenfield modulation working: tier 1 quarterly with the certifier shown usage and justification, bulk approval disabled (PR4). Exceptions carry a ninety-day maximum, an owner, and CTO approval (PR6). Non-human identities pass a creation gate, rotate credentials on a schedule per tier, and decommission with dependant verification (PR7).

**Framework supplied:** every checkbox, including the states beyond joiner, mover, leaver that most programs discover in audit findings. **Fernway decided:** the bounds, the birthright list, the manager-change call.

## Layer 6: Fernway's cadence

The cadence table takes the P2 mapping and gives it clocks:

| Setting | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Certification frequency | Quarterly | Semi-annual | Annual |
| Approval depth | Owner plus security review | Owner | Manager |
| Request approval bound, per stage | 2 business days | 3 business days | 5 business days |

Expiry is the default for contractors, exceptions, and elevated production access; the four-person IT team holds standing admin on the collaboration suite with the rationale recorded (C2). Event triggers: departure immediately, security incident within 24 hours, reorganization within ten business days (C3). Revocation executes within one business day and escalations resolve within five (C4). Measurement windows are quarterly, matching the certification cycle, held constant (C5, MS1). The quarterly executive report leads with risk movement, unreviewed drift and leaver breaches, with completion rates in the appendix, which is M2 and C6 in one decision. The failure-mode self-check is scheduled annually each January (C8).

**Framework supplied:** the rows, the discipline that they exist. **Fernway decided:** every number.

## Fernway measures

Phase 1 only, matching the adoption order. The platform's grant and revocation logs plus campaign dates give Fernway everything EDR needs (MS6), so it computes all three variants quarterly, segments human and non-human (MS3), and states scope and granularity on every figure (MS2). Its conformance claim reads exactly as MS11 prescribes: conforms to the Open IGA Operating Framework Operational Metrics Specification v0.1 for EDR. Governance Lag waits for the HR correlation work, which is phase 2 honesty rather than a gap. The Head of Security computes; the CTO consumes (MS12).

## The ratio

Count what happened. The framework supplied the six layers, the build order, roughly fifty numbered decisions, nine failure-mode checks per self-test, every worksheet row, and the two defaults Fernway kept. Fernway supplied names, one recorded overlap, one exclusion, a tier table, and about two dozen values, an afternoon of decisions it was equipped to make about itself. The structure travelled; only the judgment stayed local. That split is the reason this framework is published.

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
