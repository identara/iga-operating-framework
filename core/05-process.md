# Process

*Layer 5 of 6. Interrogative: how.*

![You are here: layer 5 of 6.](../figures/strip-05-process.svg)

*Part of the Open IGA Operating Framework, operating core. v0.1 draft for public review. Language conventions (must, should, may) are defined in the repository README.*

*Statement identifiers in this chapter use PS rather than P or PR: P is held by chapter 4, and PR reads as pull request in repository discussion.*

## 5.1 Purpose

This layer defines the mechanics: how access is requested, approved, granted, changed, certified, and revoked. It sits fifth because a process implements decisions made above it: the approvers come from the ownership layer, the governed set from scope, and the depth of control from tier. The industry's standard mistake is building this layer first, buying the tool and wiring workflows before anyone owns a decision, and the layers above exist to prevent that inversion.

The layer produces defined lifecycle, request, certification, revocation, and exception processes, each with an owner per step. The normative statements govern the access-risk-bearing core of the process surface; the wider surface a full program operates is enumerated in section 5.7.

## 5.2 Decisions

**PS1.** The joiner, mover, and leaver lifecycle must be defined end to end, with an accountable owner per step (the matrix in chapter 2, O4). The mover event must trigger re-evaluation of existing access rather than only granting new access, and the leaver event must carry a time bound from departure to revocation.

**PS2.** Every grant must carry a recorded justification: who approved it, on what basis, tied to what business reason. Birthright access is defined by written policy, and everything outside birthright arrives through a request. A grant without a recorded reason cannot be certified, only guessed at.

**PS3.** The request path must define intake, an approval chain whose depth follows tier (chapter 4, P2), and a time bound per stage. Provisioning outside the path must be detected by reconciliation and either reversed or regularized through the path.

**PS4.** Certification must be a decision, and the certifier must see what the decision needs: what the entitlement does, when it was last used, and the justification on record. Bulk approval should be constrained, and where it is permitted it must be logged and reported as a campaign quality signal.

**PS5.** Revocation must be an executed outcome with a time bound and a verification step confirming removal in the target system. This applies equally to leaver events, certification denials, and policy violations.

**PS6.** Exceptions must be time-bounded, owned, and re-justified at expiry. An exception without an expiry is a standing grant with better paperwork.

**PS7.** Non-human identities must have lifecycle events equivalent to joiner, mover, and leaver: a creation gate that assigns an owner (chapter 2, O7), ownership transfer when the holder departs, credential rotation on a defined cycle, and a decommission step that retires the credential and verifies its dependants.

**PS8.** The lifecycle must be defined as a complete state model per identity population; joiner, mover, and leaver form the spine of the model rather than its whole. For workforce and external populations the recognized transitions include, at minimum: provisioning before start, leave of absence and return, rehire, conversion between populations, extension of an end-dated identity, and post-departure disposition covering disable, retention, and deletion. Each transition names its authoritative trigger and its owner. Departure carries distinct voluntary and involuntary paths, each with its own time bound. A return or rehire is re-baselined against current need rather than reactivated with historical access, and a conversion replaces the prior population's access profile instead of adding to it. Non-human populations recognize creation, ownership transfer, dormancy, and decommission (PS7).

**PS9.** Emergency access must be defined before it is needed: who may invoke it, for which systems, and through what mechanism. Every invocation is logged as it happens, expires automatically within a defined bound, and triggers a post-use review within a defined window (chapter 6, C3). An emergency grant that skips the log is side-door provisioning with a justification attached (F4).

*Example (non-normative). An analyst moving from finance to procurement triggers re-evaluation of every finance entitlement she holds. The grants without a current justification expire with the move instead of following her into the new role.*

## 5.3 Failure modes

**F1. Leaver lag.** Departures do not propagate. Observable signal: active accounts belonging to departed people found in target systems.

**F2. Mover accumulation.** Access accretes across role changes and nothing re-evaluates the old grants. Observable signal: long-tenure staff hold a multiple of the entitlements held by new hires in the same role.

**F3. Rubber-stamp certification.** Observable signal: approval rates approaching one hundred percent with per-item decision times measured in seconds.

