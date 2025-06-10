from f1App.constants import *
from f1App.repositories.races import *

import json

def get_all_races_by_date(page):
    """Get all the races grouped by year"""

    offset = (page - 1) * LIMIT

    res = retrieve_races_by_date(offset)
    data = json.loads(res)

    results = []
    for binding in data['results']['bindings']:
        d = {}
        d['raceName'] = binding['raceName']['value']
        raceDetails = binding['raceDetails']['value'].split(",")

        d['raceDetails'] = []
        for raceDetail in raceDetails:
            raceId, year = raceDetail.split("__")
            d['raceDetails'].append({
                'raceId': raceId,
                'year': year
            })

        d['raceDetails'].sort(key=lambda x: x['year'], reverse=True)
        
        results.append(d)

    results.sort(key=lambda x: x['raceName'])

    return results

def get_all_races_by_year(year, page):

    offset = (page - 1) * LIMIT

    res = retrieve_races_by_year(year, offset)
    data = json.loads(res)

    results = []
    for binding in data['results']['bindings']:
        d = {}
        d['raceName'] = binding['raceName']['value']
        d['raceId'] = binding['raceId']['value']
        d['date'] = binding['raceDate']['value']
        d['winner'] = {
            "driverId": binding['winnerDriverId']['value'],
            "driverName": binding['winnerDriverName']['value'],
            "constructorId": binding['winnerConstructorId']['value'],
            "constructorName": binding['winnerConstructorName']['value'],
            "fastestLap": binding['winnerfastestLap']['value'],
        }
        d['fastestLap'] = {
            "time": binding['fastestLap']['value'],
            "driverId": binding['fastestDriverId']['value'],
            "driverName": binding['fastestDriverName']['value'],
            "constructorId": binding['fastestConstructorId']['value'],
            "constructorName": binding['fastestConstructorName']['value']
        }
        
        results.append(d)

    return results

def get_races_by_name(race_name):

    race_name = race_name.replace("_", " ")

    res = retrieve_races_by_name(race_name)
    data = json.loads(res)

    results = []
    if len(data) > 0:
        for binding in data['results']['bindings']:
            d = {}
            d['raceId'] = binding['raceId']['value']
            d['raceYear'] = binding['raceYear']['value']

            results.append(d)

    return results

def get_race_by_id(race_id):

    res = retrieve_race_by_id(race_id)

    print(res)

    data = json.loads(res)

    if len(data['results']['bindings']) < 1:
        raise Exception("Race not found")
    
    binding = data['results']['bindings'][0]
    race = {}
    if 'year' in binding.keys():
        race['year'] = binding['year']['value']
    
    if 'round' in binding.keys():
        race['round'] = binding['round']['value']

    if 'name' in binding.keys():
        race['name'] = binding['name']['value']

    if 'date' in binding.keys():
        race['date'] = binding['date']['value']

    if 'time' in binding.keys():    
        race['time'] = binding['time']['value']
    
    if 'raceUrl' in binding.keys():
        race['url'] = binding['raceUrl']['value']

    if 'circuitId' in binding.keys():
        race['circuitId'] = binding['circuitId']['value']

    if 'seasonId' in binding.keys():
        race['seasonId'] = binding['seasonId']['value']

    if 'winnerDriverName' in binding.keys() and 'winnerDriverId' in binding.keys():
        race['winner'] = {
            'driverId': binding['winnerDriverId']['value'],
            'driverName': binding['winnerDriverName']['value']
        }

    if (
        'fastestDriverFullName' in binding.keys() and 
        'fastestDriverId' in binding.keys() and 
        'fastestLapSpeed' in binding.keys() and
        'fastestLapTime' in binding.keys() and
        'fastestLap' in binding.keys() and
        'rank' in binding.keys() and
        'position' in binding.keys()
    ):
        race['fastestDriver'] = {
            'driverId': binding['fastestDriverId']['value'],
            'driverName': binding['fastestDriverFullName']['value'],
            'speed': binding['fastestLapSpeed']['value'],
            'time': binding['fastestLapTime']['value'],
            'lap': binding['fastestLap']['value'],
            'rank': binding['rank']['value'],
            'position': binding['position']['value']
        }

    return race

def delete_race_service(raceId):
    res = delete_race(raceId)
    return res

def insert_race_service(circuitId, date, name, round, year):
    res = insert_race(circuitId, date, name, round, year)
    return res

def get_results_by_race_id(race_id):

    res = retrieve_results_by_race_id(race_id)
    data = json.loads(res)

    # if len(data['results']['bindings']) < 1:
    #     raise Exception("Results not found")
    
    results = []
    for binding in data['results']['bindings']:
        d = {}
        d['driverId'] = binding['driverId']['value']
        d['driverName'] = binding['driverName']['value']
        d['constructorName'] = binding['constructorName']['value']
        d['position'] = binding['position']['value']

        if 'time' in binding.keys():
            d['time'] = binding['time']['value']

        if 'laps' in binding.keys():
            d['laps'] = binding['laps']['value']

        results.append(d)

    return results
