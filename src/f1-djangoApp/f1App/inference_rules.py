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
    res = db.update(query)
    
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
    res = db.update(query)

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
    res = db.update(query)