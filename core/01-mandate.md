# Mandate

*Layer 1 of 6. Interrogative: why.*

![You are here: layer 1 of 6.](../figures/strip-01-mandate.svg)

*Part of the Open IGA Operating Framework, operating core. v0.1 draft for public review. Language conventions (must, should, may) are defined in the repository README.*

## 1.1 Purpose

This layer fixes why the program exists, in writing, with authority behind it. It sits first because every layer below inherits its choices. Ownership (layer 2) distributes the authority the mandate creates, scope (layer 3) bounds what the mandate covers, and the metrics that instrument later layers measure movement against the risk the mandate names.

The six layers are ordered by dependency, and the order is a build sequence rather than a waterfall. A program revisits any layer as it matures, but a change to the mandate cascades downward, and no lower layer can repair a defect here.

The layer produces one required artifact: a program charter, signed by a sponsor with the seniority to make its authority real.

## 1.2 Decisions

**M1.** The program must state its drivers across the categories that apply, and rank them. The three categories: risk (the identity exposure the organization carries, such as standing privilege, over-provisioned access, orphaned accounts, and lifecycle gaps), compliance (regulations or frameworks that require demonstrable access governance), and business (access friction costing the organization through slow onboarding, long request cycles, or licence waste).

**M2.** Risk reduction should be written as the primary purpose. Compliance obligations should be framed as constraints the program satisfies. A program whose stated purpose is passing audits will optimize for exactly that, and its success measures will track activity rather than risk (see F1).

**M3.** Every regulation, standard, or framework named in the charter must be verified against its primary source before the charter is finalized. Secondhand descriptions of obligations do not qualify.

**M4.** The charter must state a high-level scope boundary: which identity populations and system classes sit inside the program, and which sit outside. Detailed scope definition belongs to layer 3.

**M5.** The charter must state the program's authority: the decisions it owns and the actions it can compel. Typical compellable actions include requiring access reviews on a defined cadence, revoking access that fails certification, and blocking provisioning that violates policy. Authority left implicit does not exist.

**M6.** The charter must name accountability: the body the program answers to, what it reports, and on what cycle.

**M7.** The charter must carry the signature of a sponsor senior enough to enforce the stated authority when a resource owner pushes back.

**M8.** The charter should set its own review cycle, twelve months at most, and should be re-ratified after any reorganization that changes decision ownership.

**M9.** The mandate must carry resources: a named funding source and capacity commensurate with the scope the charter claims, recorded in the charter and revisited whenever scope grows (chapter 3, S5). Authority that cannot staff its own cadence is authority on paper.

*Example (non-normative). A mid-market insurer writes its primary purpose as reducing standing privilege in claims and finance systems, with SOX and provincial privacy law listed as obligations the program satisfies. Onboarding speed is recorded as a business driver, and the chief risk officer signs as sponsor.*

## 1.3 Failure modes

**F1. Compliance-only mandate.** The program is justified to leadership on audit obligations alone, and the operating goal collapses to passing the audit. Observable signal: every success measure counts activity, such as certifications completed or reviews closed, and no measure tracks whether risk moved.

**F2. Toothless charter.** Purpose and principles are stated, authority is absent. The document reads well and compels nothing. Observable signal: the program recommends rather than requires, and access it flags stays live indefinitely.

**F3. Sponsor gap.** Authority is written down, but the signing sponsor lacks the standing to enforce it against a resistant executive. Observable signal: the first escalation that reaches leadership is overridden, and no record of the override exists.

**F4. Stale mandate.** The charter was written once and never revisited. Observable signal: it names roles, committees, or reporting lines that no longer exist.

**F5. Unfunded mandate.** The charter grants authority and the program cannot staff what the charter obliges. Observable signal: certifications and reviews slip for capacity reasons while the charter's scope and obligations stay unchanged.

## 1.4 Modulation

**By starting state.**

Greenfield: the charter can be lean. The mandate should emphasize establishing the authoritative identity source and the joiner, mover, and leaver spine before entitlement debt accumulates. No remediation clause is needed.

Bluefield: the mandate is dual. The charter should name which parts of the estate run under steady-state governance and which are being rebuilt, because the two regimes carry different authority needs.

Brownfield: the charter must add a time-boxed remediation mandate over the accumulated estate alongside the steady-state mandate. A steady-state mandate alone stalls against existing access debt.

**By archetype.** The driver mix in M1 shifts with organizational shape. A regulated enterprise leads with compliance and risk, and segregation of duties enters its guiding principles as a requirement. A small product organization leads with business and risk, concentrates authority in a few owners, and can hold the charter to a single page. A public sector body leads with compliance and process constraints, and its sponsorship is often fixed by statute rather than chosen. Detailed treatment belongs to the archetype profiles.

## 1.5 Instrumentation

No metric in the metrics specification attaches to this layer in v0.1, and none is proposed. The mandate defines what risk means for the program, which is the reference the downstream metrics measure against. The health check for this layer is qualitative: the charter exists, is signed, is inside its review cycle, and its authority has been exercised at least once. An authority never exercised is indistinguishable from an authority never granted.

## 1.6 Companion artifacts

IGA program charter template (non-normative), one page when completed: `companions/iga-program-charter-template.md`. The template operationalizes M1 through M8. Where the template and this chapter diverge, the chapter governs.

*The mandate creates authority. The next layer distributes it into named roles and decision rights.*

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
