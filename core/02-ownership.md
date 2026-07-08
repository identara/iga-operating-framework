# Ownership

*Layer 2 of 6. Interrogative: who.*

![You are here: layer 2 of 6.](../figures/strip-02-ownership.svg)

*Part of the Open IGA Operating Framework, operating core. v0.1 draft for public review. Language conventions (must, should, may) are defined in the repository README.*

## 2.1 Purpose

This layer distributes the authority the mandate creates into named roles, decision rights, and escalation routes. It sits second because every layer below consumes its output: scope declarations need a decider, tiers need an owner, and processes need approvers. The charter says the program can compel; this layer says who compels, who executes, and who checks.

The layer produces two required artifacts: a decision-rights register and a responsibility matrix covering the program's processes.

## 2.2 Decisions

**O1.** Every class of access decision must have a named owner, and ownership of access to business resources must sit with the business. Decision classes at minimum: access policy (who may hold what), individual approvals, certification outcomes, exceptions, and revocation. Where business ownership is unassigned, approval defaults to IT, and IT cannot judge business need (see F1).

**O2.** The program must separate three functions: build (implementing the platform and integrations), run (operating the processes), and govern (setting policy and certifying outcomes). In organizations too small to staff them separately, each overlap must be recorded as an accepted risk with a named accepter. The operator of a control should not certify that control.

**O3.** Every decision class must have an escalation route with a named tie-breaker and a time bound. Conflicts between a resource owner and the program escalate to the authority the charter names (chapter 1, M6 and M7).

**O4.** A responsibility matrix must exist covering, at minimum, the lifecycle processes, access request and approval, certification, exception handling, and policy change. It must be versioned and published where the people it names can find it.

**O5.** Owners must be defined as roles and filled by named people. A role with an empty seat is a defect: when an owner departs, reassignment must happen within a defined bound, and decisions pending under a vacant role must be visible rather than silently queued.

**O6.** Owners may delegate approval authority. Delegation must be recorded, time-bounded, and revocable, and the delegator retains accountability for the outcome.

**O7.** Every non-human identity must have an accountable human owner. Service accounts, API keys, workload identities, and agents each map to a named role, and ownership transfers when the holder departs (lifecycle mechanics in chapter 5, PS7).

**O8.** The program must name its interfaces: the functions it depends on and the handoff each carries. At minimum: HR as the authoritative source of lifecycle events (chapter 5, PS1 and PS8), the service desk for intake and fulfilment handoffs (PS3), application and resource teams for onboarding and revocation execution (S5, PS5), procurement or vendor management for external identity end dates (C2), and security operations for event triggers and usage signals (C3). Each interface names a counterpart owner on both sides and the time bound its handoff carries.

*Example (non-normative). The finance ERP carries its access policy A with the VP Finance rather than with IT. The platform team holds R on provisioning and, under O2, cannot certify the ERP access it provisions; disputes route to the risk committee the charter names.*

## 2.3 Failure modes

**F1. IT by default.** Business ownership was never assigned, so IT approves everything because requests have to go somewhere. Observable signal: approval logs show the same small set of IT approvers across unrelated business systems.

**F2. Self-certification.** Build, run, and govern have collapsed into one team, and the people operating access certify their own operation. Observable signal: the identity platform team appears as both provisioner and certifier for the same systems.

**F3. Escalation vacuum.** Conflicts have no route, so they die in email threads. Observable signal: disputed access has no recorded resolution, and the access stays in whatever state the dispute found it.

**F4. Orphaned ownership.** A reorganization moved the people and nobody moved the roles. Observable signal: approval queues assigned to departed employees, or a matrix naming teams that no longer exist.

**F5. Unowned non-human identities.** Observable signal: service accounts whose creator has left, with no owner of record and nobody able to say what breaks if the credential is revoked.

## 2.4 Modulation

**By starting state.**

Greenfield: the ownership map is built lean and role-first, and owners are assigned as systems enter through the scope gate (chapter 3, S5). The discipline to establish early: no system onboards without an owner.

Bluefield: the seam needs an owner. The dual mandate (chapter 1) means someone owns access decisions in the legacy estate, someone owns them in the rebuilt estate, and someone owns the transition between them, and these may be three different people.

Brownfield: assignment begins with archaeology. De facto owners already exist in approval habits and tribal knowledge; the program should surface them before formalizing or replacing them. Where scale demands it, the remediation mandate carries an owner distinct from steady-state operation.

**By archetype.** A regulated enterprise separates build, run, and govern into different reporting lines and vests governance in a committee. A small product organization accepts role overlaps under O2's recording rule and keeps escalation short, often ending at the CTO. A public sector body inherits ownership from statute and its delegation rules from administrative law, which constrains O6. Detailed treatment belongs to the archetype profiles.

## 2.5 Instrumentation

No metric in the metrics specification attaches to this layer in v0.1, and none is proposed. Ownership defects surface downstream: drift climbs where owners rubber-stamp, and lag lengthens where escalation has no route, but those readings attribute to this layer rather than measure it. The health check is qualitative: every decision class has a current named owner, no seat sits vacant past its reassignment bound, and the escalation route has been exercised at least once.

## 2.6 Companion artifacts

Decision-rights and responsibility matrix starter (non-normative): `companions/iga-raci-starter-template.md`.

*With owners named, the next declaration is what they govern: the scope boundary.*

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
