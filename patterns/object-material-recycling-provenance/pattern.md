# Pattern: Object–Material Recycling Provenance

> **Scientific status:** The 94-triple P1 ABox and its scientific interpretation were accepted through independent evaluation rounds R1–R3 on 2026-10-27. The initial integration was committed and pushed to branch `p1-r3-integration-20261027`; it has not been merged into `main` or released. This guide reorganizes and explains the accepted model without changing its RDF assertions.

## Purpose

This pattern demonstrates how to describe an end-of-use scenario while keeping four modelling layers distinct:

- an object and its material classification can apply to the **same physical individual**;
- an assessment process, its result information and its recommendation are different entities;
- a recommendation can identify a suitable end-of-use process without entailing that the process is authorized or executed; and
- asserted process inputs, outputs, subprocesses, participants and documentation can provide qualitative recycling provenance without implying quantitative or certified claims.

The example is a **synthetic, material-centred gearbox scenario**. It is intended as a modelling guide, not as an authenticated inspection, production record or conformity statement.

## Pattern artifacts

- [Accepted example data](shape-data.ttl) — 94 asserted triples; SHA-256 `96bee3a4f0c6cd5382d05bc9b73ab3ffcebbd5934c09a81cac738fa3b8c02e77`.
- [Regression runner](validation/run_queries.py) and [expected bindings](validation/expected_rows.json).
- [Seven competency questions and two structural checks](validation/queries/).
- Four SVG schematics in [`diagrams/`](diagrams/).

## How to read the schematics

The diagrams use ABox individuals as their main nodes. Compact labels show asserted class membership using the ontology term name and identifier. Solid arrows reproduce RDF predicates in their asserted subject-to-object direction. Gray dashed arrows, boxes and callouts are explicitly marked as narrative sequence, absence statements or explanatory boundaries; they are not additional triples.

The common colours distinguish material entities and objects (blue), processes (orange), information entities (purple), qualities (green), sites (red), roles (yellow) and agents (teal). The diagrams are selective views of the same ABox, not separate models.

## 1. Overall scenario

<img src="diagrams/01-overview.svg" alt="Overall gearbox end-of-use scenario showing disassembly, sorting, separate housing and gear assessments, housing recycling and a gear reuse recommendation only" width="100%"/>

The used gearbox is asserted as an object and has the housing and gear as parts. These `has part (BFO_0000051)` assertions represent the **pre-disassembly assembly** and are not temporally qualified in OWL.

The disassembly process has the gearbox as specified input and the housing and gear as specified outputs. The sorting process has each component as both specified input and specified output. The dashed sequence between disassembly and sorting in the figure is scenario context only: no temporal-order predicate connects those processes in the ABox.

The housing and gear are evaluated in two distinct end-of-use disposition assessments. The housing pathway includes an independently asserted recycling process and recovered ingot. The gear pathway ends with a potential-reuse recommendation; there is no executed gear-reuse process in the graph.

## 2. Object–material duality, composition and damage

<img src="diagrams/02-object-material-duality.svg" alt="Housing and gear object-material duality with chemical composition, crack site and defect role" width="100%"/>

The housing is **one physical individual** with two asserted types:

- `object (BFO_0000030)`; and
- `aluminium alloy (PMD_0020186)`.

The gear follows the same duality pattern and is typed as both `object (BFO_0000030)` and `steel (PMD_0020096)`. The recovered aluminium-alloy ingot is a **different individual** from the original housing.

The housing bears a `chemical composition (PMD_0000551)` quality through `has quality (RO_0000086)`. This quality is not an experimental chemical analysis, a composition value or a measured information datum. The nominal alloy designation in the housing label does not establish post-recycling grade conformity.

The structural crack is a `crack (PMD_0020202)`, which PMDco classifies under BFO site. The asserted damage structure is deliberately limited to:

- housing `location of (RO_0001015)` crack; and
- crack `has role (RO_0000087)` defect role.

No `part of` or `has part` assertion connects the crack and housing. PMDco's defect-role definition refers to a continuant part of an affected material entity; whether an immaterial crack site satisfies that intended description remains a **separate PMDco semantic clarification**. P1 does not repair that open issue by inventing a parthood assertion or damage-evolution process.

## 3. End-of-use assessments and recommendations

<img src="diagrams/03-assessment-pathways.svg" alt="Separate housing and gear assessments with condition results, recommendations, housing recycling and no executed gear reuse" width="100%"/>

Each component is evaluated by a separate `end of use disposition assessment (MATSUS_0000062)` using `evaluates (MATSUS_0000060)`. Each assessment has two specified information outputs:

1. an assessment result describing the modelled condition; and
2. an end-of-use disposition recommendation.

