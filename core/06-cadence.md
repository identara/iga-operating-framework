# Cadence

*Layer 6 of 6. Interrogative: when.*

![You are here: layer 6 of 6.](../figures/strip-06-cadence.svg)

*Part of the Open IGA Operating Framework, operating core. v0.1 draft for public review. Language conventions (must, should, may) are defined in the repository README.*

## 6.1 Purpose

This layer sets the clock. Every object defined above carries an interval this layer assigns: how often certifications run, when access expires, how fast a decision must move, and what windows measurement computes over. It sits last because a cadence belongs to something, and the somethings are defined in layers 3 through 5.

The layer produces one required artifact: a cadence table. It is also where a program's responsiveness stops being a claim and becomes a reading, which is why the timing metric attaches here (see 6.5).

## 6.2 Decisions

**C1.** A cadence table must exist, setting certification frequency per tier from the intensity mapping in chapter 4 (P2). The framework requires that the table exist and that frequency scale with tier. The specific frequencies are the program's own, and any figures appearing in companion artifacts are illustrative rather than benchmarks.

**C2.** Time-bounded access should be the default for privileged access, exceptions, external identities, and non-human credentials, with renewal requiring re-justification. Where standing access is granted in these categories, the rationale is recorded.

**C3.** Event triggers must complement the calendar. A role change, a departure, a security incident, and an organizational change each trigger out-of-cycle review of the access they affect. A calendar-only program reviews on schedule and misses the moves that happen in between (see F1).

**C4.** Every governance decision type must carry a maximum duration: request approval, revocation execution, escalation resolution. Breaches of a bound must surface to the owner, and a pattern of breaches must surface to the accountable body.

**C5.** Measurement windows must be defined and held constant across reporting cycles. The window conventions specified in the metrics specification are adopted here, and a change to a window is versioned the way a change to scope is versioned.

**C6.** Reporting to the accountable body (chapter 1, M6) runs on a fixed cycle, and its content reports risk movement against the mandate rather than activity volume.

**C7.** The cadence table itself must be revisited on a cycle, at most annually, and on the same trigger events as tiering (chapter 4, P5).

**C8.** The program must test itself against this framework's failure modes on a defined cycle, at most annually, recording which observable signals were checked and what was found. A signal never looked for is a defect that has not yet been dated.

*Example (non-normative). A program sets tier 1 certification quarterly and tier 3 annually, and bounds leaver revocation at one business day. The framework supplied the rows; the organization supplied every number, recorded in its own cadence table.*

## 6.3 Failure modes

**F1. Calendar theatre.** Reviews run on schedule and nothing moves between them. Observable signal: access changes cluster at campaign dates rather than at the events that should have triggered them.

**F2. Uniform cadence.** Observable signal: the cadence table has one row, and tier plays no part in frequency.

**F3. Unbounded decisions.** No clock exists on approvals, revocations, or escalations. Observable signal: open items age without breach alerts, and completion times show a long tail nobody is watching.

**F4. Window drift.** Each report computes over a different period. Observable signal: quarter-over-quarter figures are not comparable, and definitions shift between reports.

## 6.4 Modulation

**By starting state.**

Greenfield: lean calendar, strong event triggers. At low volume, event-driven review is cheap, and the habit is worth building before scale makes the calendar necessary.

Bluefield: one cadence table with a regime column. The legacy estate typically carries the higher frequency as a compensating control while it awaits rebuild, and the rebuilt estate settles to its tier's steady rate.

Brownfield: remediation runs as a sprint overlay on the steady-state calendar: time-boxed cleanup waves per tier under the mandate's clock, converging to the steady cadence as tiers clear.

**By archetype.** A regulated enterprise often has cadence floors fixed by regulation for material systems, and its table records the regulatory floor and the program's own rate separately. A small product organization leans on event triggers over dense calendars. A public sector body reports on cycles fixed by its oversight bodies, which constrains C6 from outside. Detailed treatment belongs to the archetype profiles.

## 6.5 Instrumentation

Governance Lag attaches to this layer, and the mapping is confirmed. Lag is the elapsed time between an access state becoming inappropriate and the program detecting it, and the clocks this layer sets are what bound it: certification frequency (C1) caps how long an inappropriate state can wait for a scheduled look, and event triggers (C3) exist to collapse the wait entirely. Speed after detection is a different quantity, bounded by C4 and read through operational telemetry such as mean time to deprovision, and the two are never blended.

This layer also hosts C5, the window conventions all four metrics compute over, so cadence is both an instrumented layer and the home of the program's measurement discipline. Calculation method and required data live in the metrics specification.

## 6.6 Companion artifacts

Cadence table template (non-normative): `companions/iga-cadence-table-template.md`.

*The core is complete. The Operational Metrics Specification (`../metrics/`) defines how to measure whether it responds.*

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
