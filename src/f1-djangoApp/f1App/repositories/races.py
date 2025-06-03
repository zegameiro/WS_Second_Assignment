from mysite.graph_db import db
from f1App.constants import *
import json

def retrieve_races_by_date(offset):
    """Retrieve all seasons from the database with pagination."""

    query = f"""
        PREFIX ns: <{NS}>
        PREFIX pred: <{PRED}>
        SELECT ?raceName (GROUP_CONCAT(CONCAT(STR(?raceId), "__", STR(?year)); SEPARATOR=",") AS ?raceDetails)
        WHERE {{
            ?raceId a ns:Race ;
                pred:name ?raceName ;
                pred:year ?year .
        }}
        GROUP BY ?raceName
        LIMIT {LIMIT}
        OFFSET {offset}
    """

    res = db.query(query)

    return res

def retrieve_races_by_year(year, offset):
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        SELECT ?raceId ?raceName ?raceDate ?fastestDriverId ?fastestDriverName ?fastestConstructorId ?fastestConstructorName ?fastestLap ?winnerDriverId ?winnerDriverName ?winnerConstructorId ?winnerConstructorName ?winnerfastestLap
        WHERE {{
            {{
                SELECT ?raceId ?raceName (MIN(?fastest) AS ?minFastestLap)
                WHERE {{
                    ?raceId a ps:Race ;
                        pred:name ?raceName ;
                        pred:year "{year}"^^xsd:int .
                    ?result a ps:Result ;
                        pred:participatedIn ?raceId ;
                        pred:fastestLapTime ?fastest .
                }}
                GROUP BY ?raceId ?raceName
            }}
            
            ?raceId a ps:Race ;
                pred:date ?raceDate .

            ?result a ps:Result ;
                    pred:participatedIn ?raceId ;
                    pred:fastestLapTime ?fastestLap ;
                    pred:hasDriver ?fastestDriverId ;
                    pred:hasConstructor ?fastestConstructorId ;
                    pred:position ?position .
                    
            FILTER(?fastestLap = ?minFastestLap)

            ?winnerResult a ps:Result ;
                    pred:participatedIn ?raceId ;
                    pred:fastestLapTime ?winnerfastestLap ;
                    pred:hasDriver ?winnerDriverId ;
                    pred:hasConstructor ?winnerConstructorId ;
                    pred:position "1"^^xsd:string .
                    
            ?winnerDriverId a ps:Driver ;
                    pred:forename ?winnerDriverForename ;
                    pred:surname ?winnerDriverSurname .

            BIND(CONCAT(?winnerDriverForename, " ",  ?winnerDriverSurname) as ?winnerDriverName) .

            ?winnerConstructorId a ps:Constructor ;
                    pred:name ?winnerConstructorName .

            ?fastestDriverId a ps:Driver ;
                    pred:forename ?fastestDriverForename ;
                    pred:surname ?fastestDriverSurname .

            BIND(CONCAT(?fastestDriverForename, " ",  ?fastestDriverSurname) as ?fastestDriverName) .

            ?fastestConstructorId a ps:Constructor ;
                pred:name ?fastestConstructorName .

        }}
        ORDER BY DESC(?raceDate)
    """


    res = db.query(query)

    return res

def retrieve_races_by_name(race_name):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        SELECT ?raceId ?raceYear
        WHERE {{
            ?raceId a ps:Race ;
                pred:name "{race_name}"^^xsd:string ;
                pred:year ?raceYear .
        }}
        ORDER BY DESC(?raceYear)
    """

    res = db.query(query)
    return res

def retrieve_race_by_id(race_id):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX ns: <{NS}race/>
        SELECT ?year ?round ?name ?date ?time ?raceUrl ?circuitId
        WHERE {{
            ns:{race_id} a ps:Race .
            
            OPTIONAL {{ ns:{race_id} pred:year ?year. }}
            OPTIONAL {{ ns:{race_id} pred:round ?round. }}
            OPTIONAL {{ ns:{race_id} pred:name ?name. }}
            OPTIONAL {{ ns:{race_id} pred:date ?date. }}
            OPTIONAL {{ ns:{race_id} pred:totalDuration ?time. }}
            OPTIONAL {{ ns:{race_id} pred:hasCircuit ?circuitId. }}
            OPTIONAL {{ ns:{race_id} pred:url ?raceUrl. }}
        }}
    """

    res = db.query(query)

    return res

def retrieve_results_by_race_id(race_id):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX ns: <{NS}race/>
        SELECT ?driverId ?driverName ?constructorId ?constructorName ?position ?time ?laps

        WHERE {{
            ?result a ps:Result ;
                pred:participatedIn ns:{race_id} ;
                pred:hasDriver ?driverId ;
                pred:hasConstructor ?constructorId ;
                pred:position ?position . 
            OPTIONAL {{ ?result pred:laps ?laps. }}
            OPTIONAL {{ ?result pred:duration ?time. }}

            ?driverId a ps:Driver ;
                pred:forename ?driverForename ;
                pred:surname ?driverSurname .
            BIND(CONCAT(?driverForename, " ", ?driverSurname) AS ?driverName)

            ?constructorId a ps:Constructor ;
                pred:name ?constructorName .
        }}
        LIMIT 3
    """

    res = db.query(query)
    return res

def retrieve_results_by_race_id(race_id):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX ns: <{NS}race/>
        SELECT ?driverId ?driverName ?constructorId ?constructorName ?position ?time ?laps

        WHERE {{
            ?result a ps:Result ;
                pred:participatedIn ns:{race_id} ;
                pred:hasDriver ?driverId ;
                pred:hasConstructor ?constructorId ;
                pred:position ?position . 
            OPTIONAL {{ ?result pred:laps ?laps. }}
            OPTIONAL {{ ?result pred:duration ?time. }}

            ?driverId a ps:Driver ;
                pred:forename ?driverForename ;
                pred:surname ?driverSurname .
            BIND(CONCAT(?driverForename, " ", ?driverSurname) AS ?driverName)

            ?constructorId a ps:Constructor ;
                pred:name ?constructorName .
        }}
        LIMIT 3
    """

    res = db.query(query)
    return res

def delete_race(raceId):
    """Delete a race"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>

        DELETE {{ <{raceId}> ?p ?o }}
        WHERE {{
            <{raceId}> a ps:Race ;
                ?p ?o .
        }}
        
    """

    res = db.update(query)

    return res

def insert_race(circuitId, date, name, round, year):
    """insert a race"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX race: <{NS}race/>

        SELECT (MAX(xsd:int(STRAFTER(str(?raceId), "/race/"))) AS ?maxRaceId)
        WHERE {{
            ?raceId a ps:Race .
        }}
    """

    res = db.query(query)
    data = json.loads(res)
    nextId = int(data["results"]["bindings"][0]["maxRaceId"]["value"]) + 1

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX race: <{NS}race/>

        INSERT DATA
        {{
            race:{nextId} a ps:Race ;
                pred:hasCircuit <{circuitId}> ;
                pred:date "{date}"^^xsd:string ;
                pred:name "{name}"^^xsd:string ;
                pred:round "{round}"^^xsd:int ;
                pred:year "{year}"^^xsd:int .
        }}
        
    """

    res = db.update(query)

    return nextId
