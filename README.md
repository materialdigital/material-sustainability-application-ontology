# Material Sustainability Application Ontology (Mat.Sus)

MatSus is a material-centred application ontology of the
[Platform MaterialDigital Core Ontology (PMDco)](https://github.com/materialdigital/core-ontology).

It connects materials science and engineering concepts with sustainability-relevant
information across material life cycles. Current development covers, among other
areas, sustainability and life-cycle assessment, circularity and end-of-use
processes, material provenance and supply-chain traceability, and information
relevant to digital product passports.

## Status and versions

### Development status

MatSus is under active development. No stable release has been published yet.
The first formal release is planned for the end of 2026.

Persistent publication through `https://w3id.org/pmd/matsus/` and versioned
GitHub Pages documentation are planned before the first formal release.

### Editors' version

The authoritative editable source is
[src/ontology/matsus-edit.owl](src/ontology/matsus-edit.owl).

## Contact

Please use this GitHub repository's
[issue tracker](https://github.com/materialdigital/material-sustainability-application-ontology/issues)
to request terms or report modelling concerns.

## Acknowledgements

This ontology repository was created using the
[Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).

## Development

This ontology is developed using OWL and managed with the
[Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).

To contribute or edit:

- Open `src/ontology/matsus-edit.owl` in
  [Protégé](https://protege.stanford.edu/) or your preferred OWL editor.
- Create new MatSus entities within the namespace
  `https://w3id.org/pmd/matsus/`.
  Example IRI: `https://w3id.org/pmd/matsus/MATSUS_0000040`
  (the `MATSUS_` prefix portion is always uppercase).
- Use the ODK wrapper for repository automation:
  - `sh run.sh make test`: run quality control.
  - `sh run.sh make refresh-imports`: update configured imports.
  - `sh run.sh make all_assets copy_release_files`: build and synchronize release artifacts.
  - `sh run.sh update_repo`: synchronize the ODK-managed repository structure.

MatSus uses pinned external ontology dependencies. Updates to PMDco and other
external sources are reviewed deliberately before their pinned versions are
changed and imports are refreshed.

## Repository Structure

| Path | Description |
|------|-------------|
| `.github/workflows/` | GitHub Actions CI, documentation and release workflows |
| `src/ontology/` | Authoritative ontology source and ODK build files |
| `src/ontology/components/` | Curated MatSus ontology and integration components |
| `src/ontology/imports/` | Pinned external ontology imports |
| `src/sparql/` | Repository-specific quality checks |
| `w3id/.htaccess` | Proposed persistent-IRI redirect configuration for future publication |

## Contribution

We welcome contributions to the Material Sustainability Application Ontology (MatSus).

- **Issue tracker**:
  [github.com/materialdigital/material-sustainability-application-ontology/issues](https://github.com/materialdigital/material-sustainability-application-ontology/issues)
  Report errors, request new terms, or flag modelling concerns.

- **Discussion forum**:
  [github.com/materialdigital/material-sustainability-application-ontology/discussions](https://github.com/materialdigital/material-sustainability-application-ontology/discussions)
  Discuss modelling decisions with the community.

- **Application ontology template**:
  [materialdigital/application-ontology-template](https://github.com/materialdigital/application-ontology-template/)
  MaterialDigital template and infrastructure for PMD application ontologies.

- **PMD Ontology Playground meetings**: Every second Friday, 1–2 pm CET.
  [Register via the mailing list](https://www.lists.kit.edu/sympa/subscribe/ontology-playground?previous_action=info)

- **Contact**:
  [info@material-digital.de](mailto:info@material-digital.de)

## Authorship, maintenance and licensing

MatSus was created and edited by Khashayar Razghandi. Maintenance is coordinated
through the MatSus issue tracker within Platform MaterialDigital.

Original MatSus content is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Reused and adapted ontology content retains its applicable source, licence,
attribution, version and modification information.

The selected DPPO component is a MatSus adaptation of CC BY 4.0 DPPO 0.1 content.

The LOG-derived component is adapted from the Platform MaterialDigital
Application Ontology for Logistics and Supply Chain (LOG), based on upstream
`main` commit `0c89424ffc17096599d5bfdcfba783686494d49e`.
Ontology source content at that revision corresponds to LOG v1.0.2.
LOG is licensed under CC BY 4.0.

The virgin material definition is independently worded for MatSus; its editor
note records only that ISO terminology informed the concept.
