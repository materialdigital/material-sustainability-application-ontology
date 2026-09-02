# MKB1 IR2 Implementation Batch 2 — Provisional Waste Cluster

**Report date:** 2026-09-02
**Scope:** Read-only implementation planning; not MKB source-mining Batch 2
**Numeric IDs:** Not allocated
**PMDco dependency:** Issue #485 — `ISSUE_SUBMITTED`

## Executive conclusion

The recommended bounded Batch 2 contains 18 provisional local MatSus classes. The batch uses a contextual waste-role pattern, retains the five human-approved waste types, and includes only the accepted processes, specifications, and analyses needed by the human-gate closure.

All 18 proposed classes are absent from the current `matsus-edit.owl` and its active local import closure. Every external parent and object property required for the minimal axioms is already present through `pmdco_import.owl`.

The human-gate migration rule is authoritative: later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions; it does not trigger deletion of MatSus specializations.

## Authoritative inputs

- `audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Implementation_Tracker_2026-08-31 (2)_working implementation.xlsx`
- `audit/mkb1-ontology-reuse-alignment/MKB1_FINAL_human-gate-completed_2026-08-31 (2)_readonly.xlsx`
- `src/ontology/matsus-edit.owl`
- `src/ontology/catalog-v001.xml`
- Existing repository imports and MKB1 audit evidence

## Tracker-state caveat

IR2 Tracker rows 5 and 21–30 contain `IMPLEMENTED_IN_MATSUS_EDIT` in the draft-status column but `NO - DRAFT ONLY` in the current-source column. Direct inspection confirms that the proposed classes are not in the current ontology. The current-source column and Class Review status `DRAFT EXISTS; NOT IN CURRENT SOURCE` reflect the actual repository state.

## Batch membership

### Approved for immediate implementation

| Tracker location | MKB ID | Concepts |
|---|---|---|
| Class Review rows 2–3 | Supporting anchors | waste role; waste material |
| IR2 Tracker row 5 / Class Review row 10 | MKB-000231 | sorting process only |
| Class Review rows 9 and 11 | Supporting processes | waste collection process; waste separation process |
| IR2 Tracker row 21 | MKB-000063 | construction and demolition waste |
| IR2 Tracker row 22 | MKB-000085 | waste-or-pollution elimination objective specification |
| IR2 Tracker row 23 | MKB-000144 | mineral waste |
| IR2 Tracker row 24 | MKB-000148 | municipal waste |
| IR2 Tracker row 25 | MKB-000155 | packaging waste |
| IR2 Tracker row 26 | MKB-000236 | waste analysis; structural waste analysis |
| IR2 Tracker row 27 | MKB-000249 | textile waste |
| IR2 Tracker row 28 | MKB-000263 | waste generation process |
| IR2 Tracker row 29 | MKB-000264 | waste prevention process; waste prevention measure specification |
| IR2 Tracker row 30 | MKB-000266 | zero-waste objective specification; zero-waste strategy specification |

### External reuse/import — outside the local Batch 2 implementation

| Human-gate location | MKB ID | Candidate | Active closure |
|---|---|---|---|
| Master Analysis row 55 | MKB-000084 | MeSH Electronic Waste — `http://id.nlm.nih.gov/mesh/D059029` | Absent |
| Master Analysis row 59 | MKB-000098 | ENVO food waste — `http://purl.obolibrary.org/obo/ENVO_03600006` | Absent |
| Master Analysis row 68 | MKB-000141 | ENVO waste material — `http://purl.obolibrary.org/obo/ENVO_00002264` | Absent |

Do not import these terms in Batch 2. Their complete dependency closures, licences, stack compatibility, and mappings require a separate reuse/import implementation assessment. ENVO waste material must not silently replace the human-approved role-based MatSus anchor.

### Dependent but deferred

- IR2 Tracker row 33, MKB-000307: end-user guidance about separate collection.
- IR2 Tracker row 36, MKB-000308: end-user guidance about waste prevention.
- `SortingMethodSpecification`, the second half of MKB-000231; it is not required to establish waste separation.
- A generic pollution class or target pattern for MKB-000085.
- Detailed temporal, participant, provenance, threshold, baseline, method, and outcome restrictions.

