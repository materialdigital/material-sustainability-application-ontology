---
layout: ontology_detail
id: matsus
title: Material Sustainability Application Ontology (Mat.Sus)
jobs:
  - id: https://github.com/materialdigital/material-sustainability-application-ontology/actions/workflows/qc.yml
    type: github-actions
build:
  checkout: git clone https://github.com/materialdigital/material-sustainability-application-ontology.git
  system: git
  path: "."
contact:
  email: info@material-digital.de
  label: MatSus maintainers
  github: materialdigital
description: MatSus represents material-sustainability concepts as an application ontology of PMDco.
domain: material sustainability
homepage: https://github.com/materialdigital/material-sustainability-application-ontology
products:
  - id: matsus.owl
    name: "Material Sustainability Application Ontology (Mat.Sus) main release in OWL format"
  - id: matsus.ttl
    name: "Material Sustainability Application Ontology (Mat.Sus) main release in Turtle format"
  - id: matsus.json
    name: "Material Sustainability Application Ontology (Mat.Sus) main release in OBO Graph JSON format"
dependencies:
- id: pmdco
tracker: https://github.com/materialdigital/material-sustainability-application-ontology/issues
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
activity_status: active
---

MatSus is maintained as a Platform MaterialDigital application ontology.

