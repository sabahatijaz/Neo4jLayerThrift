from Functions.functions import to_graph
from Neo4JLayer.Neo4j import Neo4Niha
from niha_thrift.ttypes import TNode, TRelation, TGraph, TMemoryChunk
from Wrapper.TGraphWrapper import Neo4jGraph
from Wrapper.TRelationWrapper import Neo4jRelation
from Functions.functions import *


class Neo4jMemoryChunk:
    def __init__(self, _memory_chunk=None):
        self.memory_chunk = _memory_chunk
        self.db = Neo4Niha()
        self.__relation = TRelation()
        self.__graph = Neo4jGraph()

    def set_memoryChunk(self, value):
        self.memory_chunk = value

    def create_memory_chunk(self):
        self.__graph.set_graph(value=self.memory_chunk.Graph)
        self.__graph.create_graph()

        # self.__graph.graph = self.memory_chunk.Graph
        # self.__graph.create_graph()
        query = "create (n:MemoryChunk {"
        query += "name:'MemoryChunk',TimeStamp:'{0}' ,Capacity:{1}".format(
            self.memory_chunk.TimeStamp, self.memory_chunk.Capacity)
        query += ", AttentionLevel:{0}, DecayLevel:{1}, Importance:{2}, Evaluation:{3}, gid:{4} ".format(
            self.memory_chunk.AttentionLevel, self.memory_chunk.DecayLevel, self.memory_chunk.Importance,
            self.memory_chunk.Evaluation, self.memory_chunk.Graph.Neo4jID)
        query += "}) return ID(n) as id"
        response = self.db.create(query)
        self.__graph.ID = response[0]['id']
        return str(self.__graph.ID)

    def retrieve_memory_chunk(self, _id):
        q = "match (m:MemoryChunk) where ID(m)={0} return m".format(_id)
        response = self.db.retrieve(q)
        memorychunk = to_memoryChunk(response[0]['m'])
        print(type(memorychunk))
        return memorychunk

    def update_memory_chunk(self, _id):
        query = "MATCH (n:MemoryChunk) where ID(n)={0} set n.TimeStamp='{1}', n.Capacity={2}, n.AttentionLevel={3}," \
                "n.DecayLevel={4},n.Importance={5},n.Evaluation={6} return 1".format(
            _id, self.memory_chunk.TimeStamp, self.memory_chunk.Capacity, self.memory_chunk.AttentionLevel,
            self.memory_chunk.DecayLevel, self.memory_chunk.Importance,
            self.memory_chunk.Evaluation)
        response = self.db.update(query)
        return response

    def delete_memory_chunk(self, _id):
        q = "match (m:MemoryChunk) where ID(m)={0} DETACH DELETE m return 1".format(_id)
        response = self.db.delete(q)
        return response

    def to_memory_chunck(self, neo4graph):
        memory_chunk = TMemoryChunk()
        memory_chunk.Graph = neo4graph
        memory_chunk.Nid = neo4graph.Nodes
        memory_chunk.Rid = neo4graph.Relation
        memory_chunk.rtype = neo4graph.Relation['_relation']

    def retrieve_by_id(self, _id):
        q = "match (m) where ID(m)={0} return m".format(_id)
        response = self.db.retrieve(q)
        return to_memoryChunk(response[0]['m'])


if __name__ == '__main__':
    memory_ = TMemoryChunk()
    memory = Neo4jMemoryChunk(memory_)
    memory.retrieve_by_id()
