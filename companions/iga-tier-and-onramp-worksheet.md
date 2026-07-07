# Tier Criteria and On-Ramp Worksheet

*Companion worksheet for chapter 4 (Prioritization). Replace bracketed fields, delete guidance in italics. Statements referenced: P1 to P6.*

**Organization:** [name]  **Version:** [n]  **Date:** [date]  **Owner:** [role]

## 1. Tier criteria (P1)

*Write the criteria, then the attribute values that place a system in each tier. The criteria below are the typical set from P1; add or remove to fit. The framework sets no thresholds; the values are yours.*

| Criterion | Definition for this organization | Tier 1 (highest) | Tier 2 | Tier 3 |
|---|---|---|---|---|
| Data sensitivity | | | | |
| Privilege level | | | | |
| Blast radius on compromise | | | | |
| Regulatory materiality | | | | |
| External exposure | | | | |

## 2. Tier to intensity mapping (P2)

*This mapping feeds the cadence table (chapter 6, C1).*

| Intensity dimension | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Certification frequency | | | |
| Approval depth | | | |
| Review rigour | | | |

## 3. Sequencing rule (P3)

For any two in-scope systems, the one governed first is: [state the rule; it follows from tier].

## 4. Default placements (P4)

- [ ] Privileged access sits in the top tiers
- [ ] Non-human identities sit in the top tiers
- If either is placed lower, rationale: [record it]

## 5. Revisit cycle and triggers (P5)

Cycle: [e.g. annual]. Triggers: security incident, material architecture change, new regulatory obligation, [add others].

## 6. On-ramp selector (P6)

*Answer in order. The first yes selects the starting state; record it and the first move.*

| Question | If yes |
|---|---|
| Is part of the estate being rebuilt while the rest runs as-is? | Bluefield. First move: rank estate segments by risk reduction per unit of rebuild effort; hold the legacy estate under compensating governance (section 4.4). |
| Is there an accumulated estate of grants nobody has reviewed? | Brownfield. First move: baseline the top tier, remediate its orphaned accounts and excess entitlements first (section 4.4). |
| Neither: no governance layer exists yet? | Greenfield. First move: authoritative source and lifecycle spine, then privileged access, then tier-1 systems through the scope gate (section 4.4). |

Selected on-ramp: [greenfield / bluefield / brownfield]  Recorded first move: [text]

---

*Companion artifact, Open IGA Operating Framework, v0.1. Non-normative; where this worksheet and the core diverge, the core governs. Licensed under CC BY 4.0.*