### Human decisions remaining after this batch

No unresolved question blocks provisional implementation. Later human decisions remain on:

- necessary-only versus equivalent-class treatment of `WasteMaterial`;
- time-indexing or contextualization of acquiring and losing a waste role;
- whether recurring-source analysis should be separated from structural/compositional waste analysis;
- placement of the packaging-waste production-residue exclusion;
- mapping between local `WasteMaterial`, ENVO waste material, and any future PMDco class.

## Import-closure findings

| Entity | Exact IRI | State |
|---|---|---|
| BFO role | `http://purl.obolibrary.org/obo/BFO_0000023` | Imported |
| PMDco material | `https://w3id.org/pmd/co/PMD_0000000` | Imported and locally declared |
| bearer of | `http://purl.obolibrary.org/obo/RO_0000087` | Imported |
| BFO process | `http://purl.obolibrary.org/obo/BFO_0000015` | Imported |
| has output | `http://purl.obolibrary.org/obo/RO_0002234` | Imported |
| COB planned process | `http://purl.obolibrary.org/obo/COB_0000082` | Imported |
| IAO plan specification | `http://purl.obolibrary.org/obo/IAO_0000104` | Imported |
| IAO objective specification | `http://purl.obolibrary.org/obo/IAO_0000005` | Imported and locally declared |
| OBI assay | `http://purl.obolibrary.org/obo/OBI_0000070` | Imported and locally declared |

All readable MatSus IRIs below are provisional planning handles from the tracker. Final numeric MatSus IRIs must be allocated only during an authorized implementation run.

## Common editorial note

Apply the following policy to every Batch 2 class, with the class-specific addenda below:

> Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions—not deletion of the MatSus specialization.

## Immediate implementation specifications

### 1. Waste role

- **MKB ID:** Supporting waste anchor
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteRole`
- **Definition:** A role borne by a material entity when its holder discards it, intends to discard it, or is required to discard it.
- **Parent:** `http://purl.obolibrary.org/obo/BFO_0000023`
- **Confirmed axiom:** `WasteRole SubClassOf BFO_0000023`
- **Provenance:** Class Review row 2; human-gate Closure; PMDco #485.
- **Editorial addendum:** Waste status is contextual and role-based, not an intrinsic material kind.
- **Later constraint:** Decide realization/context relations and the future PMDco mapping.
- **Dependencies/confidence:** Imported BFO role; **HIGH**.

### 2. Waste material

- **MKB ID:** Supporting waste anchor
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteMaterial`
- **Definition:** A material that bears a waste role.
- **Parent:** `https://w3id.org/pmd/co/PMD_0000000`
- **Confirmed axioms:** `WasteMaterial SubClassOf PMD_0000000`; `WasteMaterial SubClassOf RO_0000087 some WasteRole`.
- **Provenance:** Class Review row 3; human-gate Closure; PMDco #485.
- **Editorial addendum:** Use *waste* as an alternative label. Do not make recovered material a subclass of waste material.
- **Later constraint:** Decide necessary-only versus equivalence and select a temporal/context model.
- **Dependencies/confidence:** WasteRole, PMDco material, `RO_0000087`; **HIGH**.

### 3. Construction and demolition waste

- **MKB ID:** MKB-000063
- **Provisional IRI:** `https://w3id.org/pmd/matsus/ConstructionAndDemolitionWaste`
- **Definition:** A waste material that arises from construction or demolition activities.
- **Parent/axiom:** `ConstructionAndDemolitionWaste SubClassOf WasteMaterial`.
- **Provenance:** SRC-001 Circular Berlin; Master Analysis row 52.
- **Editorial addendum:** Retain this local subtype after any upstream anchor migration.
- **Later constraint:** Add source/provenance criteria only if required by data integration.
- **Dependencies/confidence:** WasteMaterial; **HIGH**.

### 4. Mineral waste

