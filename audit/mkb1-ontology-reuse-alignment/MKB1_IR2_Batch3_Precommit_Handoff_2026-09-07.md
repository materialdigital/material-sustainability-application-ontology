# MKB1 IR2 Batch 3 Pre-Commit Handoff

**Date:** 2026-09-07
**Branch:** mkb1-ir2-batch3-nonwaste
**Starting HEAD and upstream:** c2bf8cc29266444e2f90c223680c64c69695b3f2
**Main comparison commit:** 5e56b8c0c8c079451f7a153d89f52e16cb712f67
**Scope:** Approved 13-class MKB1 IR2 Batch 3 non-waste implementation
**Commit/push:** Not performed

## Outcome

The approved scope is implemented in src/ontology/matsus-edit.owl as MATSUS_0000027 through MATSUS_0000039. The tracker and planning report are synchronized with the ontology.

No existential or universal restriction, equivalence, disjointness, complement, cardinality, property-chain, closure, new import, or logical relation between RefusalProcess and RefusalStrategySpecification was added. NonVirginMaterial, AbsoluteDecoupling, FeedstockRole, CircularDesignSpecification, MaterialFlowProcess, and TextileMaterialFlowProcess were not added.

## Implemented classes

| # | Final IRI | Label | Final definition | Asserted parent |
|---:|---|---|---|---|
| 1 | MATSUS_0000027 | metric specification | A directive information entity that prescribes the quantities, calculation method, units, boundary, and interpretation used to produce a quantitative indicator datum. | IAO_0000033 |
| 2 | MATSUS_0000028 | resource efficiency datum | A data item that records the useful output, service, or value obtained per stated quantity of resource input under a specified method, boundary, and time interval. | IAO_0000027 |
| 3 | MATSUS_0000029 | material resource efficiency datum | A resource efficiency datum whose stated resource input is a quantity of material. | MATSUS_0000028 |
| 4 | MATSUS_0000030 | virgin material | A material that has never been processed into any form of an end-use product. | PMD_0000000 |
| 5 | MATSUS_0000031 | repurposing process | A planned process in which a product, component, or material is prepared or modified so that it can fulfil a purpose different from its preceding intended purpose. | COB_0000082 |
| 6 | MATSUS_0000032 | battery repurposing process | A repurposing process whose primary participant is a battery or battery component. | MATSUS_0000031 |
| 7 | MATSUS_0000033 | resource-input reduction process | A planned process intended to reduce the amount of material input used by a specified process or system. | COB_0000082 |
| 8 | MATSUS_0000034 | refill process | A planned process in which a product container or dispensing device is supplied again with a material product for further use without first becoming waste. | COB_0000082 |
| 9 | MATSUS_0000035 | refusal process | A planned process in which an agent intentionally declines to acquire, accept, or use a specified product, material, or service in order to avoid its associated resource use or waste generation. | COB_0000082 |
| 10 | MATSUS_0000036 | remanufacturing process | A planned process in which a used product or component is restored to a specified performance and quality state through inspection and one or more restorative operations. | COB_0000082 |
| 11 | MATSUS_0000037 | decoupling datum | A data item that records a comparison over a stated time interval in which the rate of change of a resource input or environmental pressure is lower than the rate of change of a specified economic or service output. | IAO_0000027 |
| 12 | MATSUS_0000038 | modularity | A quality of an entity that reflects the degree to which its parts are organized into separable, replaceable, or recombinable modules. | BFO_0000019 |
| 13 | MATSUS_0000039 | refusal strategy specification | A plan specification that prescribes product, packaging, or service features intended to enable or encourage a refusal process and thereby avoid material use or waste generation. | IAO_0000104 |

MATSUS_0000039 additionally has the approved English rdfs:comment:

> Examples include optional packaging, opt-out disposable accessories, and service provision that avoids supplying a material product. This class denotes the strategy specification; the actual refusal occurrence is represented by refusal process.

