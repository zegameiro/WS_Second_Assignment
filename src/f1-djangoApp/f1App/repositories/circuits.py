from mysite.graph_db import db
from f1App.constants import *

def retrieve_circuit_by_race_id(race_id):
    
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        PREFIX ns: <{NS}race/>
        SELECT ?circuitId ?name ?location ?country ?lat ?lng ?alt ?url
        WHERE {{
            ns:{race_id} a ps:Race ;
                pred:hasCircuit ?circuitId .

            ?circuitId a ps:Circuit ;
                pred:name ?name ;
                pred:location ?location ;
                pred:country ?country ;
                pred:lat ?lat ;
                pred:lng ?lng ;
                pred:alt ?alt ;
                pred:url ?url .
        }}
    """

    res = db.query(query)
    return res

def retrieve_all_circuits(offset=None):
    
    if offset is None:
        query = f"""
            PREFIX pred: <{PRED}>
            PREFIX ps: <{NS}>
            SELECT ?circuitId ?name ?location ?country
            WHERE {{
                ?circuitId a ps:Circuit ;
                    pred:name ?name ;
                    pred:location ?location ;
                    pred:country ?country .
            }}
            ORDER BY ?name
        """
    else:
        query = f"""
            PREFIX pred: <{PRED}>
            PREFIX ps: <{NS}>
            SELECT ?circuitId ?name ?location ?country
            WHERE {{
                ?circuitId a ps:Circuit ;
                    pred:name ?name ;
                    pred:location ?location ;
                    pred:country ?country .
            }}
            ORDER BY ?name
            LIMIT {LIMIT}
            OFFSET {offset}
        """

    res = db.query(query)
    return res

def retrieve_circuit_by_id(circuit_id):
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ns: <{NS}circuit/>
        PREFIX ps: <{NS}>
        SELECT ?circuitRef ?name ?location ?country ?lat ?lng ?alt ?url
        WHERE {{
            ns:{circuit_id} a ps:Circuit ;
                pred:circuitRef ?circuitRef ;
                pred:name ?name ;
                pred:location ?location ;
                pred:country ?country ;
                pred:lat ?lat ;
                pred:lng ?lng ;
                pred:alt ?alt ;
                pred:url ?url .
        }}
    """

    res = db.query(query)
    return res

def insert_circuit_image(circuit_id, image_url):
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ns: <{NS}driver/>
        INSERT {{
            ns:{circuit_id} pred:image "{image_url}" .
        }}
        WHERE {{
            ns:{circuit_id} a ps:Circuit .
        }}
    """

    res = db.update(query)
    return res

def insert_circuit_abstract(circuit_id, abstract):
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ns: <{NS}circuit/>
        INSERT {{
            ns:{circuit_id} pred:comment "{abstract}" .
        }}
        WHERE {{
            ns:{circuit_id} a ps:Circuit .
        }}
    """

    res = db.update(query)
    return res