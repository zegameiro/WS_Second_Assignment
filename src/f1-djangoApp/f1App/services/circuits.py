from f1App.constants import *
from f1App.repositories.circuits import *
from SPARQLWrapper import SPARQLWrapper, JSON

import json

def get_circuit_by_race_id(race_id):

    res = retrieve_circuit_by_race_id(race_id)
    data = json.loads(res)

    if len(data['results']['bindings']) < 1:
        raise Exception("Circuit not found")
    
    binding = data['results']['bindings'][0]
    circuit = {}
    circuit['circuitId'] = binding['circuitId']['value']
    circuit['name'] = binding['name']['value']
    circuit['location'] = binding['location']['value']
    circuit['country'] = binding['country']['value']
    circuit['lat'] = binding['lat']['value']
    circuit['lng'] = binding['lng']['value']
    circuit['alt'] = binding['alt']['value']
    circuit['url'] = binding['url']['value']

    return circuit

def get_all_circuits(page=None):

    if page is None:
        res = retrieve_all_circuits()
    else:
        offset = (page - 1) * LIMIT
        res = retrieve_all_circuits(offset)

    data = json.loads(res)
    
    if (len(data['results']['bindings']) > 0):
        circuits = []
        for binding in data['results']['bindings']:
            circuit = {}
            circuit['circuitId'] = binding['circuitId']['value']
            circuit['name'] = binding['name']['value']
            circuit['location'] = binding['location']['value']
            circuit['country'] = binding['country']['value']
            circuits.append(circuit)

    return circuits

def wikipedia_url_to_dbpedia_resource(wiki_url):
    article = wiki_url.split("/wiki/")[-1]
    return f"http://dbpedia.org/resource/{article}"

def get_circuit_image(circuit_name):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    resource_uri = wikipedia_url_to_dbpedia_resource(circuit_name)

    print("DBpedia resource URI: ", resource_uri)

    query = f"""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>

        SELECT ?image ?abstract WHERE {{
            OPTIONAL {{ <{resource_uri}> dbo:thumbnail ?image . }}
            OPTIONAL {{ <{resource_uri}> dbo:image ?image . }}
            OPTIONAL {{ <{resource_uri}> foaf:depiction ?image . }}
            OPTIONAL {{ <{resource_uri}> dbo:abstract ?abstract .
                   FILTER (lang(?abstract) = "en") }}
        }} LIMIT 1
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    print("DBpedia query results: ", results)

    bindings = results["results"]["bindings"]
    if bindings:
        image = bindings[0].get("image", {}).get("value", None)
        abstract = bindings[0].get("abstract", {}).get("value", None)

        if image == None:
            image = "https://img.freepik.com/premium-vector/racing-circuit-icon_609277-5994.jpg"
        if abstract == None:
            abstract = "No description was found for this circuit"

        return abstract, image
    return "No description was found for this circuit", "https://img.freepik.com/premium-vector/racing-circuit-icon_609277-5994.jpg"


def get_circuit_by_id(circuit_id):
    res = retrieve_circuit_by_id(circuit_id)

    data = json.loads(res)

    if len(data['results']['bindings']) < 1:
        return None
    
    binding = data['results']['bindings'][0]
    circuit = {}
    circuit['circuitRef'] = binding['circuitRef']['value']
    circuit['name'] = binding['name']['value']
    circuit['location'] = binding['location']['value']
    circuit['country'] = binding['country']['value']
    circuit['lat'] = binding['lat']['value']
    circuit['lng'] = binding['lng']['value']
    circuit['alt'] = binding['alt']['value']
    circuit['url'] = binding['url']['value']

    if 'image' in binding and 'comment' in binding:
        circuit['image'] = binding['image']['value']
        circuit['comment'] = binding['abstract']['value']
    else:
        abstract, image_url = get_circuit_image(circuit['url'])
        print("DBpedia abstract found: ", abstract)
        print("Image URL: ", image_url or "No image found")
        if image_url:
            insert_circuit_abstract(circuit_id, abstract)
        if abstract:
            insert_circuit_abstract(circuit_id, abstract)
        circuit['image'] = image_url
        circuit['comment'] = abstract
        
        
    return circuit