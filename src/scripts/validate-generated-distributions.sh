#!/usr/bin/env bash
set -euo pipefail

readonly validation_dir=generated-validation
mkdir -p ${validation_dir}

readonly required_files=(
  matsus.owl
  matsus.ttl
  matsus.json
  src/ontology/matsus.ttl
  src/ontology/matsus-full.owl
  src/ontology/imports/pmdco_import.owl
)
for required_file in ${required_files[@]}; do
  if [[ ! -f ${required_file} ]]; then
    echo 'Missing required generated-distribution input:' ${required_file} >&2
    exit 1
  fi
done

{
  echo source_commit=${GITHUB_SHA:-unknown}
  echo workflow_run=${GITHUB_RUN_ID:-local}
  echo workflow_attempt=${GITHUB_RUN_ATTEMPT:-local}
  echo checked_out_commit=$(git rev-parse HEAD)
  robot --version
  java -version
  python3 --version
} > ${validation_dir}/tool-versions.txt 2>&1

sha256sum ${required_files[@]} > ${validation_dir}/SHA256SUMS

if ! cmp -s matsus.ttl src/ontology/matsus.ttl; then
  echo 'Root matsus.ttl differs from tracked src/ontology/matsus.ttl.' >&2
  exit 1
fi

robot validate-profile --profile DL --input matsus.owl --output ${validation_dir}/matsus-owl2dl.txt
robot reason --reasoner HermiT --input matsus.owl --equivalent-classes-allowed all --exclude-tautologies false --output ${validation_dir}/matsus-root-hermit.owl 2>&1 | tee ${validation_dir}/matsus-hermit.log
# These are declared-entity completeness checks, not axiom-equivalence checks.
robot query --input src/ontology/matsus-full.owl --format tsv --query src/sparql/distribution-signature.sparql generated-validation/matsus-full-signature.tsv
robot query --input matsus.owl --format tsv --query src/sparql/distribution-signature.sparql generated-validation/matsus-owl-signature.tsv
robot query --input matsus.ttl --format tsv --query src/sparql/distribution-signature.sparql generated-validation/matsus-ttl-signature.tsv

diff -u generated-validation/matsus-full-signature.tsv generated-validation/matsus-owl-signature.tsv
diff -u generated-validation/matsus-owl-signature.tsv generated-validation/matsus-ttl-signature.tsv

tail -n +2 generated-validation/matsus-owl-signature.tsv | cut -f1 | LC_ALL=C sort -u > generated-validation/matsus-owl-entity-ids.tsv
#tail -n +2 generated-validation/matsus-owl-signature.tsv | cut -f1 | sort -u > generated-validation/matsus-owl-entity-ids.tsv
# OBO Graphs JSON is not an RDF/OWL input format for ROBOT and can collapse
# OWL punning. Compare its named entity IRI set; OWL/TTL retain the typed check.
python3 - matsus.json generated-validation/matsus-json-entity-ids.tsv <<'PY'
import json
import sys

source, output = sys.argv[1:]
with open(source, encoding='utf-8') as stream:
    document = json.load(stream)

graphs = document.get('graphs')
if not isinstance(graphs, list) or not graphs:
    raise SystemExit('OBO Graphs JSON must contain a non-empty graphs array')

entity_ids = set()
property_types = {'ANNOTATION', 'DATA', 'OBJECT'}
for graph in graphs:
    nodes = graph.get('nodes')
    if not isinstance(nodes, list):
        raise SystemExit('Every OBO Graph must contain a nodes array')
    for node in nodes:
        entity_id = node.get('id')
        node_type = node.get('type')
        if not isinstance(entity_id, str) or not entity_id:
            raise SystemExit('Every OBO Graph node must have a non-empty string id')
        if node_type in {'CLASS', 'INDIVIDUAL'}:
            entity_ids.add(entity_id)
        elif node_type == 'PROPERTY':
            if node.get('propertyType') not in property_types:
                raise SystemExit('PROPERTY node has an unsupported propertyType: ' + entity_id)
            entity_ids.add(entity_id)
        elif node_type is not None:
            raise SystemExit('Unsupported OBO Graph node type: ' + str(node_type))

with open(output, 'w', encoding='utf-8', newline='\n') as stream:
    for entity_id in sorted(entity_ids):
        stream.write(f'<{entity_id}>\n')
print(f'validated {len(graphs)} graph(s) and {len(entity_ids)} named entity IRI(s)')
PY
#diff -u generated-validation/matsus-owl-entity-ids.tsv generated-validation/matsus-json-entity-ids.tsv
diff -u <(LC_ALL=C sort -u generated-validation/matsus-owl-entity-ids.tsv) <(LC_ALL=C sort -u generated-validation/matsus-json-entity-ids.tsv)

robot query --input src/ontology/imports/pmdco_import.owl --format tsv --query src/sparql/pmd-signature.sparql generated-validation/pmdco-import-signature.tsv
robot query --input matsus.owl --format tsv --query src/sparql/pmd-signature.sparql generated-validation/matsus-pmd-signature.tsv
# MatSus components may add PMD-namespace declarations. Require the PMDco
# import to be a subset of the root signature and record additions separately.
awk 'NR == FNR { present[$0] = 1; next } !($0 in present)' generated-validation/matsus-pmd-signature.tsv generated-validation/pmdco-import-signature.tsv > generated-validation/missing-pmd-signature.tsv
awk 'NR == FNR { present[$0] = 1; next } !($0 in present)' generated-validation/pmdco-import-signature.tsv generated-validation/matsus-pmd-signature.tsv > generated-validation/additional-pmd-signature.tsv
if [[ -s generated-validation/missing-pmd-signature.tsv ]]; then
  echo 'Generated root is missing PMDco import declarations:' >&2
  cat generated-validation/missing-pmd-signature.tsv >&2
  exit 1
fi
