# Scope Register

*Companion worksheet for chapter 3 (Scope). Replace bracketed fields, delete guidance in italics. Statements referenced: S1 to S7.*

**Organization:** [name]  **Register version:** [n]  **Date:** [date]  **Owner:** [role]

## 1. Identity populations (S1, S4)

*Every population is declared in or out. A population declared neither way is a defect. Each in-scope population names its authoritative source; where two sources conflict, record which one wins.*

| Population | In / Out | Authoritative source | Precedence note |
|---|---|---|---|
| Workforce: employees | [in/out] | [e.g. HR system] | |
| Workforce: contractors | [in/out] | [e.g. vendor management system] | |
| External: partners, vendors | [in/out] | [source] | |
| Non-human: service accounts, keys, workloads, agents | [in/out] | [registry] | |
| Customer | [in/out, usually out: separate CIAM discipline] | | |

## 2. Resource classes (S2, S3)

*Each class names the inventory it can be reproduced from and the granularity at which it is governed. Drift below the chosen granularity is invisible; high-risk classes should sit at entitlement level.*

| Resource class | Authoritative inventory | Granularity (account / role or group / entitlement) | Rationale |
|---|---|---|---|
| [e.g. financial applications] | [e.g. CMDB] | [level] | |
| [e.g. SaaS] | | | |
| [e.g. infrastructure] | | | |

## 3. Onboarding gate (S5)

*No system enters scope without passing this gate.*

- [ ] Owner assigned (chapter 2, O5)
- [ ] Tier assigned (chapter 4, P1)
- [ ] Inventory source confirmed
- [ ] Granularity set
- [ ] Entry date recorded in this register

## 4. Exclusions (S6)

| Excluded item | Rationale | Revisit date |
|---|---|---|
| | | |

## 5. Discovery debt (S7)

*Unknown non-human populations are recorded here as debt with an owner and a bound, and they are treated as out of scope until discovered.*

| Unknown | Owner | Time bound |
|---|---|---|
| [e.g. service account population in legacy estate] | [role] | [date] |

---

*Companion artifact, Open IGA Operating Framework, v0.1. Non-normative; where this worksheet and the core diverge, the core governs. Licensed under CC BY 4.0.*
