# Recycling vocabulary selected-term import

`obi_recycling_import.owl` is a generated selected-term module. Do not edit it
manually.

- Upstream ontology: OBI v2026-07-27
- Upstream version IRI: `http://purl.obolibrary.org/obo/obi/2026-07-27/obi.owl`
- Pinned download: `https://raw.githubusercontent.com/obi-ontology/obi/v2026-07-27/obi.owl`
- Upstream SHA-256: `8874ABCCA971EE26B4E4442198387916D788D14AF3519E1040474908ED12B946`
- Seed list: `obi_recycling_terms.txt`
- Extraction: ROBOT 1.9.2, STAR locality, forced seed inclusion, individuals excluded
- Generated module SHA-256: `39756E04FFDBA2DE1CEF9888D61FFCF092726AD43DDB1F41DCEB7A7034A0C4AA`

The seed terms are OBI filtration (`OBI_0302885`) and washing
(`OBI_0302888`). The locality module retains their required hierarchy and
logical dependencies, including material component separation
(`OBI_0600014`).

Recreate the module with Java 11 or newer and the repository's ROBOT jar:

```text
robot extract --input obi-v2026-07-27.owl \
  --term-file src/ontology/imports/obi_recycling_terms.txt \
  --method STAR --force true --individuals exclude \
  --copy-ontology-annotations false --output obi-recycling-selected.owl

robot annotate --input obi-recycling-selected.owl --remove-annotations \
  --ontology-iri https://w3id.org/pmd/matsus/imports/obi_recycling_import.owl \
  --version-iri https://w3id.org/pmd/matsus/imports/obi_recycling_import/2026-07-27 \
  --annotation http://www.w3.org/2002/07/owl#versionInfo "OBI v2026-07-27 selected-term module" \
  --link-annotation http://purl.org/dc/terms/source http://purl.obolibrary.org/obo/obi/2026-07-27/obi.owl \
  --link-annotation http://purl.org/dc/terms/license https://creativecommons.org/licenses/by/4.0/ \
  --annotation http://www.w3.org/2000/01/rdf-schema#comment \
  "ROBOT 1.9.2 STAR module for OBI filtration and washing; source SHA-256 8874ABCCA971EE26B4E4442198387916D788D14AF3519E1040474908ED12B946." \
  --output src/ontology/imports/obi_recycling_import.owl
```

FoodOn is not imported. The local drying-process definition records
`FOODON_03000614` from the FoodOn artifact with version IRI
`http://purl.obolibrary.org/obo/foodon/releases/2026-09-20/foodon.owl` as
conceptual inspiration only; no equivalence or mapping is asserted.
