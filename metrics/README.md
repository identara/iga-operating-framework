# Operational Metrics Specification

*Assembled from the published research: Ganesh, V., Measuring What Moves: A Dynamic Metrics Framework for Identity Governance Responsiveness (SSRN, DOI 10.2139/ssrn.6842545; published text v3.3 at identara.ca/papers/measuring-what-moves/). The paper is the source of record; this part transcribes its definitions into specification form. Drafted for review alongside the core.*

The four metrics measure governance responsiveness: whether the program keeps pace with the rate at which access states change. They complement rather than replace activity metrics such as certification completion, which measure whether governance work was performed. This part carries no benchmark thresholds, and none will be published before a reference dataset exists.

## Conventions

**MS1.** Every metric is computed over a declared measurement window, held constant across reporting cycles (core chapter 6, C5). Where a formula uses D, it is the number of days in the window.

**MS2.** Every reported figure states the scope and entitlement granularity it was computed over (core chapter 3, S3). A drift rate computed at account granularity understates entitlement-level reality, and the report must say which it is.

**MS3.** Human and non-human identities are reported as separate segments in addition to any combined figure. The two populations exhibit different dynamics, and a blended number hides the difference.

**MS4.** Every reported figure names the specification version and, for Entitlement Drift Rate, the variant (GEV, NED, or UED).

**MS5.** Targets and thresholds are the program's own. This specification defines how to measure, and the program decides what good looks like until published reference data exists.

## Entitlement Drift Rate (EDR)

Instruments the Scope layer (core section 3.5, confirmed).

**Definition.** The rate at which entitlements change across a governed population between governance checkpoints, decomposed into three complementary measures. A single net figure can obscure dangerous volatility: if 1,000 entitlements are granted and 950 removed within a cycle, net drift is 50 while the environment churned heavily.

| Variant | Formula | Purpose |
|---|---|---|
| Gross Entitlement Velocity (GEV) | `GEV = G / (I x D)` | Total access change activity; captures churn independent of direction |
| Net Entitlement Drift (NED) | `NED = (G - R) / (I x D)` | Directional accumulation; whether the environment is expanding or contracting |
| Unreviewed Entitlement Drift (UED) | `UED = U / (I x D)` | Governance debt; unreviewed accumulation |

Where G is total new entitlement grants in the window, R is total removals, U is new grants not yet reviewed or certified, I is the number of governed identities, and D is days in the window.

![Figure 6. One declared window: grants flow in, removals flow out, and unreviewed grants accumulate as governance debt.](../figures/fig-06-entitlement-drift.svg)

**MS6.** For UED, an entitlement is classified as unreviewed if it was granted after the completion of the most recent certification campaign for its scope and has not since been subject to a completed certification decision, an event-triggered review, or an automated policy-based access evaluation. Initial request approval does not count as review; approval establishes the entitlement, and review is the subsequent validation that it remains appropriate.

*Example (non-normative), from the source paper. A unit of 5,000 identities on a 90-day cadence issues 12,000 grants and removes 4,000; 8,000 grants are unreviewed at cycle end. GEV = 0.027, NED = 0.018, UED = 0.018 per identity per day, or roughly 1.6 unreviewed entitlements per identity entering each campaign.*

**Required data.** Entitlement grant and revocation timestamps and certification cycle dates, all typically available inside the IGA platform. **Limitations.** EDR weighs all entitlements equally; risk-weighted variants are future work. It requires reliable timestamps across connected applications.

## Governance Lag (GL)

Instruments the Cadence layer (core section 6.5, confirmed).

**Definition.** The elapsed time between the moment an access state becomes inappropriate and the moment the governance program detects it and initiates remediation.

`GL = T(detection) - T(inappropriateness)`

![Figure 3. Governance Lag is the risk window between the business event and detection; remediation speed sits outside it.](../figures/fig-03-governance-lag.svg)

T(detection) is the timestamp of the governance action (certification decision, automated flag, or manual review). T(inappropriateness) is the timestamp of the business event that rendered the access unwarranted. Existing metrics measure the speed of governance actions once initiated; GL captures the latency before governance begins, which is the true risk window. A program that revokes within two hours of detection but takes four months to detect carries a four-month lag.

