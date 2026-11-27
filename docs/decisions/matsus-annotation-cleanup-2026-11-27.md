# MatSus entity annotation cleanup audit

Reviewed 2026-11-27 against MatSus main commit `9b893bce2e2836853f31c2389e9e760ec8354c46`.

This archive records the pre-edit inventory, editorial decisions and per-IRI rationale review. Entries are grouped by asserted source, since an IRI can have annotations in more than one component. The **Before** list preserves the exact assertion text for every removed or rewritten candidate (leading Turtle indentation omitted). The **Rationale** identifies what remains relevant to interpreting the entity. **After** gives the complete final editorial note text for that source, including notes retained verbatim. Useful comments, definitions, and meaningful correspondence annotations remain in their sources. The historical assertions below are documentation only.

An internal source pointer may name an organization or a corpus without identifying a publication or version. Those pointers are recorded verbatim below. Stable bibliography, standards, ontology IRIs and curated module sources are retained. The six LOG namespace exceptions use the same pinned LOG commit cited by the component. The three legacy annotation property declarations and labels remain because the current tracked distributions still contain their assertions.

The distribution pin remains `2026-11-20`. Public distributions are outside the source edit and require an official ODK regeneration before publication of this cleanup.

## Review flags

- Internal literature pointers without identifiable publications are archived. The `MATSUS_0000012` editorial note identifies the intended production-residue exclusion and distinguishes it from the textual definition and the OWL subclass axiom.
- The `MATSUS_0000015` editorial note records why generic waste collection sits outside the end-of-use management hierarchy and when a particular collection can qualify.
- The lifecycle-stage carbon footprint contribution existential remains asserted. Its `REVIEW_LATER` task is archived in that class's record.

## Unresolved LOG semantic-review findings

### LOG_1000050 organization

The definition describes an “immaterial entity”. The asserted superclass OBI organization (`OBI_0000245`) is a subclass of BFO material entity in the pinned import. The editorial note records the chosen OBI superclass. Resolve the category discrepancy in a separate semantic review of the upstream LOG term and its MatSus alignment. The definition and axioms match the baseline.

### LOG_1000117 transportation service

One definition describes consignment through transfer of possession without transfer of ownership until sale. The other describes a logistics service containing at least one transport process, which agrees with the asserted hierarchy and part restriction. Confirm the intended definition with LOG in a separate semantic review. Both definitions and all axioms match the baseline.

## Validation results

- The four source edits remove 496 integration assertions, 105 historical source literals and 131 generic LOG alignment tags. The 281 source-and-IRI records below also cover replaced notes and module metadata.
- Catalog-resolved ROBOT merges of the baseline and final sources contain the same 5,234 non-annotation axioms and declarations, 2,811 label and alternative-label assertions, 2,334 definition assertions and 30 mapping assertions. The three Turtle components parse and their logical axioms match the baseline. All 83 retained source assertions across the four authored files were verified alongside the 105 archived historical source literals.
- The final merge differs from the previously reviewed merge only in the editorial notes for `MATSUS_0000012` and `MATSUS_0000015`. All 281 archive records were reconciled with the baseline assertions and the final editorial notes.
- OWL 2 DL, full-closure ELK and HermiT, and all six configured SPARQL checks passed on the finalized ontology. The configured ROBOT report has the same rows before and after, with 0 errors and 110 warnings.
- All five checked-in SHACL examples conform. Pattern 1 passed its 10 queries and checks, and a temporary negative control detected the missing recommendation edge. Pattern 2 passed its 12 queries and checks and detected all seven programmed mutations.
- Official ODK regeneration and distribution byte-reproducibility checks are pending. The local Windows environment has no runnable ODK toolchain and this branch is local for review.

## `src/ontology/matsus-edit.owl`

### `https://w3id.org/pmd/matsus/MATSUS_0000060`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000060 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000060 "The evaluand may be a material, product, process, or represented lifecycle system. This relation does not make the evaluand a participant, input, material evaluant, or information-content subject. The relation is optional on assessment instances. No inverse is introduced in this increment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000060 "Complete pinned PMDco/IAO/OBI relation inventory and SSbD assesses comparison; final human decision 8.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000060 "MatSus-local object property using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000060 "SSbD assesses is not reused: its proper-overlap and PROV domain/range semantics are not inherited.")`

**Rationale** An evaluand may be a material, product, process, or represented lifecycle system. Review also covered the source restriction or correspondence described in the notes.

**After**

> An evaluand may be a material, product, process, or represented lifecycle system. This optional relation does not imply participation, input, material-evaluant status, or information aboutness. Its SSbD correspondence is non-entailing and does not carry proper-overlap or PROV domain and range semantics. No inverse is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000061`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000061 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000061 "This relation expresses methodological governance, not aboutness, parthood, or a value-specification link. No inverse is introduced because no approved competency question requires one."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000061 "Complete pinned PMDco/IAO/OBI relation inventory, existing MATSUS_0000027, and SSbD/CLEO indicator-pattern comparison; final human decision 9.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000061 "MatSus-local object property using the pinned PMDco/IAO/OBI backbone; no exact external relation was found")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000061 "No SSbD or CLEO property denotes this relation; the absence of a mappedTo annotation is deliberate after inventory.")`

**Rationale** This links an indicator result to the metric specification governing it. Review also covered the source restriction or correspondence described in the notes.

**After**

> This links an indicator result to the metric specification governing it. It expresses methodological governance rather than aboutness, parthood or a link to the value specification carrying the result. SSbD and CLEO do not supply a property with this scope. No inverse is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000064`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000064 "MKB2 end-of-use architecture final human decision, 2026-09-20")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000064 "This relation does not imply authorization, formal selection, uniqueness, or execution of the recommended process. It is not functional and no inverse is introduced in this increment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000064 "MKB2 end-of-use competency questions and review of the pinned PMDco/IAO/OBI relation inventory; final human decision, 2026-09-20.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000064 "MatSus-local object property; no exact relation in the pinned PMDco/IAO/OBI closure expresses recommendation of an end-of-use process")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000064 "CCO prescribes was reviewed as an external candidate but was not reused because its rule-or-guide semantics are stronger than the intended recommendation relation.")`

**Rationale** A recommendation identifies a suitable end-of-use management process without authorizing, formally selecting, or executing it. Review also covered the source restriction or correspondence described in the notes.

**After**

> A recommendation identifies a suitable end-of-use management process without authorizing, formally selecting, or executing it. Multiple pathways may be recommended. No functionality or inverse-property axiom is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/BatteryCarbonFootprintInformation`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :BatteryCarbonFootprintInformation "MKB2 SRC-005/SRC-006 approved legacy indicator-result bridge, 2026-09-16")`
- audit-only — `AnnotationAssertion(:integrationMethod :BatteryCarbonFootprintInformation "MatSus battery-specific specialization of carbon footprint result based on BatteryPass requirements")`

**Rationale** This is a calculated indicator result, not an intrinsic material quality.

**After**

> This is a calculated indicator result, not an intrinsic material quality. It may be contained in a Digital Product Passport or another information artifact; DPP containment is not part of the class definition.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :BatteryCarbonFootprintInformation <urn:samm:io.BatteryPass.CarbonFootprint:1.2.0#batteryCarbonFootprint>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :BatteryCarbonFootprintInformation "BatteryPass-ready Data Attribute Long List v1.3, attributes 28-35")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/BatteryLabelInformation`

**Before**

- audit-only — `AnnotationAssertion(:integrationMethod :BatteryLabelInformation "new MatSus DPP information class based on BatteryPass requirements")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :BatteryLabelInformation <urn:samm:io.BatteryPass.Labels:1.2.0#labels>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :BatteryLabelInformation "BatteryPass-ready Data Attribute Long List v1.3, attributes 21-25")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/BatteryModelSpecification`

**Before**

- audit-only — `AnnotationAssertion(:integrationMethod :BatteryModelSpecification "new MatSus subclass of PMDco material specification")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :BatteryModelSpecification "The model/batch/item distinction is represented through specification, existing lot/batch identifier patterns, identifiers and later SHACL rather than a new product-batch hierarchy.")`

**Rationale** Represent model-level information as a material specification. Review also covered the source restriction or correspondence described in the notes.

**After**

> Represent model-level information as a material specification. Distinguish batches and individual items using lot or batch patterns and identifiers, without inferring a new product-batch hierarchy.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :BatteryModelSpecification "BatteryPass-ready Data Attribute Long List v1.3, attribute 7")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/DPPGranularityDatum`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :DPPGranularityDatum "Granularity values are represented as literals and will be constrained in SHACL. The accepted PMD lot/LOG lot alignment and LOG batch identifier remain authoritative; no new batch class is introduced.")`
- audit-only — `AnnotationAssertion(:integrationMethod :DPPGranularityDatum "new MatSus data-item class")`

**Rationale** Granularity is represented with literal values for application-profile validation.

**After**

> Granularity is represented with literal values for application-profile validation. Use the existing PMDco/LOG lot alignment and LOG batch identifier to represent batch granularity.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :DPPGranularityDatum "BatteryPass-ready Data Attribute Long List v1.3, attribute 3")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/DPPStatusDatum`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :DPPStatusDatum "Status values are represented as literals and will be constrained in a later SHACL layer; no OWL or SKOS value vocabulary is introduced here.")`
- audit-only — `AnnotationAssertion(:integrationMethod :DPPStatusDatum "new MatSus data-item class")`

**Rationale** Status is represented with literal values for application-profile validation.

**After**

> Status is represented with literal values for application-profile validation. The ontology supplies no controlled OWL or SKOS vocabulary for those values.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :DPPStatusDatum "BatteryPass-ready Data Attribute Long List v1.3, attribute 2")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/DeclarationOfConformity`

**Before**

- audit-only — `AnnotationAssertion(:integrationMethod :DeclarationOfConformity "new MatSus document class based on BatteryPass requirements")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :DeclarationOfConformity <urn:samm:io.BatteryPass.Labels:1.2.0#declarationOfConformity>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :DeclarationOfConformity "BatteryPass-ready Data Attribute Long List v1.3, attribute 26")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/DigitalProductPassportIdentifier`

**Before**

- audit-only — `AnnotationAssertion(:integrationMethod :DigitalProductPassportIdentifier "new MatSus class using the accepted IAO identifier pattern")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :DigitalProductPassportIdentifier "BatteryPass-ready Data Attribute Long List v1.3, attribute 5")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/EndOfLifeInformation`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :EndOfLifeInformation "Detailed end-of-life processes and circular value-network semantics are deferred to CEON and BONSAI.")`
- audit-only — `AnnotationAssertion(:integrationMethod :EndOfLifeInformation "MatSus generic end-of-use information class; BatteryPass retained as source provenance and application example")`

**Rationale** This class covers information about end-of-use handling.

**After**

> This class covers information about end-of-use handling. Use process or circular value-network models for the handling occurrences and their network relationships.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :EndOfLifeInformation "BatteryPass-ready Data Attribute Long List v1.3, attributes 56-58")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/LifecycleStageCarbonFootprintContribution`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :LifecycleStageCarbonFootprintContribution "Lifecycle-stage identifiers, values, units, functional units, and calculation provenance are represented through data/value patterns and later SHACL. The suitability of the generic MatSus contributes-to pattern for this BatteryPass-specific class remains subject to later review."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :LifecycleStageCarbonFootprintContribution "new MatSus subclass based on BatteryPass requirements")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :LifecycleStageCarbonFootprintContribution "The contributes-to existential links this BatteryPass-specific result class to the generic MatSus result-contribution pattern; it does not imply arithmetic summation or that the total result has only one contributing stage."@en)`
- audit-only — `AnnotationAssertion(:integrationNote :LifecycleStageCarbonFootprintContribution "REVIEW_LATER: Reassess whether the contributes-to existential remains the right TBox commitment when lifecycle-stage result modelling and the related SHACL profile are revisited.")`

**Rationale** The contributes-to existential relates a stage result to the generic MatSus result-contribution pattern without requiring arithmetic summation or a unique contributing stage.

**After**

> The contributes-to existential relates a stage result to the generic MatSus result-contribution pattern without requiring arithmetic summation or a unique contributing stage. Stage identifiers, values, units, functional units and calculation provenance belong in data and value patterns and can be checked in an application profile.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :LifecycleStageCarbonFootprintContribution <urn:samm:io.BatteryPass.CarbonFootprint:1.2.0#carbonFootprintPerLifeCycleStage>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :LifecycleStageCarbonFootprintContribution "BatteryPass-ready Data Attribute Long List v1.3, attributes 29-32")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000001`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000001 "MKB1 IR2 Class Review: POST-MKB1-MAT-001 / MKB-000175 supporting anchor")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000001 "Post-gate accepted material anchor. A material can cease to bear a waste role while retaining its recovery provenance. Later: link the material to its recovery process/history. Do not add disjointness or a complement axiom.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000001 "new MatSus subclass of PMDco material")`

