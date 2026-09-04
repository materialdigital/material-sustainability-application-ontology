# MKB1 IR2 Batch 2 Pre-Commit Handoff

**Date:** 2026-09-04
**Branch:** mkb1-ir2-batch2-waste
**Starting HEAD:** a26d1d2c68f2c7e45e34251744b403f7960c88fe
**Scope:** Corrected 20-class MKB1 IR2 Batch 2 waste implementation
**Commit/push:** Not performed

## Outcome

The corrected 20-class scope is implemented in src/ontology/matsus-edit.owl with numeric MatSus IRIs MATSUS_0000007 through MATSUS_0000026, the required hierarchy, and only the two approved non-parent existential restrictions. The tracker and planning report are synchronized with the ontology.

No equivalent-class, disjointness, complement, temporal, threshold, baseline, method, result, additional participant/input/output/target, generic System, pollution-class, ENVO, or MeSH axioms were added. Recovered material was not made a subclass of waste material. Ontology imports did not change.

## Implemented classes

| # | Final IRI | Label | Final definition | Asserted parent |
|---:|---|---|---|---|
| 1 | MATSUS_0000007 | waste role | A role borne by a material entity when its holder discards it, intends to discard it, or is required to discard it. | BFO_0000023 |
| 2 | MATSUS_0000008 | waste material | A material that bears a waste role. | PMD_0000000 |
| 3 | MATSUS_0000009 | construction and demolition waste | A waste material that arises from construction or demolition activities. | MATSUS_0000008 |
| 4 | MATSUS_0000010 | mineral waste | A waste material composed predominantly of mineral matter. | MATSUS_0000008 |
| 5 | MATSUS_0000011 | municipal waste | A waste material collected from households or a waste material from another source that is similar in nature and composition to household waste. | MATSUS_0000008 |
| 6 | MATSUS_0000012 | packaging waste | A waste material that was packaging or packaging material before it acquired a waste role. | MATSUS_0000008 |
| 7 | MATSUS_0000013 | textile waste | A waste material composed predominantly of textile material or discarded textile products. | MATSUS_0000008 |
| 8 | MATSUS_0000014 | collection system | An object aggregate whose members are organized to enable one or more collection processes. | BFO_0000027 |
| 9 | MATSUS_0000015 | waste collection process | A planned process in which waste material is gathered from one or more holders or locations for transport, storage, sorting, recovery, treatment, or disposal. | COB_0000082 |
| 10 | MATSUS_0000016 | sorting process | A planned process in which material entities are assigned to different groups or streams according to specified criteria. | COB_0000082 |
| 11 | MATSUS_0000017 | sorting method specification | A plan specification that prescribes how a sorting process is to be carried out. | IAO_0000104 |
| 12 | MATSUS_0000018 | waste separation process | A sorting process in which waste material is assigned to different groups or streams according to specified criteria. | MATSUS_0000016 |
| 13 | MATSUS_0000019 | waste generation process | A process that has as output a material entity that bears a waste role. | BFO_0000015 |
| 14 | MATSUS_0000020 | waste prevention process | A planned process that is intended to reduce the quantity or harmfulness of waste generated, or the adverse impacts of generated waste on the environment and human health. | COB_0000082 |
| 15 | MATSUS_0000021 | waste prevention measure specification | A plan specification that prescribes actions intended to realize a waste prevention process. | IAO_0000104 |
| 16 | MATSUS_0000022 | zero-waste objective specification | An objective specification that describes an intended endpoint in which waste generation and disposal are prevented or minimized through responsible production, consumption, reuse, and recovery. | IAO_0000005 |
| 17 | MATSUS_0000023 | zero-waste strategy specification | A plan specification that prescribes actions intended to achieve a zero-waste objective. | IAO_0000104 |
| 18 | MATSUS_0000024 | waste elimination objective specification | An objective specification that specifies the intended absence of a specified waste output within a stated scope. | IAO_0000005 |
| 19 | MATSUS_0000025 | waste analysis | An assay intended to produce information about waste material, a waste-generating process, or a waste stream. | OBI_0000070 |
| 20 | MATSUS_0000026 | structural waste analysis | A waste analysis intended to produce information about the composition, organization, or distribution of material constituents within a waste material or waste stream. | MATSUS_0000025 |

Exact external parent IRIs:

