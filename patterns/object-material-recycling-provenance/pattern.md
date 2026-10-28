# Pattern: Component End-of-Use Assessment and Recycling Provenance

## Purpose

This pattern uses a synthetic gearbox example to connect **end-of-use assessment**, **component recycling**, and **qualitative material provenance**. It also illustrates how a component can be modelled as both an object and a material without introducing separate physical individuals.

## 1. Overall scenario

A used gearbox is disassembled into an aluminium-alloy housing and a steel gear. Separate assessments recommend recycling the housing and potential reuse of the gear. Only the housing recycling is represented as an executed process.

![Overall gearbox scenario](diagrams/01-overview.svg)

*Reading the figures: coloured boxes are individuals, with their asserted types shown in smaller text. Solid arrows are RDF assertions (subject → object); dashed annotations provide context, not additional assertions.*

## 2. Object–material duality and damage

The **same housing individual** is typed as both `object (BFO_0000030)` and `aluminium alloy (PMD_0020186)`; the gear likewise has object and steel types. This follows the [PMDco object–material duality pattern](https://github.com/materialdigital/core-ontology/tree/main/patterns/duality%20object%20material). The housing also has a chemical-composition quality and is the location of a crack site bearing a defect role.

![Object–material duality and damage](diagrams/02-object-material-duality.svg)

## 3. End-of-use assessments and recommendations

Each component is evaluated in a separate **end-of-use disposition assessment**, which outputs a condition result and a recommendation. The housing recommendation identifies a recycling process that is also independently modelled as executed. The gear's potential-reuse recommendation does **not** identify an executed reuse process.

![Component assessments and recommendations](diagrams/03-assessment-pathways.svg)

## 4. Recycling provenance

The housing and additional **primary aluminium raw material** are inputs to recycling. The model records remelting, an intermediate melt, casting/solidification and a recovered aluminium-alloy ingot. A recycling document is explicitly *about* the housing, recycling process, ingot and operator.

![Recycling process, inputs, outputs, subprocesses and record](diagrams/04-recycling-provenance.svg)

The input–output links establish **qualitative provenance**, not a mass balance, recycled-content percentage, verified alloy grade or certified chain of custody. The additional charge is typed as **primary raw material**; a **virgin material** classification is not asserted.

## Appendix — example, reuse and validation

- **Example ABox:** [`shape-data.ttl`](shape-data.ttl) — 94 asserted triples in a synthetic scenario. For this example, gearbox `has part` links describe the assembly **before disassembly**; the RDF does not encode when those links cease to hold.
- **Executable checks:** [seven competency questions and two structural checks](validation/queries/); [runner](validation/run_queries.py) and [expected answers](validation/expected_rows.json). From this directory run `python validation/run_queries.py`.
- **Evidence:** The example was accepted in evaluation rounds R1–R3; nine asserted-RDF checks passed. ROBOT/HermiT compatibility was assessed with the pinned PMDco v3.1.2 import closure. These checks do not establish empirical validity or P1-specific SHACL conformance; the nine queries are not part of standard repository CI.
- **Semantic boundary:** PMDco's crack-site/defect-role parthood interpretation remains unresolved. No crack–housing parthood edge is asserted. Recommendations do not themselves imply execution.

### Key predicates for adaptation

| Predicate | Use in this pattern |
| --- | --- |
| `evaluates (MATSUS_0000060)` | Link an end-of-use assessment to the component being evaluated. |
| `has specified input / output (OBI_0000293 / OBI_0000299)` | Identify process inputs and outputs. |
| `recommends (MATSUS_0000064)` | Link a recommendation to a proposed management process, without asserting execution. |
| `has occurrent part (BFO_0000117)` | Identify the recycling subprocesses. |
| `is about (IAO_0000136)` | Connect result or record information to its subject matter. |
