"""Run reproducible asserted-RDF (NOT OWL reasoning) P1 SPARQL checks.
Usage: python run_queries.py [path-to-gearbox-example.ttl]
Requires: pip install rdflib (tested with rdflib 7.x)
"""
import json
import sys
from pathlib import Path
from rdflib import Dataset, Graph, URIRef

root = Path(__file__).resolve().parent
input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "gearbox-example.ttl"
expected_file = root / "expected_rows.json"

if input_file.suffix.lower() == ".trig":
    dataset = Dataset()
    dataset.parse(input_file, format="trig")
    graph = dataset.graph(URIRef("urn:vg:data"))
elif input_file.suffix.lower() == ".ttl":
    graph = Graph()
    graph.parse(input_file, format="turtle")
else:
    raise ValueError("Expected .trig or .ttl input")

def encode(results):
    cols = [str(v) for v in results.vars]
    rows = []
    for row in results:
        rows.append({col: str(row[i]) if row[i] is not None else None for i, col in enumerate(cols)})
    return sorted(rows, key=lambda v: json.dumps(v, sort_keys=True))

if not expected_file.is_file():
    raise FileNotFoundError(f"Missing expected results: {expected_file}")
expected = json.loads(expected_file.read_text(encoding="utf-8"))
actual = {}
status_ok = True
for qfile in sorted((root / "queries").glob("*.sparql")):
    result = graph.query(qfile.read_text(encoding="utf-8"))
    actual[qfile.name] = encode(result)
    passed = expected.get(qfile.name) == actual[qfile.name]
    status_ok = status_ok and passed
    print(f"{'PASS' if passed else 'FAIL'} {qfile.name}: {len(actual[qfile.name])} row(s)")
    if not passed:
        print("  Expected:", json.dumps(expected.get(qfile.name), ensure_ascii=False))
        print("  Actual:  ", json.dumps(actual[qfile.name], ensure_ascii=False))
print(f"Asserted RDF triples: {len(graph)}")
if len(sys.argv) > 2 and sys.argv[2] == "--record-expected":
    expected_file.write_text(json.dumps(actual, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Recorded expected rows from the input supplied")
else:
    raise SystemExit(0 if status_ok else 1)