## Provenance

- MATSUS_0000027: ADD-SCO-012; SCO.
- MATSUS_0000028: MKB-000205; SRC-001 Circular Berlin; UNEP domain meaning.
- MATSUS_0000029: MKB-000137; SRC-003 European Environment Agency.
- MATSUS_0000030: MKB-000150; SRC-002 Ellen MacArthur Foundation; ISO 21067-2:2015 terminology reproduced in ISO/DIS 15270-1.
- MATSUS_0000031: MKB-000202; SRC-001 Circular Berlin.
- MATSUS_0000032: MKB-000009; SRC-002 Ellen MacArthur Foundation.
- MATSUS_0000033: MKB-000180; SRC-001 Circular Berlin.
- MATSUS_0000034: MKB-000181 and MKB-000182; SRC-002 Ellen MacArthur Foundation.
- MATSUS_0000035: MKB-000184; SRC-001 Circular Berlin.
- MATSUS_0000036: MKB-000189; SRC-003 European Environment Agency.
- MATSUS_0000037: MKB-000002, SRC-003 European Environment Agency; MKB-000069, SRC-002 Ellen MacArthur Foundation.
- MATSUS_0000038: MKB-000146; SRC-002 Ellen MacArthur Foundation.
- MATSUS_0000039: human-gate refinement derived from the MKB-000184 review and the 2026-09-04 Batch 3 review; not a seventeenth original source candidate.

## Annotation and logical-axiom counts

| Item | Count |
|---|---:|
| Class declarations | 13 |
| English rdfs:label | 13 |
| English skos:definition | 13 |
| dcterms:source | 13 |
| skos:editorialNote | 13 |
| integrationMethod | 13 |
| English rdfs:comment | 1, on MATSUS_0000039 only |
| Asserted subclass axioms | 13 |
| Other new logical axioms | 0 |

The local RDF graph has 92 new triples whose subjects are the 13 new classes. ROBOT's no-import serialization additionally emits declarations for the already imported parents IAO_0000033 and BFO_0000019. Those serializer-generated declarations do not represent source or logical-axiom additions.

## Exact logical axioms

~~~text
MATSUS_0000027 SubClassOf IAO_0000033
MATSUS_0000028 SubClassOf IAO_0000027
MATSUS_0000029 SubClassOf MATSUS_0000028
MATSUS_0000030 SubClassOf PMD_0000000
MATSUS_0000031 SubClassOf COB_0000082
MATSUS_0000032 SubClassOf MATSUS_0000031
MATSUS_0000033 SubClassOf COB_0000082
MATSUS_0000034 SubClassOf COB_0000082
MATSUS_0000035 SubClassOf COB_0000082
MATSUS_0000036 SubClassOf COB_0000082
MATSUS_0000037 SubClassOf IAO_0000027
MATSUS_0000038 SubClassOf BFO_0000019
MATSUS_0000039 SubClassOf IAO_0000104
~~~

## Tracker changes

- Updated 13 consolidated Class Review records: rows 19, 21–24, 26–30, 32, 35, and new row 47.
- Updated the corresponding original-source IR2 Tracker rows 3, 7–15, and 17–20. Rows 11–12 still map to one RefillProcess, and rows 17–18 still map to one DecouplingDatum.
- Added IR2 Tracker row 43 and Class Review row 47 for RefusalStrategySpecification, explicitly identifying it as a human-gate refinement rather than an original source candidate.
- Recorded final IDs, definitions, parents, provenance, integration methods, validation results, editorial decisions, and deferred modelling.
- Updated IR2 Tracker rows 4 and 6 and Class Review rows 31 and 36 to preserve the PMDco-dependent CircularDesignSpecification and FeedstockRole exclusions.
- Updated IR2 Tracker row 16 and Class Review rows 33–34 to preserve the MaterialFlowProcess and TextileMaterialFlowProcess deferrals.
- Extended the existing Start Here formula ranges in B6, B7, and B10 through IR2 Tracker row 43. All six workbook formulas remain formulas.
- Preserved all four sheets, merged cells, validations, hyperlinks, freeze panes, filters, and existing-cell styles. New rows use established styles.
- Workbook ZIP integrity and openpyxl reload passed.
- Tracker SHA-256 changed from E8DA3CA6E07A72FB876491A03B7C453F8CF9329770940F1D09E63AB2CB40ADF5 to 117D9ECD466F43687683C3F3E3BBB53135D152ECF6FDBBB4125289C59CBBF087.

