from mysite.graph_db import db
from f1App.constants import *

def apply_inference_rules():
    
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?s a ps:DriverStanding .
        }}
        WHERE {{
            ?s a ps:Standing .
            ?s pred:hasDriver ?c .
        }}
    """
    db.update(query)
    
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?s a ps:ConstructorStanding .
        }}
        WHERE {{
            ?s a ps:Standing .
            ?s pred:hasConstructor ?c .
        }}
    """
    db.update(query)

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?entity a ps:Season .
        }}
        WHERE {{
            ?entity pred:url ?url .
            FILTER NOT EXISTS {{
                ?entity rdf:type ?anyType .
            }}
        }}
    """
    db.update(query)

def apply_plus_inference_rules():

    # Add the total number of races that occured in each circuit
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?circuit pred:numberOfRaces ?count .
        }}
        WHERE {{
            SELECT ?circuit (COUNT(?race) AS ?count)
                WHERE {{
                    ?race a ps:Race ;
                        pred:hasCircuit ?circuit .
                }}
            GROUP BY ?circuit
        }}
    """
    db.update(query)

    # Add a rule to infer the winner of a race
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?driver pred:hasWonRace ?race
        }} 
        WHERE {{
            ?result a ps:Result ;
                pred:hasDriver ?driver ;
                pred:position "1"^^xsd:integer ;
                pred:participatedIn ?race .
        }}
    """
    db.update(query)

    # Infer that a race belongs to a season
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?race pred:partOfSeason ?season .
        }}
        WHERE {{
            ?race a ps:Race ;
                pred:year ?year .
            ?season a ps:Season ;
                pred:url ?url . 
            FILTER(CONTAINS(STR(?url), STR(?year))) 
        }}
    """
    db.update(query)

    # Infer driver's full name
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?driver pred:fullName ?fullName .
        }}
        WHERE {{
            ?driver a ps:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname .
            BIND(CONCAT(?forename, " ", ?surname) AS ?fullName)
        }}
    """
    db.update(query)

    # Infer fastestDriver in a race based on the fastest Speed lap
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        INSERT {{
            ?driver pred:fastestInRace ?race .
        }}
        WHERE {{
            {{
                SELECT ?race (MAX(xsd:decimal(?speedVal)) AS ?maxSpeed)
                WHERE {{
                    ?result a ps:Result ;
                        pred:participatedIn ?race ;
                        pred:fastestLapSpeed ?speedRaw .
                    BIND(xsd:decimal(?speedRaw) AS ?speedVal)
                }}
                GROUP BY ?race
            }}

            ?result a ps:Result ;
                pred:participatedIn ?race ;
                pred:hasDriver ?driver ;
                pred:fastestLapSpeed ?driverSpeedRaw .
            BIND(xsd:decimal(?driverSpeedRaw) AS ?driverSpeed)
            FILTER(?driverSpeed = ?maxSpeed)
        }}
    """
    db.update(query)


