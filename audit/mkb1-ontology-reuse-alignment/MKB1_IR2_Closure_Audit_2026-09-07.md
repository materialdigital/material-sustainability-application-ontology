# MKB1 IR2 Closure Audit

**Date:** 2026-09-07

**Branch:** `mkb1-ir2-closure`

**Starting main:** `acfe2c58d43ddd583ca5ebe7247f03266e566f17`

**Mode:** Read-only assessment of all existing repository evidence; this report is the only authorized repository change.

## 1. Executive conclusion

The bounded Batch 1-3 MKB1 implementation is internally complete and technically reconcilable: 39 local classes were introduced in three validated batches, increasing the locally defined MatSus class count from 13 to 52. Every one of the 128 reviewed records receives a current closure status in this report, and no tracker row falsely claims an IRI that is absent from the ontology.

The bounded MKB1 IR2 integration is complete and ready for closure. Remaining external-issue and architecture-dependent items are documented follow-up work and are not MKB1 closure blockers.

MaterialFlowProcess is required future MatSus/LOG architecture work, but it is outside the bounded MKB1 implementation scope and does not block MKB1 closure. Its boundary against LOG transport, material-location-change, and logistics processes requires concrete competency examples, review of the improved LOG process architecture, and team discussion after MatSus public migration. TextileMaterialFlowProcess remains deferred with its generic parent.

Public migration has one separate hierarchy-quality dependency: the PMDco 3.1.0 artifact packages `qudt:QuantityValue` and `qudt:Unit` without the named parents and restrictions present in authoritative QUDT 2.1. MatSus reproduces that upstream omission exactly. It should be resolved or explicitly accepted in PMDco/import governance before public migration; unsupported local bridge axioms must not be added. The CEON `Event` display is not a MatSus defect.

The open PMDco issues #485-#488, the pending LOG reverse-logistics handoff, and the remaining modelling/LCA/SHACL backlog are documented future work. They do not, by themselves, block closure of the bounded MKB1 implementation.

## 2. Repository gate

All gates passed before this branch and report were created.

| Check | Result |
|---|---|
| Active starting branch | `main` |
| Local `main` | `acfe2c58d43ddd583ca5ebe7247f03266e566f17` |
| `origin/main` | `acfe2c58d43ddd583ca5ebe7247f03266e566f17` |
| Upstream | `main` tracked `origin/main` |
| Tracked/staged changes | 0 |
| Existing untracked status entries | 32; left untouched |
| Batch 1 commit | `2a4a5c0` is an ancestor of `main` |
| Batch 2 commit | `1bd0111` is an ancestor of `main` |
| Batch 3 commit | `c69b98d30ff84d0d6552c819ef400221dc685660` is an ancestor of `main` |
| Numeric local classes | `MATSUS_0000000`-`MATSUS_0000039` all present exactly once as classes in the assembled graph |
| Current local MatSus classes | 52 |

`MATSUS_0000000` is declared in `components/matsus-ceon.ttl`; `MATSUS_0000001`-`MATSUS_0000039` are declared in `matsus-edit.owl`. This module split explains why counting only numeric declarations in the edit file gives 39 rather than 40. The assembled `matsus.ttl` graph contains all 40 numeric classes plus 12 pre-MKB1 named local classes.

## 3. Original recommendation totals

The `Master Analysis` sheet contains exactly 128 data records. The requested original recommendation strata are verified:

| Original recommendation | Records |
|---|---:|
| `ALIGN_EXISTING` | 48 |
| `ALREADY_COVERED_NO_ACTION` | 3 |
| `CONSIDER_LOCAL_MATSUS_TERM` | 35 |
| `REUSE_EXTERNAL` | 8 |
| `NEEDS_MODELLING_DISCUSSION` | 14 |
| `MODELLING_PATTERN_ONLY` | 12 |
| `DEFER` | 7 |
| `DATA_SHACL_ONLY` | 1 |
| **Total** | **128** |

