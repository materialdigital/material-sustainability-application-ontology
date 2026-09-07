# MKB1 IR2 Batch 3 Non-Waste Planning Report

**Date:** 2026-09-04
**Branch:** mkb1-ir2-batch3-nonwaste
**Starting main:** 5e56b8c0c8c079451f7a153d89f52e16cb712f67
**Purpose:** MKB1 IR2 implementation planning
**Implementation state:** Planning only; no ontology class, tracker, or FINAL-workbook change

This is MKB1 IR2 implementation planning, not MKB source-mining Batch 2.

## Executive decision

The recommended bounded Batch 3 implementation scope is **13 local MatSus classes**:

1. MetricSpecification
2. ResourceEfficiencyDatum
3. MaterialResourceEfficiencyDatum
4. VirginMaterial
5. RepurposingProcess
6. BatteryRepurposingProcess
7. ResourceInputReductionProcess
8. RefillProcess
9. RefusalProcess
10. RemanufacturingProcess
11. DecouplingDatum
12. Modularity
13. RefusalStrategySpecification

The original tracker review contains 16 consolidated candidate families. RefusalStrategySpecification is not a seventeenth original source candidate; it is an additional human-gate modelling refinement derived from the RefusalProcess discussion.

These classes have stable imported parents or depend only on another class in the same proposed batch. The implementation should add only one asserted parent per class. No equivalence, disjointness, complement, universal restriction, or existential restriction is proposed at this stage.

Four reviewed candidate families are outside the bounded implementation scope:

- FeedstockRole is EXTERNAL_ISSUE_DEPENDENT on open PMDco issue #486.
- CircularDesignSpecification is EXTERNAL_ISSUE_DEPENDENT on open PMDco issue #488.
- MaterialFlowProcess is REUSE_CHECK_REQUIRED because its boundary against LOG material-location, transport, and logistics processes is not settled.
- TextileMaterialFlowProcess is DEFER because its proposed parent, MaterialFlowProcess, is not ready.

ProductSpecification, DesignSpecification, and ReverseLogisticsProcess remain external handoffs. No MatSus duplicates should be minted.

The proposed numeric IRIs MATSUS_0000027 through MATSUS_0000039 are tentative planning allocations only. They are not allocated in the ontology and must be rechecked against the repository ID policy immediately before any implementation.

## Repository gate

The planning branch was created only after the following checks passed:

- Active branch was main.
- Local main and origin/main both resolved to 5e56b8c0c8c079451f7a153d89f52e16cb712f67.
- main tracked origin/main.
- No tracked or staged changes existed.
- Each class declaration from MATSUS_0000001 through MATSUS_0000026 was present exactly once in src/ontology/matsus-edit.owl.
- Existing unrelated untracked files were left in place.

The new branch is mkb1-ir2-batch3-nonwaste.

## Authoritative inputs and method

The review used:

- src/ontology/matsus-edit.owl;
- the working IR2 implementation tracker, read-only for this planning task;
- the human-gate-completed FINAL workbook, opened read-only;
- Class Review records and the FINAL Master Analysis, Decision Register, Closure, and Post-gate Additions sheets;
- alignment-analysis.tsv, reuse-discovery-candidates.tsv, reformulation-log.tsv, exact-queries-and-sources.md, ontology-source-assessment.tsv, and the stored OLS results;
- the checked-in PMDco import and selected LOG and CEON integration components;
- authoritative ontology repositories and release metadata for term-level follow-up.

The focused reuse checks considered definitions, asserted parents, logical axioms, import closure, licence, version, and maintenance. Lexical similarity alone was not accepted as evidence of equivalence.

The current MatSus import closure comprises the checked-in PMDco import plus the local imports, shared axioms, selected CEON, DPPO, LOG Stage A, and shared components. IOF Core, CCO, and AutomatCE are not imported as full ontologies. Any proposal to add one of those closures would be a separate dependency decision, not an incidental consequence of Batch 3.

## Tracker-row normalization

IR2 Tracker rows 3–20 were reviewed, excluding row 5 because its sorting classes were completed in Batch 2.