**MS7.** T(inappropriateness) is anchored per scenario and the anchor used is recorded. Approximations, where no clean anchor exists, are documented as such.

| Scenario | Event anchor | Data source |
|---|---|---|
| Employee termination | Termination effective date | HR system |
| Role change (mover) | Role change effective date | HR system |
| Project-based access | Project end date or phase completion | Project management system |
| Temporary elevation | Approved expiration date | IGA platform or ticketing |
| Non-human identity | Last validated owner date, integration retirement date, or last usage date | IGA platform, CMDB, or SIEM |
| Vendor or contractor access | Contract end date | Procurement or vendor management |

**Reporting.** Program-level GL is reported as a weighted median across scenario categories, with the non-human segment reported separately per MS3. The source paper's worked sample shows a 74-day human median alongside a 211-day non-human figure, which is the machine-identity governance vacuum made visible. **Limitations.** GL requires correlating IGA data with HR, project, or CMDB data, and gradual reorganizations produce no single anchor date.

## Justification Half-Life (JHL)

Proposed for the Process layer (core section 5.5); the mapping carries no normative weight until confirmed.

**Definition.** The estimated duration before the business justification for an access grant of a given type loses half its original relevance, derived from a composite of governance and usage signals.

`JHL = T at which P(revocation or disuse) >= 0.5 for a given access category`

![Figure 4. Relevance decays at category-specific rates; the half-life is where each curve crosses one half.](../figures/fig-04-justification-half-life.svg)

P(revocation or disuse) is the cumulative probability that an entitlement in the category will be revoked at certification or become dormant by elapsed time T after approval. Justifications decay at different rates: access to a core ERP module decays slowly, and access to a project environment decays fast once the project ends.

**MS8.** Where usage telemetry exists, JHL must be estimated from multiple signals rather than certification outcomes alone, because rubber-stamped certifications understate real decay.

| Signal | Relevance |
|---|---|
| Certification revocation rate | Direct reviewer decisions, segmented by access type and time since approval |
| Entitlement usage decay | Access no longer exercised is access whose justification may have expired |
| Role or job change frequency | High mover rates shorten JHL for role-specific access |
| Project or contract end dates | Known expiry of the justifying business context |
| Peer-group deviation | Divergence from current-role peers signals the access may no longer fit |

**Application.** JHL makes certification cadence risk-proportionate: shorter cycles for short half-life categories, longer for stable ones, which concentrates reviewer attention where decay is fastest. **Limitations.** JHL is estimated rather than directly observed, and its precision depends on usage and project lifecycle data; without them it leans on revocation patterns with the acknowledged rubber-stamping distortion.

## Trust Gradient (TG)

Proposed for the Prioritization layer (core section 4.5); the mapping carries no normative weight until confirmed.

**Definition.** A composite, continuously updated confidence score estimating the degree to which a standing access grant is believed to remain appropriate, based on governance-layer signals.

`TG = f(w1 x TimeSinceValidation, w2 x UsageRecency, w3 x ContextStability, w4 x PeerAlignment)`

![Figure 5. Four weighted signals combine into a confidence score that prioritizes review attention.](../figures/fig-05-trust-gradient.svg)

The weights w1 through w4 are organization-specific, calibrated against historical certification outcomes. Certification currently refreshes trust to full confidence and measures nothing between events; TG models the reality that confidence degrades continuously as time passes, context shifts, and usage signals go quiet. It is vendor-neutral and portable by design, so two organizations on different platforms can compare governance confidence posture, which product-specific analytics cannot offer.

**MS9.** TG weights are calibrated against historical certification outcomes, documented, and recalibrated on a cycle, with the validation question recorded: does a low score predict revocation.

**MS10.** TG is a prioritization input for review attention. It is never used as an automated revocation decision.

**Application.** TG converts certification from a bulk periodic exercise into continuously prioritized attention, surfacing declining scores for early review. **Limitations.** The most complex metric in the set, with the highest implementation burden. Opaque weighting produces misleading confidence, which is what MS9 guards.

## Adoption order

Implementation complexity varies by metric, and the source paper recommends phased adoption:

