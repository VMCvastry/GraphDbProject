from neo4j import GraphDatabase

DEFAULT_URI = "bolt://localhost:7687"
DEFAULT_USERNAME = "neo4j"
DEFAULT_PW = "galileo-ski-watch-orchid-plate-1558"
SUPPLY_DB = "supply-chain"


class Database:
    def __init__(
        self, uri=DEFAULT_URI, user=DEFAULT_USERNAME, password=DEFAULT_PW, db=SUPPLY_DB
    ):
        self.db = db
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def __del__(self):
        self.close()

    def query(self, query, parameters=None):
        session = self.driver.session(database=self.db)
        result = list(session.run(query, parameters))
        session.close()
        return result


query = "SHOW DATABASES"
db = Database()
result = db.query(query)
print(result)
