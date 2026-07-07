# Scope

*Layer 3 of 6. Interrogative: what.*

![You are here: layer 3 of 6.](../figures/strip-03-scope.svg)

*Part of the Open IGA Operating Framework, operating core. v0.1 draft for public review. Language conventions (must, should, may) are defined in the repository README.*

## 3.1 Purpose

This layer bounds what the program governs, through three declarations: which identity populations, which resource classes, and at what entitlement granularity. It sits third because the owners defined in layer 2 make these declarations, and prioritization in layer 4 sequences inside the boundary this layer draws.

The granularity declaration carries more weight than it appears to. What the program chooses to see determines what it can govern, which is why the first metric attaches here (see 3.5).

The layer produces one required artifact: a versioned scope register with an onboarding gate.

## 3.2 Decisions

**S1.** Identity populations must be enumerated and each declared in or out of scope: workforce (employees and contractors), external (partners, vendors, suppliers), non-human (service accounts, API keys, workload identities, agents), and customer. Customer identity usually sits with a separate customer IAM discipline; the declaration must still be explicit. A population neither declared in nor declared out is a defect (see F5).

**S2.** Resource classes in scope must be enumerated, and each must name its authoritative inventory source. The register must be reproducible from the named inventories on request; a scope declaration over resources nobody can list is aspiration.

**S3.** Entitlement granularity must be set per resource class: account level, role or group level, or fine-grained entitlement level. The chosen level bounds what governance can see, and drift below the chosen level is invisible. High-risk resource classes should be governed at entitlement level.

**S4.** Each identity population must name its authoritative source: the HR system for employees, the vendor management system for contractors, a registry for non-human identities. Where sources conflict, a precedence rule must exist.

**S5.** Scope must be versioned, and systems must enter through a defined onboarding gate that assigns an owner (chapter 2, O5) and a tier (chapter 4, P1) at entry. Additions and removals are recorded with dates.

**S6.** Exclusions must be written down with a rationale and a revisit date. An exclusion nobody recorded is indistinguishable from an oversight.

**S7.** Every non-human credential class in use must be declared in or out. Where the population is unknown, the unknown itself is recorded as discovery debt with an owner and a time bound.

*Example (non-normative). Payroll and the ERP are governed at entitlement level while the marketing CMS sits at group level, with the decision recorded under S3. Customer identity is declared out and pointed at the CIAM program, so the declaration exists even though the population is excluded.*

## 3.3 Failure modes

**F1. Scope by connector.** The governed estate is whatever the platform happens to connect to. Observable signal: the scope register mirrors the tool's connector list, and critical systems without connectors appear in no register at all.

**F2. Granularity mismatch.** Governance runs at account level while risk lives at entitlement level. Observable signal: certifications approve that a person holds an account while entitlement growth inside the account goes unexamined.

**F3. Phantom inventory.** Scope names resource classes with no authoritative list behind them. Observable signal: nobody can produce the in-scope system list on request, or two requests produce two different lists.

**F4. Non-human blind spot.** Observable signal: the service account population is estimated rather than counted, and no registry exists.

**F5. Silent exclusion.** Observable signal: an audit or an incident surfaces a system everyone assumed someone else governed.

## 3.4 Modulation

**By starting state.**

Greenfield: scope grows with the estate. The onboarding gate (S5) costs little at low volume and prevents the debt other programs spend years discovering. Start narrow and entitlement-deep on the highest-value systems rather than broad and shallow.

Bluefield: one register with a regime tag per entry. The rebuilt estate onboards through the gate; the legacy estate is scoped as found, with its granularity debt recorded under S3 rather than hidden.

Brownfield: discovery precedes declaration, because in and out cannot be assigned to systems nobody has found. Scope v1 is the discovered estate, the unknown is recorded under S7, and discovery runs time-boxed under the remediation mandate (chapter 1).

**By archetype.** A regulated enterprise scopes financially material systems at entitlement granularity because its obligations demand demonstrable review at that level. A small product organization may hold scope to core SaaS and infrastructure at group level, with that granularity decision recorded. A public sector body often inherits its scope boundary from system accreditation. Detailed treatment belongs to the archetype profiles.

## 3.5 Instrumentation

Entitlement Drift Rate attaches to this layer, and the mapping is confirmed. Drift is the widening gap between access granted and access needed, and it reads at the resolution the S3 granularity decision sets: a program governing at account level cannot observe entitlement-level drift, and its measured rate will understate reality. Calculation method, measurement windows, and required data live in the metrics specification.

## 3.6 Companion artifacts

Scope register template, including population declarations (non-normative): `companions/iga-scope-register-template.md`.

*Scope draws the boundary. The next layer sequences what is inside it, because nothing gets governed all at once.*

---

*Open IGA Operating Framework, v0.1 draft. Licensed under CC BY 4.0.*
