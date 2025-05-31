from mysite.graph_db import db
from f1App.constants import *

def retrieve_all_drivers(offset):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>

        SELECT ?driverId ?number ?code ?forename ?surname ?nationality
        WHERE {{
            ?driverId a type:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname ;
                pred:nationality ?nationality ;
                
            OPTIONAL {{
                ?driverId pred:number ?number ;
                        pred:code ?code .
            }}
        }}
        ORDER BY ?forename
        LIMIT {LIMIT}
        OFFSET {offset}
    """

    res = db.query(query)
    return res

def retrieve_driver_by_id(driver_id):

    query = f"""
        PREFIX ns: <{NS}driver/>
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>

        SELECT * 
        WHERE {{
            ns:{driver_id} a type:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname ;
                pred:dob ?dob ;
                pred:nationality ?nationality ;
                pred:url ?url .

            OPTIONAL {{ ns:{driver_id} pred:number ?number . }}
            OPTIONAL {{ ns:{driver_id} pred:code ?code . }}
        }}
    """

    res = db.query(query)
    return res

def retrieve_drivers_by_regex(query, offset):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>

        SELECT ?driverId ?forename ?surname ?nationality
        WHERE {{
            ?driverId a type:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname ;
                pred:nationality ?nationality
            
            FILTER regex(CONCAT(?forename, " ", ?surname), "{query}", "i") .
        }}
        LIMIT {LIMIT}
        OFFSET {offset}
    """

    res = db.query(query)
    return res

def retrieve_driver_race_wins(driver_id):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        PREFIX ns: <{NS}driver/>
        SELECT ?raceId ?raceName ?points ?raceYear
        WHERE {{
            
            ?qualifyingId a type:Result ;
                pred:driverId ns:{driver_id};
                pred:position "1"^^xsd:string ;
                pred:raceId ?raceId ;
                pred:points ?points .
            
            ?raceId a type:Race ;
                pred:name ?raceName ;
                pred:year ?raceYear .
        }}
        ORDER BY DESC(?points)
    """

    res = db.query(query)
    return res