**F4. Side-door provisioning.** Observable signal: reconciliation finds grants with no corresponding request record.

**F5. Zombie exceptions.** Observable signal: exceptions active past their expiry, or no exception register to check.

**F6. Revocation theatre.** The denial is recorded and the access persists. Observable signal: re-checks after certification find denied entitlements still live in target systems.

**F7. Rehire trap.** A returning identity is reactivated with the access of its previous tenure. Observable signal: rehires hold entitlements granted before their departure date, with no new justification on record.

**F8. Conversion accumulation.** A population conversion adds the new population's birthright while the old population's grants stay live. Observable signal: converted identities match two access profiles at once.

**F9. Suspended but live.** Leave of absence suspends employment while access stays active. Observable signal: authentications or active sessions during a recorded leave period.

## 5.4 Modulation

**By starting state.**

Greenfield: build the lifecycle spine first and the request path second. Certification can start manual and light at low volume, and automation follows demand rather than preceding it.

Bluefield: the seam is the risk. Two process regimes will exist during the rebuild, and the program must define which regime governs requests and events that span both estates, or the seam becomes the side door (see F4).

Brownfield: certification and revocation carry the remediation load first, run as cleanup waves under the mandate's time box, and request-path modernization follows. The accumulated risk sits in existing grants, and cleanup addresses it while intake redesign does not.

**By archetype.** A regulated enterprise runs segregation-of-duties checks inline in approval rather than after the fact. A small product organization may run single-approver chains on lower tiers, provided justifications are recorded. A public sector body operates under procedural law that lengthens its time bounds; the bounds must exist regardless. Detailed treatment belongs to the archetype profiles.

## 5.5 Instrumentation

Justification Half-Life is proposed for this layer. Status: proposed, pending empirical confirmation against pilot data, and this section carries no normative weight until that evidence exists.

Rationale for the proposal: PS2 creates the recorded reason for access, and certification (PS4) is where that reason is re-tested and either survives or expires. The decay of justifications over time reads as a process-layer phenomenon. Confirmation here is empirical rather than editorial: the mapping is confirmed when pilot data shows the metric moving in response to this layer's decisions, and the reference dataset on the roadmap is where that evidence comes from.

## 5.6 Companion artifacts

Lifecycle definition checklist (non-normative): `companions/iga-lifecycle-checklist.md`.

Certification campaign design checklist (non-normative): `companions/iga-certification-checklist.md`.

## 5.7 The wider process surface (non-normative)

The statements in this chapter govern the processes that carry access risk directly. A full program operates a wider surface, enumerated here so chapter scope is never mistaken for program scope. The families align with the publicly established IGA capability set. A granular, numbered taxonomy is on the roadmap as a community-derivable artifact.

| Family | Representative processes | Where the core touches it |
|---|---|---|
| Identity lifecycle | Joiner, mover, leaver; leave and return; rehire and conversion; contractor extension; non-human creation, transfer, decommission | PS1, PS7, PS8 |
| Access request and fulfilment | Intake and approval; provisioning to targets; emergency access grant and closure | PS3, PS9; C4 |
| Access review | Scheduled campaigns; event-triggered reviews; revocation follow-through | PS4, PS5; C1, C3 |
| Access model management | Role definition and refinement; birthright policy maintenance; entitlement catalogue and descriptions | PS2; S3 |
| Policy, SoD, and exceptions | Policy lifecycle; segregation-of-duties rule management and violation handling; exception grant, renewal, expiry | PS6; O4 |
| Application onboarding | Scope gate execution; connector and feed onboarding; owner and tier assignment at entry | S5; O5; P1 |
| Identity data quality | Authoritative source reconciliation; attribute completeness remediation; duplicate and correlation handling | S4 |
| Privileged access governance | Elevation request and expiry; privileged inventory; interface to PAM tooling | P4; C2 |
| Platform operation and change | Workflow and rule configuration; upgrades and releases; access to the governance platform itself | O2; chapter 2, F2 |
| Measurement and reporting | Metric computation; breach surfacing; reporting to the accountable body | Part III; C4 to C6 |

*Processes define the mechanics. The last layer sets their clocks.*

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
