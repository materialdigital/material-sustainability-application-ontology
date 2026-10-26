# MKB2 — Proposed conditional scientific closure

Date prepared: 2026-10-23

Decision state: **PROPOSED — HUMAN APPROVAL REQUIRED**

Authoritative baseline: main at 845546e2b88a0fc6c0465377f74a10c26a68ae85

Merged content commit: 494306044991d8682dca5feb8b20eb8824ba1a37

## Purpose and boundary

This record consolidates MKB2 scientific decisions and implementation status for
revised SRC-005–010, relevant MKB1 carryovers, and the later life cycle costing
(LCC) and ENVO waste-role increments.

It is a proposal. It does not approve recommendations, reopen approved decisions or
authorize ontology changes. The six items below remain at the human decision gate.
Scientific closure is separate from PoC/ABox/SHACL work, CI maintenance, generated
artifact publication and release work. Closure means findings are reconciled and
assigned a controlled status, not that every deferred pattern is implemented.

## Evidence and statuses

Evidence comprised authoritative ontology source, PMDco v3.1.2, integrated LOG,
CEON and DPPO components, PR history, the tracked 2026-10-19 handoff, MKB1 closure
history, and all nine untracked MKB2 audit records present on 2026-10-23.

Merged increments are PR #9 (MKB1), #11 (assessment), #13 (LCA/end-of-use), #18/#19
(material efficiency/CRM), #21 (LCC), and #22 (PMDco v3.1.2/ENVO waste).

| Status | Meaning |
|---|---|
| **IMPLEMENTED** | Approved MatSus content is present in authoritative source. |
| **REUSED** | Existing MatSus or imported content covers the requirement. |
| **REJECTED FOR BATCH** | Explicitly excluded from the approved batch, not necessarily permanently rejected. |
| **DEFERRED** | Intentionally postponed and not required for conditional closure. |
| **UNRESOLVED** | A human decision or external dependency remains open. |
| **INSUFFICIENTLY EVIDENCED** | Durable evidence is inadequate to claim a verified decision or reuse. |

Detailed final SRC-008, SRC-009 and SRC-010 source-gate reports are not tracked.
Implemented outcomes are verifiable, but complete source-corpus closure remains
insufficiently evidenced until suitable reports are accepted or archived.

## Revised numbering and historical aliases

| Revised | Governing meaning | Historical allocation |
|---|---|---|
| SRC-005 | SSbD Core; assessment architecture | Original SRC-005 was JRC material efficiency. |
| SRC-006 | CLEO; LCA and results | Original SRC-006 was RMIS. |
| SRC-007 | JRC material efficiency/ecodesign | Original SRC-007 was official SSbD. |
| SRC-008 | JRC RMIS; CRM/resource security | Earlier SRC-008 meant literature and, temporarily, end-of-use/waste. |
| SRC-009 | Official EC/JRC SSbD | Original SRC-009 combined SSbD Core and CLEO. |
| SRC-010 | Li, Kurteva, Raabe, and Allwood and Raabe | Previously SRC-008a–d. |

September end-of-use/waste work is a cross-cutting increment, not revised SRC-008.
Historical labels remain chronology evidence, not current source identifiers.

## Consolidated register

### SRC-005 — SSbD Core

| Item | Status | Reconciliation |
|---|---|---|
| Assessment process, safety/sustainability branches, specifications and results | **IMPLEMENTED** | MATSUS_0000043–0000059; material sustainability assessment uses the approved architecture. |
| evaluates; has indicator specification | **IMPLEMENTED** | MATSUS_0000060–0000061. |
| SSbD Core correspondence annotations | **IMPLEMENTED** | MatSus contains annotation-only, non-entailing mapping assertions. This is not an import or reuse of SSbD Core OWL semantics. |
| Generic assessment/specification governance relation | **DEFERRED** | No method-specific workaround approved. |

### SRC-006 — CLEO and LCA