The housing condition result is about both the housing and crack. Its recycling recommendation is about the housing and `recommends (MATSUS_0000064)` the housing recycling process. The recommendation does **not** entail authorization, selection or execution. The recycling process is represented as executed in the scenario because its participants, inputs, subprocesses and outputs are independently asserted.

The gear condition result and potential-reuse recommendation are both about the gear. No `recommends` edge connects the gear recommendation to a process, and no executed reuse-process individual is present.

These are stipulated demonstration judgements, not verified crack-inspection findings, certified fitness decisions or validated performance measurements. The ABox contains neither a formal process timeline nor independently authenticated operation logs.

## 4. Recycling provenance and traceability

<img src="diagrams/04-recycling-provenance.svg" alt="Housing recycling inputs, remelting, melt, casting and solidification, recovered ingot, operator and recycling record" width="100%"/>

The housing recycling process has two specified inputs: the original housing and an additional aluminium charge. It has remelting and casting/solidification as occurrent parts, the recovered ingot as specified output, and the recycling organization as participant.

The detailed material flow is asserted independently:

- remelting consumes the housing and additional aluminium charge and outputs an aluminium-alloy melt;
- casting/solidification consumes that melt and outputs the recovered ingot; and
- the recovered ingot is typed as aluminium alloy, ingot and `recycled material (MATSUS_0000002)`.

The additional charge is typed as aluminium alloy and `primary raw material (MATSUS_0000041)`. Its primary origin is a deliberate synthetic assumption, not a fact verified from supplier or extraction records. MatSus defines primary raw material as both primary material and LOG raw material, but the P1 ABox does not identify a separate named raw-material-role bearer. MatSus also asserts no equivalence, disjointness or hierarchy between primary material and `virgin material (MATSUS_0000030)`, so the charge is **not** asserted as virgin material.

This is a plausible simplified route that supplies **qualitative input/output provenance**. It does not establish a mass balance, recovery yield, recycled-content fraction, input-to-output allocation, contamination clearance or material-grade conformity.

The synthetic recycling document is `is about (IAO_0000136)` the housing, recycling process, recovered ingot and recycling operator. Aboutness and operator participation do not establish authorship, attestation, regulatory conformance, certified recovery or authenticated chain of custody.

## Core asserted relationship pattern

| Subject kind | Predicate | Object kind | Modelling use |
| --- | --- | --- | --- |
| assembly object | `has part (BFO_0000051)` | component object/material | pre-disassembly assembly structure |
| process | `has specified input (OBI_0000293)` | material entity | declared process input |
| process | `has specified output (OBI_0000299)` | material or information entity | declared process output |
| assessment | `evaluates (MATSUS_0000060)` | evaluated entity | assessment target without asserting participation |
| recommendation | `recommends (MATSUS_0000064)` | end-of-use management process | suitability recommendation, not execution |
| process | `has occurrent part (BFO_0000117)` | subprocess | process decomposition |
| process | `has participant (RO_0000057)` | continuant | involved operator |
| information entity | `is about (IAO_0000136)` | entity | information subject matter, not certification |

## Validation and evidence status

From this pattern directory, run the asserted-data regression with its default input:

```powershell
python validation/run_queries.py
```

Or provide the data explicitly:

```powershell
python validation/run_queries.py shape-data.ttl
```

The runner requires `expected_rows.json`, the query directory, exactly nine `.sparql` files and a one-to-one match between query filenames and expected-result keys. Missing or mismatched fixtures cause a non-zero failure rather than a silent successful run.

The suite contains seven competency questions and two structural checks. It evaluates **asserted RDF only**, not inferred-query coverage. The final ABox parses as Turtle and contains 94 asserted triples. Its exact RDF delta from the evaluator-accepted 93-triple baseline was one added `rdf:type` assertion and zero removals.

Fresh ROBOT/HermiT evidence for the final 94-triple ABox was independently inspected and accepted for the configured baseline and combined-ontology checks against MatSus with pinned PMDco v3.1.2. The recorded eight commands succeeded and the generated OWL outputs matched their manifests. This evidence does not establish P1-specific SHACL conformance, empirical validation or resolution of the crack-site/parthood clarification. The nine P1 queries are not currently executed by standard repository CI.

## Review boundaries

- No MatSus or PMDco class, property, axiom, import or pinned dependency is introduced or changed by this pattern.
- No P1-specific SHACL shape is included or claimed.
- Diagram sequence arrows and absence callouts are labelled as non-RDF context.
- Repository branch publication is not a merge or release.
- The crack-site/defect-role parthood interpretation remains unresolved and does not require changing the accepted P1 RDF in this documentation update.

This guide is an expanded presentation of the accepted scientific model. Its SHA-256 is intentionally different from the R3 evaluation document and must be reviewed as a new documentation artifact.
