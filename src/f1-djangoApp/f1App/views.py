import json
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.template import loader
from f1App.nacionality import flagCountries
import re

from django.views.decorators.csrf import csrf_protect

from f1App.services.circuits import get_all_circuits, get_circuit_by_race_id
from f1App.services.constructors import get_all_constructors
from f1App.services.driver import get_all_drivers, get_driver_by_id, get_driver_qualifying, search_drivers
from f1App.services.races import delete_race_service, get_all_races_by_date, get_all_races_by_year, get_race_by_id, get_races_by_name, get_results_by_race_id, insert_race_service
from f1App.services.seasons import delete_season_service, get_all_seasons, get_constructor_podium, get_driver_podium, insert_season_service

# Create your views here.
def index(request):
    template = loader.get_template("base.html")
    context = {"latest_question_list": "woof"}
    return HttpResponse(template.render(context, request))

# |==========================|
# |          Races           |
# |==========================|
def races(request):
    template = loader.get_template("races.html")
    page = int(request.GET.get("page", 1))
    results = get_all_races_by_date(page)
    circuits = get_all_circuits()
    for c in circuits:
        c["id"] = c["circuitId"]
    if (results == []):
        return redirect('/races')
    sendResults = []
    for i,result in enumerate(results):
        s = {}
        s["raceName"] = result["raceName"]
        s["firstYear"] = result["raceDetails"][0]["year"]
        s["lastYear"] = result["raceDetails"][-1]["year"]
        s["link"] = re.sub(r"\s", "_", result["raceName"])
        s["index"] = (page-1) * 20 + (i+1)
        sendResults.append(s)
    page_obj = {}
    page_obj["page"] = page
    if(page > 1):
        page_obj["has_previous"] = True
        page_obj["previous_page_number"] = page-1
    page_obj["next_page_number"] = page+1


    context = {"races": sendResults,"page_obj": page_obj,"circuits":circuits}
    
    return HttpResponse(template.render(context, request))

def race_year(request,name):
    results = get_races_by_name(name)
    for r in results:
        r["id"] = r["raceId"].split("race/")[1]
    context = {
        "races": results,
        "raceName": name.replace("_"," "),
        "race_name":name,
    }
    return render(request,"race_year.html",context=context)

def race_profile(request,id):
    race = get_race_by_id(id)
    circuit = get_circuit_by_race_id(id)
    results = get_results_by_race_id(id)
    for r in results:
        r["id"] = int(r["driverId"].split("/driver/")[1])

    context = {
        "race":race,
        "circuit":circuit,
        "results":results,
    }
    template = loader.get_template("raceProfile.html")
    return HttpResponse(template.render(context))

@csrf_protect
def race_delete(request):
    if request.method == "POST":
        id = request.POST.get("raceId")
        delete_race_service(id)
    return redirect("races")

@csrf_protect
def add_race(request):
    if request.method == "POST":
        circuitId = request.POST.get("circuit_id")
        date = request.POST.get("date")
        name = request.POST.get("name")
        round = request.POST.get("round")
        year = request.POST.get("year")
        print(f"Received Race Data: name={name}, date={date}, year={year}, round={round}, circuit_id={circuitId}")
        insert_race_service(circuitId, date, name, round, year)
    return redirect('races')


# |==========================|
# |          Drivers         |
# |==========================|

def drivers(request):
    page = int(request.GET.get("page", 1))
    query = request.GET.get("query", "")
    if query != "":
        results = search_drivers(query, page)
    else:
        results = get_all_drivers(page)
    if (results == []):
        return redirect('/drivers')
    page_obj = {}
    page_obj["page"] = page
    for i,r in enumerate(results):
        r["id"] = (r["driverId"].split("/driver/")[1])
        r["flag"] = flagCountries[r["nationality"]]
        r["index"] = (page-1) * 20 + (i+1)
    if(page > 1):
        page_obj["has_previous"] = True
        page_obj["previous_page_number"] = page-1
    page_obj["next_page_number"] = page+1
    context = {
        "drivers":results,
        "page_obj": page_obj
    }
    template = loader.get_template("drivers.html")
    return HttpResponse(template.render(context=context))

def driver_profile(request,id):
    results = get_driver_by_id(id)
    wins = get_driver_qualifying(id)
    flag = flagCountries[results["nationality"]]
    for r in wins:
        r["id"] = r["raceId"].split("race/")[1]

    context = {
        "driver":results,
        "wins":wins,
        "flag":flag
    }
    template = loader.get_template("driverProfile.html")
    return HttpResponse(template.render(context=context))
    
# |==========================|
# |       Constructors       |
# |==========================|

def constructors(request):
    page = int(request.GET.get('page', 1))
    results = get_all_constructors(page)
    for i,r in enumerate(results):
        r["flag"] = flagCountries[r["nationality"]]
        r["index"] = (page-1) * 20 + (i+1)
    page_obj = {}
    page_obj["page"] = page
    if (results == []):
        return redirect('/constructors')
    if(page > 1):
        page_obj["has_previous"] = True
        page_obj["previous_page_number"] = page-1
    page_obj["next_page_number"] = page+1
    context ={
        "constructors":results,
        "page_obj": page_obj
    }
    template = loader.get_template("constructors.html")
    return HttpResponse(template.render(context))

# |==========================|
# |       Seasons            |
# |==========================|

def seasons(request):
    page = int(request.GET.get('page', 1))
    results = get_all_seasons(page)
    if (results == []):
        return redirect('/seasons')
    page_obj = {}
    page_obj["page"] = page
    if(page > 1):
        page_obj["has_previous"] = True
        page_obj["previous_page_number"] = page-1
    page_obj["next_page_number"] = page+1
    for i,r in enumerate(results):
        r["index"] = (page-1) * 20 + (i+1)
    context ={
        "seasons":results,
        "page_obj": page_obj
    }
    return render(request,template_name="seasons.html",context=context)

def season_profile(request, year):

    races_by_season = get_all_races_by_year(year,1)
    driver_podium = get_driver_podium(year)
    const_podium = get_constructor_podium(year)
    print(races_by_season)
    print("================")
    print(driver_podium)
    for d in driver_podium:
        d["id"] = (d["driverId"].split("/driver/")[1])
    print("================")
    print(const_podium)
    context = {
        "year": year,
        "drivers":driver_podium,
        "teams":const_podium,
        "races":races_by_season,
    }
    template = loader.get_template("seasonProfile.html")
    return HttpResponse(template.render(context))

@csrf_protect
def add_season(request):
    if request.method == "POST":
        year = request.POST.get("year")
        url = request.POST.get("url")

        if year and url:
            insert_season_service(year, url)
            return redirect('seasons')
    return render(request, "add_season.html")

@csrf_protect
def delete_season(request,year):
    if request.method == "POST":
        delete_season_service(year)
    return redirect('seasons')