The completed workbook refines the 35 local-candidate records into `IMPLEMENT_LOCAL_MATSUS_TERM` (14), `ALIGN_TO_LOCAL_CANONICAL` (5), `IMPLEMENT_LOCAL_MATSUS_PATTERN` (5), `REFORMULATE_TO_SPECIFICATION_AND_IMPLEMENT` (1), `REFORMULATE_TO_PROCESS_AND_IMPLEMENT` (3), `DEFER_TO_PMDCO` (1), `DEFER_TO_LOG` (1), and `DEFER_MODELLING_USE_CASE` (5). These refinements sum to 35 and do not alter the original total.

## 4. Verified before/after class counts

The checked-in generated ontology at pre-Batch-1 commit `d9ea1ad` contains 13 class IRIs in the MatSus namespace. The current generated ontology contains 52. The difference is exactly 39.

| State | Local classes |
|---|---:|
| Pre-MKB1 (`d9ea1ad:src/ontology/matsus.ttl`) | 13 |
| Batch 1 addition | +6 |
| Batch 2 addition | +20 |
| Batch 3 addition | +13 |
| Current (`acfe2c5:src/ontology/matsus.ttl`) | **52** |

The 13-class baseline comprises `MATSUS_0000000` and 12 named MatSus classes. The count is based on distinct MatSus IRIs typed `owl:Class`, not on labels or source-file line counts.

## 5. Mapping of the 39 implemented classes

Source-record count and class count are intentionally different. Some records expand into process/specification pairs, some require supporting parent classes, and the refill and decoupling source pairs are consolidated.

| Batch | IRI | Label | Source record or refinement |
|---:|---|---|---|
| 1 | `MATSUS_0000001` | recovered material | Supporting anchor for `MKB-000175` |
| 1 | `MATSUS_0000002` | recycled material | `MKB-000175` |
| 1 | `MATSUS_0000003` | secondary material | `MKB-000223` |
| 1 | `MATSUS_0000004` | material sustainability assessment | Supporting anchor for `MKB-000180` |
| 1 | `MATSUS_0000005` | resource-input reduction assessment | `MKB-000180-ASS` refinement |
| 1 | `MATSUS_0000006` | resource-input reduction objective specification | `MKB-000180-OBJ` refinement |
| 2 | `MATSUS_0000007` | waste role | Supporting waste anchor; PMDco #485 |
| 2 | `MATSUS_0000008` | waste material | `MKB-000141` plus supporting waste anchor; PMDco #485 |
| 2 | `MATSUS_0000009` | construction and demolition waste | `MKB-000063` |
| 2 | `MATSUS_0000010` | mineral waste | `MKB-000144` |
| 2 | `MATSUS_0000011` | municipal waste | `MKB-000148` |
| 2 | `MATSUS_0000012` | packaging waste | `MKB-000155` |
| 2 | `MATSUS_0000013` | textile waste | `MKB-000249` |
| 2 | `MATSUS_0000014` | collection system | `MKB-000059` |
| 2 | `MATSUS_0000015` | waste collection process | Supporting Batch 2 process |
| 2 | `MATSUS_0000016` | sorting process | `MKB-000231` process half |
| 2 | `MATSUS_0000017` | sorting method specification | `MKB-000231` specification half |
| 2 | `MATSUS_0000018` | waste separation process | Supporting specialization of sorting process |
| 2 | `MATSUS_0000019` | waste generation process | `MKB-000263` |
| 2 | `MATSUS_0000020` | waste prevention process | `MKB-000264` process half |
| 2 | `MATSUS_0000021` | waste prevention measure specification | `MKB-000264` specification half |
| 2 | `MATSUS_0000022` | zero-waste objective specification | `MKB-000266` objective half |
| 2 | `MATSUS_0000023` | zero-waste strategy specification | `MKB-000266` strategy half |
| 2 | `MATSUS_0000024` | waste elimination objective specification | `MKB-000085` |
| 2 | `MATSUS_0000025` | waste analysis | Supporting parent for `MKB-000236` |
| 2 | `MATSUS_0000026` | structural waste analysis | `MKB-000236` |
| 3 | `MATSUS_0000027` | metric specification | `ADD-SCO-012` |
| 3 | `MATSUS_0000028` | resource efficiency datum | `MKB-000205` |
| 3 | `MATSUS_0000029` | material resource efficiency datum | `MKB-000137` |
| 3 | `MATSUS_0000030` | virgin material | Positive refinement of `MKB-000150`; also covers `MKB-000261` |
| 3 | `MATSUS_0000031` | repurposing process | `MKB-000202` |
| 3 | `MATSUS_0000032` | battery repurposing process | `MKB-000009` |
| 3 | `MATSUS_0000033` | resource-input reduction process | `MKB-000180` |
| 3 | `MATSUS_0000034` | refill process | Consolidates `MKB-000181` and `MKB-000182` |
| 3 | `MATSUS_0000035` | refusal process | `MKB-000184` |
| 3 | `MATSUS_0000036` | remanufacturing process | `MKB-000189` |
| 3 | `MATSUS_0000037` | decoupling datum | Consolidates `MKB-000002` and `MKB-000069` |
| 3 | `MATSUS_0000038` | modularity | `MKB-000146` |
| 3 | `MATSUS_0000039` | refusal strategy specification | Human-gate refinement from `MKB-000184` |

