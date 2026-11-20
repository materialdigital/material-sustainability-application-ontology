"""Run reproducible asserted-RDF (not OWL reasoning) Pattern 2 checks.

Usage: python validation/run_queries.py [path/to/shape-data.ttl]
Requires RDFLib 7.x. The local term audit checks selected reused IRIs against
the pinned repository sources; it is not a semantic or scientific validator.
"""
import json
import sys
from pathlib import Path
from rdflib import Graph, URIRef

here = Path(__file__).resolve().parent
path_args = [arg for arg in sys.argv[1:] if arg != "--print-actual"]
if len(path_args) > 1:
    raise ValueError("Provide at most one Turtle input path")
data_file = Path(path_args[0]) if path_args else here.parent / "shape-data.ttl"
expected_file = here / "expected_rows.json"
query_dir = here / "queries"
query_files = sorted(query_dir.glob("*.sparql"))
if len(query_files) != 12:
    raise FileNotFoundError(f"Expected 12 query files, found {len(query_files)}")
expected = json.loads(expected_file.read_text(encoding="utf-8"))
if set(expected) != {p.name for p in query_files}:
    raise ValueError("Query names and expected-result fixture differ")

graph = Graph().parse(data_file, format="turtle")
def encode(result):
    cols = [str(v) for v in result.vars]
    rows = [{c: str(row[i]) if row[i] is not None else None for i, c in enumerate(cols)} for row in result]
    return sorted(rows, key=lambda v: json.dumps(v, sort_keys=True))

ok = True
actual = {}
for query_file in query_files:
    rows = encode(graph.query(query_file.read_text(encoding="utf-8")))
    actual[query_file.name] = rows
    passed = rows == expected[query_file.name]
    ok &= passed
    print(f"{'PASS' if passed else 'FAIL'} {query_file.name}: {len(rows)} row(s)")
    if not passed:
        print("  Expected:", json.dumps(expected[query_file.name], ensure_ascii=False))
        print("  Actual:  ", json.dumps(rows, ensure_ascii=False))

def graph_without(pattern):
    """Return a graph with every triple matching (s, p, o), where None is a wildcard, removed."""
    mutated = Graph()
    removed = 0
    for triple in graph:
        if all(wanted is None or wanted == found for wanted, found in zip(pattern, triple)):
            removed += 1
        else:
            mutated.add(triple)
    return mutated, removed

p2 = "https://w3id.org/pmd/matsus/pattern/recycled-polymer-carbon-footprint-provenance/hdpe/"
iao_is_about = URIRef("http://purl.obolibrary.org/obo/IAO_0000136")
qudt_numeric = URIRef("http://qudt.org/schema/qudt/numericValue")
qudt_unit = URIRef("http://qudt.org/schema/qudt/hasUnit")
dcterms_source = URIRef("http://purl.org/dc/terms/source")
rdf_type = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
bfo_has_occurrent_part = URIRef("http://purl.obolibrary.org/obo/BFO_0000117")
mutation_cases = [
    ("final CF subject removal", "CHECK-01-cf-completeness.sparql",
     (URIRef(p2 + "finalBottleCFResult"), iao_is_about, URIRef(p2 + "finalBottleBatch")),
     [{"result": p2 + "finalBottleCFResult"}]),
    ("final CF scalar-number removal", "CHECK-01-cf-completeness.sparql",
     (URIRef(p2 + "finalBottleCFValue"), qudt_numeric, None),
     [{"result": p2 + "finalBottleCFResult"}]),
    ("final CF scalar-unit removal", "CHECK-01-cf-completeness.sparql",
     (URIRef(p2 + "finalBottleCFValue"), qudt_unit, None),
     [{"result": p2 + "finalBottleCFResult"}]),
    ("washing-electricity source removal", "CHECK-03-subprocess-inventory.sparql",
     (URIRef(p2 + "washingElectricityDatum"), dcterms_source, None),
     [{"step": p2 + "washing"}]),
    ("supplier declaration-result link removal", "CHECK-04-supplier-result-traceability.sparql",
     (URIRef(p2 + "virginSupplierDeclaration"), iao_is_about, URIRef(p2 + "virginSupplierCFResult")),
     [{"declaration": p2 + "virginSupplierDeclaration", "result": p2 + "virginSupplierCFResult"}]),
    ("shredding exact-type removal", "CHECK-05-process-vocabulary.sparql",
     (URIRef(p2 + "shredding"), rdf_type, URIRef("https://w3id.org/pmd/matsus/MATSUS_0000093")),
     [{"process": p2 + "shredding", "requiredType": "https://w3id.org/pmd/matsus/MATSUS_0000093",
       "container": p2 + "mechanicalRecycling"}]),
    ("melt-filtration constituent removal", "CHECK-05-process-vocabulary.sparql",
     (URIRef(p2 + "extrusionMeltFiltration"), bfo_has_occurrent_part, URIRef(p2 + "meltFiltration")),
     [{"process": p2 + "meltFiltration", "requiredType": "https://w3id.org/pmd/matsus/MATSUS_0000094",
       "container": p2 + "extrusionMeltFiltration"}]),
]
for label, query_name, removal, expected_violation in mutation_cases:
    mutated, removed = graph_without(removal)
    query_text = (query_dir / query_name).read_text(encoding="utf-8")
    rows = encode(mutated.query(query_text))
    detected = removed == 1 and rows == expected_violation
    ok &= detected
    print(f"{'PASS' if detected else 'FAIL'} mutation: {label} detected ({removed} triple removed)")
    if not detected:
        print("  Expected violation:", json.dumps(expected_violation, ensure_ascii=False))
        print("  Actual violation:  ", json.dumps(rows, ensure_ascii=False))