- **MKB ID:** MKB-000144
- **Provisional IRI:** `https://w3id.org/pmd/matsus/MineralWaste`
- **Definition:** A waste material composed predominantly of mineral matter.
- **Parent/axiom:** `MineralWaste SubClassOf WasteMaterial`.
- **Provenance:** SRC-003 European Environment Agency; Master Analysis row 69.
- **Editorial addendum:** *Predominantly* is intentionally not assigned an OWL cutoff.
- **Later constraint:** Represent thresholds through data or a classification specification.
- **Dependencies/confidence:** WasteMaterial; **MEDIUM**.

### 5. Municipal waste

- **MKB ID:** MKB-000148
- **Provisional IRI:** `https://w3id.org/pmd/matsus/MunicipalWaste`
- **Definition:** A waste material collected from households or a waste material from another source that is similar in nature and composition to household waste.
- **Parent/axiom:** `MunicipalWaste SubClassOf WasteMaterial`.
- **Provenance:** SRC-003 European Environment Agency; Master Analysis row 71.
- **Editorial addendum:** Record *municipal solid waste* as an alternative label, not an equivalent class.
- **Later constraint:** Assert equivalence only if the scopes are confirmed identical.
- **Dependencies/confidence:** WasteMaterial; **HIGH**.

### 6. Packaging waste

- **MKB ID:** MKB-000155
- **Provisional IRI:** `https://w3id.org/pmd/matsus/PackagingWaste`
- **Definition:** A waste material that was packaging or packaging material before it acquired a waste role.
- **Parent/axiom:** `PackagingWaste SubClassOf WasteMaterial`.
- **Provenance:** SRC-003 European Environment Agency; Master Analysis row 74. TransformON exact-label evidence was insufficient for reuse.
- **Editorial addendum:** The selected source scope excludes production residues.
- **Later constraint:** Represent former packaging status and the exclusion only with a validated pattern.
- **Dependencies/confidence:** WasteMaterial; **MEDIUM**.

### 7. Textile waste

- **MKB ID:** MKB-000249
- **Provisional IRI:** `https://w3id.org/pmd/matsus/TextileWaste`
- **Definition:** A waste material composed predominantly of textile material or discarded textile products.
- **Parent/axiom:** `TextileWaste SubClassOf WasteMaterial`.
- **Provenance:** SRC-001 Circular Berlin; Master Analysis row 111.
- **Editorial addendum:** Intentionally broad provisional subtype.
- **Later constraint:** Add fibre, composition, or product-type refinements only from concrete use cases.
- **Dependencies/confidence:** WasteMaterial; **MEDIUM**.

### 8. Waste collection process

- **MKB ID:** Supporting waste process
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteCollectionProcess`
- **Definition:** A planned process in which waste material is gathered from one or more holders or locations for transport, storage, sorting, recovery, treatment, or disposal.
- **Parent:** `http://purl.obolibrary.org/obo/COB_0000082`
- **Confirmed axiom:** `WasteCollectionProcess SubClassOf COB_0000082`.
- **Provenance:** Class Review row 9; human-gate Closure related-terms decision.
- **Editorial addendum:** Supporting process with no standalone MKB ID.
- **Later constraint:** Add waste participant, origin, destination, and responsible-agent relations.
- **Dependencies/confidence:** COB planned process; WasteMaterial semantically; **HIGH**.

### 9. Sorting process

- **MKB ID:** MKB-000231 supporting class
- **Provisional IRI:** `https://w3id.org/pmd/matsus/SortingProcess`
- **Definition:** A planned process in which material entities are assigned to different groups or streams according to specified criteria.
- **Parent:** `http://purl.obolibrary.org/obo/COB_0000082`
- **Confirmed axiom:** `SortingProcess SubClassOf COB_0000082`.
- **Provenance:** SRC-001 Circular Berlin; Master Analysis row 106; no acceptable maintained equivalent found.
- **Editorial addendum:** Only the process half of MKB-000231 is needed in this batch.
- **Later constraint:** Connect criteria/method specifications and sorted inputs/outputs.
- **Dependencies/confidence:** COB planned process; **HIGH**.