## 6. Current reconciliation totals

| Closure status | Records | Interpretation |
|---|---:|---|
| `IMPLEMENTED_LOCAL` | 29 | Record is represented by one or more approved local classes, including an approved substitute or supporting local anchor. |
| `REUSED_EXTERNAL` | 0 | No original external candidate IRI is currently present in the resolved MatSus graph. |
| `COVERED_OR_ALIGNED_EXISTING` | 48 | Existing PMDco/LOG/DPPO/CEON/MatSus coverage or approved alignment closes the record without a new class. |
| `EXTERNAL_ISSUE_DEPENDENT` | 4 | Await PMDco or LOG governance; no MatSus duplicate is authorized. |
| `DEFERRED_MODELLING` | 31 | A later competency query, category decision, or dependency review is required. |
| `FUTURE_PATTERN_OR_SHACL` | 15 | Explicit modelling-pattern, LCA-architecture, or SHACL/profile work. |
| `DEFERRED_ARCHITECTURE_NOT_A_CLOSURE_BLOCKER` | 1 | `MKB-000128 Material flow`; required future MatSus/LOG architecture outside the bounded MKB1 scope. |
| **Total** | **128** | Complete reconciliation. |

No record is silently omitted. `MKB-000150` is classified `IMPLEMENTED_LOCAL` because the approved positive response was to implement VirginMaterial while expressly declining a NonVirginMaterial complement; the non-virgin composition/proportion pattern remains deferred. `MKB-000261` is covered by that same class. `MKB-000175`, `MKB-000223`, and `MKB-000141` were superseded by approved local implementations after their earlier alignment/reuse recommendations.

## 7. Eight external-reuse candidates

All eight candidate IRIs were tested against the current generated/resolved graph; none occurs as a subject and none is typed `owl:Class` there.

| Record / candidate | Current assessment | Closure status | Migration blocker? |
|---|---|---|---|
| `ADD-BON-008` Functional Unit | Candidate is from an ISO-oriented research LCA ontology with no tagged release in the recorded review. It remains useful evidence, but Functional Unit must be handled with Reference Unit and Reference Flow in the future LCA architecture. | `FUTURE_PATTERN_OR_SHACL` | No |
| `ADD-SCO-002` interaction | SCO-B term remains a plausible selective reuse candidate for mutual influence, not ordinary co-participation. SCO is not imported and its selected dependency closure has not been approved. | `DEFERRED_MODELLING` | No |
| `ADD-SCO-004` system history | SCO-B term is potentially useful for lifecycle/provenance queries, but no approved competency query currently requires its closure. | `DEFERRED_MODELLING` | No |
| `ADD-SCO-008` perspective information content entity | SCO-B usefully distinguishes perspective from information about it, but its complex-system/environment dependencies remain a boundary decision. | `DEFERRED_MODELLING` | No |
| `MKB-000084` electronic waste | MeSH `D059029` is authoritative terminology, but importing a MeSH descriptor as an OWL waste subtype and aligning it to the local role-based waste model still require a term-level dependency/category review. | `DEFERRED_MODELLING` | No |
| `MKB-000098` food waste | ENVO `ENVO_03600006` remains a strong selective candidate. Its parent/axiom closure must be reconciled with local `MATSUS_0000008` before reuse. | `DEFERRED_MODELLING` | No |
| `MKB-000114` Life Cycle Assessment | Recorded candidate is from the same untagged research ontology as Functional Unit. Defer it to the assessment/LCA architecture rather than selectively importing a lone class now. | `FUTURE_PATTERN_OR_SHACL` | No |
| `MKB-000141` waste material | ENVO `ENVO_00002264` is not imported. The approved role-based local `MATSUS_0000008` supersedes it for the bounded scope, pending PMDco #485. | `IMPLEMENTED_LOCAL` | No |

