# MatSus Pattern 1 — Object–Material Recycling Provenance

**Gearbox demonstrator — R3-accepted scientific documentation**  
**Status:** R3 accepted by the independent evaluator on 2026-10-27; required editorial status correction applied. Repository integration is pending review, commit and merge.  
**RDF source:** [`gearbox-example.ttl`](gearbox-example.ttl) (94 asserted triples; SHA-256 `96bee3a4f0c6cd5382d05bc9b73ab3ffcebbd5934c09a81cac738fa3b8c02e77`).

## Scope and physical individuals

This example is a **synthetic material-centred gearbox end-of-use scenario**. The used gearbox initially includes an aluminium-alloy housing and a steel gear. The gearbox `has part` assertions represent the **pre-disassembly assembly**; they are not temporally qualified in OWL. Each of the housing and gear is **one physical individual** with both object and material-related types. The recovered aluminium-alloy ingot is a **distinct** material entity from the original housing.

## Housing defect and physical qualities

A structural crack in the housing is an instance of PMDco `PMD_0020202` (*crack*, a BFO site). It bears a `PMD_0020205` *defect role* via RO `has role`; the housing is the RO `location of` the crack. **Location does not assert mereological parthood.** PMDco's defect-role wording refers to a continuant part of an affected material entity; whether this use of an immaterial crack site meets that intended description remains a **separate PMDco semantic clarification**. No additional parthood axiom or named damage-evolution process is asserted by P1.

The housing also bears a `PMD_0000551` chemical-composition **quality**. This is **not** an experimental chemical analysis, composition value or measured information datum.

## End-of-use evaluations, decisions and timing

Two separate synthetic `MATSUS_0000062` end-of-use disposition assessments evaluate the housing and gear. The housing's modelled condition result says unsuitable for continued object use and produces a recycling recommendation. The gear's modelled condition result supports a *potential* reuse recommendation. These are **stipulated demonstration judgements**, not verified crack inspection findings, certified fitness decisions or validated performance measurements.

In the scenario narrative, a housing recycling pathway is **modelled as executed after the recommendation**. The recycling process has independently asserted participants, inputs, subprocesses and outputs; the recommendation **does not entail execution**. The gear-reuse pathway is **recommended only**, with no corresponding executed reuse process in this ABox. The graph includes neither a formal process timeline nor independently authenticated operation logs.

## Primary input, recycling and provenance

The remelting route consumes the recovered housing and an additional aluminium charge. The charge is explicitly typed as:

- PMDco `PMD_0020186` — aluminium alloy; and
- MatSus `MATSUS_0000041` — **primary raw material**.

The additional charge's **primary origin is a deliberate synthetic scenario assumption**, **not** verified by external supplier or extraction records. MatSus defines `MATSUS_0000041` as a subclass of `MATSUS_0000040` (*primary material*) and LOG `LOG_1000102` (*raw material*). This illustrates the connection between material provenance and production-input context. **No separate, explicitly identified raw-material-role bearer is asserted in the P1 ABox.** MatSus does not currently establish equivalence between primary and virgin material, so this instance is **not** also asserted to be `MATSUS_0000030` (*virgin material*).

The housing recycling process includes remelting, an intermediate aluminium-alloy melt, casting/solidification, and a newly produced recovered aluminium-alloy ingot typed as MatSus `MATSUS_0000002` (*recycled material*). This is a plausible **simplified** route and supplies **qualitative input/output provenance**. It does not establish a numerical recycled-content fraction, mass balance, recovery yield, input-to-output allocation or contamination clearance. Because the original housing is labelled with nominal alloy `EN AC-46000 / AlSi9Cu3(Fe)` and remelting has another aluminium charge, neither the ingot's post-process chemical composition nor grade conformity is established by these assertions alone.

## Documentation and traceability limit

The synthetic recycling document (`IAO_0000310`) is *about* the housing, the recycling process, the recovered ingot and the recycling operator. Aboutness and operator participation do **not** alone establish authorship, attestation, regulatory conformance or certification of material recovery.

## Evidence and publication status

The final 94-triple ABox parses as Turtle. Its **exact RDF delta** from the evaluator-accepted 93-triple baseline is **one added `rdf:type` assertion and zero removals**. The original seven asserted-data competency-query regressions and two auxiliary checks passed on the new snapshot; they verify **asserted RDF only**, not OWL-entailment results. Fresh ROBOT/HermiT reasoning evidence for the final 94-triple ABox was inspected and accepted for the configured baseline and combined-ontology checks. The recorded eight commands succeeded, and the generated OWL outputs match their manifests. These checks do not establish P1-specific SHACL conformance, empirical validation, or resolution of the PMDco crack-site/parthood clarification. Repository integration and publication are not claimed.

**Separate issue:** the PMDco crack/site–defect-role parthood interpretation remains unresolved but does not require changing the P1 RDF in this R3 batch.