| Tracker row(s) | Source record(s) | Consolidated candidate |
|---:|---|---|
| 3 | ADD-SCO-012 | MetricSpecification |
| 4 | MKB-000028 | CircularDesignSpecification |
| 6 | MKB-000016 | FeedstockRole |
| 7 | MKB-000137 | MaterialResourceEfficiencyDatum |
| 8 | MKB-000150 | VirginMaterial |
| 9 | MKB-000009 | BatteryRepurposingProcess |
| 10 | MKB-000180 | ResourceInputReductionProcess |
| 11–12 | MKB-000181; MKB-000182 | RefillProcess |
| 13 | MKB-000184 | RefusalProcess |
| 14 | MKB-000189 | RemanufacturingProcess |
| 15 | MKB-000202 | RepurposingProcess |
| 16 | MKB-000247 plus supporting class | MaterialFlowProcess; TextileMaterialFlowProcess |
| 17–18 | MKB-000002; MKB-000069 | DecouplingDatum |
| 19 | MKB-000146 | Modularity |
| 20 | MKB-000205 | ResourceEfficiencyDatum |

MKB-000181 and MKB-000182 are consolidated into one RefillProcess. “At home” and “on the go” remain source contexts, not subclasses.

MKB-000002 and MKB-000069 are consolidated into one DecouplingDatum. Absolute and relative decoupling classifications remain deferred until a baseline, time interval, ratio, and comparison pattern has been tested.

## Candidate classification

| Candidate family | Classification | Batch 3 decision |
|---|---|---|
| MetricSpecification | READY_FOR_BATCH3_IMPLEMENTATION | Include. The specification is a directive information entity; the resulting metric value remains a data item. |
| CircularDesignSpecification | EXTERNAL_ISSUE_DEPENDENT | Exclude pending PMDco #488 and the generic DesignSpecification pattern. |
| FeedstockRole | EXTERNAL_ISSUE_DEPENDENT | Exclude pending PMDco #486 and resolution of its relationship to LOG raw material role/material resource role. |
| ResourceEfficiencyDatum | READY_FOR_BATCH3_IMPLEMENTATION | Include as an IAO data item, not an intrinsic efficiency quality. |
| MaterialResourceEfficiencyDatum | READY_FOR_BATCH3_IMPLEMENTATION | Include as the material-input specialization of ResourceEfficiencyDatum. |
| VirginMaterial | READY_FOR_BATCH3_IMPLEMENTATION | Include with the ISO-grounded positive definition below. Do not define a complement class. |
| RepurposingProcess | READY_FOR_BATCH3_IMPLEMENTATION | Include; no maintained compatible process class was verified. |
| BatteryRepurposingProcess | READY_FOR_BATCH3_IMPLEMENTATION | Include as a narrow local child of RepurposingProcess. |
| ResourceInputReductionProcess | READY_FOR_BATCH3_IMPLEMENTATION | Include as an intentional planned process. Baseline semantics remain editorial. |
| RefillProcess | READY_FOR_BATCH3_IMPLEMENTATION | Include one consolidated generic process. |
| RefusalProcess | READY_FOR_BATCH3_IMPLEMENTATION | Include as an intentional planned process. |
| RemanufacturingProcess | READY_FOR_BATCH3_IMPLEMENTATION | Include the process; do not duplicate the separate remanufacturability disposition candidate. |
| MaterialFlowProcess | REUSE_CHECK_REQUIRED | Exclude until the LOG boundary and the intended meaning of “flow” are fixed by a competency example. |
| TextileMaterialFlowProcess | DEFER | Exclude until MaterialFlowProcess has an approved parent and boundary. |
| DecouplingDatum | READY_FOR_BATCH3_IMPLEMENTATION | Include one consolidated comparative temporal data item. |
| Modularity | READY_FOR_BATCH3_IMPLEMENTATION | Include as a BFO quality; do not model it as an object aggregate. |

The table above preserves the original review of 16 consolidated candidate families. **RefusalStrategySpecification** is additionally classified READY_FOR_BATCH3_IMPLEMENTATION as a human-gate modelling refinement derived from the MKB-000184 RefusalProcess review and the 2026-09-04 Batch 3 review; it is not a seventeenth original source candidate.

## Proposed bounded 13-class implementation