Selective reuse remains possible for the five deferred candidates, but none has been implemented or imported. Therefore the current count for `REUSED_EXTERNAL` is zero, not eight.

## 8. Deferred dependencies and future backlog

Current GitHub API state was checked read-only on 2026-09-07: PMDco issues #485, #486, #487, and #488 are open.

| Item | Current disposition | Before public migration? |
|---|---|---|
| FeedstockRole / PMDco #486 | External issue dependent. Await upstream role decision; do not mint a duplicate. | Documented future work; not automatically blocking. |
| CircularDesignSpecification / PMDco #488 | External issue dependent through generic DesignSpecification. | Documented future work; not automatically blocking. |
| ProductSpecification / PMDco #487 | External handoff; no MatSus duplicate. | Documented future work; not automatically blocking. |
| WasteRole/WasteMaterial / PMDco #485 | Local provisional role/material pattern is implemented and validated. Reconcile or map if PMDco accepts upstream anchors. | Non-blocking for bounded MKB1; migration mapping plan required. |
| MaterialFlowProcess | Required future MatSus/LOG architecture; its boundary against transport, material-location-change, and logistics processes awaits concrete competency examples, review of improved LOG architecture, and post-migration team discussion. | Deferred architecture work; not an MKB1 closure blocker. |
| TextileMaterialFlowProcess | Deferred with its generic MaterialFlowProcess parent. | Non-blocking future architecture work. |
| ReverseLogisticsProcess | LOG issue/contribution route still pending. | Documented future work; tracker already says it does not block IR2. |
| AbsoluteDecoupling | Generic `MATSUS_0000037` DecouplingDatum implemented; absolute/relative classifications, baseline, ratio, and interval remain deferred. | Non-blocking. |
| Assessment/LCA architecture | Functional Unit, Reference Unit, Reference Flow, LCA, impact/result and assessment distinctions remain a dedicated work package. | Future architecture unless a release competency query requires it. |
| Modelling patterns and SHACL | Time-indexed values, composition, flow/exchange, DPP relations, stakeholder perspectives, due diligence, lifecycle status, and BatteryPass compatibility remain pattern/profile work. | Non-blocking for the class-integration milestone. |

## 9. Event, Quantity value, and Unit hierarchy investigation

### 9.1 Exact identities and results

| Label | Exact IRI | Selected/import source | Named asserted parent in source used by MatSus | Generated/resolved MatSus result |
|---|---|---|---|---|
| Event | `http://w3id.org/CEON/ontology/processODP/Event` | CEON processODP 0.5 via `matsus-ceon.ttl` | None; two anonymous restrictions | Named parent `ceon-processODP:Process` plus one anonymous restriction |
| Quantity value | `http://qudt.org/schema/qudt/QuantityValue` | QUDT material embedded in PMDco 3.1.0 and `pmdco_import.owl` | None | No named parent |
| Unit | `http://qudt.org/schema/qudt/Unit` | QUDT material embedded in PMDco 3.1.0 and `pmdco_import.owl` | None | No named parent |

No IRI mismatch was found between source modules, `pmdco_import.owl`, and `matsus.ttl`.

### 9.2 Event

Authoritative CEON processODP 0.5 does not assert a named superclass for Event. It asserts input/output existential restrictions and an all-parts-Event restriction. Both `hasInput` and `hasOutput` have domain `ceon-processODP:Process`; the existential restrictions therefore entail `Event SubClassOf Process`. The selected checked-in CEON component preserves those source axioms. The checked-in generated MatSus graph materializes `Event SubClassOf Process`.

