from f1_pitstop.graph_db import db
from app.constants import *

def retrieve_all_seasons(offset):
    """Retrieve all seasons from the database with pagination."""

    query = f"""
        PREFIX ns: <{NS}>
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>

        SELECT ?year ?url
        WHERE {{
            ?year a type:Season ;
                pred:url ?url
        }}
        ORDER BY DESC(?year)
        LIMIT {LIMIT}
        OFFSET {offset}
    """

    res = db.query(query)

    return res

def get_drivers_podium(year):
    """Retrive the drivers podium"""

    query = f"""
        PREFIX ns: <{NS}>
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>

        SELECT ?driverId ?driverName (SUM(?points) AS ?totalPoints)
        WHERE {{
            ?raceId a type:Race ;
                pred:name ?raceName ;
                pred:year "{year}"^^xsd:int .
            ?result a type:Result ;
                pred:raceId ?raceId ;
                pred:driverId ?driverId ;
                pred:points ?points .
            ?driverId a type:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname .

            BIND(CONCAT(?forename, " ",  ?surname) as ?driverName) .
        }}
        GROUP BY ?driverId ?driverName
        ORDER BY DESC (?totalPoints)
        LIMIT 3
    """

    res = db.query(query)

    return res

def get_constructors_podium(year):
    """Retrive the constructors podium"""

    query = f"""
        PREFIX ns: <{NS}>
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>

        SELECT ?constructorId ?constructorName (SUM(?points) AS ?totalPoints)
        WHERE {{
            ?raceId a type:Race ;
                pred:name ?raceName ;
                pred:year "{year}"^^xsd:int .
            ?result a type:Result ;
                pred:raceId ?raceId ;
                pred:constructorId ?constructorId ;
                pred:points ?points .
            ?constructorId a type:Constructor ;
                pred:name ?constructorName .

        }}
        GROUP BY ?constructorId ?constructorName
        ORDER BY DESC (?totalPoints)
        LIMIT 3
    """

    res = db.query(query)

    return res

def delete_season(year):
    """Delete a season"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        PREFIX season: <{NS}season/>

        DELETE {{ season:{year} ?p ?o }}
        WHERE {{
            season:{year} a type:Season ;
                ?p ?o .
        }}
        
    """

    res = db.update(query)

    return res

def insert_season(year, url):
    """insert a season"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        PREFIX season: <{NS}season/>

        INSERT DATA
        {{
            season:{year} a type:Season ;
                pred:url <{url}> .
        }}
        
    """

    res = db.update(query)

    return res