**Rationale** Recovery provenance can persist after the material ceases to bear a waste role.

**After**

> Recovery provenance can persist after the material ceases to bear a waste role. Recovery and waste-role status need separate descriptions. No disjointness or complement axiom is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000002`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000002 "MKB1 IR2 Class Review: MKB-000175")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000002 "Post-gate accepted. Recycled material and secondary material are not exclusive categories. Later: link to the recycling process/history. Do not assert disjointness from secondary material.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000002 "new MatSus subclass of recovered material")`

**Rationale** Recycled and secondary material can overlap.

**After**

> Recycled and secondary material can overlap. No disjointness between them is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000003`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000003 "MKB1 IR2 Class Review: MKB-000223")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000003 "Post-gate accepted as a positive material category rather than a complement of virgin material. Later: represent suitability or intended use only when a stable relation pattern is selected. Do not assert disjointness from recycled material.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000003 "new MatSus subclass of recovered material")`

**Rationale** Secondary material is a positive recovery-derived category rather than the complement of virgin material.

**After**

> Secondary material is a positive recovery-derived category rather than the complement of virgin material. It may also be recycled material.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000004`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000004 "MKB1 IR2 Class Review: POST-MKB1-ASS-001 / MKB-000180 supporting anchor")`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000004 "MKB2 SRC-005/SRC-006 final human decision 3, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000004 "MKB2 SRC-005/SRC-006 final decision: this class denotes a broader sustainability-assessment process rather than an OBI assay. PMDco/OBI assays may be subprocesses or supply evidence in particular assessments, but are not universal parents. Material subject scope may overlap environmental, economic, or social aspect classifications. Resource-input reduction assessment remains its child."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000004 "Existing MKB1 MatSus class reclassified under MatSus sustainability assessment during MKB2 SRC-005/SRC-006 consolidation")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000004 "The SSbD mapping is conceptual only; MatSus adds material, product, process, or lifecycle-system subject scope and inherits no SSbD restrictions.")`

**Rationale** This class denotes a sustainability assessment with a material-related subject. Review also covered the source restriction or correspondence described in the notes.

**After**

> This class denotes a sustainability assessment with a material-related subject. An OBI or PMDco assay may supply evidence or occur within an assessment without being a universal superclass. The subject may be a material, product, process, or represented lifecycle system, and the assessment can also fall under environmental, economic or social aspects. The SSbD correspondence is conceptual and entails no inherited restrictions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000005`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000005 "MKB1 IR2 Class Review: MKB-000180-ASS")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000005 "Post-gate accepted. Keep assessment distinct from the process and its objective specification. Later: model the evaluated process or system, baseline, comparison conditions and output datum.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000005 "new MatSus subclass of material sustainability assessment")`

**Rationale** The assessment evaluates resource-input reduction and is distinct from both the performance of a reduction process and the specification of its objective.

**After**

> The assessment evaluates resource-input reduction and is distinct from both the performance of a reduction process and the specification of its objective. Comparison depends on the evaluated system or process, baseline and conditions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000006`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000006 "MKB1 IR2 Class Review: MKB-000180-OBJ")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000006 "Example: reduce virgin aluminium input by 20% relative to the 2025 baseline. Later: relate the objective specification to the targeted process or system, baseline, reduction amount and unit. No separate resource-input reduction strategy specification is required.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000006 "new MatSus subclass of IAO objective specification")`

**Rationale** A reduction strategy may prescribe actions to achieve it, without requiring a separate resource-input reduction strategy class.

**After**

> A reduction strategy may prescribe actions to achieve it, without requiring a separate resource-input reduction strategy class.

Additional annotation text

- `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#example> :MATSUS_0000006 "An objective to reduce virgin aluminium input by 20% relative to the 2025 baseline."@en)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000007`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000007 "MKB1 IR2 Class Review: supporting waste anchor; human-gate Closure; PMDco issue #485")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000007 "deprecated historical MatSus identifier; active use replaced by imported ENVO_01000665")`

**Rationale** Deprecated historical identifier retained for compatibility.

**After**

> Deprecated historical identifier retained for compatibility. Active use is replaced by ENVO_01000665 waste role, imported through PMDco v3.1.2. No equivalence or subclass mapping is asserted between the deprecated local identifier and ENVO_01000665.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000008`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000008 "MKB1 IR2 Class Review: supporting waste anchor; human-gate Closure; PMDco issue #485")`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000008 "MatSus approved ENVO waste-role migration, 2026-10-22; PMDco v3.1.2")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000008 "Waste status is contextual and role-based, not an intrinsic material kind. ENVO_01000665 waste role is reused through PMDco v3.1.2. The has role restriction is necessary only; do not assert equivalence. Because ENVO_01000665 is disjoint with a role borne by a PMDco portion of matter, do not classify a waste-role bearer as PMD_0000001 portion of matter. Do not make recovered material a subclass of waste material. Later: select a temporal or contextual model for acquiring and losing the role.")`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000008 "PMDco v3.1.2 imports ENVO_01000665 waste role and its disjointness with roles borne by PMD_0000001 portion of matter.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000008 "MatSus primitive subclass of BFO material entity with a necessary has role some ENVO waste role restriction")`

**Rationale** Waste status is contextual and role-based.

**After**

> Waste status is contextual and role-based. The ENVO waste-role restriction imported through PMDco v3.1.2 is necessary only. ENVO_01000665 is disjoint with a role borne by a PMDco portion of matter, so do not classify the bearer as PMD_0000001. Recovery provenance alone does not establish that a material still bears a waste role. This class does not encode role acquisition or loss.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000009`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000009 "MKB1 IR2 Class Review: MKB-000063; SRC-001 Circular Berlin; Master Analysis row 52")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000009 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Retain this local subtype after any upstream anchor migration. Later: add source or provenance criteria only if required by data integration. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000009 "new MatSus subclass of waste material")`

**Rationale** This class specializes waste material by the scope stated in its definition.

**After**

> This class specializes waste material by the scope stated in its definition. It has no additional source or provenance restriction.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000010`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000010 "MKB1 IR2 Class Review: MKB-000144; SRC-003 European Environment Agency; Master Analysis row 69")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000010 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Predominantly is intentionally not assigned an OWL cutoff. Later: represent thresholds through data or a classification specification. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000010 "new MatSus subclass of waste material")`

**Rationale** No OWL cutoff is assigned to 'predominantly'.

**After**

> No OWL cutoff is assigned to 'predominantly'. Record any quantitative threshold in the applicable data or classification specification.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000011`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000011 "MKB1 IR2 Class Review: MKB-000148; SRC-003 European Environment Agency; Master Analysis row 71")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000011 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Municipal solid waste is an alternative label, not an equivalent class. Later: assert equivalence only if the scopes are confirmed identical. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000011 "new MatSus subclass of waste material")`

**Rationale** Municipal solid waste is an alternative label.

**After**

> Municipal solid waste is an alternative label. The annotation entails no equivalent-class relationship.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000012`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000012 "MKB1 IR2 Class Review: MKB-000155; SRC-003 European Environment Agency; Master Analysis row 74; TransformON exact-label evidence insufficient for reuse")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000012 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. The selected source scope excludes production residues. Later: represent former packaging status and the exclusion only with a validated pattern. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000012 "new MatSus subclass of waste material")`

**Rationale** The intended scope excludes production residues. The definition specifies former packaging status. The subclass axiom places the class under waste material.

**After**

> The intended scope excludes production residues. The textual definition states that the material was packaging or packaging material before it acquired a waste role. The OWL axioms classify packaging waste under waste material without an explicit production-residue exclusion. A matching label alone does not establish scope agreement.

**Preservation** Preserved. The editorial note distinguishes the intended exclusion from the unchanged definition and OWL axioms. The internal SRC-003 pointer names the European Environment Agency but contains no publication identifier. The exact historical pointer appears above.

### `https://w3id.org/pmd/matsus/MATSUS_0000013`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000013 "MKB1 IR2 Class Review: MKB-000249; SRC-001 Circular Berlin; Master Analysis row 111")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000013 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. This is intentionally a broad provisional subtype. Later: add fibre, composition, or product-type refinements only from concrete use cases. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000013 "new MatSus subclass of waste material")`

**Rationale** This waste subtype has broad scope and does not impose fibre, composition, or product-type criteria beyond its definition.

**After**

> This waste subtype has broad scope and does not impose fibre, composition, or product-type criteria beyond its definition.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000014`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000014 "MKB1 IR2 Class Review: MKB-000059")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000014 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. The object-aggregate parent is provisional. Later: model members or components, enabling function, responsible agent, and collection processes when those queries become central. Do not introduce a universal generic system class. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000014 "new MatSus subclass of BFO object aggregate")`

**Rationale** The object-aggregate placement groups the physical collection system without committing to fixed membership, function, responsible agents or collection-process relations.

**After**

