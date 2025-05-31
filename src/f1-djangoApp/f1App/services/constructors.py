from f1App.repositories.constructor import *
from f1App.constants import *

import json

def get_all_constructors(page):
    """Get all constructors"""

    offset = (page - 1) * LIMIT
    res = retrieve_all_constructors(offset)
    data = json.loads(res)

    results = []
    for binding in data['results']['bindings']:
        d = {}
        d['id'] = binding['c']['value']
        d['name'] = binding['name']['value']
        d['nationality'] = binding['nationality']['value']
        d['url'] = binding['url']['value']
        results.append(d)

    return results

def get_constructors_by_nationality():
    """Get all the constructors grouped by nationality"""

    res = retrieve_constructors_by_nationality()
    data = json.loads(res)

    results = []
    for binding in data['results']['bindings']:
        d = {}

        d['nationality'] = binding['nationality']['value']
        d["constructors"] = [constructor for constructor in binding['constructors']['value'].split(", ")]
        results.append(d)

    return results

def get_constructors_by_id(constructor_id):
    """Get a constructor from by it's id"""

    res = retrieve_constructors_by_id(constructor_id)
    data = json.loads(res)

    binding = data['results']['bindings'][0]
    result = {}
    result['name'] = binding['name']['value']
    result['nationality'] = binding['nationality']['value']
    result['url'] = binding['url']['value']

    return result