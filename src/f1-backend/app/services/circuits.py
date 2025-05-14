from f1_pitstop.graph_db import db
from app.constants import *
from app.repositories.circuits import *

import json

def get_circuit_by_race_id(race_id):

    res = retrieve_circuit_by_race_id(race_id)
    data = json.loads(res)

    if len(data['results']['bindings']) < 1:
        raise Exception("Circuit not found")
    
    binding = data['results']['bindings'][0]
    circuit = {}
    circuit['name'] = binding['name']['value']
    circuit['location'] = binding['location']['value']
    circuit['country'] = binding['country']['value']
    circuit['lat'] = binding['lat']['value']
    circuit['lng'] = binding['lng']['value']
    circuit['alt'] = binding['alt']['value']
    circuit['url'] = binding['url']['value']

    return circuit

def get_all_circuits():
    res = retrieve_all_circuits()
    data = json.loads(res)
    
    if (len(data['results']['bindings']) > 0):
        circuits = []
        for binding in data['results']['bindings']:
            circuit = {}
            circuit['circuitId'] = binding['circuitId']['value']
            circuit['name'] = binding['name']['value']
            circuits.append(circuit)

    return circuits