- BFO_0000015: http://purl.obolibrary.org/obo/BFO_0000015
- BFO_0000023: http://purl.obolibrary.org/obo/BFO_0000023
- BFO_0000027: http://purl.obolibrary.org/obo/BFO_0000027
- COB_0000082: http://purl.obolibrary.org/obo/COB_0000082
- IAO_0000005: http://purl.obolibrary.org/obo/IAO_0000005
- IAO_0000104: http://purl.obolibrary.org/obo/IAO_0000104
- OBI_0000070: http://purl.obolibrary.org/obo/OBI_0000070
- PMD_0000000: https://w3id.org/pmd/co/PMD_0000000

Alternative labels: MATSUS_0000008 has “waste”; MATSUS_0000011 has “municipal solid waste”.

Every class has exactly one English rdfs:label, one English skos:definition, one dcterms:source, one skos:editorialNote, and one integrationMethod.

## Logical axioms added

The 20 asserted parent axioms are given by the parent column above and each occurs exactly once. The only non-parent restrictions are:

~~~text
MATSUS_0000008 SubClassOf RO_0000087 some MATSUS_0000007
MATSUS_0000019 SubClassOf RO_0002234 some MATSUS_0000008
~~~

RO_0000087 is referred to by its standard label “has role”. Both restrictions are necessary conditions only.

## Tracker changes

- Updated exactly 20 Class Review records: rows 2–18, 20, 25, and 37.
- Replaced readable planning IRIs with final numeric MatSus IRIs.
- Added explicit Source / provenance, integrationMethod, and Validation status fields.
- Recorded final definitions, exact parents and parent IRIs, confirmed logical axioms, implementation status, validation status, editorial notes, and deferred modelling.
- Corrected StructuralWasteAnalysis and preserved the human comment with a recorded resolution.
- Replaced the waste-or-pollution record with WasteEliminationObjectiveSpecification while retaining MKB-000085 provenance.
- Updated affected IR2 Tracker summary rows 2, 5, and 21–30.
- Replaced contradictory source statuses with YES - MKB1 IR2 BATCH 2 and IMPLEMENTED_VALIDATED_WITH_BASELINE_EXPLAINED_WARNINGS.
- Preserved unrelated rows, original human decisions, and provenance.
- Workbook ZIP integrity and openpyxl reload passed; all four original sheets remain.

The MKB1 FINAL workbook remained strictly read-only (SHA-256: 8A48C3A5F03337041C89A5CB3D4FCB7BC9BFB9303C67AC4031DAD02A5844BF67).

## Planning-report corrections

The report now states the 20-class scope; adds CollectionSystem without a generic System; adds SortingMethodSpecification as an IAO plan specification and not a SortingProcess subclass; replaces the waste-or-pollution objective with WasteEliminationObjectiveSpecification; retains MKB-000085 provenance; defers pollution elimination; narrows StructuralWasteAnalysis; defers recurring-source analysis as a sibling; uses “has role” for RO_0000087; and records final numeric IRIs.

## Validation environment

GNU Make, Docker, a WSL distribution, and dicer-cli are unavailable on the Windows host. The existing untracked root robot.jar is ROBOT 1.9.2 and rejects the ODK v1.6 options --include-subclass-of and --include-subproperties.

Official ROBOT 1.9.10 was downloaded only to system temp to run the configured pipeline:

- URL: https://github.com/ontodev/robot/releases/download/v1.9.10/robot.jar
- SHA-256: 16A73C074F3DF359A7338A84B4E0788785FE06117F931BB9796E9619EA776105
- Artifacts: %TEMP%\matsus-ir2-batch2-validation-20260904

No validation artifact was written into the repository.

## Validation results

