# Material Sustainability Application Ontology (Mat.Sus)

Description: PMD Core application ontology generated via ODK Template.


More information can be found at http://obofoundry.org/ontology/matsus

## Versions

### Stable release versions

The latest version of the ontology can always be found at:

https://w3id.org/pmd/matsus.owl

(note this will not show up until the request has been approved by obofoundry.org)

### Editors' version

Editors of this ontology should use the edit version, [src/ontology/matsus-edit.owl](src/ontology/matsus-edit.owl)

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/materialdigital/KhashiYaar/material-sustainability-application-ontology/issues) to request new terms/classes or report errors or specific concerns related to the ontology.

## Acknowledgements

This ontology repository was created using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).
## Development

This ontology is developed using OWL and managed with the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).
To contribute or edit:

- Open  in [Protege](https://protege.stanford.edu/) or your preferred OWL editor.
- Create new entities within the namespace .
  Example IRI: 
  (the prefix portion is always uppercase).
- Use the  for automation:
  -  : Run quality control (reasoner checks, syntax validation).
  -  : Update imported ontologies via SLME extraction.
  -  : Build all release artifacts (TTL, OWL, JSON formats).
  -  : Sync repo structure after editing .

## Import Architecture

The modular import structure used by this ontology:



## Repository Structure

| Path | Description |
|------|-------------|
|  | GitHub Actions CI/CD workflows |
|  | Ontology source files (edit here) |
|  | Modular OWL component files |
|  | Extracted import modules (SLME) |
|  | ROBOT template TSV files for components |
|  | External ontology imports configuration |
|  | Creator names for ID range allocation |

## Contribution

We welcome contributions to the Material Sustainability Application Ontology (Mat.Sus) ontology!

- **Issue tracker**: [github.com/KhashiYaar/material-sustainability-application-ontology/issues](https://github.com/KhashiYaar/material-sustainability-application-ontology/issues)
  Report errors, request new terms, or flag modeling concerns.
- **Discussion forum**: [github.com/KhashiYaar/material-sustainability-application-ontology/discussions](https://github.com/KhashiYaar/material-sustainability-application-ontology/discussions)
  Discuss modeling decisions with the community.
- **Application ontology template**:
  [application-ontology-template](https://github.com/materialdigital/application-ontology-template/)
  The framework used here; mirrors pmdco with all its modules.
- **PMD Playground Meetings**: Every second Friday, 1-2 pm CET.
  [Register via mailing list](https://www.lists.kit.edu/sympa/subscribe/ontology-playground?previous_action=info)
- **Contact**: [info@material-digital.de](mailto:info@material-digital.de)