## Planning-report changes

The planning report retains its decision history, focused reuse checks, excluded candidates, and deferred modelling. It now records approval and implementation of the 13-class scope, final ID use, exact annotation and logical limits, tracker synchronization, validation results, ROBOT comparison with main, and protected-workbook status. Its original planning-only checkpoint remains clearly labelled as historical.

## Deferred and external items

- FeedstockRole remains outside Batch 3 pending PMDco issue #486. Reuse it if accepted upstream; otherwise reconsider a local class.
- CircularDesignSpecification remains outside Batch 3 pending PMDco issue #488. Reconsider it locally only if the generic PMDco DesignSpecification proposal is rejected.
- MaterialFlowProcess remains deferred pending dedicated analysis of LOG transport, material-location-change, logistics, and material-flow-datum patterns.
- TextileMaterialFlowProcess remains deferred with its unsettled parent.
- ProductSpecification remains with PMDco issue #487; ReverseLogisticsProcess remains a pending LOG handoff.
- Absolute and relative decoupling classifications, indicators, baseline, comparison interval, calculation method, ratio, and temporal relations remain deferred.
- Metric calculation relations; resource-efficiency inputs and outputs; material composition and proportion; repurposing purposes and participants; reduction baselines; refill context; refusal agents and objects; remanufacturing state; and modularity bearer/measurement relations remain deferred.
- The existing positive SecondaryMaterial class MATSUS_0000003 is used. NonVirginMaterial and a complement axiom were not added.
- Relations among RefusalProcess, RefusalStrategySpecification, objective specifications, design specifications, affected product features, and realization remain deferred.

## Deferred hierarchy audit

Before public migration, investigate why Event, Quantity value and Unit appear as direct children of owl:Thing in the MatSus asserted hierarchy. Compare exact IRIs and parent axioms in PMDco source, pmdco_import.owl and the generated MatSus ontology. Do not add unsupported local bridge axioms.

No bridge axiom was added in Batch 3.

## Protected FINAL workbook

The FINAL workbook remained strictly read-only.

- SHA-256 before implementation: 8A48C3A5F03337041C89A5CB3D4FCB7BC9BFB9303C67AC4031DAD02A5844BF67
- SHA-256 after implementation: 8A48C3A5F03337041C89A5CB3D4FCB7BC9BFB9303C67AC4031DAD02A5844BF67
- Result: unchanged.

## Validation environment

- Java: OpenJDK 17.0.19.
- ROBOT: 1.9.10.
- ROBOT jar SHA-256: 16A73C074F3DF359A7338A84B4E0788785FE06117F931BB9796E9619EA776105.
- RDFLib: 7.6.0.
- openpyxl: 3.1.5.
- Validation artifacts: `%TEMP%\matsus-ir2-batch3-validation-20260907`.
- GNU Make, Docker, and dicer-cli were unavailable. The repository's untracked ROBOT 1.9.2 jar was not modified; ROBOT 1.9.10 was used from system temp for ODK v1.6 option compatibility.

No validation artifact was written into the repository, and generated matsus.ttl was not modified.

## Validation commands

