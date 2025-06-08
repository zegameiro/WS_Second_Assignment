from mysite.graph_db import db
from f1App.constants import *

def retrieve_all_seasons(offset):
    """Retrieve all seasons from the database with pagination."""

    query = f"""
        PREFIX ps: <{NS}>
        PREFIX pred: <{PRED}>

        SELECT ?year ?url
        WHERE {{
            ?year a ps:Season ;
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
        PREFIX ps: <{NS}>
        PREFIX pred: <{PRED}>

        SELECT ?driverId ?driverName (SUM(?points) AS ?totalPoints)
        WHERE {{
            ?raceId a ps:Race ;
                pred:name ?raceName ;
                pred:year {year} .
            ?result a ps:Result ;
                pred:participatedIn ?raceId ;
                pred:hasDriver ?driverId ;
                pred:obtainedPoints ?points .
            ?driverId a ps:Driver ;
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
        PREFIX ps: <{NS}>
        PREFIX pred: <{PRED}>

        SELECT ?constructorId ?constructorName (SUM(?points) AS ?totalPoints)
        WHERE {{
            ?raceId a ps:Race ;
                pred:name ?raceName ;
                pred:year {year} .
            ?result a ps:Result ;
                pred:participatedIn ?raceId ;
                pred:hasConstructor ?constructorId ;
                pred:obtainedPoints ?points .
            ?constructorId a ps:Constructor ;
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
        PREFIX ps: <{NS}>
        PREFIX season: <{NS}season/>

        DELETE {{ season:{year} ?p ?o }}
        WHERE {{
            season:{year} a ps:Season ;
                ?p ?o .
        }}
    """

    res = db.update(query)

    return res

def insert_season(year, url):
    """insert a season"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX season: <{NS}season/>

        INSERT DATA
        {{
            season:{year} a ps:Season ;
                pred:url <{url}> .
        }}
        
    """

    res = db.update(query)

    return res