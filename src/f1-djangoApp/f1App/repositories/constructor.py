from f1_pitstop.graph_db import db
from app.constants import *

def retrieve_all_constructors(offset):
    """Get all constructors"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        SELECT ?c ?name ?nationality ?url WHERE {{
            ?c a type:Constructor ;
            pred:name ?name ;
            pred:nationality ?nationality ;
            pred:url ?url .
        }}
        LIMIT {LIMIT}
        OFFSET {offset}
    """

    res = db.query(query)

    return res

def retrieve_constructors_by_nationality():
    """Get all the constructors grouped by nationality"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        SELECT ?nationality (GROUP_CONCAT(?name; separator=", ") AS ?constructors) WHERE {{
            ?c a type:Constructor ;
            pred:name ?name ;
            pred:nationality ?nationality .
        }}
        GROUP BY ?nationality
    """

    res = db.query(query)

    return res

def retrieve_constructors_by_id(constructor_id):
    """Get a constructor from by it's id"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX type: <{TYPE}>
        SELECT ?name ?nationality ?url WHERE {{
            <{constructor_id}> a type:Constructor ;
            pred:name ?name ;
            pred:nationality ?nationality ;
            pred:url ?url .
        }}
    """

    res = db.query(query)

    return res