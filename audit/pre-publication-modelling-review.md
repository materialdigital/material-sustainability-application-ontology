# Mandatory pre-publication review: disassembling, dismantling, and deconstruction

Status: **required before the next Mat.Sus publication**.

This review does not block the approved Phase-12 integration. It records provisional application-level axioms that must be reassessed before publication.

## Terms in scope

- PMDco `PMD_0000612` - "disassembling"
- CEON `DisassemblingProcess`
- CEON `DismantleProcess`
- CEON `DeconstructionProcess`
- Mat.Sus `MATSUS_0000000` - "product end-of-life management process"

## Provisional application-level axioms to review

- `PMD_0000612 rdfs:subClassOf MATSUS_0000000`
- `CEON DisassemblingProcess rdfs:subClassOf MATSUS_0000000`
- `CEON DismantleProcess rdfs:subClassOf MATSUS_0000000`
- `CEON DeconstructionProcess rdfs:subClassOf MATSUS_0000000`

No equivalence axiom is asserted among these classes.

## Required review questions

1. Are disassembling, dismantling, and deconstruction semantically distinct processes in the intended Mat.Sus publication scope?
2. Do their source definitions support distinct necessary and sufficient conditions, or should any terms be consolidated?
3. Should the CEON classes align to PMDco `PMD_0000612`, form subclasses of it, or remain sibling classes?
4. Are all four provisional application-level subclass axioms under the product end-of-life management branch defensible for every instance?
5. Is hierarchy refinement needed to separate product, building, and general material-entity contexts?

## Evidence to use

- PMDco 3.1.0 definition and hierarchy for `PMD_0000612`
- CEON v1.0.0 process module at commit `9cdcae1b68f4e9d5a55697c8e3e3f8df788fc937`
- Competency questions and publication examples for product end-of-life management
- Results of the later consolidated ROBOT, reasoner, and regression validation

Completion requires a documented modelling decision and any necessary ontology changes before publication.