> The object-aggregate placement groups the physical collection system without committing to fixed membership, function, responsible agents or collection-process relations.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000015`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000015 "MKB1 IR2 Class Review: supporting waste process; human-gate Closure related-terms decision")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000015 "The generic waste collection class remains outside the end of use management hierarchy because waste collection also applies to production, construction, process, and other waste streams that are not necessarily post-use."@en)`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000015 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. This is a supporting process with no standalone MKB ID. Later: add waste participant, origin, destination, and responsible-agent relations. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000015 "new MatSus subclass of COB planned process")`

**Rationale** Generic waste collection applies to waste streams beyond the post-use context. Its generic superclass placement and the conditions for treating a particular collection as end-of-use management are separate questions.

**After**

> Generic waste collection also covers production, construction, process and other waste streams that need not arise after a use phase. It therefore sits outside the end-of-use management process hierarchy. A particular collection can qualify as end-of-use management when it handles waste arising after a use phase.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000016`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000016 "MKB1 IR2 Class Review: MKB-000231; SRC-001 Circular Berlin; Master Analysis row 106")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000016 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. No acceptable maintained equivalent was found. Later: connect criteria or method specifications and sorted inputs and outputs. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000016 "new MatSus subclass of COB planned process")`

**Rationale** This process performs sorting.

**After**

> This process performs sorting. The criteria or method specification and the identities of the sorted inputs and outputs belong to the description of an occurrence and are not further constrained here.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000017`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000017 "MKB1 IR2 Class Review: MKB-000231; SRC-001 Circular Berlin; Master Analysis row 106")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000017 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. This is an information content entity and is not a subclass of sorting process. Later: relate the method specification to the sorting process it prescribes. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000017 "new MatSus subclass of IAO plan specification")`

**Rationale** A sorting method specification is directive information describing how to sort.

**After**

> A sorting method specification is directive information describing how to sort. It is placed under plan specification rather than under the sorting process it can prescribe.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000018`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000018 "MKB1 IR2 Class Review: supporting waste process; human-gate Closure related-terms decision")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000018 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. This is a supporting process with no standalone MKB ID. Later: add waste input and separated-stream output restrictions after example testing. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000018 "new MatSus subclass of sorting process")`

**Rationale** This is a sorting process specialized to waste material.

**After**

> This is a sorting process specialized to waste material. No additional waste-input or separated-stream output restriction is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000019`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000019 "MKB1 IR2 Class Review: MKB-000263; SRC-003 European Environment Agency; Master Analysis row 115")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000019 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Waste generation is not assumed to be planned production or synthesis. Later: distinguish planned and unplanned generation through context unless required otherwise. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000019 "new MatSus subclass of BFO process with a necessary waste-material output restriction")`

**Rationale** Waste generation can occur in planned or unplanned contexts.

**After**

> Waste generation can occur in planned or unplanned contexts. A waste-material output is required, without the process necessarily being production or synthesis.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000020`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000020 "MKB1 IR2 Class Review: MKB-000264; SRC-001 Circular Berlin; SRC-003 European Environment Agency; Master Analysis row 116")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000020 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Keep the performed process distinct from its measure specification. Later: relate the process to targeted streams and prevention outcomes. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000020 "new MatSus subclass of COB planned process")`

**Rationale** This denotes a performed prevention process, distinct from the measure specification that prescribes how prevention should be carried out.

**After**

> This denotes a performed prevention process, distinct from the measure specification that prescribes how prevention should be carried out.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000021`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000021 "MKB1 IR2 Class Review: MKB-000264; SRC-001 Circular Berlin; SRC-003 European Environment Agency; Master Analysis row 116")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000021 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. This is an information artifact, not a process. Later: connect it to the prescribed process. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000021 "new MatSus subclass of IAO plan specification")`

**Rationale** This information artifact prescribes a waste prevention measure.

**After**

> This information artifact prescribes a waste prevention measure. The process that carries it out is a separate entity.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000022`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000022 "MKB1 IR2 Class Review: MKB-000266; SRC-001 Circular Berlin; Master Analysis row 117")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000022 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Zero waste is normative information content, not a material or process. Later: represent scope, baseline, and tolerated residual waste if needed. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000022 "new MatSus subclass of IAO objective specification")`

**Rationale** Zero waste is the objective expressed by directive information.

**After**

> Zero waste is the objective expressed by directive information. Any scope, baseline, or tolerated residual waste belongs to the stated objective or application profile.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000023`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000023 "MKB1 IR2 Class Review: MKB-000266; SRC-001 Circular Berlin; Master Analysis row 117")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000023 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Keep the strategy distinct from its objective. Later: relate it to the objective and prescribed prevention, reuse, and recovery processes. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000023 "new MatSus subclass of IAO plan specification")`

**Rationale** The strategy specifies a plan to pursue a zero-waste objective.

**After**

> The strategy specifies a plan to pursue a zero-waste objective. The objective and the performed prevention, reuse or recovery processes are distinct entities.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000024`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000024 "MKB1 IR2 Class Review: MKB-000085; SRC-002 Ellen MacArthur Foundation; Master Analysis row 56")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000024 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. MKB-000085 is retained as provenance. Do not create an undefined generic elimination process. Later: link to a scoped waste target and boundary. Pollution-elimination modelling is deferred until a suitable pollution target pattern is established. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000024 "new MatSus subclass of IAO objective specification")`

**Rationale** This class specifies an objective for waste elimination.

**After**

> This class specifies an objective for waste elimination. It does not denote a generic elimination process or extend the target to pollution without a separate scope specification.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000025`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000025 "MKB1 IR2 Class Review: MKB-000236; SRC-001 Circular Berlin; Master Analysis row 107")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000025 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Analysis is an assay, not the information output itself. Later: add evaluant, method, and output-datum relations using a concrete example. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000025 "new MatSus subclass of OBI assay")`

**Rationale** Waste analysis is an assay.

**After**

> Waste analysis is an assay. Its evaluand, method and information outputs are distinct from the analysis process.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000026`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000026 "MKB1 IR2 Class Review: MKB-000236; SRC-001 Circular Berlin; Master Analysis row 107")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000026 "Human-gate-authorized provisional MKB1 IR2 waste implementation. PMDco issue #485 is ISSUE_SUBMITTED. Recurring-generation-pattern analysis is outside this definition. Later: consider recurring-source analysis as a sibling class. Later PMDco acceptance triggers migration or reconciliation of mappings, parents, and restrictions, not deletion of the MatSus specialization.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000026 "new MatSus subclass of waste analysis")`

**Rationale** Recurring patterns of waste generation fall outside this definition.

**After**

> Recurring patterns of waste generation fall outside this definition.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000027`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000027 "MKB1 IR2 Class Review: ADD-SCO-012; SCO")`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000027 "MKB2 SRC-005/SRC-006 final human decision 9, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000027 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. Metric specifications prescribe methods; resulting metric values remain data items. Later: relate prescribed quantities, calculation method, units, boundary, interpretation, and resulting datum. No further logical restrictions are asserted in this batch.")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000027 "In the MKB2 assessment architecture, metric specification is the governing indicator specification linked to an indicator result by has indicator specification. It remains distinct from the result and from any OBI value specification that carries the result's value."@en)`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000027 "No mappedTo annotation is asserted: SSbD Indicator and CLEO lifecycle model datum are not metric specifications.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000027 "new MatSus subclass of IAO directive information entity")`

**Rationale** A metric specification prescribes how a metric is determined. Review also covered the source restriction or correspondence described in the notes.

**After**

> A metric specification prescribes how a metric is determined. It governs an indicator result through has indicator specification and is distinct from both the result datum and the OBI value specification carrying its value. SSbD Indicator and CLEO lifecycle model datum do not express this directive-information category.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000028`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000028 "MKB1 IR2 Class Review: MKB-000205; SRC-001 Circular Berlin; UNEP domain meaning")`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000028 "MKB2 SRC-005/SRC-006 approved legacy indicator-result bridge, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000028 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. This is a calculated result datum, not an intrinsic efficiency quality. Later: model numerator or output, resource input, method, boundary, unit, time interval, and calculation relations.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000028 "new MatSus subclass of IAO data item")`

**Rationale** This is a calculated result datum.

**After**

> This is a calculated result datum. Interpretation depends on its numerator or output, resource input, method, boundary, unit and time interval.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000029`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000029 "MKB1 IR2 Class Review: MKB-000137; SRC-003 European Environment Agency")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000029 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. This is the material-input specialization of resource efficiency datum. Later: constrain the stated resource input to a material quantity and add method, unit, or boundary relations only through an approved pattern.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000029 "new MatSus subclass of resource efficiency datum")`

**Rationale** This specializes resource efficiency datum by using a material input.

**After**

> This specializes resource efficiency datum by using a material input. The class adds no restriction on the input quantity, method, unit or boundary.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000030`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000030 "MKB1 IR2 Class Review: MKB-000261; SRC-002 Ellen MacArthur Foundation; SRC-003 European Environment Agency")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000030 "new MatSus subclass of PMDco material")`

**Rationale** European regulatory and circular-economy terminology uses 'virgin material' in ways that may overlap with 'primary material', particularly when distinguishing material without recovered or recycled origin.

**After**

> European regulatory and circular-economy terminology uses 'virgin material' in ways that may overlap with 'primary material', particularly when distinguishing material without recovered or recycled origin. MatSus currently asserts no equivalence, disjointness or hierarchy between virgin material and primary material. Sector-specific legal classifications may impose additional conditions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000031`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000031 "MKB1 IR2 Class Review: MKB-000202; SRC-001 Circular Berlin")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000031 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. No maintained compatible repurposing-process class was verified in the reviewed sources. Later: represent prior purpose, new purpose, participants, inputs, and outputs.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000031 "MatSus subclass of end of use management process")`

**Rationale** The class definition and superclass express the repurposing scope. Search status and future assertion patterns are historical.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000032`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000032 "MKB1 IR2 Class Review: MKB-000009; SRC-002 Ellen MacArthur Foundation")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000032 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. Later: add battery-participant and second-life or new-purpose relations from an approved use case.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000032 "new MatSus subclass of repurposing process")`

**Rationale** The class definition and superclass express the repurposing scope. Search status and future assertion patterns are historical.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000033`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000033 "MKB1 IR2 Class Review: MKB-000180; SRC-001 Circular Berlin")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000033 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. Keep this process distinct from resource-input reduction assessment MATSUS_0000005 and resource-input reduction objective specification MATSUS_0000006. Later: model the affected process or system, material input, stated baseline, comparison conditions, and comparable output or function.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000033 "new MatSus subclass of COB planned process")`

**Rationale** This is the process of reducing resource input, distinct from assessing a reduction or specifying a reduction objective.

**After**

> This is the process of reducing resource input, distinct from assessing a reduction or specifying a reduction objective. Interpret comparisons against the stated baseline, conditions and comparable output or function.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000034`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000034 "MKB1 IR2 Class Review: MKB-000181 and MKB-000182; SRC-002 Ellen MacArthur Foundation")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000034 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. MKB-000181 and MKB-000182 are consolidated into this one generic process; at-home and on-the-go are source contexts, not subclasses. Later: model container or device, refilled material, location, agent, and context relations.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000034 "new MatSus subclass of COB planned process")`

**Rationale** The same process class covers at-home and on-the-go refilling.

**After**

> The same process class covers at-home and on-the-go refilling. These are occurrence contexts and do not define distinct subclasses.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000035`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000035 "MKB1 IR2 Class Review: MKB-000184; SRC-001 Circular Berlin")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000035 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. Refusal process represents the actual intentional refusal occurrence. It does not represent the strategy specification or objective specification that motivates, enables, or encourages that occurrence. Later: add agent, refused entity or service, and avoidance-objective relations.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000035 "new MatSus subclass of COB planned process")`

**Rationale** This class denotes the actual intentional refusal occurrence.

**After**

> This class denotes the actual intentional refusal occurrence. A strategy or objective that motivates or prescribes refusal is a separate information entity.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000036`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000036 "MKB1 IR2 Class Review: MKB-000189; SRC-003 European Environment Agency")`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000036 "MKB2 SRC-007 consolidated human-gate decision, 2026-10-09")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000036 "Remanufacturing is distinct from refurbishment: this class requires reprocessing to meet the performance and quality requirements of an equivalent new product, whereas refurbishment restores performance or functionality within the originally intended use and performance range. Regulation (EU) 2024/1781 uses remanufacturing for actions that produce a new product and include at least one substantial change affecting safety, performance, purpose, or type; that regulatory meaning is not adopted as an equivalent definition here. No equivalence, subclass, or disjointness relation with refurbishment is asserted. The separate remanufacturability disposition candidate remains deferred."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000036 "MatSus subclass of end of use management process")`

**Rationale** Remanufacturing requires reprocessing to meet the performance and quality requirements of an equivalent new product.

**After**

> Remanufacturing requires reprocessing to meet the performance and quality requirements of an equivalent new product. Refurbishment restores performance or functionality within the originally intended use and performance range. Regulation (EU) 2024/1781 uses a different remanufacturing scope, requiring a new product and a substantial change affecting safety, performance, purpose or type. No equivalence, subclass or disjointness relationship with refurbishment is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000037`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000037 "MKB1 IR2 Class Review: MKB-000002, SRC-003 European Environment Agency; MKB-000069, SRC-002 Ellen MacArthur Foundation")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000037 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. This records the established sustainability and resource-efficiency meaning of decoupling, not dismantling, disassembly, or another physical separation process. Later: model absolute and relative classifications, baseline and comparison interval, resource-input or environmental-pressure indicator, economic or service-output indicator, calculation method, ratio, and temporal relations.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000037 "new MatSus subclass of IAO data item")`

**Rationale** This datum records decoupling in the sustainability and resource-efficiency sense.

**After**

> This datum records decoupling in the sustainability and resource-efficiency sense. Interpretation depends on the relationship between resource input or environmental pressure and economic or service output over a comparison interval. It does not describe dismantling, disassembly or physical separation.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000038`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000038 "MKB1 IR2 Class Review: MKB-000146; SRC-002 Ellen MacArthur Foundation")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000038 "Human-gate-authorized MKB1 IR2 Batch 3 implementation. Modularity is a dependent quality of a bearer, not an object aggregate. Later: model the bearer, measurement datum, degree, method, and any device- or design-specific subclasses.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000038 "new MatSus subclass of BFO quality")`