~~~powershell
robot --catalog src/ontology/catalog-v001.xml convert --input src/ontology/matsus-edit.owl --format ofn
robot --catalog src/ontology/catalog-v001.xml remove --input src/ontology/matsus-edit.owl --select imports --trim false
robot validate-profile --profile DL --input <batch3-noimports.owl>
robot --catalog src/ontology/catalog-v001.xml merge --input src/ontology/matsus-edit.owl
robot validate-profile --profile DL --input <batch3-merged.owl>
robot reason --input <batch3-merged.owl> --reasoner ELK --equivalent-classes-allowed asserted-only --exclude-tautologies structural
robot --catalog src/ontology/catalog-v001.xml --add-prefixes src/ontology/config/context.json merge --input src/ontology/matsus-edit.owl reason --reasoner ELK --equivalent-classes-allowed asserted-only --exclude-tautologies structural relax --include-subclass-of true reduce --reasoner ELK --include-subproperties true annotate ...
robot verify --input <batch3-merged.owl> --queries src/sparql/*-violation.sparql
robot report --input <batch3-merged.owl> --labels true --fail-on None --base-iri https://w3id.org/pmd/matsus/
git diff --check
git diff --cached --check
~~~

Every ontology command was also run against the main comparison source from commit 5e56b8c0c8c079451f7a153d89f52e16cb712f67 where a baseline comparison was required.

## Validation results and comparison with main

1. **Functional Syntax parsing — PASS.** Batch 3 and main converted successfully.
2. **Local-source OWL 2 DL — PASS.** Both no-import sources are in profile.
3. **Catalog merge — PASS.** Both merged graphs have zero remaining owl:imports axioms.
4. **Merged OWL 2 DL — PASS.** Both catalog-merged closures are in profile under ROBOT 1.9.10.
5. **ELK reasoning and consistency — PASS.** Batch 3 and main reasoned successfully with no inconsistency or unsatisfiable-class error.
6. **ODK-compatible full build — PASS.** The merge → ELK → relax → reduce → annotate sequence completed for Batch 3 and main.
7. **IDs — PASS.** MATSUS_0000001 through MATSUS_0000039 are each declared once; Batch 3 IDs are unique and satisfy the seven-digit 0–9999 allocation policy.
8. **Declarations, parents, annotations, and logical limits — PASS.** All exact counts above hold. The only Batch 3 logical axioms are the 13 asserted parents. Imports are unchanged.
9. **Forbidden classes and axioms — PASS.** No deferred class, restriction, equivalence, disjointness, complement, or refusal process/strategy relation was added.
10. **Repository SPARQL — PASS.** owldef-self-reference, iri-range, label-with-iri, multiple-replaced_by, and dc-properties each return zero for Batch 3 and main.
11. **ROBOT report — BASELINE-EXPLAINED WARNINGS.** Batch 3 has 58 warnings and no errors; main has 45 warnings and no errors. The +13 is exactly one missing_definition warning per new class because the default rule does not count the required English skos:definition. The one annotation_whitespace warning is unchanged.
12. **Workbook integrity — PASS.** ZIP, openpyxl reload, four-sheet topology, formulas, merges, validations, hyperlinks, filters, freeze panes, and expected styles pass.
13. **git diff --check — PASS.** No whitespace error; only expected Windows LF-to-CRLF notices appear.
14. **git diff --cached --check — PASS.** The staged four-file set has no whitespace errors.

## Pre-commit staging

Only these four paths are authorized and intended for staging:

1. src/ontology/matsus-edit.owl
2. audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Implementation_Tracker_2026-08-31 (2)_working implementation.xlsx
3. audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch3_NonWaste_Planning_Report_2026-09-04.md
4. audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch3_Precommit_Handoff_2026-09-07.md

**Exact staged paths:** verified as the four paths listed above; no additional path is staged.

**Staged diff/stat:** planning report 21 insertions and 5 deletions; handoff 191 insertions; tracker binary 34315 to 35834 bytes; ontology 131 insertions; total 4 files changed, 343 insertions and 5 deletions.

No commit or push has been performed. The implementation must stop after final staging for human review.