Consequently, Event can appear directly under `owl:Thing` in Protege's **asserted** hierarchy when the selected source is viewed without inferred relationships, while it appears below Process in the generated/inferred hierarchy. This is source modelling plus asserted-versus-inferred display behavior, not an extraction omission or MatSus integration defect.

### 9.3 Quantity value and Unit

Authoritative QUDT 2.1 asserts:

- `QuantityValue SubClassOf Concept` and `QuantityValue SubClassOf Quantifiable`, with unit-cardinality restrictions;
- `Unit SubClassOf Concept` and `Unit SubClassOf Verifiable`, with additional restrictions.

The tagged PMDco 3.1.0 root artifact contains the same exact class IRIs, labels and definitions but omits those parent and restriction axioms. The checked-in MatSus `pmdco_import.owl` matches PMDco 3.1.0, and the generated/resolved MatSus graph consequently has no superclass axioms for either class. Their appearance directly below `owl:Thing` is therefore real in the present closure, but the omission originates in PMDco's packaged QUDT slice rather than a MatSus IRI, serialization, catalog, or merge defect.

Recommended handling: raise or link an upstream PMDco import/module issue, compare the intended QUDT extraction policy, and consume a corrected upstream artifact when available. Do not add local MatSus bridge axioms unless PMDco/QUDT maintainers explicitly approve the exact subset and semantics.

## 10. Public-migration blockers versus non-blocking work

### Must resolve or explicitly accept before public migration

1. Resolve or formally accept/document the PMDco 3.1.0 QUDT parent-axiom omission for `QuantityValue` and `Unit`. The correction belongs upstream or in the approved import pipeline, not as unsupported MatSus bridge axioms.
2. Record the migration policy for provisional WasteRole/WasteMaterial if PMDco #485 is accepted after this audit.

### Documented non-blocking future work

- PMDco #486-#488 and the pending LOG reverse-logistics request;
- MaterialFlowProcess and TextileMaterialFlowProcess through concrete competency examples, review of the improved LOG process architecture, and team discussion after MatSus public migration;
- AbsoluteDecoupling and relative-decoupling calculation semantics;
- external SCO/ENVO/MeSH candidate reuse;
- assessment/LCA architecture;
- remaining modelling-pattern and SHACL work;
- deferred relation-level axiomatization already recorded in the three handoffs.

## 11. Tracker and report consistency findings

1. **No false implementation claim found.** Every tracker IRI claimed as implemented is present in the assembled ontology, including the duplicated source-row mappings to one RefillProcess and one DecouplingDatum.
2. **22 stale next-action cells.** Implemented tracker rows still say “Ready for human pre-commit review” after the commits were merged. This is operationally stale but does not alter ontology truth.
3. **36 likely encoding artifacts.** Batch 3 tracker cells contain the literal separator ` ? ` where an em dash was evidently intended, including acceptance, validation and N/A text. These are editorial data-quality issues, not semantic status failures.
4. **Material flow lacks a standalone final tracker closure.** `MKB-000128` carries the explicit human requirement; the later deferral appears indirectly in the `MKB-000247` tracker/Class Review material-flow family. This human-gate correction classifies `MKB-000128` as `DEFERRED_ARCHITECTURE_NOT_A_CLOSURE_BLOCKER`; recording that standalone status in the tracker is separate follow-up work and does not block MKB1 closure.
5. **Final workbook versus later tracker.** The FINAL archive says to keep FeedstockRole and CircularDesignSpecification drafts for current use, and says to implement TextileMaterialFlowProcess. The later approved Batch 3 report/tracker supersede those operational instructions by excluding the first two pending PMDco and deferring the flow pair. The FINAL workbook remains a read-only decision-history artifact and should not be edited.
6. **Non-virgin/virgin record is qualified, not false.** The tracker marks `MKB-000150` implemented because it produced the approved positive VirginMaterial response. NonVirginMaterial and complement axioms remain deferred. The separate `MKB-000261` Virgin material record is covered by the same class.
7. **Historical reports are not current status dashboards.** Batch planning and pre-commit handoffs correctly describe their point-in-time gates. Their pre-commit language is historical rather than an instruction to reopen implementation.

## 12. Recommended minimal next actions