**Rationale** Modularity is a dependent quality of a bearer.

**After**

> Modularity is a dependent quality of a bearer. Its degree and measurement can be recorded separately from the bearer and its physical components.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000039`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000039 "MKB1 IR2 human-gate modelling refinement derived from MKB-000184 and the 2026-09-04 Batch 3 review")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000039 "Human-gate-authorized MKB1 IR2 Batch 3 addition derived from the MKB-000184 RefusalProcess review and the 2026-09-04 Batch 3 review. Relations to refusal processes, resource-input-reduction objectives, design specifications, affected product features, and realization remain deferred. Do not assert that every refusal process realizes a refusal strategy specification or add another logical relation between these classes in this batch.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000039 "new MatSus subclass of IAO plan specification")`

**Rationale** This plan specification prescribes a refusal strategy.

**After**

> This plan specification prescribes a refusal strategy. A refusal occurrence need not realize such a strategy, and the ontology asserts no universal realization link.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000040`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000040 "MKB1 IR2 Class Review: MKB-000163; SRC-003 European Environment Agency")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000040 "This definition represents the provenance-based use of 'primary material' in European circular-economy discourse rather than every possible use of the term. Its relationship to virgin material requires later review through competency questions and provenance modelling. MatSus currently asserts no equivalence, disjointness or hierarchy between primary material and virgin material.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000040 "new MatSus subclass of PMDco material")`

**Rationale** The definition uses the provenance-based sense of primary material in European circular-economy discourse.

**After**

> The definition uses the provenance-based sense of primary material in European circular-economy discourse. MatSus asserts no equivalence, disjointness or hierarchy between primary and virgin material.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000041`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000041 "MatSus derived modelling decision based on the primary material distinction")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000041 "This class applies the LOG raw-material-role pattern to primary material. It distinguishes provenance as primary material from production-input context as raw material. Its relationship to sector-specific uses of 'virgin raw material' may require later review.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000041 "new MatSus subclass of primary material")`

**Rationale** The LOG raw-material-role pattern distinguishes primary provenance from use or intended use as a production input.

**After**

> The LOG raw-material-role pattern distinguishes primary provenance from use or intended use as a production input. Sector-specific uses of 'virgin raw material' may impose different conditions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000042`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000042 "MKB1 IR2 Class Review: MKB-000224; SRC-002 Ellen MacArthur Foundation")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000042 "new MatSus subclass of LOG raw material")`

**Rationale** European circular-economy terminology commonly uses 'secondary raw material' for recovery-derived material returned to production.

**After**

> European circular-economy terminology commonly uses 'secondary raw material' for recovery-derived material returned to production. This class applies the LOG raw-material-role pattern to the existing MatSus secondary material class. No equivalence with recovered material or recycled material is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000043`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000043 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000043 "This class covers ongoing, completed, and incompletely described assessments. It has no universal specification, evaluand, input, or output existential."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000043 "SRC-005 SSbD Core 0.0.1 Assessment and SpecifiedAssessment at commit a96b121df9fd16c00797f61f93e3e61360b6ced1; September MKB1 assessment-architecture carryover; final human decision 2.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000043 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000043 "MatSus uses the BFO/COB planned-process category and does not inherit SSbD output, assesses, PROV, or mereology axioms.")`

**Rationale** This BFO/COB planned-process class covers ongoing, completed, and incompletely described assessments. Review also covered the source restriction or correspondence described in the notes.

**After**

> This BFO/COB planned-process class covers ongoing, completed, and incompletely described assessments. No universal specification, evaluand, input, or output existential is asserted. The SSbD correspondence is conceptual and does not inherit its output, assesses, PROV or mereology axioms.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000044`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000044 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000044 "This class is an umbrella: it does not assert regulatory compliance and does not require all three child kinds."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000044 "SRC-005 SSbD Core 0.0.1 SafetyAssessment; final human decisions 2 and 10.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000044 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000044 "No SSbD restriction is inherited.")`

**Rationale** This umbrella class neither entails regulatory compliance nor requires all three child kinds. Review also covered the source restriction or correspondence described in the notes.

**After**

> This umbrella class neither entails regulatory compliance nor requires all three child kinds. The SSbD correspondence is conceptual and carries no inherited restrictions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000045`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000045 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000045 "This local umbrella is broader than SSbD's environment-, human-health-, and intrinsic-chemical-hazard leaves. Hazard is not modelled here as an assessment result or disposition."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000045 "SRC-005 SSbD hazard-assessment leaves; MatSus broader umbrella approved by final human decision 2.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000045 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000045 "There is no generic SSbD HazardAssessment IRI.")`

**Rationale** This umbrella is broader than the SSbD environment, human-health and intrinsic chemical hazard assessment terms. Review also covered the source restriction or correspondence described in the notes.

**After**

> This umbrella is broader than the SSbD environment, human-health and intrinsic chemical hazard assessment terms. It denotes a process, distinct from an assessment result or a hazard disposition.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000046`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000046 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000046 "SSbD output-like wording is not inherited. No exposure-estimate information-content class is introduced in this increment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000046 "SRC-005 SSbD environmental and human-health exposure-assessment leaves; MatSus broader process approved by final human decision 2.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000046 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000046 "The SSbD result-like textual wording is not inherited.")`

**Rationale** Exposure assessment denotes the process. Review also covered the source restriction or correspondence described in the notes.

**After**

> Exposure assessment denotes the process. SSbD result-like wording does not define the MatSus class, and the model does not introduce a separate exposure-estimate information class.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000047`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000047 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000047 "Risk assessment is a process; risk estimate is information resulting from such an assessment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000047 "SRC-005 SSbD environmental and human-health risk-assessment leaves; process/result distinction approved by final human decisions 2 and 5.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000047 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000047 "SSbD EnvironmentalRiskAssessment has estimate-like wording; MatSus retains a process category.")`

**Rationale** Risk assessment denotes the process. Review also covered the source restriction or correspondence described in the notes.

**After**

> Risk assessment denotes the process. Its risk estimate is resulting information. This distinction matters for interpreting the conceptual SSbD correspondence, since its environmental risk assessment uses estimate-like wording.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000048`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000048 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000048 "This class does not require all three dimensions, and its aspect branches are neither disjoint nor exhaustive."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000048 "SRC-005 SSbD SustainabilityAssessment; September MKB1 Material Sustainability Assessment carryover; final human decisions 2 and 3.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000048 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000048 "SSbD dimension restrictions are not inherited.")`

**Rationale** An assessment need not cover all three sustainability dimensions. Review also covered the source restriction or correspondence described in the notes.

**After**

> An assessment need not cover all three sustainability dimensions. The aspect branches are neither disjoint nor exhaustive, and the conceptual SSbD correspondence does not carry its dimension restrictions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000049`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000049 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000049 "Impact categories, environmental effects, and indicator results are not subclasses of this process. Dedicated life-cycle-assessment process classes are modelled under sustainability assessment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000049 "SRC-005 SSbD EnvironmentalSustainabilityAssessment; LCA content was deferred during SRC-005 and introduced in the subsequent SRC-006 LCA implementation batch.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000049 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000049 "No SSbD impact-category descendants are imported or reproduced.")`

**Rationale** Impact categories, environmental effects and indicator results are distinct from the assessment process. Review also covered the source restriction or correspondence described in the notes.

**After**

> Impact categories, environmental effects and indicator results are distinct from the assessment process. Life cycle assessment processes sit under sustainability assessment, and the conceptual SSbD correspondence introduces no SSbD impact-category descendants.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000050`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000050 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000050 "This is a thin interoperability anchor. No method, criterion, child, or specialized-result axioms are added in this increment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000050 "SRC-005 SSbD EconomicSustainabilityAssessment; thin-anchor scope fixed by final human decision 10.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000050 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000050 "Only the superclass and annotation-level SSbD correspondence are asserted.")`

**Rationale** This class provides a general economic sustainability assessment anchor. Review also covered the source restriction or correspondence described in the notes.

**After**

> This class provides a general economic sustainability assessment anchor. Its SSbD correspondence is annotation-only, and no method, criterion, specialized result or child is specified.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000051`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000051 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000051 "This is a thin interoperability anchor. No method, criterion, child, or specialized-result axioms are added in this increment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000051 "SRC-005 SSbD SocialSustainabilityAssessment; thin-anchor scope fixed by final human decision 10.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000051 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000051 "Only the superclass and annotation-level SSbD correspondence are asserted.")`

**Rationale** This class provides a general social sustainability assessment anchor. Review also covered the source restriction or correspondence described in the notes.

**After**

> This class provides a general social sustainability assessment anchor. Its SSbD correspondence is annotation-only, and no method, criterion, specialized result or child is specified.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000052`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000052 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000052 "Ordinary material-characterization assays are not subclasses merely because they measure functional properties. PMDco assays and their results may be subprocesses or evidence when a concrete assessment uses them."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000052 "SRC-005 SSbD FunctionalityAssessment and pinned PMDco assay comparison; sustainability-context narrowing fixed by final human decision 4.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000052 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000052 "MatSus requires a sustainability or SSbD decision context; ordinary characterization is not included automatically.")`

**Rationale** Functionality assessment here requires a sustainability or safe-and-sustainable-by-design decision context. Review also covered the source restriction or correspondence described in the notes.

**After**

> Functionality assessment here requires a sustainability or safe-and-sustainable-by-design decision context. Ordinary characterization assays can provide evidence or occur as subprocesses without automatically falling under this class.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000053`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000053 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000053 "This is directive information, not a report, result, material input, or process. It inherits the plan-specification requirements for objective- and action-specification parts. A merely retrospective description is not thereby an assessment specification."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000053 "MKB1 assessment-method/specification carryover; imported IAO plan-specification axioms; CLEO lifecycle calculation request reviewed as partial evidence; final human decision 6.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000053 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000053 "CLEO lifecycle calculation request is a parameter specification, not a general assessment specification. No mapping to SSbD SpecifiedAssessment is asserted because that class denotes a process.")`

**Rationale** An assessment specification is directive information and inherits plan-specification requirements for objective and action specification parts. Review also covered the source restriction or correspondence described in the notes.

**After**

> An assessment specification is directive information and inherits plan-specification requirements for objective and action specification parts. A retrospective report, assessment result, material input or assessment process does not satisfy that scope. The CLEO lifecycle calculation request provides a partial correspondence as a parameter specification. SSbD SpecifiedAssessment denotes a process.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000054`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000054 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000054 "This is the broad common category for informational outputs of an assessment. It includes actual findings and documents but is not limited to either, and it does not imply specified-output provenance without an explicit process assertion."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000054 "SRC-005 information-output requirement and MKB1 process/specification/output distinction; final human decision 5.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000054 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000054 "SSbD Sign/Data categories are not aligned to BFO/IAO.")`

**Rationale** This information category covers both findings and documents from an assessment. Review also covered the source restriction or correspondence described in the notes.

**After**

> This information category covers both findings and documents from an assessment. Specified-output provenance requires an explicit process assertion. The SSbD Sign and Data categories do not provide a BFO/IAO category alignment.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000055`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000055 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000055 "This is the common parent for quantitative and qualitative findings. A plan, method, or report is not an individual result merely because it discusses one."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000055 "SRC-005 findings architecture and MKB1 result-information carryover; final human decision 5.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000055 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000055 "SSbD Property is a semiotic Sign, not a BFO quality or MatSus result class.")`

**Rationale** This is the common category for qualitative and quantitative findings. Review also covered the source restriction or correspondence described in the notes.

**After**

> This is the common category for qualitative and quantitative findings. A plan, method or report does not become a result by discussing one. The related SSbD Property denotes a semiotic sign, distinct from a BFO quality or a MatSus result.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000056`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000056 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000056 "This class inherits IAO's truth-intended and reliable-method semantics. It is not the process, specification, or report that generated or communicates it."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000056 "Imported IAO data-item semantics, SSbD Datum, and CLEO lifecycle-analysis result datum reviewed; final human decision 5.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000056 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000056 "CLEO is lifecycle-specific and SSbD uses a different upper category.")`

