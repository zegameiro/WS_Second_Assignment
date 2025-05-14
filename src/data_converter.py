import pandas as pd
import os
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.namespace import XSD

def csv_to_rdf(csv_file, main_graph, PRED, TYPE, namespaces):
    file_name = os.path.splitext(os.path.basename(csv_file))[0]
    name_space = file_name

    # Handle special cases that should not remove 's'
    if not (name_space == "status" or name_space == "qualifying"):
        name_space = name_space[:-1]  # Remove plural

    BASE_URI = f"http://pitstop.org/{name_space}/"
    NS = Namespace(BASE_URI)

    df = pd.read_csv(csv_file)

    # Store the namespace with its prefix
    ns_prefix = name_space
    main_graph.bind(ns_prefix, NS)
    namespaces[name_space] = NS  # Store for lookup

    entity_type = URIRef(TYPE[name_space.capitalize()])

    for _, row in df.iterrows():
        entity_uri = URIRef(NS[f"{row.iloc[0]}"])  # Use first column as subject

        main_graph.add((entity_uri, RDF.type, entity_type))

        for col in df.columns[1:]:
            value = row[col]

            if pd.notna(value):
                if "Id" in col:
                    entity = col[:-2]  # Remove "Id" to get the related entity type
                    if entity in namespaces:
                        related_ns = namespaces[entity]
                        main_graph.add((entity_uri, PRED[col], URIRef(related_ns[f"{value}"])))
                    else:
                        print(f"Warning: No namespace found for {entity}, using full URI.")
                        main_graph.add((entity_uri, PRED[col], URIRef(f"http://pitstop.org/{entity}/{value}")))

                elif isinstance(value, (int, float)):
                    datatype = XSD.float if isinstance(value, float) else XSD.int
                    main_graph.add((entity_uri, PRED[col], Literal(value, datatype=datatype)))

                elif str(value).startswith("http"):
                    main_graph.add((entity_uri, PRED[col], URIRef(value)))

                elif value != '\\N':
                    main_graph.add((entity_uri, PRED[col], Literal(value, datatype=XSD.string)))

    print(f"Processed: {file_name}")

# Create main graph & namespaces dictionary
main_graph = Graph()
PRED = Namespace("http://pitstop.org/pred/")
TYPE = Namespace("http://pitstop.org/type/")
main_graph.bind("pred", PRED)
main_graph.bind("type", TYPE)

namespaces = {}

csv_files = [os.path.join("../data", file) for file in os.listdir("../data") if file.endswith(".csv")]

# First pass: Register namespaces
for file in csv_files:
    file_name = os.path.splitext(os.path.basename(file))[0]
    name_space = file_name[:-1] if file_name not in ["status", "qualifying"] else file_name
    namespaces[name_space] = Namespace(f"http://pitstop.org/{name_space}/")

# Second pass: Convert CSV to RDF with correct references
for file in csv_files:
    csv_to_rdf(file, main_graph=main_graph, PRED=PRED, TYPE=TYPE, namespaces=namespaces)

# Save the combined RDF file
os.makedirs("output", exist_ok=True)
output_file = "output/data.n3"
main_graph.serialize(destination=output_file, format="n3")

print(f"All RDF data combined into {output_file}")