1. In a separately authorized task, record `MKB-000128` as `DEFERRED_ARCHITECTURE_NOT_A_CLOSURE_BLOCKER` in the working tracker, replace stale pre-commit next actions, and correct the 36 separator artifacts.
2. Open or cross-link a PMDco issue documenting the missing QUDT 2.1 parent/restriction axioms for `QuantityValue` and `Unit`; do not patch MatSus locally.
3. Maintain a small external-dependency register for PMDco #485-#488 and the future LOG reverse-logistics/material-flow discussions; do not block bounded closure merely because an issue is open.
4. Schedule the MatSus/LOG material-flow architecture discussion after public migration, using concrete competency examples and the improved LOG process architecture.
5. Schedule assessment/LCA and modelling-pattern/SHACL work only against approved competency queries.

## Appendix A. Closure status for every reviewed record

| Record | Reviewed label/concept | Current closure status |
|---|---|---|
| `ADD-BAT-001` | generic product/material condition | `DEFERRED_MODELLING` |
| `ADD-BAT-002` | generic degradation / fade | `DEFERRED_MODELLING` |
| `ADD-BAT-003` | remaining capability | `DEFERRED_MODELLING` |
| `ADD-BAT-004` | time-indexed measurement and state | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-005` | nominal/original/current/remaining performance distinction | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-006` | composition statement | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-007` | negative lifecycle event record | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-008` | due-diligence claim, evidence and assurance pattern | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-009` | circular-process-to-DPP-information relation | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-010` | carbon-footprint semantic backbone | `DEFERRED_MODELLING` |
| `ADD-BAT-011` | BatteryPass compatibility and SHACL profile | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BAT-012` | battery status, condition and lifecycle-date distinction | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BON-001` | quantified flow / exchange | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BON-002` | flow object | `COVERED_OR_ALIGNED_EXISTING` |
| `ADD-BON-003` | activity/process classification | `DEFERRED_MODELLING` |
| `ADD-BON-004` | shared input/output exchange pattern | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BON-005` | balanceable property | `DEFERRED_MODELLING` |
| `ADD-BON-006` | balanceable property type | `DEFERRED_MODELLING` |
| `ADD-BON-007` | reference unit | `DEFERRED_MODELLING` |
| `ADD-BON-008` | functional unit | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-BON-009` | reference flow / determining flow | `DEFERRED_MODELLING` |
| `ADD-SCO-001` | complex system | `DEFERRED_MODELLING` |
| `ADD-SCO-002` | interaction | `DEFERRED_MODELLING` |
| `ADD-SCO-003` | system development | `DEFERRED_MODELLING` |
| `ADD-SCO-004` | system history | `DEFERRED_MODELLING` |
| `ADD-SCO-005` | stakeholder role | `DEFERRED_MODELLING` |
| `ADD-SCO-006` | stakeholder | `DEFERRED_MODELLING` |
| `ADD-SCO-007` | perspective | `DEFERRED_MODELLING` |
| `ADD-SCO-008` | perspective information content entity | `DEFERRED_MODELLING` |
| `ADD-SCO-009` | stakeholder perspective / perspective information | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-SCO-010` | indicator bearer/entity and indicator role | `DEFERRED_MODELLING` |
| `ADD-SCO-011` | indicator value | `DEFERRED_MODELLING` |
| `ADD-SCO-012` | metric / indicator specification | `IMPLEMENTED_LOCAL` |
| `ADD-SCO-013` | system boundary versus assessment boundary | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-SCO-014` | system component and environment pattern | `FUTURE_PATTERN_OR_SHACL` |
| `ADD-SCO-015` | emergence and self-organization | `DEFERRED_MODELLING` |
| `ADD-SCO-016` | worth and worth role | `DEFERRED_MODELLING` |
| `MKB-000001` | 5R strategies | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000002` | Absolute decoupling / decoupling | `IMPLEMENTED_LOCAL` |
| `MKB-000004` | Adaptive reuse | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000007` | product life extension | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000008` | Battery recycling | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000009` | Battery repurposing | `IMPLEMENTED_LOCAL` |
| `MKB-000016` | Biowaste feedstock / feedstock role | `EXTERNAL_ISSUE_DEPENDENT` |
| `MKB-000017` | Building component reuse | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000028` | Circular design specification | `EXTERNAL_ISSUE_DEPENDENT` |
| `MKB-000036` | Circular Material Use Rate | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000041` | Circular supply chain | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000055` | Closed-loop recycling | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000059` | collection system | `IMPLEMENTED_LOCAL` |
| `MKB-000063` | construction and demolition waste | `IMPLEMENTED_LOCAL` |
| `MKB-000069` | Decoupling | `IMPLEMENTED_LOCAL` |
| `MKB-000070` | Design for disassembly | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000084` | electronic waste | `DEFERRED_MODELLING` |
| `MKB-000085` | waste-elimination objective specification | `IMPLEMENTED_LOCAL` |
| `MKB-000088` | End of life | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000094` | EV battery value chain | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000098` | food waste | `DEFERRED_MODELLING` |
| `MKB-000102` | High-quality recycling | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000113` | Life cycle | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000114` | Life Cycle Assessment | `FUTURE_PATTERN_OR_SHACL` |
| `MKB-000118` | product longevity | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000120` | Maintenance | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000128` | Material flow | `DEFERRED_ARCHITECTURE_NOT_A_CLOSURE_BLOCKER` |
| `MKB-000137` | material resource efficiency datum | `IMPLEMENTED_LOCAL` |
| `MKB-000139` | Material stock | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000141` | waste material | `IMPLEMENTED_LOCAL` |
| `MKB-000144` | mineral waste | `IMPLEMENTED_LOCAL` |
| `MKB-000146` | modularity | `IMPLEMENTED_LOCAL` |
| `MKB-000148` | municipal waste | `IMPLEMENTED_LOCAL` |
| `MKB-000150` | non-virgin material / positive VirginMaterial response | `IMPLEMENTED_LOCAL` |
| `MKB-000152` | Open-loop recycling | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000155` | packaging waste | `IMPLEMENTED_LOCAL` |
| `MKB-000158` | product life extension | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000163` | Primary material | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000164` | Product durability | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000165` | Product life extension | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000168` | product specification | `EXTERNAL_ISSUE_DEPENDENT` |
| `MKB-000172` | Recyclability | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000173` | Recyclable material | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000174` | Recycled content | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000175` | recycled material | `IMPLEMENTED_LOCAL` |
| `MKB-000177` | Recycling quality | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000178` | Recycling rate | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000180` | resource-input reduction | `IMPLEMENTED_LOCAL` |
| `MKB-000181` | refill at home | `IMPLEMENTED_LOCAL` |
| `MKB-000182` | refill on the go | `IMPLEMENTED_LOCAL` |
| `MKB-000184` | refusal | `IMPLEMENTED_LOCAL` |
| `MKB-000189` | remanufacturing process | `IMPLEMENTED_LOCAL` |
| `MKB-000192` | Renewable feedstock | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000193` | Renewable material | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000195` | Renewable resource | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000201` | Repairability | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000202` | repurposing process | `IMPLEMENTED_LOCAL` |
| `MKB-000205` | resource efficiency datum | `IMPLEMENTED_LOCAL` |
| `MKB-000207` | Resource productivity | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000210` | product return process, from-home context | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000211` | product return process, away-from-home context | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000212` | Reusability | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000213` | reusable material / material reusability | `DEFERRED_MODELLING` |
| `MKB-000214` | reusable packaging | `DEFERRED_MODELLING` |
| `MKB-000217` | reverse logistics process | `EXTERNAL_ISSUE_DEPENDENT` |
| `MKB-000223` | secondary material | `IMPLEMENTED_LOCAL` |
| `MKB-000224` | Secondary raw material | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000231` | sorting process and method specification | `IMPLEMENTED_LOCAL` |
| `MKB-000236` | waste analysis and structural waste analysis | `IMPLEMENTED_LOCAL` |
| `MKB-000245` | Take-back system | `DEFERRED_MODELLING` |
| `MKB-000247` | textile material flow process | `DEFERRED_MODELLING` |
| `MKB-000248` | product longevity | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000249` | textile waste | `IMPLEMENTED_LOCAL` |
| `MKB-000250` | Textile-to-textile recycling | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000251` | Traceability | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000261` | Virgin material | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000263` | waste generation process | `IMPLEMENTED_LOCAL` |
| `MKB-000264` | waste prevention process and measure specification | `IMPLEMENTED_LOCAL` |
| `MKB-000266` | zero-waste objective and strategy specifications | `IMPLEMENTED_LOCAL` |
| `MKB-000270` | battery carbon footprint per Functional Unit | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000274` | model identifier | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000282` | Carbon footprint label | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000283` | Carbon footprint performance class | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000297` | Expected lifetime in calendar years | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000298` | Expected lifetime in charge-discharge cycles | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000302` | impact family | `DEFERRED_MODELLING` |
| `MKB-000307` | end-user guidance about separate collection | `DEFERRED_MODELLING` |
| `MKB-000308` | end-user guidance about waste prevention | `DEFERRED_MODELLING` |
| `MKB-000334` | Separate collection symbol | `DEFERRED_MODELLING` |
| `MKB-000343` | unique product identifier | `COVERED_OR_ALIGNED_EXISTING` |
| `MKB-000349` | Warranty period | `COVERED_OR_ALIGNED_EXISTING` |