**Rationale** This class inherits IAO data-item semantics for truth-intended information produced by reliable methods, distinct from a process, specification or report. Review also covered the source restriction or correspondence described in the notes.

**After**

> This class inherits IAO data-item semantics for truth-intended information produced by reliable methods, distinct from a process, specification or report. CLEO's result datum is lifecycle-specific and the SSbD datum uses a different upper category. Both correspondences are non-entailing.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000057`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000057 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000057 "This class is distinct from metric specification and from the OBI value specification carrying its numeric or structured value. SSbD Indicator has a different input/property meaning."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000057 "MKB1 ADD-SCO-011 indicator-value carryover, existing MATSUS_0000027, SSbD Indicator mismatch, and CLEO result example reviewed; final human decisions 5 and 9.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000057 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; external correspondence is annotation-only and non-entailing")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000057 "SSbD Indicator is an input/property; CLEO's mapped class is climate-specific and carries the rejected carbon-dioxide-equivalent-disposition restriction.")`

**Rationale** An indicator result is distinct from its governing metric specification and from the OBI value specification carrying its value. Review also covered the source restriction or correspondence described in the notes.

**After**

> An indicator result is distinct from its governing metric specification and from the OBI value specification carrying its value. SSbD Indicator denotes an input or property, and CLEO's climate-specific correspondence does not carry its carbon-dioxide-equivalent disposition restriction into MatSus.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000058`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000058 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000058 "Qualitative estimates are allowed. A quantitative risk estimate may additionally be typed as assessment result datum or indicator result when warranted; no disjointness is asserted."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000058 "SRC-005 risk branch and process/result distinction; final human decision 5.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000058 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; no exact external class mapping was found")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000058 "SSbD risk-assessment candidates denote processes, not this result; the absence of a mappedTo annotation is deliberate.")`

**Rationale** A risk estimate may be qualitative. Review also covered the source restriction or correspondence described in the notes.

**After**

> A risk estimate may be qualitative. A quantitative estimate may also be typed as an assessment result datum or indicator result when warranted. No disjointness is asserted. SSbD risk assessments denote processes rather than these findings.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000059`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000059 "MKB2 SRC-005/SRC-006 final human decision, 2026-09-16")`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000059 "MKB1 assessment-report carryover, imported IAO document, and current MatSus report review; final human decisions 5 and 11.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000059 "MatSus-local class using the pinned PMDco/IAO/OBI backbone; no exact external class mapping was found")`
- essential modelling rationale — `AnnotationAssertion(:integrationNote :MATSUS_0000059 "Neither inspected ontology provides an assessment-report class matching this meaning; the absence of a mappedTo annotation is deliberate.")`

**Rationale** An assessment report is not identical to an individual result. Review also covered the source restriction or correspondence described in the notes.

**After**

> An assessment report is not identical to an individual result. It may have result information as actual content or be about an external result; those cases require different assertions.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000062`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000062 "MKB2 end-of-use architecture final human decision, 2026-09-20")`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000062 "MKB2 end-of-use competency questions and existing MatSus assessment architecture; final human decision, 2026-09-20.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000062 "MatSus-local assessment-process specialization using the existing evaluates relation")`

**Rationale** The assessment is distinct from the subsequent management process and does not imply that a recommended pathway is selected or executed.

**After**

> The assessment is distinct from the subsequent management process and does not imply that a recommended pathway is selected or executed. Functionality assessments, assays, and other analyses may provide evidence for the assessment.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000063`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000063 "MKB2 end-of-use architecture final human decision, 2026-09-20")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000063 "No universal is-about existential is asserted in this increment. In complete local records, consistency between the assessment's evaluated material entity and the recommendation's aboutness target is to be checked in the application-profile/SHACL layer."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000063 "MKB2 end-of-use competency questions and existing MatSus assessment-result architecture; final human decision, 2026-09-20.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000063 "MatSus-local specialization of assessment result information")`

**Rationale** The ontology asserts no universal is-about existential for a recommendation.

**After**

> The ontology asserts no universal is-about existential for a recommendation. For complete records, application-profile validation should check that the recommendation's aboutness target is the material entity evaluated by the associated assessment.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/RecycledContentInformation`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :RecycledContentInformation "MKB2 SRC-005/SRC-006 approved legacy indicator-result bridge, 2026-09-16")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :RecycledContentInformation "This is a calculated composition indicator, not an intrinsic quality. Detailed circularity and resource-flow semantics are deferred to CEON/BONSAI.")`
- audit-only — `AnnotationAssertion(:integrationMethod :RecycledContentInformation "new MatSus DPP data-item class based on BatteryPass requirements")`

**Rationale** This is a calculated composition indicator rather than an intrinsic quality.

**After**

> This is a calculated composition indicator rather than an intrinsic quality. Circularity and resource-flow assertions require a corresponding process or flow model.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :RecycledContentInformation <urn:samm:io.BatteryPass.Circularity:1.2.0#recycledContent>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :RecycledContentInformation "BatteryPass-ready Data Attribute Long List v1.3, attributes 48-54")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/SupplyChainDueDiligenceReport`

**Before**

- audit-only — `AnnotationAssertion(:integrationMethod :SupplyChainDueDiligenceReport "new MatSus document class based on BatteryPass requirements")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :SupplyChainDueDiligenceReport <urn:samm:io.BatteryPass.SupplyChainDueDiligence:1.2.0#supplyChainDueDiligenceReport>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :SupplyChainDueDiligenceReport "BatteryPass-ready Data Attribute Long List v1.3, attribute 36")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/TestReport`

**Before**

- audit-only — `AnnotationAssertion(:integrationMethod :TestReport "new MatSus document class based on BatteryPass requirements")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :TestReport <urn:samm:io.BatteryPass.Labels:1.2.0#resultOfTestReport>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :TestReport "BatteryPass-ready Data Attribute Long List v1.3, attribute 27")`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000065`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000065 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000065 "MKB2 SRC-006 CLEO/LCA source gate and final MatSus LCA architecture decision, 2026-09-18.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000065 "MatSus-local sustainability-assessment specialization using the existing PMDco/IAO/OBI backbone")`

**Rationale** Life cycle inventory analysis and life cycle impact assessment are represented as process parts of a life cycle assessment, not as subclasses of it.

**After**

> Life cycle inventory analysis and life cycle impact assessment are represented as process parts of a life cycle assessment, not as subclasses of it. No universal specified-output restriction is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000066`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000066 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000066 "This process is modelled under planned process rather than assessment process. Its occurrence may be a process part of a life cycle assessment."@en)`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000066 "MKB2 SRC-006 CLEO/LCA source gate and final MatSus LCA architecture decision, 2026-09-18.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000066 "MatSus-local planned-process specialization")`

**Rationale** Inventory analysis is a planned process for compiling inputs and outputs.

**After**

> Inventory analysis is a planned process for compiling inputs and outputs. It may occur as part of a life cycle assessment without itself being classified as an assessment process.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000067`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000067 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000067 "MKB2 SRC-006 CLEO/LCA source gate and final MatSus LCA architecture decision, 2026-09-18.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000067 "MatSus-local sustainability-assessment specialization")`

**Rationale** This class is parallel to life cycle assessment under sustainability assessment and may occur as a process part of a life cycle assessment.

**After**

> This class is parallel to life cycle assessment under sustainability assessment and may occur as a process part of a life cycle assessment.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000068`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000068 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationBasis :MATSUS_0000068 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18.")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000068 "MatSus-local specialization of assessment specification")`

**Rationale** Functional unit, reference flow, and system boundary specifications are represented as information parts of the life cycle assessment specification.

**After**

> Functional unit, reference flow, and system boundary specifications are represented as information parts of the life cycle assessment specification.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000069`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000069 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000069 "MatSus-local directive information entity")`

**Rationale** This is information specifying the reference basis of the assessment, not a physical unit and not the assessed process itself.

**After**

> This is information specifying the reference basis of the assessment, not a physical unit and not the assessed process itself.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000070`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000070 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000070 "The exact directive-information subtype is intentionally not asserted in this increment."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000070 "MatSus-local information-content specialization")`

**Rationale** This information content entity specifies a reference flow.

**After**

> This information content entity specifies a reference flow. The ontology does not commit to a narrower directive-information subtype.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000071`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000071 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000071 "MatSus-local directive information entity")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000072`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000072 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000072 "This is a generic system-model class. A separate lifecycle system model is intentionally deferred."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000072 "MatSus-local generic information-content specialization")`

**Rationale** This information class models systems generically, including in lifecycle contexts.

**After**

> This information class models systems generically, including in lifecycle contexts. No separate lifecycle-system-model subclass is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000073`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000073 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000073 "MatSus-local information-content specialization")`

**Rationale** An impact category is information used to organize and interpret impact assessment; it is not itself an assessment process or environmental effect.

**After**

> An impact category is information used to organize and interpret impact assessment; it is not itself an assessment process or environmental effect.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000074`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000074 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000074 "MatSus-local specialization of assessment result information")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000076`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000076 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000076 "MatSus-local primitive specialization of indicator result")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000077`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000077 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000077 "MatSus-local result-to-result relation")`

**Rationale** This relation does not assert parthood, arithmetic summation, exhaustive coverage, or transitivity.

**After**

> This relation does not assert parthood, arithmetic summation, exhaustive coverage, or transitivity.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000078`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000078 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000079`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000079 "MKB2 SRC-006 LCA architecture final human decision, 2026-09-18")`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000080`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000080 "MKB2 SRC-007 consolidated human-gate decision, 2026-10-09")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000080 "This is a generic disposition whose intended bearer is a material entity. PMDco PMD_0080133 uses a narrower wear-, tear-, and damage-resistance meaning and is classified under PMDco's provisional unclassified property branch; no equivalence or subclass relation is asserted pending separate alignment approval."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000080 "MatSus-local disposition specialization using the pinned BFO semantics")`

**Rationale** Durability here is a generic disposition of a material entity.

**After**

> Durability here is a generic disposition of a material entity. PMDco PMD_0080133 has the narrower meaning of resistance to wear, tear and damage and sits under PMDco's unclassified property branch. No equivalence or subclass relationship is asserted.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000081`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000081 "MKB2 SRC-007 consolidated human-gate decision, 2026-10-09")`
- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000081 "This generic datum is not asserted to be an indicator result or DPPInformation. The existing battery-specific RecycledContentInformation class is unchanged; any future relationship between the classes requires separate approval."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000081 "MatSus-local data-item specialization using the pinned IAO semantics")`

**Rationale** This general datum is separate from the battery-specific RecycledContentInformation class.

**After**

> This general datum is separate from the battery-specific RecycledContentInformation class. It has no asserted indicator-result or DPPInformation superclass.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000082`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000082 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** CRM status is contextual, not an intrinsic quality.

**After**

> CRM status is contextual, not an intrinsic quality. EU reference: Regulation (EU) 2024/1252, Article 4 and Annex II, as amended. Eligible bearers may include portions of matter, objects and aggregates, but mere containment of a critical raw material does not establish this role. The designation-to-bearer linkage requires contextual evidence.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000083`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000083 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Record the authority, jurisdiction, legal basis, applicable material category and temporal validity.

**After**

> Record the authority, jurisdiction, legal basis, applicable material category and temporal validity. This is not the physical material, CRM role, or technical criticality assessment result. No separate designation-list class is introduced.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000084`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000084 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Typical bearers are objects and aggregates.

**After**

> Typical bearers are objects and aggregates. Repair may require spare parts, tools and expertise. Repairability is distinct from assignment to a repair program and from a repairability assessment result.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000085`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000085 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Typical bearers are functional objects and assemblies.

**After**

> Typical bearers are functional objects and assemblies. Maintenance may be preventive or corrective. Maintainability is distinct from repairability; neither is asserted as a subclass of the other.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000086`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000086 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Bearers may include objects, aggregates and portions of matter.

