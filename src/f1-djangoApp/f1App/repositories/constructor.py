from mysite.graph_db import db
from f1App.constants import *

def retrieve_all_constructors(offset):
    """Get all constructors"""

    query = f"""
        PREFIX pred: <{PRED}>
        PREFIX ps: <{NS}>
        SELECT ?c ?name ?nationality ?url WHERE {{
            ?c a ps:Constructor ;
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
        PREFIX ps: <{NS}>
        SELECT ?nationality (GROUP_CONCAT(?name; separator=", ") AS ?constructors) WHERE {{
            ?c a ps:Constructor ;
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
        PREFIX ps: <{NS}>
        SELECT ?name ?nationality ?url WHERE {{
            <{constructor_id}> a ps:Constructor ;
            pred:name ?name ;
            pred:nationality ?nationality ;
            pred:url ?url .
        }}
    """

    res = db.query(query)

    return res