repo = here.parents[2]
sources = "\n".join((repo / p).read_text(encoding="utf-8") for p in [
    "src/ontology/matsus-edit.owl", "src/ontology/imports/pmdco_import.owl",
    "src/ontology/imports/obi_recycling_import.owl",
    "src/ontology/components/matsus-ceon.ttl", "src/ontology/components/matsus-log-stageA.ttl"])
required = [
    "MATSUS_0000000", "MATSUS_0000002", "MATSUS_0000016", "MATSUS_0000030",
    "MATSUS_0000065", "MATSUS_0000066", "MATSUS_0000068", "MATSUS_0000069",
    "MATSUS_0000070", "MATSUS_0000071", "MATSUS_0000072", "MATSUS_0000076",
    "MATSUS_0000077", "MATSUS_0000081", "MATSUS_0000093", "MATSUS_0000094",
    "MATSUS_0000095", "MATSUS_0000096", "OBI_0302885", "OBI_0302888",
    "OBI_0600014", "PMD_0000614", "PMD_0000778", "PMD_0000583", "PMD_0000833",
    "PMD_0020102", "PMD_0050007",
    "PMD_0050009", "PMD_0080205", "PMD_0200004", "PMD_0200007",
    "RecycleProcess", "LOG_1000020"]
missing = [term for term in required if term not in sources]
print(f"{'PASS' if not missing else 'FAIL'} pinned-term audit: {len(required)-len(missing)}/{len(required)} found")
if missing:
    print("  Missing:", missing)
    ok = False

matsus_source = (repo / "src/ontology/matsus-edit.owl").read_text(encoding="utf-8")
local_hierarchy = [
    "SubClassOf(:MATSUS_0000093 <https://w3id.org/pmd/co/PMD_0000614>)",
    "SubClassOf(:MATSUS_0000094 <http://purl.obolibrary.org/obo/OBI_0302885>)",
    "SubClassOf(:MATSUS_0000095 <http://purl.obolibrary.org/obo/OBI_0600014>)",
    "SubClassOf(:MATSUS_0000096 <https://w3id.org/pmd/co/PMD_0000833>)",
]
missing_hierarchy = [axiom for axiom in local_hierarchy if axiom not in matsus_source]
forbidden_equivalence = [
    term for term in ("MATSUS_0000093", "MATSUS_0000094", "MATSUS_0000095", "MATSUS_0000096")
    if f"EquivalentClasses(:{term}" in matsus_source
]
obi_graph = Graph().parse(repo / "src/ontology/imports/obi_recycling_import.owl")
rdfs_subclass = URIRef("http://www.w3.org/2000/01/rdf-schema#subClassOf")
external_hierarchy = [
    (URIRef("http://purl.obolibrary.org/obo/OBI_0302885"), rdfs_subclass,
     URIRef("http://purl.obolibrary.org/obo/OBI_0600014")),
    (URIRef("http://purl.obolibrary.org/obo/OBI_0302888"), rdfs_subclass,
     URIRef("http://purl.obolibrary.org/obo/COB_0000035")),
]
missing_external_hierarchy = [axiom for axiom in external_hierarchy if axiom not in obi_graph]
hierarchy_ok = not (missing_hierarchy or missing_external_hierarchy or forbidden_equivalence)
ok &= hierarchy_ok
print(f"{'PASS' if hierarchy_ok else 'FAIL'} process hierarchy and primitive-class audit")
if missing_hierarchy:
    print("  Missing local axioms:", missing_hierarchy)
if missing_external_hierarchy:
    print("  Missing imported axioms:", missing_external_hierarchy)
if forbidden_equivalence:
    print("  Forbidden local equivalences:", forbidden_equivalence)

rdfs_label = URIRef("http://www.w3.org/2000/01/rdf-schema#label")
regranulation_labels = [str(label) for label in graph.objects(None, rdfs_label)
                        if "regranulation" in str(label).lower()]
ok &= not regranulation_labels
print(f"{'PASS' if not regranulation_labels else 'FAIL'} no regranulation label synonym")
if regranulation_labels:
    print("  Labels:", regranulation_labels)
print(f"Asserted RDF triples: {len(graph)}")
if "--print-actual" in sys.argv:
    print(json.dumps(actual, indent=2, ensure_ascii=False))
raise SystemExit(0 if ok else 1)