| Item | Status | Reconciliation |
|---|---|---|
| LCA, LCI, LCIA, specification, functional unit, reference flow, boundary, model, impact category and results | **IMPLEMENTED** | Includes carbon-footprint result and climate-change/GWP100 references. |
| CLEO correspondence annotations | **IMPLEMENTED** | MatSus contains annotation-only, non-entailing correspondence assertions informed by CLEO. This is not an import or reuse of CLEO OWL semantics. |
| Generic reference unit, dedicated LCA report, lifecycle-stage taxonomy and CLEO CO2 disposition | **REJECTED FOR BATCH** | Not justified for the approved batch. |
| Generic lifecycle contribution and SHACL profile | **DEFERRED** | Existing contribution modelling remains marked for review. |

### SRC-007 — material efficiency

| Item | Status | Reconciliation |
|---|---|---|
| Durability and recycled-content datum | **IMPLEMENTED** | MATSUS_0000080–0000081. |
| Relationship between MATSUS_0000081 and RecycledContentInformation | **DEFERRED** | MATSUS_0000081 is a generic data item; RecycledContentInformation is a battery-specific DPP indicator result. No subclass, equivalence or mapping relation is approved. |
| Repairability, maintainability, reusability and remanufacturability | **IMPLEMENTED** | MATSUS_0000084–0000087; remanufacturing definition also revised. |
| Expected lifetime and actual service life | **IMPLEMENTED** | MATSUS_0000088–0000089. |
| Refurbishability disposition | **DEFERRED** | Retained but not implemented; distinct from refurbishment process. |
| Upgradability | **REJECTED FOR BATCH** | Explicitly excluded. |
| Reliability | **REUSED** | Existing metric-specification/result architecture covers the current need. |
| Guaranteed lifetime, warranty and performance-class assignment | **DEFERRED** | Partial DPPO reuse; no generic profile approved. |

### SRC-008 — RMIS

| Item | Status | Reconciliation |
|---|---|---|
| Critical raw material role and designation | **IMPLEMENTED** | MATSUS_0000082–0000083; designation information is distinct from the contextual role. |
| Criticality methods, metrics, thresholds and legal mappings | **DEFERRED** | Require specifications, results and mappings, not more core classes. |
| Primary, virgin and secondary anchors | **REUSED** | Existing classes cover categories; their precise relation is unresolved. |
| Material flow and time-dependent stock | **DEFERRED** | LOG inventory and PMDco mass-flow rate are not a complete dynamic pattern. |
| Complete RMIS provenance | **INSUFFICIENTLY EVIDENCED** | Implemented classes are verifiable; no durable final report was found. |

### SRC-009 — official SSbD

| Item | Status | Reconciliation |
|---|---|---|
| Carbon-footprint result | **REUSED** | MATSUS_0000076 covers the need. |
| Integrated SSbD profile | **DEFERRED** | No monolithic SSbD hierarchy authorized. |
| Substance of concern | **UNRESOLVED** | Scope, bearer, context and reuse choice require decision. |
| Complete source-gate provenance | **INSUFFICIENTLY EVIDENCED** | No durable final SRC-009 report found. |

### SRC-010 — surveys and materials science

Sources: Li et al. (2023), DOI 10.1145/3543873.3587613; Kurteva et al. (2024),
DOI 10.3233/SW-243586; Raabe (2023), DOI 10.1021/acs.chemrev.2c00799; Allwood
and Raabe (2024), DOI 10.1098/rsta.2023.0247.

| Item | Status | Reconciliation |
|---|---|---|
| PMDco materials/composition, LOG traceability, CEON processes, DPPO composition and MatSus assessments | **REUSED** | Verified anchors, not complete dynamic relationships. |
| Other ontologies named in surveys | **INSUFFICIENTLY EVIDENCED** | No durable register preserves definitions, axioms, versions and dependencies. |
| Quality degradation/impurity accumulation | **DEFERRED** | No approved time-indexed change profile. |
| Recycling yield/loss and mass balance | **DEFERRED** | Inputs, outputs and results exist; calculation profile is unimplemented. |
| Composition-to-performance relation | **DEFERRED** | No approved evidence/causal pattern connects endpoints. |
| Primary/secondary provenance and availability | **DEFERRED** | Existing anchors are partial. |
| Recycling/durability/efficiency/carbon/cost trade-offs | **DEFERRED** | Existing results need an integrated comparison profile. |
| Separate recyclate class | **INSUFFICIENTLY EVIDENCED** | Existing recycled, recovered and secondary classes may cover it. |