| Phase | Metric | Data requirements |
|---|---|---|
| 1 | Entitlement Drift Rate, all three variants | IGA grant and revocation logs, certification cycle dates |
| 2 | Governance Lag | IGA data correlated with HR, project management, and CMDB data |
| 3 | Justification Half-Life | Historical certification outcomes, usage telemetry, project lifecycle data |
| 4 | Trust Gradient | Real-time composite scoring across sources, calibrated against outcomes |

Phase 1 requires only fields native to the IGA platform. Later phases add cross-system dependencies that raise complexity and precision together. The full minimum data model, field by field with source systems, is in the source paper, section 7.1.1.

## Conformance

**MS11.** A program, tool, or platform may claim conformance for a named subset of the four metrics. The claim requires that each named metric is computed per the definitions above, that the required data elements are recorded, that conventions MS1 through MS5 are followed, and that the claim states the specification version. Claim form: conforms to the Open IGA Operating Framework Operational Metrics Specification v0.1 for EDR and GL.

**MS12.** Every reported metric and telemetry indicator names who computes it and who acts on its movement. A figure without a named consumer is reporting; the mandate requires risk movement to reach someone accountable (chapter 1, M6; chapter 6, C6).

## Operational telemetry catalogue (non-normative)

Programs also track operational telemetry: point-in-time counts and event measures that evidence specific decisions and failure modes. Telemetry counts states; the four metrics above read responsiveness. A program reports both, alongside rather than in place of one another, and every telemetry figure follows the same discipline as the metrics: a declared window per MS1, scope and granularity stated per MS2, values and thresholds the program's own per MS5.

The catalogue is representative rather than exhaustive. The framework tie names the statement or failure-mode signal each indicator evidences, which is what separates a governance reading from a dashboard count.

#### Lifecycle hygiene

| Indicator | What it reads | Framework tie |
|---|---|---|
| Orphaned accounts | Accounts whose owner has left or cannot be identified | PR1, PR5; chapter 5, F1 |
| Leaver revocation breaches | Departures where removal exceeded the time bound | C4; chapter 5, F1 |
| Mean time to deprovision | Average elapsed time from departure to removal | C4 |
| Dormant accounts | Active accounts unused beyond the program's dormancy threshold | MS8 usage signal; chapter 5, F2 |
| Mover re-evaluations completed | Role changes whose existing access was re-evaluated | PR1; C3 |
| Lifecycle event coverage | Share of authoritative-source lifecycle events that triggered their defined transition within its bound | PR1, PR8; C3 |

#### Coverage and data quality

| Indicator | What it reads | Framework tie |
|---|---|---|
| Integrated application coverage | Share of in-scope systems feeding the platform | S2, S5; chapter 3, F1 |
| Attribute completeness | Identities with required attributes populated from authoritative sources | S4 |
| Uncorrelated accounts | Accounts not mapped to a human or non-human identity | S1, S7; chapter 3, F3 |
| External identities without end dates | Contractor or vendor identities lacking expiry | C2; S1 |

#### Certification quality

| Indicator | What it reads | Framework tie |
|---|---|---|
| Campaign completion rate | Reviews finished on time; an activity measure, read with M2 in mind | C1 |
| Bulk approval rate | Share of items approved in bulk | PR4; chapter 5, F3 |
| Median per-item decision time | Reviewer attention per entitlement | Chapter 5, F3 |
| Revocation follow-through | Denials verified removed in target systems | PR5; chapter 5, F6 |

#### Policy and exception

| Indicator | What it reads | Framework tie |
|---|---|---|
| Exceptions past expiry | Approved departures still active beyond their bound | PR6; chapter 5, F5 |
| Standing access without rationale | Expiry-default categories granted standing access with no recorded reason | C2 |
| Open segregation-of-duties violations | Unresolved toxic combinations | Chapter 1 guiding principles; PR3 |
| Side-door grants found | Provisioning discovered outside the request path | PR3; chapter 5, F4 |

#### Privileged and non-human

| Indicator | What it reads | Framework tie |
|---|---|---|
| Privileged identity count and growth | Size and trajectory of the highest-risk population | P4 |
| Non-human identities without owners | Non-human identities lacking an accountable human | O7; chapter 2, F5 |
| Credentials past rotation cycle | Non-human credentials older than their rotation bound | PR7 |
| Unknown non-human population | Estimated non-human identities outside the registry, recorded as discovery debt | S7; chapter 3, F4 |

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