### 10. Waste separation process

- **MKB ID:** Supporting waste process
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteSeparationProcess`
- **Definition:** A sorting process in which waste material is assigned to different groups or streams according to specified criteria.
- **Parent/axiom:** `WasteSeparationProcess SubClassOf SortingProcess`.
- **Provenance:** Class Review row 11; human-gate Closure related-terms decision.
- **Editorial addendum:** Supporting process with no standalone MKB ID.
- **Later constraint:** Add waste input and separated-stream output restrictions after example testing.
- **Dependencies/confidence:** SortingProcess; WasteMaterial semantically; **HIGH**.

### 11. Waste generation process

- **MKB ID:** MKB-000263
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteGenerationProcess`
- **Definition:** A process that has as output a material entity that bears a waste role.
- **Parent:** `http://purl.obolibrary.org/obo/BFO_0000015`
- **Confirmed axioms:** `WasteGenerationProcess SubClassOf BFO_0000015`; `WasteGenerationProcess SubClassOf RO_0002234 some WasteMaterial`.
- **Provenance:** SRC-003 European Environment Agency; Master Analysis row 115.
- **Editorial addendum:** Generation is not assumed to be planned production or synthesis.
- **Later constraint:** Distinguish planned and unplanned generation through context unless required otherwise.
- **Dependencies/confidence:** WasteMaterial, BFO process, `RO_0002234`; **HIGH**.

### 12. Waste prevention process

- **MKB ID:** MKB-000264
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WastePreventionProcess`
- **Definition:** A planned process that is intended to reduce the quantity or harmfulness of waste generated, or the adverse impacts of generated waste on the environment and human health.
- **Parent:** `http://purl.obolibrary.org/obo/COB_0000082`
- **Confirmed axiom:** `WastePreventionProcess SubClassOf COB_0000082`.
- **Provenance:** SRC-001 Circular Berlin; SRC-003 European Environment Agency; Master Analysis row 116.
- **Editorial addendum:** Keep the performed process distinct from its measure specification.
- **Later constraint:** Relate the process to targeted streams and prevention outcomes.
- **Dependencies/confidence:** COB planned process; **HIGH**.

### 13. Waste prevention measure specification

- **MKB ID:** MKB-000264
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WastePreventionMeasureSpecification`
- **Definition:** A plan specification that prescribes actions intended to realize a waste prevention process.
- **Parent:** `http://purl.obolibrary.org/obo/IAO_0000104`
- **Confirmed axiom:** `WastePreventionMeasureSpecification SubClassOf IAO_0000104`.
- **Provenance:** Same MKB-000264 sources and decision.
- **Editorial addendum:** This is an information artifact, not a process.
- **Later constraint:** Connect it to the prescribed process.
- **Dependencies/confidence:** IAO plan specification; WastePreventionProcess semantically; **HIGH**.

### 14. Zero-waste objective specification

- **MKB ID:** MKB-000266
- **Provisional IRI:** `https://w3id.org/pmd/matsus/ZeroWasteObjectiveSpecification`
- **Definition:** An objective specification that describes an intended endpoint in which waste generation and disposal are prevented or minimized through responsible production, consumption, reuse, and recovery.
- **Parent:** `http://purl.obolibrary.org/obo/IAO_0000005`
- **Confirmed axiom:** `ZeroWasteObjectiveSpecification SubClassOf IAO_0000005`.
- **Provenance:** SRC-001 Circular Berlin; Master Analysis row 117.
- **Editorial addendum:** Zero waste is normative information content, not a material or process.
- **Later constraint:** Represent scope, baseline, and tolerated residual waste if needed.
- **Dependencies/confidence:** IAO objective specification; **HIGH**.

### 15. Zero-waste strategy specification

