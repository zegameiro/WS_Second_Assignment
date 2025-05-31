from f1App.constants import *
from f1App.repositories.seasons import *


import json

def get_all_seasons(page):
    """Get all the seasons"""
    
    offset = (page - 1) * LIMIT

    res = retrieve_all_seasons(offset)
    data = json.loads(res)
    results = []

    for binding in data['results']['bindings']:
        season = {}
        season['seasonId'] = binding['year']['value']
        season['year'] = binding['year']['value'].split("/")[-1]
        season['url'] = binding['url']['value']
        results.append(season)

    return results

def get_driver_podium(year):

    res = get_drivers_podium(year)
    data = json.loads(res)
    results = []

    for binding in data['results']['bindings']:
        d = {}
        d["driverId"] = binding['driverId']['value']
        d["driverName"] = binding['driverName']['value']
        d["totalPoints"] = binding['totalPoints']['value']

        results.append(d)
    
    return results

def get_constructor_podium(year):

    res = get_constructors_podium(year)
    data = json.loads(res)
    results = []

    for binding in data['results']['bindings']:
        d = {}
        d["constructorId"] = binding['constructorId']['value']
        d["constructorName"] = binding['constructorName']['value']
        d["totalPoints"] = binding['totalPoints']['value']

        results.append(d)
    
    return results

def delete_season_service(year):
    res = delete_season(year)
    return res

def insert_season_service(year, url):
    res = insert_season(year, url)
    return res