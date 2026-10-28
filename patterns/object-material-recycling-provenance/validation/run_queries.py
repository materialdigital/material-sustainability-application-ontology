"""Run reproducible asserted-RDF (NOT OWL reasoning) P1 SPARQL checks.

Usage:
    python validation/run_queries.py
    python validation/run_queries.py path/to/shape-data.ttl

Requires: pip install rdflib (tested with rdflib 7.x)
"""
import json
import sys
from pathlib import Path
from rdflib import Dataset, Graph, URIRef

script_dir = Path(__file__).parent
input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else script_dir.parent / "shape-data.ttl"
expected_file = script_dir / "expected_rows.json"
queries_dir = script_dir / "queries"

if not expected_file.is_file():
    raise FileNotFoundError(f"Missing expected results: {expected_file}")
if not queries_dir.is_dir():
    raise FileNotFoundError(f"Missing query directory: {queries_dir}")

query_files = sorted(queries_dir.glob("*.sparql"))
if len(query_files) != 10:
    raise FileNotFoundError(
        f"Expected 10 SPARQL query files in {queries_dir}, found {len(query_files)}"
    )

expected = json.loads(expected_file.read_text(encoding="utf-8"))
expected_names = set(expected)
query_names = {qfile.name for qfile in query_files}
if expected_names != query_names:
    missing_expected = sorted(query_names - expected_names)
    missing_queries = sorted(expected_names - query_names)
    raise ValueError(
        "Query/expected fixture mismatch: "
        f"missing expected entries={missing_expected}; missing query files={missing_queries}"
    )

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

actual = {}
status_ok = True
for qfile in query_files:
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
