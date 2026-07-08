# Prioritization

*Layer 4 of 6. Interrogative: which.*

![You are here: layer 4 of 6.](../figures/strip-04-prioritization.svg)

*Part of the Open IGA Operating Framework, operating core. v0.1 draft for public review. Language conventions (must, should, may) are defined in the repository README.*

## 4.1 Purpose

This layer sequences governance across the scoped estate. Scope draws the boundary; this layer decides which parts of the bounded estate are governed first and how much governance each part receives. It exists because no program has the capacity to govern everything at once and at equal depth, and a program that pretends otherwise governs everything badly (see F1).

This is also the layer where starting state bites hardest, so the on-ramps are specified here (see 4.4).

The layer produces two required artifacts: a risk-tier register and a sequencing rule.

## 4.2 Decisions

**P1.** A risk-tiering model must exist, with written criteria, and every in-scope resource must hold a tier. Typical criteria: data sensitivity, privilege level, blast radius on compromise, regulatory materiality, and external exposure. The criteria are the program's own; the requirement is that they are written and applied consistently.

**P2.** Tier must determine governance intensity. Certification frequency, approval depth, and review rigour scale with tier, and the mapping from tier to intensity is recorded. The cadence table (chapter 6, C1) consumes this mapping.

**P3.** A sequencing rule must exist: for any two in-scope systems, the program can state which is governed first and why, and the answer follows from tier rather than from convenience.

**P4.** Privileged access and non-human identities should sit in the top tiers by default. A decision to place either lower must be recorded with its rationale.

**P5.** Tier assignments must be revisited on a cycle and on trigger events: a security incident, a material architecture change, a new regulatory obligation.

**P6.** The program must select and record its on-ramp according to its starting state (see 4.4), because the first sequencing move differs by state, and an unstated on-ramp defaults to vendor order or audit order (see F2 and F3).

*Example (non-normative). A system holding regulated financial data lands in tier 1 on regulatory materiality alone. The internal wiki lands in tier 3, and the program can state why the ERP onboards first without reference to which connector was easiest.*

## 4.3 Failure modes

**F1. Uniform governance.** Every system receives the same intensity, the program's capacity spreads thin, and the highest-risk systems get the same rubber stamp as the lowest. Observable signal: campaign scope and frequency are identical across tiers, or no tier register exists.

**F2. Audit-driven sequencing.** Whatever the last finding named jumps the queue. Observable signal: the roadmap reshuffles after each audit while the tier register sits unchanged.

**F3. Vendor-driven sequencing.** Governance order follows connector availability. Observable signal: low-risk SaaS is fully governed while higher-tier systems wait, because the connector was easy.

**F4. Static tiers.** Observable signal: the tier register has not changed in years while the architecture has.

## 4.4 Modulation

This layer is where the three starting states diverge most, so the on-ramps are specified as normative sequences.

**Greenfield on-ramp.** There is no accumulated estate to remediate, so prioritization governs onboarding order: the authoritative identity source and the lifecycle spine first, privileged access second, then tier-1 systems as they enter through the scope gate. Onboarding whatever integrates most easily reproduces F3 from day one.

**Bluefield on-ramp.** The rebuild sequence is the prioritization decision. Rank estate segments by risk reduction per unit of rebuild effort, rebuild in that order, and hold the legacy estate under compensating governance, typically heavier certification, while it waits. The seam between regimes carries its own owner (chapter 2).

**Brownfield on-ramp.** Discovery first, then cleanup by tier. Baseline the top tier, remediate its orphaned accounts and excess entitlements first, and work downward. The remediation mandate (chapter 1) executes through this tier model; cleanup run alphabetically or by system age is effort without risk logic.

**By archetype.** A regulated enterprise finds its top tier partly pre-drawn by regulation, since financially material systems can sit nowhere else. A small product organization may hold three tiers and one page of criteria. A public sector body often inherits tiering from information classification already fixed in law. Detailed treatment belongs to the archetype profiles.

## 4.5 Instrumentation

Trust Gradient is proposed for this layer. Status: proposed, pending empirical confirmation against pilot data, and this section carries no normative weight until that evidence exists.

Rationale for the proposal: tiering is where the program assigns differentiated trust across the estate, which makes this layer the natural host for a metric that reads how trust is distributed and how it moves. Confirmation here is empirical rather than editorial: the mapping is confirmed when pilot data shows the metric moving in response to this layer's decisions, and the reference dataset on the roadmap is where that evidence comes from.

## 4.6 Companion artifacts

Risk-tiering criteria and on-ramp selector worksheet (non-normative): `companions/iga-tier-and-onramp-worksheet.md`.

*With tiers set, the next layer builds the machinery that runs the decisions.*

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
