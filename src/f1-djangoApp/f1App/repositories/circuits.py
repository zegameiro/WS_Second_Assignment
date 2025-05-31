from mysite.graph_db import db
from f1App.constants import *

def retrieve_circuit_by_race_id(race_id):
    
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        PREFIX ns: <{NS}race/>
        SELECT ?name ?location ?country ?lat ?lng ?alt ?url
        WHERE {{
            ns:{race_id} a type:Race ;
                pred:circuitId ?circuitId .

            ?circuitId a type:Circuit ;
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

def retrieve_all_circuits():
    
    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        SELECT ?circuitId ?name
        WHERE {{
            ?circuitId a type:Circuit ;
                pred:name ?name .
        }}
        ORDER BY ?name
    """

    res = db.query(query)
    return res