1. **Syntax/parsing — PASS.** ROBOT converted matsus-edit.owl to Functional Syntax.
2. **Complete import resolution — PASS.** Catalog-driven merge completed; the merged graph has zero owl:imports axioms and contains every required imported entity.
3. **OWL 2 DL — LOCAL PASS; FULL-CLOSURE BASELINE FAILURE.** The local source with imports removed is in OWL 2 DL. The merged closure has six undeclared Dublin Core Elements annotation-property uses; the report is identical to current main (zero delta lines).
4. **Repository build — PASS.** The exact generated sequence merge → ELK reason → relax --include-subclass-of true → reduce --include-subproperties true → annotate completed.
5. **ELK consistency — PASS.** No inconsistency or unsatisfiable-class error was reported.
6. **Numeric IDs — PASS.** Policy is seven digits, 0–9999. There are 26 numeric class declarations and 26 unique values. Batch 2 uses 7–26 and all are in range. Because dicer-cli is unavailable, the check was performed directly against matsus-idranges.owl and matsus-odk.yaml.
7. **Declarations/parents — PASS.** All 20 declarations and 20 required parent axioms exist exactly once.
8. **Restrictions — PASS.** Exactly the two approved existential restrictions occur in the new block; no equivalent, disjoint, or complement axiom occurs.
9. **Imports unchanged — PASS.** The scoped diff has no added or removed Import statement.
10. **Repository SPARQL — FOUR PASS, ONE BASELINE-EXPLAINED FAILURE.** owldef-self-reference, iri-range, label-with-iri, and multiple-replaced_by each return zero. dc-properties reports 49 findings versus 29 on main. The exact +20 is one merged-serialization dc:source finding per new provenance annotation. Direct validation of matsus-edit.owl reports zero and confirms dcterms:source in source.
11. **ROBOT report versus main — BASELINE-EXPLAINED WARNINGS.** Current: 1 error, 45 warnings, 46 total. Main: 1 error, 25 warnings, 26 total. The sole error is unchanged. The +20 delta is exactly one missing_definition warning per new class even though every class has the required English skos:definition; the default OBO report rule does not count that property.
12. **git diff --check — PASS.** Only the repository’s Windows LF-to-CRLF notice appeared; there are no whitespace errors.
13. **Scoped Git diff/stat — recorded below.**

The full-closure OWL profile issue, DC merge findings, ROBOT license error, and ROBOT console query-shape warnings all reproduce on current main and were not silently accepted.

## Validation commands

~~~powershell
robot convert --input src/ontology/matsus-edit.owl --format ofn
robot --catalog src/ontology/catalog-v001.xml merge --input src/ontology/matsus-edit.owl
robot validate-profile --profile DL --input <local-no-imports.owl>
robot validate-profile --profile DL --input <full-merged.owl>
robot reason --input <full-merged.owl> --reasoner ELK --equivalent-classes-allowed asserted-only --exclude-tautologies structural
robot merge ... reason --reasoner ELK ... relax --include-subclass-of true reduce --reasoner ELK --include-subproperties true annotate ...
robot verify --input <local-source-merge.owl> --queries src/sparql/*-violation.sparql
robot report --input <local-source-merge.owl> --labels true --fail-on None --base-iri https://w3id.org/pmd/matsus/
git diff --check
~~~

## Scoped Git diff/stat

Complete staged review commands:

~~~powershell
git diff --cached --check
git diff --cached --stat
git diff --cached -- src/ontology/matsus-edit.owl
git diff --cached -- "audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch2_Provisional_Waste_Planning_Report_2026-09-02.md"
git diff --cached -- "audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch2_Precommit_Handoff_2026-09-04.md"
git diff --cached --numstat
~~~

~~~text
172 0 handoff; 127 71 planning report; - - tracker workbook (binary 32575 -> 34315 bytes); 213 1 ontology; total: 4 files changed, 512 insertions(+), 72 deletions(-).
~~~

## Deferred modelling

- Necessary-only versus eventual equivalence for waste material.
- Temporal/context modelling for acquiring and losing waste role.
- Collection-system members, function, responsible agent, and processes.
- Sorting criteria/method links and sorted inputs/outputs.
- Collection participants, origins, destinations, and agents.
- Planned versus unplanned waste-generation context.
- Prevention targets/outcomes and measure-to-process links.
- Zero-waste objective scope/baseline/residual and strategy links.
- Waste-elimination target/boundary.
- Pollution elimination until a suitable target pattern exists.
- Waste-analysis evaluant, method, and output datum.
- Recurring-source analysis as a possible sibling of structural waste analysis.
- Composition thresholds and packaging former-status/exclusion patterns.
- PMDco issue #485 reconciliation and separate ENVO/MeSH reuse assessment.

## Scope confirmation

Only these four authorized paths are intended for staging:

1. src/ontology/matsus-edit.owl
2. audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Implementation_Tracker_2026-08-31 (2)_working implementation.xlsx
3. audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch2_Provisional_Waste_Planning_Report_2026-09-02.md
4. audit/mkb1-ontology-reuse-alignment/MKB1_IR2_Batch2_Precommit_Handoff_2026-09-04.md

The FINAL workbook and every unrelated tracked or untracked path remain untouched.