- **MKB ID:** MKB-000266
- **Provisional IRI:** `https://w3id.org/pmd/matsus/ZeroWasteStrategySpecification`
- **Definition:** A plan specification that prescribes actions intended to achieve a zero-waste objective.
- **Parent:** `http://purl.obolibrary.org/obo/IAO_0000104`
- **Confirmed axiom:** `ZeroWasteStrategySpecification SubClassOf IAO_0000104`.
- **Provenance:** Same MKB-000266 source and decision.
- **Editorial addendum:** Keep the strategy distinct from its objective.
- **Later constraint:** Relate it to the objective and prescribed prevention, reuse, and recovery processes.
- **Dependencies/confidence:** IAO plan specification; ZeroWasteObjectiveSpecification semantically; **HIGH**.

### 16. Waste-or-pollution elimination objective specification

- **MKB ID:** MKB-000085
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteOrPollutionEliminationObjectiveSpecification`
- **Definition:** An objective specification that describes an intended endpoint in which a specified waste or pollution output is absent.
- **Parent:** `http://purl.obolibrary.org/obo/IAO_0000005`
- **Confirmed axiom:** `WasteOrPollutionEliminationObjectiveSpecification SubClassOf IAO_0000005`.
- **Provenance:** SRC-002 Ellen MacArthur Foundation; Master Analysis row 56.
- **Editorial addendum:** Do not create an undefined generic elimination process.
- **Later constraint:** Link to a scoped target and boundary after the pollution pattern is resolved.
- **Dependencies/confidence:** IAO objective specification; pollution target deferred; **MEDIUM**.

### 17. Waste analysis

- **MKB ID:** MKB-000236
- **Provisional IRI:** `https://w3id.org/pmd/matsus/WasteAnalysis`
- **Definition:** An assay intended to produce information about waste material, a waste-generating process, or a waste stream.
- **Parent:** `http://purl.obolibrary.org/obo/OBI_0000070`
- **Confirmed axiom:** `WasteAnalysis SubClassOf OBI_0000070`.
- **Provenance:** SRC-001 Circular Berlin; Master Analysis row 107.
- **Editorial addendum:** Analysis is an assay, not the information output itself.
- **Later constraint:** Add evaluant, method, and output-datum relations using a concrete example.
- **Dependencies/confidence:** OBI assay; **HIGH**.

### 18. Structural waste analysis

- **MKB ID:** MKB-000236
- **Provisional IRI:** `https://w3id.org/pmd/matsus/StructuralWasteAnalysis`
- **Definition:** A waste analysis intended to produce information about the composition, organization, distribution, or recurring generation patterns of a waste stream or waste-generating system.
- **Parent/axiom:** `StructuralWasteAnalysis SubClassOf WasteAnalysis`.
- **Provenance:** Same MKB-000236 source and decision.
- **Editorial addendum:** Broad provisional scope retained under the authoritative implementation decision.
- **Later constraint:** Decide whether recurring-source analysis should become a sibling of structural/compositional analysis.
- **Dependencies/confidence:** WasteAnalysis; **MEDIUM**.

## Ontological coherence of the role/material pattern

The pattern is coherent when implemented with necessary axioms only:

```text
WasteRole SubClassOf BFO role

WasteMaterial SubClassOf PMDco material
WasteMaterial SubClassOf bearer_of some WasteRole
```

This does not assert that every material is waste or that waste status is intrinsic. Only instances classified under `WasteMaterial` inherit the requirement to bear a `WasteRole`.

Constraints:

- Do not define `WasteMaterial` as an intrinsic material kind without the role restriction.
- Do not make `RecoveredMaterial` a subclass of `WasteMaterial`.
- Do not assert disjointness between recovered material and waste material.
- Do not add an equivalent-class definition in Batch 2.
- Do not encode permanent acquisition or loss of the role until a temporal/context pattern is selected.
- The five waste subtypes may inherit the role restriction through `WasteMaterial`.

This remains consistent with Batch 1: recovery provenance can remain true after a material stops bearing a waste role.

## Recommended implementation order

1. Check repository ID policy and allocate collision-free numeric MatSus IDs during the authorized implementation run.
2. Add locally required declarations for imported parents and properties.
3. Implement `WasteRole`.
4. Implement `WasteMaterial` and its necessary role restriction.
5. Implement the five waste-material subtypes.
6. Implement `SortingProcess`.
7. Implement collection, separation, generation, and prevention processes.
8. Implement prevention-measure, zero-waste, and elimination-objective specifications.
9. Implement `WasteAnalysis`, then `StructuralWasteAnalysis`.
10. Update only the corresponding tracker and Class Review records.
11. Run syntax, reasoner/build, profile, duplicate-IRI, IRI-range, import-resolution, and diff checks before staging.

