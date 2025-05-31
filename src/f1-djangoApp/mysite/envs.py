import os

class Settings:
    def __init__(self):
        # GraphDB database
        self.graph_db_endpoint = os.getenv("GRAPH_DB_ENDPOINT")
        self.repo_name = os.getenv("REPO_NAME")
        print(self.repo_name)

ENVIRONMENTS = Settings()
