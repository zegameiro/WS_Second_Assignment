import os

class Settings:
    def __init__(self):
        # GraphDB database
        self.graph_db_endpoint = "http://localhost:7200"
        self.repo_name = "woof"
        print(self.repo_name)

ENVIRONMENTS = Settings()