## Appendix B. Evidence, checks, and limitations

### Repository files inspected

- `src/ontology/matsus-edit.owl`
- `src/ontology/matsus.ttl`
- `src/ontology/catalog-v001.xml`
- `src/ontology/components/matsus-ceon.ttl`
- `src/ontology/components/matsus-log-stageA.ttl`
- `src/ontology/components/matsus-dppo.ttl`
- `src/ontology/components/matsus-shared.owl`
- `src/ontology/components/matsus-axioms-shared.owl`
- `src/ontology/components/imports-edit.owl`
- `src/ontology/imports/pmdco_import.owl`
- `src/ontology/imports/pmdco_terms.txt`
- `audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Implementation_Tracker_2026-08-31 (2)_working implementation.xlsx`
- `audit/mkb1-ontology-reuse-alignment/MKB1_FINAL_human-gate-completed_2026-08-31 (2)_readonly.xlsx`
- Batch 1-3 planning/pre-commit handoff reports in the same audit directory
- `alignment-analysis.tsv`, `reuse-discovery-candidates.tsv`, `reformulation-log.tsv`, `ontology-source-assessment.tsv`, `semantic-issues.md`, `summary.md`, and `exact-queries-and-sources.md`

### External authoritative material inspected read-only

- PMDco tag `v3.1.0`, root `pmdco.ttl`: `https://raw.githubusercontent.com/materialdigital/core-ontology/v3.1.0/pmdco.ttl`
- CEON processODP version 0.5: `http://w3id.org/CEON/ontology/processODP/0.5/`
- QUDT 2.1 schema: `http://qudt.org/2.1/schema/qudt`
- GitHub issue API records for PMDco #485-#488 on 2026-09-07

### Checks used

- Git branch, revision, upstream, status and merge-base ancestry checks.
- Exact numeric declaration/source searches and RDF graph class counts.
- In-memory RDF parsing of current `matsus.ttl`, selected CEON, and `pmdco_import.owl`.
- In-memory RDF parsing of `d9ea1ad:src/ontology/matsus.ttl` from Git history.
- Read-only workbook inspection with `openpyxl`; record/recommendation/status counts and row-level reconciliation.
- Exact external-candidate IRI presence tests against the current resolved graph.
- Source/import/generated `rdfs:subClassOf` comparison for Event, QuantityValue, and Unit.
- Read-only current-state lookup of PMDco issues #485-#488.

### Limitations

- The checked-in generated `matsus.ttl` was used as the complete resolved/reasoned ontology artifact; no build or reasoner was rerun because the task prohibited changes and implementation.
- Workbook formulas were inspected but not recalculated or saved.
- External ontologies were not imported. Candidate decisions rely on the stored MKB1 term-level evidence plus the targeted authoritative source checks described above.
- GitHub issue state is time-sensitive; the state reported here is the state returned on 2026-09-07.
- No ontology, workbook, existing report, import component, generated artifact, or untracked file was modified.