All IRIs in this section are provisional. Each proposed logical axiom is a necessary asserted parent only.

### 1. MetricSpecification

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000027
- **Provenance:** ADD-SCO-012; SCO
- **Definition:** A directive information entity that prescribes the quantities, calculation method, units, boundary, and interpretation used to produce a quantitative indicator datum.
- **Parent:** IAO directive information entity (http://purl.obolibrary.org/obo/IAO_0000033)
- **High-confidence axiom:** MATSUS_0000027 SubClassOf IAO_0000033
- **Deferred:** Relations to prescribed quantities, calculation method, units, boundary, interpretation, and resulting datum.

### 2. ResourceEfficiencyDatum

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000028
- **Provenance:** MKB-000205; SRC-001 Circular Berlin; UNEP domain meaning
- **Definition:** A data item that records the useful output, service, or value obtained per stated quantity of resource input under a specified method, boundary, and time interval.
- **Parent:** IAO data item (http://purl.obolibrary.org/obo/IAO_0000027)
- **High-confidence axiom:** MATSUS_0000028 SubClassOf IAO_0000027
- **Deferred:** Numerator/output, resource input, method, boundary, unit, time interval, and calculation relations.

### 3. MaterialResourceEfficiencyDatum

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000029
- **Provenance:** MKB-000137; SRC-003 European Environment Agency
- **Definition:** A resource efficiency datum whose stated resource input is a quantity of material.
- **Parent:** proposed MatSus ResourceEfficiencyDatum
- **High-confidence axiom:** MATSUS_0000029 SubClassOf MATSUS_0000028
- **Deferred:** Logical constraint to a material quantity and any method, unit, or boundary pattern.

### 4. VirginMaterial

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000030
- **Provenance:** MKB-000150; SRC-002 Ellen MacArthur Foundation; ISO 21067-2:2015 terminology as reproduced in the ISO/DIS 15270-1 plastics-recovery draft
- **Definition:** A material that has never been processed into any form of an end-use product.
- **Parent:** PMDco material (https://w3id.org/pmd/co/PMD_0000000)
- **High-confidence axiom:** MATSUS_0000030 SubClassOf PMD_0000000
- **Deferred:** Provenance and composition relations, including virgin/recovered content proportions.

This positive definition resolves the prior source gap. The official ISO terminology uses “virgin material” or “primary material” for material never processed into an end-use product. The source is terminological evidence, not an external OWL class to import.

Do not model NonVirginMaterial as the complement of VirginMaterial. Mixed-content materials are common, and under the open-world assumption failure to establish virgin status does not establish non-virgin status. Use the existing positive SecondaryMaterial class (MATSUS_0000003). Defer additional recovered-content, composition, and proportion axioms until supported by an approved competency query.

### 5. RepurposingProcess

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000031
- **Provenance:** MKB-000202; SRC-001 Circular Berlin
- **Definition:** A planned process in which a product, component, or material is prepared or modified so that it can fulfil a purpose different from its preceding intended purpose.
- **Parent:** COB planned process (http://purl.obolibrary.org/obo/COB_0000082)
- **High-confidence axiom:** MATSUS_0000031 SubClassOf COB_0000082
- **Deferred:** Prior purpose, new purpose, participant, input, and output relations.

### 6. BatteryRepurposingProcess

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000032
- **Provenance:** MKB-000009; SRC-002 Ellen MacArthur Foundation
- **Definition:** A repurposing process whose primary participant is a battery or battery component.
- **Parent:** proposed MatSus RepurposingProcess
- **High-confidence axiom:** MATSUS_0000032 SubClassOf MATSUS_0000031
- **Deferred:** Battery participant and second-life/new-purpose relations.

### 7. ResourceInputReductionProcess

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000033
- **Provenance:** MKB-000180; SRC-001 Circular Berlin
- **Definition:** A planned process intended to reduce the amount of material input used by a specified process or system.
- **Parent:** COB planned process (http://purl.obolibrary.org/obo/COB_0000082)
- **High-confidence axiom:** MATSUS_0000033 SubClassOf COB_0000082
- **Deferred:** Affected process or system, material input, stated baseline, comparison conditions, and comparable output or function.

The process remains distinct from the already implemented ResourceInputReductionAssessment and ResourceInputReductionObjectiveSpecification.

### 8. RefillProcess

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000034
- **Provenance:** MKB-000181 and MKB-000182; SRC-002 Ellen MacArthur Foundation
- **Definition:** A planned process in which a product container or dispensing device is supplied again with a material product for further use without first becoming waste.
- **Parent:** COB planned process (http://purl.obolibrary.org/obo/COB_0000082)
- **High-confidence axiom:** MATSUS_0000034 SubClassOf COB_0000082
- **Deferred:** Container/device, refilled material, location, agent, and at-home/away-from-home context relations.

### 9. RefusalProcess

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000035
- **Provenance:** MKB-000184; SRC-001 Circular Berlin
- **Definition:** A planned process in which an agent intentionally declines to acquire, accept, or use a specified product, material, or service in order to avoid its associated resource use or waste generation.
- **Parent:** COB planned process (http://purl.obolibrary.org/obo/COB_0000082)
- **High-confidence axiom:** MATSUS_0000035 SubClassOf COB_0000082
- **Deferred:** Agent, refused entity/service, and avoidance-objective relations.

**Planning-stage editorial clarification:** RefusalProcess represents the actual intentional refusal occurrence. It does not represent the strategy specification or objective specification that motivates, enables or encourages that occurrence.

### 10. RemanufacturingProcess

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000036
- **Provenance:** MKB-000189; SRC-003 European Environment Agency
- **Definition:** A planned process in which a used product or component is restored to a specified performance and quality state through inspection and one or more restorative operations.
- **Parent:** COB planned process (http://purl.obolibrary.org/obo/COB_0000082)
- **High-confidence axiom:** MATSUS_0000036 SubClassOf COB_0000082
- **Deferred:** Used input, retained identity/components, restorative operations, and specified output state.

AutomatCE AUTOMATCE_0010231 is a separate remanufacturability disposition candidate. It does not replace the required process class and should be evaluated only if a later capability query needs it.

### 11. DecouplingDatum

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000037
- **Provenance:** MKB-000002, SRC-003 European Environment Agency; MKB-000069, SRC-002 Ellen MacArthur Foundation
- **Definition:** A data item that records a comparison over a stated time interval in which the rate of change of a resource input or environmental pressure is lower than the rate of change of a specified economic or service output.
- **Parent:** IAO data item (http://purl.obolibrary.org/obo/IAO_0000027)
- **High-confidence axiom:** MATSUS_0000037 SubClassOf IAO_0000027
- **Deferred:** Absolute and relative decoupling classifications; baseline and comparison interval; resource-input or environmental-pressure indicator; economic or service-output indicator; calculation method; ratio and temporal relations.

This is the established sustainability and resource-efficiency meaning of decoupling, not dismantling, disassembly, or another physical separation process.

### 12. Modularity

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000038
- **Provenance:** MKB-000146; SRC-002 Ellen MacArthur Foundation
- **Definition:** A quality of an entity that reflects the degree to which its parts are organized into separable, replaceable, or recombinable modules.
- **Parent:** BFO quality (http://purl.obolibrary.org/obo/BFO_0000019)
- **High-confidence axiom:** MATSUS_0000038 SubClassOf BFO_0000019
- **Deferred:** Bearer, measurement datum, degree, method, and any device- or design-specific subclasses.

Modularity is a dependent quality of a bearer. It is not itself an object aggregate.

### 13. RefusalStrategySpecification

- **Provisional IRI:** https://w3id.org/pmd/matsus/MATSUS_0000039
- **Provenance:** Human-gate modelling refinement derived from the MKB-000184 RefusalProcess review and the 2026-09-04 Batch 3 review.
- **Definition:** A plan specification that prescribes product, packaging, or service features intended to enable or encourage a refusal process and thereby avoid material use or waste generation.
- **Parent:** IAO plan specification (http://purl.obolibrary.org/obo/IAO_0000104)
- **High-confidence axiom:** MATSUS_0000039 SubClassOf IAO_0000104
- **Proposed rdfs:comment:** Examples include optional packaging, opt-out disposable accessories, and service provision that avoids supplying a material product. This class denotes the strategy specification; the actual refusal occurrence is represented by refusal process.
- **Proposed skos:editorialNote:** This is a human-gate modelling addition derived from the MKB-000184 RefusalProcess review and the 2026-09-04 Batch 3 review. Relations to refusal processes, resource-input-reduction objectives, design specifications, affected product features, and realization remain deferred for later axiomatization.

No existential restriction or other logical relation between RefusalProcess and RefusalStrategySpecification is proposed in this batch. In particular, do not assert that every RefusalProcess realizes a RefusalStrategySpecification.

## Focused reuse checks

### Feedstock role

**Definitions, parents, and axioms**

- LOG LOG_1000106 material resource role is a BFO role with a material-entity bearer restriction. Its definition concerns availability to a person, group of agents, or engineered system.
- LOG LOG_1000079 raw material role is also a BFO role, but its definition and restrictions depend on organizational acquisition and a plan to transform the material.
- AutomatCE AUTOMATCE_0010000 raw material feedstock is defined as a material entity intended to be consumed, transformed, or incorporated as process input. It is asserted under LOG LOG_1000102 raw material and has no role axiom. Its own comment nevertheless says the status is workflow-dependent.
- The AutomatCE candidate supplies useful wording but has the wrong ontological category for the intended context-dependent FeedstockRole.

**Closure, licence, version, and maintenance**

- AutomatCE is not in the MatSus import closure.
- [AutomatCE v1.0.0](https://github.com/materialdigital/automatce/releases/tag/v1.0.0) is CC BY 4.0, has a 2026-06-19 version IRI, is not archived, and is maintained in the PMD ecosystem.
- Importing AutomatCE merely for this class would bring an additional PMDco/LOG-aligned closure and would not solve the class-versus-role mismatch.

**Decision**

PMDco issue [#486](https://github.com/materialdigital/core-ontology/issues/486) is open as of 2026-09-04. It proposes a BFO feedstock role and leaves its relationship to LOG raw material role open. FeedstockRole is EXTERNAL_ISSUE_DEPENDENT and excluded from the bounded implementation.

### Circular design

**Definitions, parents, and axioms**

- [IOF Core 202602 DesignSpecification](https://github.com/iofoundry/ontology/blob/Release_202602/core/Core.rdf) is an InformationContentEntity that prescribes something intentionally created. It has an all-values restriction limiting prescribes fillers to continuants.
- [CCO 2.2 Artifact Design](https://github.com/CommonCoreOntology/CommonCoreOntologies/blob/v2.2/src/cco-modules/ArtifactOntology.ttl) is a Prescriptive Information Content Entity with an existential prescribes-some-Material-Artifact restriction.
- Both are credible information-artifact anchors, but both are narrower and more prescriptive than the mixed descriptive-or-directive pattern requested for PMDco.
- Stored OLS “circular design” hits were unrelated biomedical loop-study-design homonyms.

**Closure, licence, version, and maintenance**

- [IOF release 202602](https://github.com/iofoundry/ontology/releases/tag/Release_202602) is MIT licensed and maintained; Core imports BFO and the IOF annotation vocabulary.
- CCO 2.2 is BSD-3-Clause, versioned 2026-08-13, and actively maintained; ArtifactOntology imports InformationEntityOntology and BFO.
- Neither ontology is in the current MatSus import closure. Full import would overlap the PMDco/IAO/BFO information stack, so no new import is justified for one specialization.

**Decision**

PMDco issue [#488](https://github.com/materialdigital/core-ontology/issues/488) is open as of 2026-09-04. It proposes DesignSpecification as a specification document able to communicate descriptive or directive information and explicitly names circular design specification as an application subclass. CircularDesignSpecification is EXTERNAL_ISSUE_DEPENDENT.

### Modularity

No exact maintained class with compatible circular-material semantics was verified in PMDco 3.1.0, LOG, IOF 202602, CCO 2.2, CEON, or AutomatCE. Stored discovery hits were unrelated qualities, subject classifications, or lexical mentions.

The intended entity is not a collection of modules. It is the degree to which a bearer is organized into separable, replaceable, or recombinable modules. BFO quality is already present in the PMDco import and supplies the correct specifically dependent continuant parent. No new import or external axiom set is required.

Modularity is READY_FOR_BATCH3_IMPLEMENTATION. Measurement and bearer restrictions remain deferred.

### Repurposing

The checked-in selected CEON v1.0.0 component contains ReuseProcess, RepairProcess, RefurbishmentProcess, RecycleProcess, TakeBackProcess, and related process axioms, but no RepurposingProcess. Those neighboring classes do not capture changing from a preceding intended purpose to a different intended purpose. AutomatCE mentions repurposing only contextually and supplies no exact process. The legacy CAMO label lacks adequate version and maintenance evidence.

The selected CEON terms are already curated into the MatSus closure. The component records CEON v1.0.0 commit 9cdcae1b68f4e9d5a55697c8e3e3f8df788fc937 and CC BY 4.0; the [current CEON repository](https://github.com/LiUSemWeb/CEON) is active and reports an MIT repository licence. This metadata discrepancy should be reconciled if further CEON terms are imported, but it does not affect this decision because no CEON repurposing term is reused.

AutomatCE v1.0.0 is current, maintained, and CC BY 4.0, but is not in the import closure and supplies no exact RepurposingProcess.

A local planned-process class is justified and READY_FOR_BATCH3_IMPLEMENTATION. Its battery specialization may be implemented in the same batch. Only asserted parent axioms are proposed.

### Resource efficiency

No maintained compatible OWL class for the intended calculated resource-efficiency result was verified in the reviewed PMD/CE sources. Stored OLS results included unrelated subject areas and processes. MeSH Efficiency supplies ratio-like wording but is biomedical terminology with weak relevant axiomatization and does not provide the required method, boundary, time, and resource-input pattern.

The intended entity records a result derived from output or service relative to resource input. It is therefore an IAO data item, not an intrinsic “efficiency” universal or BFO quality. IAO data item is already in the maintained PMDco 3.1.0 closure. UNEP informs the domain meaning but is not an OWL class source. No external ontology import is required.

ResourceEfficiencyDatum and MaterialResourceEfficiencyDatum are READY_FOR_BATCH3_IMPLEMENTATION. Calculation components remain a later instance/modelling pattern.

## VirginMaterial source-gap resolution

The earlier draft had an adequate positive modelling direction but no explicit authoritative terminology source. The gap is resolved by the ISO Online Browsing Platform entry for the [ISO/DIS 15270-1 plastics recovery and recycling draft](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso%3A15270%3A-1%3Adis%3Aed-1%3Av1%3Aen), which reproduces the ISO 21067-2:2015 concept of virgin or primary material as material never processed into an end-use product.

For MatSus, use the domain-neutral formulation:

> A material that has never been processed into any form of an end-use product.

This is a primitive MatSus subclass of PMDco material. It is not an equivalence axiom and does not imply that a mixed-content material can be classified solely from missing assertions.

Do not model NonVirginMaterial as the complement of VirginMaterial. Mixed-content materials are common, and open-world absence of virgin status does not establish non-virgin status. Use positive recovered/recycled-content assertions and the existing recovered-material anchor.

## LOG boundary for material flow

The checked-in LOG component contains:

- LOG_1000120 logistics process, a business process combining transport, shipment preparation, storage, or receiving processes;
- a transport process for movement by transport equipment;
- material location change process specializations;
- supply-chain resource and role patterns.

It contains no generic MaterialFlowProcess. The tracker proposal—movement of material entities between locations, agents, lifecycle stages, or transformation processes—partly overlaps LOG transport/location-change semantics but is broader and may also be confused with a flow quantity or flow record.

Before implementation, one competency example must determine:

1. whether material flow denotes the physical movement process, a quantity/datum describing movement, or both as separate entities;
2. whether the process belongs upstream in LOG or locally in MatSus;
3. whether movement between transformation stages is already representable through LOG/PMDco process-input/output relations;
4. which source, destination, participant, and time relations are required.

Until that review is accepted, MaterialFlowProcess is REUSE_CHECK_REQUIRED. TextileMaterialFlowProcess is DEFER because it depends on that unsettled parent. No local classes or bridge axioms are proposed now.

## External and dependent items kept separate

| Item | Owner/dependency | Current status and action |
|---|---|---|
| ProductSpecification | PMDco issue [#487](https://github.com/materialdigital/core-ontology/issues/487) | Open as of 2026-09-04. Await PMDco; do not mint a MatSus duplicate. |
| DesignSpecification | PMDco issue [#488](https://github.com/materialdigital/core-ontology/issues/488) | Open as of 2026-09-04. Await the generic mixed descriptive/directive parent. |
| CircularDesignSpecification | PMDco #488 | Await PMDco #488. If the generic PMDco DesignSpecification proposal is rejected, reconsider CircularDesignSpecification as a MatSus class. |
| FeedstockRole | PMDco issue [#486](https://github.com/materialdigital/core-ontology/issues/486) | Await PMDco #486. If accepted upstream, reuse it in MatSus; if rejected or left outside PMDco, reconsider a local MatSus class. |
| ReverseLogisticsProcess | LOG issue pending | No MatSus axiom or duplicate. Open the LOG issue when the contribution route is known. |
| MaterialFlowProcess | LOG boundary assessment | Defer pending dedicated analysis of LOG transport, material-location-change, logistics, and material-flow-datum patterns. |
| TextileMaterialFlowProcess | MaterialFlowProcess | Defer with its unsettled parent. |

The three PMDco issues were created on 2026-08-31 and remained open and unchanged when checked on 2026-09-04.

## Additional deferred modelling

- Absolute and relative decoupling classifications; baseline and comparison interval; resource-input or environmental-pressure indicator; economic or service-output indicator; calculation method; ratio and temporal relations.
- NonVirginMaterial and any logical complement of VirginMaterial.
- Feedstock bearer/realization/input restrictions pending PMDco #486.
- Circular-design relations and parent pending PMDco #488.
- Material-flow and textile-flow classes pending the LOG boundary.
- Resource-efficiency numerator, denominator, method, unit, boundary, and time relations.
- Modularity bearer and metric relations.
- Repurposing prior/new-purpose and participant restrictions.
- Battery participant restrictions.
- Resource-input-reduction baseline and target relations.
- Refill context subclasses or restrictions.
- Refusal-process agent/object/objective restrictions and every logical relation between RefusalProcess and RefusalStrategySpecification.
- Refusal-strategy relations to resource-input-reduction objectives, design specifications, affected product features, and realization.
- Remanufacturing input/output/state restrictions.
- All equivalence, disjointness, closure, complement, and cardinality axioms.

## Deferred hierarchy audit

Add the following item to a later audit backlog. It is not part of Batch 3 implementation and must not be fixed speculatively:

> Before public migration, investigate why Event, Quantity value and Unit appear as direct children of owl:Thing in the MatSus asserted hierarchy. Compare exact IRIs and parent axioms in PMDco source, pmdco_import.owl and the generated MatSus ontology. Do not add unsupported local bridge axioms.

## Human-review gates

Before any ontology implementation:

1. Approve or revise the 13-class bounded scope.
2. Approve the tentative MATSUS_0000027–MATSUS_0000039 allocation after a fresh ID check.
3. Approve the revised ISO-grounded VirginMaterial definition and provenance.
4. Confirm that FeedstockRole and CircularDesignSpecification remain outside the batch while #486 and #488 are open.
5. Confirm that MaterialFlowProcess and TextileMaterialFlowProcess remain outside the batch pending the LOG-boundary review.
6. Confirm that RefusalProcess remains the actual intentional refusal occurrence and that RefusalStrategySpecification remains a distinct plan specification, with no logical relation asserted between them in this batch.
7. Confirm that only the 13 asserted subclass axioms listed here may be added initially.

If approved, the implementation phase should update the ontology, working tracker, this planning report, and a new pre-commit handoff as separately authorized. The FINAL workbook must remain read-only.

## Planning-scope confirmation

This planning task creates only:

audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch3_NonWaste_Planning_Report_2026-09-04.md

No ontology class was implemented. The working tracker and FINAL workbook were not modified. Nothing was staged, committed, pushed, cleaned, deleted, renamed, merged, or rebased.
