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

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?entity a ps:ConstructorResult .
        }}
        WHERE {{
            ?entity pred:obtainedPoints ?points .
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
    print("Added SPIN rule for total number of races in each circuit")

    # Add a rule to infer the winner of a race
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        INSERT {{
            ?race pred:wasWonBy ?driver
        }} 
        WHERE {{
            ?result a ps:Result ;
                pred:hasDriver ?driver ;
                pred:position "1"^^xsd:integer ;
                pred:participatedIn ?race .
        }}
    """
    db.update(query)
    print("Added SPIN rule for inferring the winner of a race")

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
    print("Added SPIN rule for inferring the season that a race belongs to")

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
    print("Added SPIN rule for inferring driver's full name")

    # Infer fastestDriver in a race based on the fastest Speed lap
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

        INSERT {{
            ?race pred:fastestDriver ?driver .
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
    print("Added SPIN rule for inferring the fastest driver in a race")

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>

        INSERT {{
            \<\< ?driverId pred:wasInConstructor ?constructorId \>\> pred:year ?year .
        }}
        WHERE {{
        ?result a ps:Result ;
                pred:participatedIn ?raceId ;
                pred:hasDriver ?driverId ;
                pred:hasConstructor ?constructorId .
        

        ?raceId a ps:Race ;
                pred:year ?year .

        }}
    """
    db.update(query)
    print("Added SPIN rule for inferring the constructors of drivers")