**After**

> Bearers may include objects, aggregates and portions of matter. Distinguish capability from actual reuse and designation for reuse. EU Waste Framework Directive reuse terminology is narrower, focusing on non-waste products or components reused for the same purpose.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000087`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000087 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Interpret consistently with MatSus remanufacturing process MATSUS_0000036.

**After**

> Interpret consistently with MatSus remanufacturing process MATSUS_0000036. Do not assert equivalence with the distinct remanufacturing definition in Regulation (EU) 2024/1781. Typical bearers are used products and components.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000088`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000088 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Distinguish expected lifetime from observed service life, warranty, guarantee and the durability disposition.

**After**

> Distinguish expected lifetime from observed service life, warranty, guarantee and the durability disposition. Record assumptions, method, units and uncertainty. It may be an LCA input assumption or an assessment result, but is not universally an indicator result.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000089`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000089 "MatSus MKB2 SRC-007/008 human-gate decisions, October 2026"@en)`

**Rationale** Distinguish observed service duration from estimated lifetime.

**After**

> Distinguish observed service duration from estimated lifetime. Record start and end events and any interruption or uncertainty. Ongoing service records require explicit treatment of the observation endpoint; do not imply final retirement.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000090`

**Before**

- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000090 "MatSus LCC source gate and approved modelling specification, 2026-10-21"@en)`
- audit-only with genuine external sources already cited — `AnnotationAssertion(:integrationBasis :MATSUS_0000090 "Commission Recommendation (EU) 2026/510; JRC143022; Hunkeler, Lichtenvort and Rebitzer (eds.), Environmental Life Cycle Costing (2008); Swarr et al., Environmental Life Cycle Costing: A Code of Practice (2011); approved MatSus LCC modelling decision."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000090 "MatSus-local primitive specialization of assessment process; no external import or logical mapping added"@en)`

**Rationale** Conventional, environmental, and societal life cycle costing are distinguished by the scope and perspective prescribed by the governing specification.

**After**

> Conventional, environmental, and societal life cycle costing are distinguished by the scope and perspective prescribed by the governing specification. This class is not a subclass of economic sustainability assessment (MATSUS_0000050), because conventional life cycle costing need not evaluate economic sustainability. A life cycle costing assessment instance used for sustainability evaluation may additionally be typed as MATSUS_0000050. This class is distinct from life cycle assessment process (MATSUS_0000065).

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000090 <https://eur-lex.europa.eu/eli/reco/2026/510/oj/eng>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000090 <https://doi.org/10.2760/5103785>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000090 <https://doi.org/10.1201/9781420054736>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000090 <https://www.setac.org/resource/enviro-life-cycle-costing-code-practice.html>)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000091`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000091 "Relevant parameters include the life cycle costing variant, cost bearers, functional reference, lifecycle boundaries, time horizon, currency, reference year, discounting, cost categories, and externality treatment. These parameters remain at the information or application-profile level; no mandatory OWL restrictions are asserted. This class is distinct from life cycle assessment specification (MATSUS_0000068). A generic relation linking assessment processes to their governing specifications remains deferred."@en)`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000091 "MatSus LCC source gate and approved modelling specification, 2026-10-21"@en)`
- audit-only with genuine external sources already cited — `AnnotationAssertion(:integrationBasis :MATSUS_0000091 "Hunkeler, Lichtenvort and Rebitzer (eds.), Environmental Life Cycle Costing (2008); Swarr et al., Environmental Life Cycle Costing: A Code of Practice (2011); approved MatSus LCC modelling decision."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000091 "MatSus-local primitive specialization of assessment specification; method parameters remain information-level and unconstrained in this increment"@en)`

**Rationale** Relevant parameters include the costing variant, cost bearers, functional reference, lifecycle boundaries, time horizon, currency, reference year, discounting, cost categories, and externality treatment.

**After**

> Relevant parameters include the costing variant, cost bearers, functional reference, lifecycle boundaries, time horizon, currency, reference year, discounting, cost categories, and externality treatment. These are information-level or application-profile parameters without mandatory OWL restrictions. The scope is distinct from life cycle assessment specification (MATSUS_0000068). No generic relation from an assessment process to its governing specification is asserted.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000091 <https://doi.org/10.1201/9781420054736>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000091 <https://www.setac.org/resource/enviro-life-cycle-costing-code-practice.html>)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000092`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000092 "Cost results are distinct from revenues and benefits, which may remain generic indicator results and should be represented separately unless a governing metric specification explicitly calculates a net cost. A monetized externality may be represented as a cost result only when the life cycle costing method treats it as a monetary cost; the underlying physical environmental impact remains distinct. This class inherits the has indicator specification pattern from MATSUS_0000057. Currency vocabulary and monetary-value encoding remain deferred."@en)`
- audit-only — `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000092 "MatSus LCC source gate and approved modelling specification, 2026-10-21"@en)`
- audit-only with genuine external sources already cited — `AnnotationAssertion(:integrationBasis :MATSUS_0000092 "Hunkeler, Lichtenvort and Rebitzer (eds.), Environmental Life Cycle Costing (2008); Swarr et al., Environmental Life Cycle Costing: A Code of Practice (2011); approved MatSus LCC modelling decision."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000092 "MatSus-local primitive specialization of indicator result using the inherited indicator-specification pattern"@en)`

**Rationale** Cost results are distinct from revenues and benefits, which can be recorded separately as indicator results unless the governing metric specification calculates a net cost.

**After**

> Cost results are distinct from revenues and benefits, which can be recorded separately as indicator results unless the governing metric specification calculates a net cost. A monetized externality is a cost result only when the costing method treats it as a monetary cost. The underlying physical impact remains distinct. This class inherits the indicator-specification pattern. Currency and monetary-value encoding are not fixed by the class.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000092 <https://doi.org/10.1201/9781420054736>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000092 <https://www.setac.org/resource/enviro-life-cycle-costing-code-practice.html>)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000093`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000093 "This primitive specialization is not equivalent to PMDco dividing or separating. Its parent is PMD_0000614 because that class explicitly covers shear cutting, splitting, tearing, and breaking; no sorting, stream-separation, recycling-context, or product-shape restriction is asserted."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000093 "MatSus-local primitive specialization of PMDco dividing; no equivalence or additional logical restriction asserted"@en)`

**Rationale** PMDco dividing includes mechanical shear cutting, splitting, tearing and breaking, so shredding specializes that process without being equivalent to dividing or separating.

**After**

> PMDco dividing includes mechanical shear cutting, splitting, tearing and breaking, so shredding specializes that process without being equivalent to dividing or separating. No sorting, stream-separation, recycling-context or product-shape restriction is asserted.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000093 <https://www.basel.int/Portals/4/download.aspx?d=UNEP-CHW-WAST-GUID-ESM-PlasticWastes-20230512.English.pdf>)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000094`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000094 "This generic class is not restricted to polymers, recycling, a particular filter geometry, or a particular manufacturing operation. It is distinct from extrusion even when both occur within one integrated operation."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000094 "MatSus-local primitive specialization of OBI filtration from pinned OBI v2026-07-27; no equivalence or polymer/recycling restriction asserted"@en)`

**Rationale** Melt filtration specializes OBI filtration because the filter separates particles from a fluid melt.

**After**

> Melt filtration specializes OBI filtration because the filter separates particles from a fluid melt. It remains distinct from extrusion, even within an integrated operation. No equivalence or restriction to polymers, recycling, filter geometry, or a particular manufacturing operation is asserted.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000094 <http://purl.obolibrary.org/obo/OBI_0302885>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000094 <https://www.basel.int/Portals/4/download.aspx?d=UNEP-CHW.16-CRP.31.English.pdf>)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000095`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000095 "FoodOn drying FOODON_03000614 in the FoodOn 2026-09-20 artifact is conceptual inspiration for this materials-oriented definition. No equivalence, mapping, or FoodOn import is asserted. The class is not restricted to polymers, food, recycling, or a particular drying mechanism."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000095 "MatSus-local primitive specialization of OBI material component separation; FoodOn used as non-normative conceptual inspiration only"@en)`

**Rationale** Drying specializes material component separation by reducing a material's liquid content.

**After**

> Drying specializes material component separation by reducing a material's liquid content. FoodOn drying (FOODON_03000614, release 2026-09-20) provides conceptual inspiration without an import, equivalence, or mapping. The class is not restricted to food, polymers, recycling, or a particular drying mechanism.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000095 <http://purl.obolibrary.org/obo/FOODON_03000614>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000095 <http://purl.obolibrary.org/obo/foodon/releases/2026-09-20/foodon.owl>)`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/MATSUS_0000096`

**Before**

- valuable semantic note — `AnnotationAssertion(<http://www.w3.org/2004/02/skos/core#editorialNote> :MATSUS_0000096 "This generic class is not restricted to polymers, recycling, a particular pelletizing method, or particular machinery. Regranulation is not an alternative label or equivalent class; its process boundary remains unresolved. PMDco manufacturing process is the minimal parent because cutting or dividing is not common to every pelletizing method."@en)`
- audit-only — `AnnotationAssertion(:integrationMethod :MATSUS_0000096 "MatSus-local primitive specialization of PMDco manufacturing process; no equivalence or method-specific restriction asserted"@en)`

**Rationale** The manufacturing-process parent accommodates different pellet-formation mechanisms, which need not involve dividing.

**After**

> The manufacturing-process parent accommodates different pellet-formation mechanisms, which need not involve dividing. The class is not restricted to polymers, recycling, a particular method, or machinery. Regranulation is not an alternative label or equivalent class because its process boundary has not been established.

External sources retained

- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000096 <https://www.basel.int/Portals/4/download.aspx?d=UNEP-CHW-WAST-GUID-ESM-PlasticWastes-20230512.English.pdf>)`
- `AnnotationAssertion(<http://purl.org/dc/terms/source> :MATSUS_0000096 <https://publications.jrc.ec.europa.eu/repository/bitstream/JRC91637/2014-jrc91637%20.pdf>)`

**Preservation** Preserved.

## `src/ontology/components/matsus-log-stageA.ttl`

### `https://w3id.org/pmd/co/PMD_0040121`

**Before**

- audit-only — `dcterms:source "Supplied via LOGao; absent from the PMDco release in use for comparison." ;`
- valuable semantic note — `rdfs:comment "Namespace/version anomaly: this PMDco-namespace object property is supplied through LOGao but is absent from the compared PMDco release used for validation. It is retained for LOGao compatibility only and must not be treated as a stable PMDco backbone property without manual review." ;`
- audit-only — `skos:editorialNote "LOG compatibility exception" ;`
- audit-only — `skos:note "needs human review" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "LOG supplies this PMDco-namespace object property; added without altering existing PMDco hierarchy or adding new Mat.Sus modelling commitments." .`

**Rationale** LOGao supplies this PMDco-namespace object property for compatibility. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOGao supplies this PMDco-namespace object property for compatibility. It is absent from the pinned PMDco release and should not be used as an authoritative PMDco backbone property without checking the upstream release.

Additional annotation text

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/co/PMD_0040129`

**Before**

- audit-only — `dcterms:source "Supplied via LOGao; absent from the PMDco release in use for comparison." ;`
- valuable semantic note — `rdfs:comment "Namespace/version anomaly: this PMDco-namespace class is present in this combined ontology via LOGao, but is absent from the compared PMDco release used for validation (pmdco-full.ttl). It is retained for LOGao compatibility only, must not be treated as a stable PMDco backbone anchor, and should not be used to justify broader PMDco restructuring without manual review." ;`
- audit-only — `skos:editorialNote "LOG compatibility exception" ;`
- audit-only — `skos:note "needs human review" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "LOG introduces this PMDco-namespace extension class; integrated without altering existing PMDco superclass logic." .`

**Rationale** LOGao supplies this PMDco-namespace class for compatibility. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOGao supplies this PMDco-namespace class for compatibility. It is absent from the pinned PMDco release and should not be used as an authoritative PMDco backbone class without checking the upstream release.

Additional annotation text

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/co/PMD_0040151`

