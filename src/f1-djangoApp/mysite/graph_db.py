from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient
from .envs import ENVIRONMENTS

class GraphDB:
    def __init__(self):
        self.client = ApiClient(endpoint=ENVIRONMENTS.graph_db_endpoint)
        self.accessor = GraphDBApi(self.client)
        self.repo_name = ENVIRONMENTS.repo_name
    
    def query(self,query):
        payload_query = {"query": query}

        res = self.accessor.sparql_select(body=payload_query, repo_name=self.repo_name)

        return res

    def update(self,query):
        payload_query = {"update": query}

        res = self.accessor.sparql_update(body=payload_query, repo_name=self.repo_name)

        return res

db = GraphDB()