## Independent increments

### LCC

| Item | Status | Reconciliation |
|---|---|---|
| LCC assessment, specification and cost result | **IMPLEMENTED** | MATSUS_0000090–0000092. LCC is distinct from environmental LCA and not universally economic sustainability assessment. |
| Currency, discounting, boundaries, comparison profile and LCA–LCC integration | **DEFERRED** | Retained for generic information/profile modelling. |

### PMDco v3.1.2 and ENVO waste

| Item | Status | Reconciliation |
|---|---|---|
| PMDco v3.1.2 and ENVO_01000665 | **REUSED** | Pin d8a4677f250d0ea3d3529752b636ff8b8a2407ed; no duplicate ENVO import. |
| MATSUS_0000007 | **IMPLEMENTED** | Deprecated historical IRI; active logic removed and no mapping asserted. |
| MATSUS_0000008 | **IMPLEMENTED** | BFO material entity with has role some ENVO_01000665. |
| Five waste subtypes and waste generation | **IMPLEMENTED** | Identifiers and process structure retained. |
| Waste-role acquisition/loss | **DEFERRED** | No temporal transition pattern introduced. |
| PMDco/ENVO portion-of-matter constraint | **REUSED** | Imported PMDco/ENVO axioms make a PMD_0000001 portion of matter bearing ENVO_01000665 inconsistent. This is an active imported logical constraint, not a rejected MatSus modelling candidate. |

## MKB1 carryovers

| Item | Status | Reconciliation |
|---|---|---|
| Feedstock role | **UNRESOLVED** | PMDco #486 remains an external dependency. |
| Product specification | **UNRESOLVED** | PMDco #487 was withdrawn and redirected to possible MatSus modelling. |
| Design/circular-design specifications | **UNRESOLVED** | PMDco #488 was withdrawn and redirected to MatSus reassessment. |
| interacts with | **REUSED** | PMDco v3.1.2 imports RO_0002434. |
| Generic interaction-process class | **REJECTED FOR BATCH** | PMDco #498 used relation reuse, not the proposed class. |
| Aggregate system-history description | **REJECTED FOR BATCH** | PMDco #497 was withdrawn; no aggregate-record CQ established. |
| Reverse logistics, recovery history, sorting linkage, suitability, provenance, thresholds and profiles | **DEFERRED** | Non-blocking architecture/PoC work. |
| E-waste, food waste, pollution and absolute decoupling | **DEFERRED** | No later gate approved implementation. |

The precise historical evidence is
audit/MatSus_MKB2_LCA_Product_Design_Implementation_Batch_Handoff_2026-09-19.md:
its status says “implementation authorized,” section 2 says to implement Product
Specification, section 3 says to implement Design Specification, and section 4
records the approved Circular Design Specification hierarchy. PR #13 did not
implement those classes. The later withdrawal of PMDco #487/#488 and redirection to
MatSus do not silently cancel the September approval, but neither this closure
proposal nor the absence of implementation establishes that the old authorization
remains operative now. Current implementation authority therefore requires human
confirmation; the register status remains UNRESOLVED rather than rejected.

## Six unresolved human decisions

Every disposition is a recommendation only and is not approved.