**Before**

- audit-only — `dcterms:source "Supplied via LOGao; absent from the PMDco release in use for comparison." ;`
- valuable semantic note — `rdfs:comment "Namespace/version anomaly: this PMDco-namespace class is present in this combined ontology via LOGao, but is absent from the compared PMDco release used for validation (pmdco-full.ttl). It is retained for LOGao compatibility only, must not be treated as a stable PMDco backbone anchor, and should not be used to justify broader PMDco restructuring without manual review." ;`
- audit-only — `skos:editorialNote "LOG compatibility exception" ;`
- audit-only — `skos:note "needs human review" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "LOG introduces this PMDco-namespace extension class; integrated without altering existing PMDco superclass logic." .`

**Rationale** LOGao supplies this PMDco-namespace class for compatibility. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOGao supplies this PMDco-namespace class for compatibility. It is absent from the pinned PMDco release and should not be used as an authoritative PMDco backbone class without checking the upstream release.

Additional annotation text

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0000000`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0000002`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0080000`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0080001`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0080002`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000002`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000004`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000007`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000009`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000010`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_10000105`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000012`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000013`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000014`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000015`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000017`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "Named parent adjusted during Stage A integration. LOG manufacturer kept as a class under agent/organization and additionally aligned to OBI manufacturer." .`

**Rationale** A LOG manufacturer is an organization in the LOG agent branch that bears a manufacturer role. Review also covered the source restriction or correspondence described in the notes.

**After**

> A LOG manufacturer is an organization in the LOG agent branch that bears a manufacturer role. Its OBI correspondence preserves that LOG agent structure.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000018`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000024`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000025`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000026`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000027`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000031`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000033`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000035`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000036`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000039`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000040`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000042`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000043`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000044`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000046`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000059`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000061`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "Named parent adjusted during Stage A integration. LOG manufacturer role aligned to OBI manufacturer role while preserving LOG agent-role structure." .`

**Rationale** The role of an organization producing material products is aligned with the OBI manufacturer role within the LOG agent-role hierarchy. Review also covered the source restriction or correspondence described in the notes.

**After**

> The role of an organization producing material products is aligned with the OBI manufacturer role within the LOG agent-role hierarchy.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000066`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000068`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000069`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000079`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000088`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000089`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000090`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000093`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000096`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000099`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000100`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000101`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000102`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000103`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000115`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000116`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000119`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000120`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000122`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000129`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000132`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000135`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000141`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000142`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000145`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/components/matsus-log-stageA.ttl`

**Before**

- audit-only — `"Preserves the accepted Mat.Sus Stage A integration of LOG classes, properties, alignments, weakened axioms, compatibility exceptions, definitions, and integration annotations. This Mat.Sus component is adapted from the Platform MaterialDigital Application Ontology for Logistics and Supply Chain (LOG), based on upstream main commit 0c89424ffc17096599d5bfdcfba783686494d49e; ontology source content at that revision corresponds to LOG v1.0.2." ;`

**Rationale** Module-level external attribution, source, licence, and version remain available.

**After**

No editorial note in this source.

Additional annotation text

- `"Contains selected LOG classes, properties, alignments, compatibility exceptions and definitions curated for Mat.Sus. This Mat.Sus component is adapted from the Platform MaterialDigital Application Ontology for Logistics and Supply Chain (LOG), based on upstream main commit 0c89424ffc17096599d5bfdcfba783686494d49e. The ontology source content at that revision corresponds to LOG v1.0.2." ;`

External sources retained

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/co/PMD_0040122`

**Before**

- audit-only — `dcterms:source "Supplied via LOGao; absent from the PMDco release in use for comparison." ;`
- valuable semantic note — `rdfs:comment "Namespace/version anomaly: this PMDco-namespace object property is supplied through LOGao but is absent from the compared PMDco release used for validation. It is retained for LOGao compatibility only and must not be treated as a stable PMDco backbone property without manual review." ;`
- audit-only — `skos:editorialNote "LOG compatibility exception" ;`
- audit-only — `skos:note "needs human review" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "LOG supplies this PMDco-namespace object property; added without altering existing PMDco hierarchy or adding new Mat.Sus modelling commitments." .`

**Rationale** LOGao supplies this PMDco-namespace object property for compatibility. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOGao supplies this PMDco-namespace object property for compatibility. It is absent from the pinned PMDco release and should not be used as an authoritative PMDco backbone property without checking the upstream release.

Additional annotation text

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0000003`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000016`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000019`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000021`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000051`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000095`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000118`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000124`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000125`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000134`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000146`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "Named parent adjusted during Stage A integration. Physical premises treated as material facility/object aggregate located at a geospatial site; org:Site kept only as external interpretation, not as superclass." .`

**Rationale** Physical premises are a material facility modelled as an object aggregate located at a geospatial site. Review also covered the source restriction or correspondence described in the notes.

**After**

> Physical premises are a material facility modelled as an object aggregate located at a geospatial site. The correspondence to org:Site is conceptual and supplies no superclass.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_0000001`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000000`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000003`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000006`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000008`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000030`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000032`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000037`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "Named parent adjusted during Stage A integration. LOG lot integrated as a narrower subclass of PMDco lot to avoid unsafe equivalence." .`

**Rationale** The shared production history and specifications make this LOG lot narrower than a PMDco lot, so it is a subclass without an equivalence assertion. Review also covered the source restriction or correspondence described in the notes.

**After**

> The shared production history and specifications make this LOG lot narrower than a PMDco lot, so it is a subclass without an equivalence assertion.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000052`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000053`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000056`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000060`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000062`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000067`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000070`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000071`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000072`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000073`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000075`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000076`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000077`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000078`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000080`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000081`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000082`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000083`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000098`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000104`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000105`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000111`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000114`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000117`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved. Both definitions and all axioms match the baseline. See the separate [unresolved semantic-review finding](#log_1000117-transportation-service).

### `https://w3id.org/pmd/log/LOG_1000121`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000126`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000005`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000022`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000028`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000034`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000041`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000047`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- audit-only — `matsus:integrationNote "Named parent adjusted during Stage A integration." .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000055`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000058`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000063`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000106`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000128`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000144`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/co/PMD_0040030`

**Before**

- audit-only — `dcterms:source "Supplied via LOGao; absent from the PMDco release in use for comparison." ;`
- valuable semantic note — `rdfs:comment "Namespace/version anomaly: this PMDco-namespace class is present in this combined ontology via LOGao, but is absent from the compared PMDco release used for validation (pmdco-full.ttl). It is retained for LOGao compatibility only, must not be treated as a stable PMDco backbone anchor, and should not be used to justify broader PMDco restructuring without manual review." ;`
- audit-only — `skos:editorialNote "LOG compatibility exception" ;`
- audit-only — `skos:note "needs human review" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "LOG introduces this PMDco-namespace extension class; integrated without altering existing PMDco superclass logic." .`

**Rationale** LOGao supplies this PMDco-namespace class for compatibility. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOGao supplies this PMDco-namespace class for compatibility. It is absent from the pinned PMDco release and should not be used as an authoritative PMDco backbone class without checking the upstream release.

Additional annotation text

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000001`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000023`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000038`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000057`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000064`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000065`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000084`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000097`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000143`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000140`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000085`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000091`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000123`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_10001247`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000131`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000020`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000112`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000113`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000029`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000050`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "Named parent adjusted during Stage A integration. LOG organization kept as a distinct LOG class but placed under OBI organization; external org:FormalOrganization superclass removed." .`

**Rationale** LOG organization is a distinct specialization of OBI organization. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOG organization is a distinct specialization of OBI organization. The W3C org:FormalOrganization class supplies no superclass.

**Preservation** Preserved. The definition and axioms match the baseline. See the separate [unresolved semantic-review finding](#log_1000050-organization) for the conflict between the definition and the imported OBI superclass hierarchy.

### `https://w3id.org/pmd/co/PMD_0040029`

**Before**

- audit-only — `dcterms:source "Supplied via LOGao; absent from the PMDco release in use for comparison." ;`
- valuable semantic note — `rdfs:comment "Namespace/version anomaly: this PMDco-namespace class is present in this combined ontology via LOGao, but is absent from the compared PMDco release used for validation (pmdco-full.ttl). It is retained for LOGao compatibility only, must not be treated as a stable PMDco backbone anchor, and should not be used to justify broader PMDco restructuring without manual review." ;`
- audit-only — `skos:editorialNote "LOG compatibility exception" ;`
- audit-only — `skos:note "needs human review" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "LOG introduces this PMDco-namespace extension class; integrated without altering existing PMDco superclass logic." .`

**Rationale** LOGao supplies this PMDco-namespace class for compatibility. Review also covered the source restriction or correspondence described in the notes.

**After**

> LOGao supplies this PMDco-namespace class for compatibility. It is absent from the pinned PMDco release and should not be used as an authoritative PMDco backbone class without checking the upstream release.

Additional annotation text

- `dcterms:source <https://github.com/materialdigital/logistics-application-ontology/commit/0c89424ffc17096599d5bfdcfba783686494d49e> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000054`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "BFO role preserved as authoritative; external org/skos role branch not imported." .`

**Rationale** This agent role uses the BFO role category. Review also covered the source restriction or correspondence described in the notes.

**After**

> This agent role uses the BFO role category. Correspondence to web organization roles does not import the external org/SKOS role hierarchy.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000130`

**Before**

- audit-only — `matsus:alignmentRelation "related extension" ;`
- audit-only — `matsus:integrationBasis "b) LOGao logic" ;`
- audit-only — `matsus:integrationMethod "subclassing" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

**Preservation** Preserved.

### `https://w3id.org/pmd/log/LOG_1000011`

**Before**

- audit-only — `matsus:integrationBasis "d) justified new Mat.Sus integration decision" ;`
- audit-only — `matsus:integrationMethod "subclassing" ;`
- essential modelling rationale — `matsus:integrationNote "Single LOG agent branch retained under material entity; external PROV/DC/FOAF agent branches excluded." .`

**Rationale** The LOG agent branch is grounded under material entity. Review also covered the source restriction or correspondence described in the notes.

**After**

> The LOG agent branch is grounded under material entity. Correspondences to PROV, DC and FOAF agent notions do not import their hierarchies.

**Preservation** Preserved.

## `src/ontology/components/matsus-dppo.ttl`

### `http://w3id.org/dppo/ontology/dpp-comp/aboutPart`

**Before**

- essential modelling rationale — `matsus:integrationMethod "selective reuse with corrected unversioned dpp-info reference" .`

**Rationale** The domain uses the unversioned DPPO CompositionInformation IRI defined in dpp-info. Review also covered the source restriction or correspondence described in the notes.

**After**

> The domain uses the unversioned DPPO CompositionInformation IRI defined in dpp-info.

External sources retained

- `dcterms:source dpp-comp: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-core/ComponentDPP`

**Before**

- essential modelling rationale — `matsus:integrationMethod "selective reuse with weakened source axiom" ;`

**Rationale** MatSus uses a necessary IAO aboutness restriction to the LOG Component anchor. Review also covered the source restriction or correspondence described in the notes.

**After**

> MatSus uses a necessary IAO aboutness restriction to the LOG Component anchor. Aboutness does not make every DPP record mentioning a component an instance of this subtype.

External sources retained

- `dcterms:source dpp-core: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-core/ConsumerProductDPP`

**Before**

- valuable semantic note — `skos:editorialNote "The source preferred label contains the spelling 'Comsumer'; the corrected label is used and the source spelling is retained as an alternative label." ;`
- essential modelling rationale — `matsus:integrationMethod "selective reuse with weakened source axiom" ;`

**Rationale** The IAO aboutness restriction to the broader LOG material-product anchor is necessary only. Review also covered the source restriction or correspondence described in the notes.

**After**

