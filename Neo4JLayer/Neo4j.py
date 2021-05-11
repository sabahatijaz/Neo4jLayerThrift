from neo4j import GraphDatabase

from Functions.functions import load_config


class Neo4Niha:
    def __init__(self):
        url, user, password = load_config()
        self.driver = GraphDatabase.driver(url, auth=(user, password))

    def close(self):
        self.driver.close()

    def create(self, query):
        with self.driver.session() as session:
            response = session.write_transaction(self.__create, query)
        return response

    def retrieve(self, query):
        with self.driver.session() as session:
            return session.read_transaction(self.__retrieve, query)

    def delete(self, query):
        with self.driver.session() as session:
            return session.write_transaction(self.__delete, query)

    def update(self, query):
        with self.driver.session() as session:
            return session.write_transaction(self.__update, query)

    @staticmethod
    def __create(tx, query):
        result = tx.run(query)
        nodes = [node for node in result]
        return nodes

    @staticmethod
    def __retrieve(tx, query):
        result = tx.run(query)
        nodes = [node for node in result]
        return nodes

    @staticmethod
    def __delete(tx, query):
        result = tx.run(query)
        return result

    @staticmethod
    def __update(tx, query):
        result = tx.run(query)
        #print("Response : ", result.single()[0])
        return result
