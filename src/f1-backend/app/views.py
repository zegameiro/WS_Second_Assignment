from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from app.services.races import *
from app.services.driver import *
from app.services.seasons import *
from app.services.constructors import *
from app.services.circuits import *

# Get all the races grouped by year
@api_view(['GET'])
def get_all_races_by_date_view(request):
    page = int(request.GET.get('page', 1))
    results = get_all_races_by_date(page)
    final_res = {
        'data': results
    }

    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_races_by_year_view(request, year):
    page = int(request.GET.get('page', 1))
    results = get_all_races_by_year(year,page)
    final_res = {
        'data': results
    }

    return Response(final_res, status=status.HTTP_200_OK)

# Get all the drivers
@api_view(['GET'])
def get_all_drivers_view(request):
    page = int(request.GET.get('page', 1))
    results = get_all_drivers(page)
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

# Get drivers by regex
@api_view(['GET'])
def search_drivers_view(request):
    page = int(request.GET.get('page', 1))
    regex = request.GET.get('query', "")
    results = search_drivers(regex, page)
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

# Get all the seasons
@api_view(['GET'])
def get_all_seasons_view(request):
    page = int(request.GET.get('page', 1))
    results = get_all_seasons(page)
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_constructors_view(request):
    page = int(request.GET.get('page', 1))
    results = get_all_constructors(page)
    final_res = {
        'data': results
    }

    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_constructors_by_nationality_view(request):

    results = get_constructors_by_nationality()
    final_res = {
        'data': results
    }

    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_constructors_by_id_view(request):
    
    if not request.body:
        return Response("Missing Body", status=status.HTTP_404_NOT_FOUND)
    data = json.loads(request.body.decode('utf-8'))
    if "id" not in data:
        return Response("Missing Constructor ID", status=status.HTTP_404_NOT_FOUND)
    
    constructor_id = data["id"]
    results = get_constructors_by_id(constructor_id)
    final_res = {
        'data': results
    }        

    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_driver_by_id_view(request, driverId):
    
    try:
        results = get_driver_by_id(driverId)
        wins = get_driver_qualifying(driverId)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    final_res = {
        'data': results,
        'wins': wins
    }        

    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_season_driver_podium_view(request, year):
    try:
        results = get_driver_podium(year)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
    final_res = {
        'data': results
    }

    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_season_constructor_podium_view(request, year):
    try:
        results = get_constructor_podium(year)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
    final_res = {
        'data': results
    }

    return Response(final_res, status=status.HTTP_200_OK)  

@api_view(['GET'])
def get_races_by_name_view(request, raceName):

    results = get_races_by_name(raceName)
    final_res = {
        'races': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_race_by_id_view(request, raceId):

    try:
        race = get_race_by_id(raceId)
        circuit = get_circuit_by_race_id(raceId)
        results = get_results_by_race_id(raceId)
    except Exception as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)
    
    final_res = {
        "race": race,
        "circuit": circuit,
        "results": results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_season_view(request):
    if not request.body:
        return Response("Missing Body", status=status.HTTP_404_NOT_FOUND)
    data = json.loads(request.body.decode('utf-8'))
    if "year" not in data:
        return Response("Missing Year", status=status.HTTP_404_NOT_FOUND)

    year = data["year"]

    results = delete_season_service(year)
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['POST'])
def insert_season_view(request):
    if not request.body:
        return Response("Missing Body", status=status.HTTP_404_NOT_FOUND)
    data = json.loads(request.body.decode('utf-8'))
    if "year" not in data:
        return Response("Missing Year", status=status.HTTP_404_NOT_FOUND)
    if "url" not in data:
        return Response("Missing URL", status=status.HTTP_404_NOT_FOUND)
    
    year = data["year"]
    url = data["url"]

    results = insert_season_service(year, url)
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_race_view(request):
    if not request.body:
        return Response("Missing Body", status=status.HTTP_404_NOT_FOUND)
    
    data = json.loads(request.body.decode('utf-8'))
    
    if "raceId" not in data:
        return Response("Missing raceId", status=status.HTTP_404_NOT_FOUND)
    
    raceId = data["raceId"]

    results = delete_race_service(raceId)
    
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['POST'])
def insert_race_view(request):
    if not request.body:
        return Response("Missing Body", status=status.HTTP_404_NOT_FOUND)
    
    data = json.loads(request.body.decode('utf-8'))
    
    required_fields = ["circuitId", "date", "name", "round", "year"]
    
    for field in required_fields:
        if field not in data:
            return Response(f"Missing {field}", status=status.HTTP_404_NOT_FOUND)
    
    circuitId = data["circuitId"]
    date = data["date"]
    name = data["name"]
    round = data["round"]
    year = data["year"]

    results = insert_race_service(circuitId, date, name, round, year)
    
    final_res = {
        'data': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_circuits_view(request):
    results = get_all_circuits()
    final_res = {
        'circuits': results
    }
    return Response(final_res, status=status.HTTP_200_OK)