> The IAO aboutness restriction to the broader LOG material-product anchor is necessary only. A passport about a material product is not thereby a consumer-product passport. The source spelling 'Comsumer' is retained as an alternative label.

External sources retained

- `dcterms:source dpp-core: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-core/MaterialDPP`

**Before**

- essential modelling rationale — `matsus:integrationMethod "selective reuse with weakened source axiom" ;`

**Rationale** MatSus uses a necessary IAO aboutness restriction to the PMDco material anchor. Review also covered the source restriction or correspondence described in the notes.

**After**

> MatSus uses a necessary IAO aboutness restriction to the PMDco material anchor. Aboutness alone does not establish membership in this passport subtype.

External sources retained

- `dcterms:source dpp-core: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-core/SubstanceDPP`

**Before**

- essential modelling rationale — `matsus:integrationMethod "selective reuse with weakened source axiom" ;`

**Rationale** MatSus uses a necessary IAO aboutness restriction to the PMDco-imported chemical substance anchor. Review also covered the source restriction or correspondence described in the notes.

**After**

> MatSus uses a necessary IAO aboutness restriction to the PMDco-imported chemical substance anchor. Aboutness alone does not establish membership in this passport subtype.

External sources retained

- `dcterms:source dpp-core: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/ProductCharacteristic`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "This is an information content entity, not the physical characteristic or its value." .`

**Rationale** This information content entity describes a physical characteristic. Review also covered the source restriction or correspondence described in the notes.

**After**

> This information content entity describes a physical characteristic. The characteristic and its value are separate entities.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/ProductQuality`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "This is an information content entity and is not subclassed under BFO quality." .`

**Rationale** This class covers information about a quality. Review also covered the source restriction or correspondence described in the notes.

**After**

> This class covers information about a quality. The described quality is a separate entity in the BFO quality branch.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/containsInformation`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-prov/ValueChainActor`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse aligned through DPPO Actor to LOG agent" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source dpp-prov: ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/matsus/components/matsus-dppo.ttl`

**Before**

- audit-only — `dcterms:description "Mat.Sus selected and modified/adapted content from five DPPO 0.1 modules. Existing DPPO entity IRIs are retained; local integration annotations and selected axioms document the Mat.Sus adaptation." ;`
- audit-only — `dcterms:rights "DPPO 0.1 content is reused under CC BY 4.0. Mat.Sus selected and modified/adapted that content and identifies the changes through integration annotations." ;`

**Rationale** Module-level external attribution, source, licence, and version remain available.

**After**

No editorial note in this source.

Additional annotation text

- `dcterms:description "Mat.Sus selected and modified/adapted content from five DPPO 0.1 modules. The Mat.Sus adaptation retains the DPPO entity IRIs. Selected axioms and editorial notes describe the adaptation." ;`
- `dcterms:rights "DPPO 0.1 content is reused under CC BY 4.0. Mat.Sus selected and modified/adapted that content and records the adaptation in the repository's decision archive." ;`

External sources retained

- `dcterms:source <https://github.com/LiUSemWeb/DPPO/tree/dd39101cdf2bde6d1749123b6fb250c13644ddbd/ontology/dpp-comp/0.1>,`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-comp/aboutWhole`

**Before**

- essential modelling rationale — `matsus:integrationMethod "selective reuse with corrected unversioned dpp-info reference" .`

**Rationale** The domain uses the unversioned DPPO CompositionInformation IRI defined in dpp-info. Review also covered the source restriction or correspondence described in the notes.

**After**

> The domain uses the unversioned DPPO CompositionInformation IRI defined in dpp-info.

External sources retained

- `dcterms:source dpp-comp: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/CertificateInformation`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "Kept distinct from the certificate document and from a compliance result." .`

**Rationale** This is information about a certificate. Review also covered the source restriction or correspondence described in the notes.

**After**

> This is information about a certificate. The certificate document and a compliance result are separate entities.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/DisassemblyInformation`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/RepairInstruction`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "Not classified as a repair process or a repairability disposition. A stricter directive-information-entity placement is deferred." .`

**Rationale** This term denotes information about how to repair and belongs to the DPP information branch. Review also covered the source restriction or correspondence described in the notes.

**After**

> This term denotes information about how to repair and belongs to the DPP information branch. Repair occurrences and repairability dispositions are separate entities. No narrower directive-information placement is asserted.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/hasCompositionInformation`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse with PMDco-aligned interpretation" .`

**Rationale** The source dpp-comp versioned reference dpp-info/0.1/hasCompositionInformation is mapped to this unversioned IRI.

**After**

> The source dpp-comp versioned reference dpp-info/0.1/hasCompositionInformation is mapped to this unversioned IRI.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/LegalGuarantee`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/CompositionInformation`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" .`

**Rationale** The unversioned IRI defined in dpp-info is authoritative in this materialization; versioned dpp-info/0.1 references in dpp-comp are mapped to it.

**After**

> The unversioned IRI defined in dpp-info is authoritative in this materialization; versioned dpp-info/0.1 references in dpp-comp are mapped to it.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/externalDocument`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse with IAO-aligned range" .`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-prov/Actor`

**Before**

- audit-only — `matsus:integrationMethod "subclassing under the authoritative LOG agent branch" ;`

**Rationale** No independent rationale in the removed workflow text beyond the retained definition, axiom or mapping.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source dpp-prov: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-odp/DPP`

**Before**

- audit-only — `matsus:integrationBasis "DPPO ontology-level semantic source aligned to the PMDco/IAO backbone" ;`
- audit-only — `matsus:integrationMethod "selective direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "Placed under IAO information content entity. The source all-values-from hasPart restriction was intentionally omitted, and DPP is not yet classified as a document." .`

**Rationale** A DPP is an IAO information content entity, with no commitment that every passport is a document. Review also covered the source restriction or correspondence described in the notes.

**After**

> A DPP is an IAO information content entity, with no commitment that every passport is a document. Its information can include subordinate DPP information. The omitted source all-values-from restriction on hasPart leaves the types of parts open.

External sources retained

- `dcterms:source dpp-odp: ;`

**Preservation** Preserved.

### `http://w3id.org/dppo/ontology/dpp-info/DPPInformation`

**Before**

- audit-only — `matsus:integrationMethod "selective direct reuse" ;`
- essential modelling rationale — `matsus:integrationNote "The source restriction to DPPO Product was omitted. Instances use IAO is about to refer to authoritative PMDco/LOG entities." .`

**Rationale** The class is an IAO information content entity. Review also covered the source restriction or correspondence described in the notes.

**After**

> The class is an IAO information content entity. Its subject is represented by IAO is about using the appropriate PMDco or LOG entity, without the source restriction to DPPO Product.

External sources retained

- `dcterms:source dpp-info: ;`

**Preservation** Preserved.

## `src/ontology/components/matsus-ceon.ttl`

### `https://w3id.org/pmd/matsus/MATSUS_0000000`

**Before**

- audit-only — `dcterms:source "Mat.Sus CEON Phase 12 approved modelling decision; MKB2 end-of-use architecture refinement, 2026-09-20" ;`
- audit-only — `matsus:integrationBasis "MatSus application-level end-of-use process branch grounded under the PMDco-imported planned process hierarchy" ;`
- audit-only — `matsus:integrationMethod "MatSus-local class with selected CEON and MatSus process subclasses" .`

**Rationale** This branch is grounded in planned process because it covers planned handling following a use phase.

**After**

> This branch is grounded in planned process because it covers planned handling following a use phase. Generic process classes can apply in other contexts and do not automatically fall under end-of-use management.

**Preservation** Preserved.

### `http://w3id.org/CEON/ontology/process/ReuseProcess`

**Before**

- essential modelling rationale — `matsus:integrationMethod "MatSus-authored subclassing under end of use management process" .`

**Rationale** The end-of-use interpretation is expressed by the existing superclass and reuse definition.

**After**

No editorial note in this source.

External sources retained

- `dcterms:source <http://w3id.org/CEON/ontology/process/0.5/> ;`

**Preservation** Preserved.

### `http://w3id.org/CEON/ontology/process/RefurbishmentProcess`

**Before**

- essential modelling rationale — `matsus:integrationMethod "MatSus-authored subclassing under end of use management process" .`

**Rationale** The alternative label reconditioning is a MatSus application-level terminology decision, not an asserted synonym from the CEON source. Review also covered the source restriction or correspondence described in the notes.

**After**

> The alternative label reconditioning is a MatSus application-level terminology decision, not an asserted synonym from the CEON source.

External sources retained

- `dcterms:source <http://w3id.org/CEON/ontology/process/0.5/> ;`

**Preservation** Preserved.

### `http://w3id.org/CEON/ontology/process/RepairProcess`

**Before**

- essential modelling rationale — `matsus:integrationMethod "MatSus-authored grounding under COB planned process; end-of-use status is contextual" .`

**Rationale** The generic repair class is not placed under end of use management process because repair may also occur during ordinary use, maintenance, or other non-end-of-use contexts. Review also covered the source restriction or correspondence described in the notes.

**After**

> The generic repair class is not placed under end of use management process because repair may also occur during ordinary use, maintenance, or other non-end-of-use contexts.

External sources retained

- `dcterms:source <http://w3id.org/CEON/ontology/process/0.5/> ;`

**Preservation** Preserved.

### `http://w3id.org/CEON/ontology/process/RecycleProcess`

**Before**

- essential modelling rationale — `matsus:integrationMethod "MatSus-authored grounding under COB planned process; end-of-use status is contextual" .`

**Rationale** The generic recycle class is not placed under end of use management process because recycling may also concern pre-consumer, production, or other material streams that are not end-of-use. Review also covered the source restriction or correspondence described in the notes.

**After**

> The generic recycle class is not placed under end of use management process because recycling may also concern pre-consumer, production, or other material streams that are not end-of-use.

External sources retained

- `dcterms:source <http://w3id.org/CEON/ontology/process/0.5/> ;`

**Preservation** Preserved.

### `https://w3id.org/pmd/co/PMD_0000612`

**Before**

- essential modelling rationale — `matsus:integrationMethod "PMDco class reused as the authoritative MSE disassembling concept; end-of-use status is contextual" .`

**Rationale** The generic PMDco disassembling class remains outside the end of use management hierarchy because disassembling can also occur in manufacturing, maintenance, inspection, reconfiguration, or other non-end-of-use contexts. Review also covered the source restriction or correspondence described in the notes.

**After**

> The generic PMDco disassembling class remains outside the end of use management hierarchy because disassembling can also occur in manufacturing, maintenance, inspection, reconfiguration, or other non-end-of-use contexts. MatSus reuses PMDco PMD_0000612 instead of retaining the overlapping CEON DisassemblingProcess and DismantleProcess terms.

**Preservation** Preserved.

### `http://w3id.org/CEON/ontology/process/DeconstructionProcess`

**Before**

- essential modelling rationale — `matsus:integrationMethod "MatSus-authored grounding under COB planned process; end-of-use status is contextual" .`

**Rationale** The generic deconstruction class is not placed under end of use management process because deconstruction can also occur in other technical or operational contexts. Review also covered the source restriction or correspondence described in the notes.

**After**

> The generic deconstruction class is not placed under end of use management process because deconstruction can also occur in other technical or operational contexts.

External sources retained

- `dcterms:source <http://w3id.org/CEON/ontology/process/0.5/> ;`

**Preservation** Preserved.

### `http://w3id.org/CEON/ontology/process/TakeBackProcess`

**Before**

- essential modelling rationale — `matsus:integrationMethod "MatSus-authored grounding under COB planned process; end-of-use status is contextual" .`

**Rationale** The generic take-back class remains outside the end of use management hierarchy because take-back denotes a return or logistics activity and does not by itself determine the subsequent disposition. Review also covered the source restriction or correspondence described in the notes.

**After**

> The generic take-back class remains outside the end of use management hierarchy because take-back denotes a return or logistics activity and does not by itself determine the subsequent disposition.

External sources retained

- `dcterms:source <http://w3id.org/CEON/ontology/process/0.5/> ;`

**Preservation** Preserved.