| No. | Decision | Recommended disposition — not approved |
|---:|---|---|
| 1 | Product, design and circular-design specifications after #487/#488 | Confirm explicitly whether the 2026-09-19 MatSus authorization remains operative after the later PMDco withdrawals. If reaffirmed, evaluate primitive local classes under PMD_0095001, reuse LOG material product and add no unsupported equivalence. |
| 2 | Evidence required to close SRC-008–010 | Archive dated source-gate reports, or explicitly approve identified records as sufficient. Do not infer source closure from implementation. |
| 3 | Durability alignment to PMD_0080133 | Keep scopes separate; reconsider only with competency questions supporting a safe relation. |
| 4 | Substance-of-concern modelling | Establish regulatory scope, bearer, contextual designation and queries before selecting reuse or a class. |
| 5 | Primary versus virgin material relation | Keep classes separate until route examples establish a stable relation. |
| 6 | Next dynamic science profile | Treat degradation/impurity, yield/loss, provenance and stocks as a separate CQ-led PoC; do not block closure. |

PMDco #486 and the LOG product-role label remain dependencies, not additional
closure decisions.

## Proposed annotation and historical-record corrections

These require a separate reviewed annotation-only patch. No logical axiom should
change.

1. MATSUS_0000009–MATSUS_0000026 notes still call PMDco #485 ISSUE_SUBMITTED and
   migration future work. Preserve class-specific cautions, but replace that
   boilerplate with current PMDco v3.1.2/ENVO_01000665 status.
2. MATSUS_0000080 describes PMDco durability as provisionally unclassified. Replace
   that claim with its current narrower wear-, tear- and damage-resistance scope.
   Retain the no-mapping decision.
3. Add exact RMIS/JRC and applicable legal-source provenance to the CRM role and
   designation classes MATSUS_0000082–MATSUS_0000083 only after the SRC-008 evidence
   is accepted. Preserve existing human-decision provenance.
4. Add exact JRC material-efficiency/ecodesign provenance to the capability and
   lifetime classes MATSUS_0000084–MATSUS_0000089 only after the SRC-007 evidence is
   accepted. Preserve existing human-decision provenance.

Keep docs/decisions/MKB2_SRC007-008_Handoff_2026-10-19.md as historical evidence.
Do not rewrite its decisions or validation. A future documentation patch may add a
notice that waste item 1 was superseded by PR #22, PMDco is v3.1.2,
MATSUS_0000007 is deprecated, MATSUS_0000008 was migrated, and five subtypes were
retained. Other deferred items remain historical unless explicitly superseded.

Keep the LCA/product-design handoff unchanged. This record documents that its three
specification classes were not implemented and now require decision 1.

## Proposed evidence curation

Proposed location:

    docs/decisions/mkb2/
      README.md
      evidence/

The index should record date, revised SRC, historical aliases, decision authority
and supersession state. Recommended first-pass set, subject to approval:

1. MKB2_SRC005_SRC006_Assessment_Decision_Handoff.md
2. MKB2_LCA_Implementation_Specification_v2_2026-09-19.md
3. MatSus_MKB2_End_of_Use_Process_Architecture_Final_Report_2026-09-20.md
4. MatSus_MKB2_LCA_Product_Design_Implementation_Batch_Handoff_2026-09-19.md
5. MatSus_MKB2_Next_Stage_Decisions_Addendum_2026-09-19.md

Do not copy all nine automatically. Review duplication, stale branch state,
licensing and historical numbering. Preserve original text; record corrections in
index metadata or companion notes.

Add the SSbD Core PDF only after distribution status and provenance are confirmed.
The assessment implementation specification, LOG handoff and things-not-to-lose
handoff may remain externally archived if the selected set preserves their unique
decisions.

## Conditional closure recommendation

Recommended, but not approved:

1. Accept this register as the final conditional MKB2 scientific status record.
2. Close implemented/reused findings without treating deferred PoC/profile work as
   missing class implementation.
3. Carry the six decisions and dependencies into the next backlog.
4. Require durable SRC-008–010 provenance before claiming fully auditable closure.
5. Keep CI, generated artifacts and release publication outside this closure.

Approval does not authorize ontology, workflow, import, generated-artifact or
release changes.
