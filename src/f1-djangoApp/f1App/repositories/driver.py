from mysite.graph_db import db
from f1App.constants import *

def retrieve_all_drivers(offset):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>

        SELECT ?driverId ?number ?code ?forename ?surname ?nationality
        WHERE {{
            ?driverId a ps:Driver ;
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
        PREFIX ps: <{NS}>

        SELECT * 
        WHERE {{
            ns:{driver_id} a ps:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname ;
                pred:dob ?dob ;
                pred:nationality ?nationality ;
                pred:url ?url .

            OPTIONAL {{ ns:{driver_id} pred:number ?number . }}
            OPTIONAL {{ ns:{driver_id} pred:code ?code . }}
            OPTIONAL {{ ns:{driver_id} pred:image ?image . }}
            OPTIONAL {{ ns:{driver_id} pred:fullName ?fullName .}}
        }}
    """

    res = db.query(query)
    return res

def retrieve_drivers_by_regex(query, offset):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>

        SELECT ?driverId ?forename ?surname ?nationality
        WHERE {{
            ?driverId a ps:Driver ;
                pred:forename ?forename ;
                pred:surname ?surname ;
                pred:nationality ?nationality
            
            OPTIONAL {{ ?driverId pred:fullName ?fullName . }}
            
            BIND(COALESCE(?fullName, CONCAT(?forename, " ", ?surname)) AS ?nameToSearch) .

            FILTER regex(?nameToSeach,"{query}", "i") .
        }}
        LIMIT {LIMIT}
        OFFSET {offset}
    """

    res = db.query(query)
    return res

def retrieve_driver_race_wins(driver_id):

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX ns: <{NS}driver/>
        SELECT ?raceId ?raceName ?points ?raceYear
        WHERE {{
            
            ?resultId a ps:Result ;
                pred:hasDriver ns:{driver_id};
                pred:position 1 ;
                pred:participatedIn ?raceId ;
                pred:obtainedPoints ?points .
            
            ?raceId a ps:Race ;
                pred:name ?raceName ;
                pred:year ?raceYear .
        }}
        ORDER BY DESC(?points)
    """

    res = db.query(query)
    return res

def insert_driver_image(driver_id, url):
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ns: <{NS}driver/>

        INSERT {{
            ns:{driver_id} pred:image "{url}" .
        }}
        WHERE {{
            ns:{driver_id} a ?type .
        }}
    """

    res = db.update(query)
    return res
