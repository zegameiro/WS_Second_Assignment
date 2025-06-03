from f1App.constants import *
from f1App.repositories.driver import *

import json

def get_all_drivers(page):
    """Get all the drivers"""

    offset = (page - 1) * LIMIT

    res = retrieve_all_drivers(offset)

    data = json.loads(res)
    results = []

    for binding in data['results']['bindings']:
        driver = {}

        driver['driverId'] = binding['driverId']['value']
        driver['forename'] = binding['forename']['value']
        driver['surname'] = binding['surname']['value']
        driver['nationality'] = binding['nationality']['value']

        if 'number' in binding.keys():
            driver['number'] = binding['number']['value']
            
        if 'code' in binding.keys():
            driver['code'] = binding['code']['value']
        
        results.append(driver)

    return results

def get_driver_by_id(driver_id):
    """Get driver by id"""

    res = retrieve_driver_by_id(driver_id)
    data = json.loads(res)
    
    if len(data['results']['bindings']) < 1:
        raise Exception("Driver not found")

    binding = data['results']['bindings'][0]

    driver = {}
    driver['forename'] = binding['forename']['value']
    driver['surname'] = binding['surname']['value']
    driver['dob'] = binding['dob']['value']
    driver['nationality'] = binding['nationality']['value']
    driver['url'] = binding['url']['value']

    if 'number' in binding.keys():
        driver['number'] = binding['number']['value']
    if 'code' in binding.keys():
        driver['code'] = binding['code']['value']

    return driver



def search_drivers(regex, page):
    """Get all the drivers"""

    offset = (page - 1) * LIMIT

    res = retrieve_drivers_by_regex(regex, offset)
    data = json.loads(res)
    results = []

    for binding in data['results']['bindings']:
        driver = {}

        driver['driverId'] = binding['driverId']['value']
        driver['forename'] = binding['forename']['value']
        driver['surname'] = binding['surname']['value']
        driver['nationality'] = binding['nationality']['value']

        results.append(driver)

    return results

def get_driver_qualifying(driver_id):
    
    res = retrieve_driver_race_wins(driver_id)
    data = json.loads(res)
    results = []

    if len(data['results']['bindings']) > 0:

        for binding in data['results']['bindings']:
            qualifying = {}

            qualifying['raceId'] = binding['raceId']['value']
            qualifying['raceName'] = binding['raceName']['value']
            qualifying['points'] = binding['points']['value']
            qualifying['raceYear'] = binding['raceYear']['value']

            results.append(qualifying)

    return results
        