## Ready-to-use implementation prompt

```text
Work from the MatSus repository root.

Implement MKB1 IR2 implementation Batch 2 — provisional waste cluster.
This is not MKB source-mining Batch 2.

Use as authoritative inputs:
- the working MKB1 IR2 implementation tracker;
- the read-only MKB1 FINAL human-gate workbook;
- src/ontology/matsus-edit.owl;
- existing repository imports and audit evidence.

Human decisions:
- Implement the provisional MatSus waste pattern now.
- PMDco issue #485 is ISSUE_SUBMITTED.
- Later PMDco acceptance triggers migration/reconciliation, not deletion.
- Use role-based waste modelling and necessary-only restrictions.
- Do not make recovered material a subclass of waste material.
- Do not add disjointness, complements, or equivalence axioms.

Implement exactly these 18 classes:
1. waste role
2. waste material
3. construction and demolition waste
4. mineral waste
5. municipal waste
6. packaging waste
7. textile waste
8. waste collection process
9. sorting process
10. waste separation process
11. waste generation process
12. waste prevention process
13. waste prevention measure specification
14. zero-waste objective specification
15. zero-waste strategy specification
16. waste-or-pollution elimination objective specification
17. waste analysis
18. structural waste analysis

Use the exact definitions, sources, parents, confidence assessments,
editorial constraints, and confirmed axioms in the tracker Class Review:
- rows 2–18 for anchors, types, processes, specifications, and analyses;
- row 25 for waste-or-pollution elimination objective specification.

Use these exact imported entities:
- BFO role: http://purl.obolibrary.org/obo/BFO_0000023
- PMDco material: https://w3id.org/pmd/co/PMD_0000000
- bearer of: http://purl.obolibrary.org/obo/RO_0000087
- BFO process: http://purl.obolibrary.org/obo/BFO_0000015
- has output: http://purl.obolibrary.org/obo/RO_0002234
- COB planned process: http://purl.obolibrary.org/obo/COB_0000082
- IAO plan specification: http://purl.obolibrary.org/obo/IAO_0000104
- IAO objective specification: http://purl.obolibrary.org/obo/IAO_0000005
- OBI assay: http://purl.obolibrary.org/obo/OBI_0000070

Required non-parent restrictions:
- WasteMaterial bearer_of some WasteRole.
- WasteGenerationProcess has_output some WasteMaterial.

Allocate final numeric IDs only after checking repository policy and current
IDs. Treat readable tracker IRIs as provisional planning handles.

Do not import or duplicate in this batch:
- MKB-000084 MeSH Electronic Waste;
- MKB-000098 ENVO food waste;
- MKB-000141 ENVO waste material.

Keep deferred:
- MKB-000307;
- MKB-000308;
- SortingMethodSpecification;
- a generic pollution class/pattern;
- detailed temporal, threshold, participant, baseline, method, provenance,
  and outcome axioms.

Update only affected tracker records: IR2 Tracker rows 5 and 21–30 and the
corresponding Class Review records. Verify actual ontology state rather than
carrying forward the stale IMPLEMENTED_IN_MATSUS_EDIT draft-status value.

Validate ontology parsing, the full build, reasoner consistency, OWL profile,
numeric-ID uniqueness/range, imports, exact axioms, and scoped Git diffs.
Run git diff --check.

Do not modify unrelated files. Do not stage, commit, push, merge, clean,
delete, create a branch, or switch branches unless separately instructed.
Report results and stop for review.
```

## Planning-pass repository state

The planning pass made no ontology, tracker, branch, index, or Git-history changes. At the time of planning, `mkb1-ir2-batch1` was synchronized with `origin/mkb1-ir2-batch1`, and only pre-existing untracked files were present.
