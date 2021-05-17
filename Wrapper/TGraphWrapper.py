from Neo4JLayer.Neo4j import Neo4Niha
from genpy.niha_thrift.ttypes import TGraph
from Wrapper.TRelationWrapper import Neo4jRelation

from Functions.functions import *


class Neo4jGraph:
    def __init__(self, _graph=None):
        self.graph = _graph
        self.db = Neo4Niha()
        self.__relation = Neo4jRelation()

    def set_graph(self, value):
        self.graph = value

    def retrieve_graph(self):
        query = "MATCH (m:TEST3)-[r:isA]->(n:TEST4) RETURN m,r,n LIMIT 25"
        response = self.db.retrieve(query)
        to_graph(response)
        return self.graph

    def create_graph(self):
        global label
        #print(self.graph)
        _node_ids = set()
        _edge_ids = set()
        for _rel in self.graph.Relations.values():
            self.__relation.set_relation(_rel)
            _ids = self.__relation.create_relation()
            #print(_ids)
            sid, rid, tid = _ids['sid'], _ids['rid'], _ids['tid']
            _rel.SourceNode.Neo4jID = sid
            _rel.TargetNode.Neo4jID = tid
            _rel.Neo4jID = rid
            _node_ids.update([sid, tid])
            _edge_ids.add(rid)
        query = "create (g"
        for label in self.graph.SubjectSpecializationOf:
            query += ":{label}".format(label=label)
        query += " {"
        query += "nodetype:'{0}', name:'{1}'".format("Graph", label)
        namelist = []
        for labels in self.graph.NameLabels:
            namelist.append(labels)
        query += ", NameLabels:{0}".format(list(namelist))
        query += ", GraphID:{0}, AoKID:{1}".format(list(self.graph.GraphID), list(self.graph.AoKID))
        typelist = []
        for typ in self.graph.Type:
            typelist.append(typ)
        query += ", Type:{0}".format(list(typelist))
        if self.graph.ScratchPad is not None:
            Keylis = []
            for key in self.graph.ScratchPad.keys():
                Keylis.append(key)
            query += ", sp_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.graph.ScratchPad.keys(), self.graph.ScratchPad.values()):
                query += ",{0} :'{1}'".format(key, value)
        query += ",nid:{0},rid:{1}, RepresentationType:{2}, HasUserCreatedTheGraph:{3}, DateTimeStamp:'{4}' ,UserID:'{5}', UserName:'{6}',AppKey:'{7}',RegisteredDevices:{8}".format(
            list(_node_ids), list(_edge_ids), self.graph.RepresentationType, self.graph.HasUserCreatedTheGraph,
            self.graph.DateTimeStamp, self.graph.SignedInUser.UserID,self.graph.SignedInUser.UserName,self.graph.SignedInUser.AppKey,list(self.graph.SignedInUser.RegisteredDevices))
        query += "}) return ID(g) as id"
        #print(query)
        response = self.db.create(query)
        _id = ""
        for record in response:
            _id = record['id']
        #print(type(_id))
        #print(_id)
        return str(_id)

    def update_query(self, g_id):
        query = "match (g) where ID(g)={0} set".format(g_id)
        namelist = []
        for labels in self.graph.NameLabels:
            namelist.append(labels)
        query += " g.NameLabels={0}".format(list(namelist))
        query += ", g.GraphID={0}, AoKID={1}".format(list(self.graph.GraphID), list(self.graph.AoKID))
        typelist = []
        for typ in self.graph.Type:
            typelist.append(typ)
        query += ", g.Type={0}".format(list(typelist))
        if self.graph.ScratchPad is not None:
            Keylis = []
            for key in self.graph.ScratchPad.keys():
                Keylis.append(key)
            query += ", g.sp_Keys={0}".format(list(Keylis))
            for key, value in zip(self.graph.ScratchPad.keys(), self.graph.ScratchPad.values()):
                query += ",g.{0} ='{1}'".format(key, value)
        query += ",g.nid={0},g.rid={1}, g.RepresentationType={2}, g.HasUserCreatedTheGraph={3}, g.DateTimeStamp='{4}' " \
                 ",g.UserID='{5}', g.UserName='{6}',g.AppKey='{7}',g.RegisteredDevices={8}".format(
            self.graph.nid, self.graph.rid, self.graph.RepresentationType, self.graph.HasUserCreatedTheGraph,
            self.graph.DateTimeStamp, self.graph.SignedInUser.UserID, self.graph.SignedInUser.UserName,
            self.graph.SignedInUser.AppKey, list(self.graph.SignedInUser.RegisteredDevices))
        query += " 1"
        response = self.db.update(query)
        return response

    def delete_query(self, g_id):
        q = "match (g) where ID(g)={0} DETACH DELETE g RETURN 1".format(g_id)
        response = self.db.delete(q)
        return response

    def retrieve_by_id(self, _id):
        q = "match (g) where ID(g)={0} and g.nodetype='Graph' return g".format(_id)
        response = self.db.retrieve(q)
        properties = response[0].data()
        rel = []
        for rid in properties['g']['rid']:
            r = self.__relation.retrieve_by_id(rid)
            rel += r
        _graph = to_graph(rel, properties)
        _graph.ScratchPad["CQL"]=q
        _graph.ID = str(response[0]['g'].id)
        self.graph = _graph
        return _graph

    def retrieve_by_query(self, query):
        response = self.db.retrieve(query)
        list_of_graphs = []
        rel = []
        # response[0]['n']
        #print(response)
        for graph in response:
            # g = graph['g']
            # properties=dict(g)
            # properties=graph['g']
            properties = graph.data()
            #print(properties)
            for rid in properties['g']['rid']:
                #print(rid)
                r = self.__relation.retrieve_by_id(rid)
                rel += r
            _graph = to_graph(rel, properties)
            _graph.Neo4jID = str(graph['g'].id)
            _graph.SubjectSpecializationOf = set(graph['g'].labels)
            _graph.ScratchPad["CQL"] = query
            list_of_graphs.append(_graph)
        # self.graph = _graph
        #print(type(list_of_graphs))
        return list_of_graphs

    def retrieve_by_AnySubjectSpecializationOf(self, criteria, limit):
        if limit==-1:
            query = "match (g:{0})".format(criteria)
            query += "where g.nodetype='Graph' return g"
        else:
            query = "match (g:{0})".format(criteria)
            query += "where g.nodetype='Graph' return g LIMIT {0} ".format(limit)
        response = self.db.retrieve(query)
        list_of_graphs = []
        rel = []
        # response[0]['n']
        #print(response)
        for graph in response:
            # g = graph['g']
            # properties=dict(g)
            # properties=graph['g']
            properties = graph.data()
            #print(properties)
            for rid in properties['g']['rid']:
                #print(rid)
                r = self.__relation.retrieve_by_id(rid)
                rel += r
            _graph = to_graph(rel, properties)
            _graph.Neo4jID = str(graph['g'].id)
            _graph.SubjectSpecializationOf = set(graph['g'].labels)
            _graph.ScratchPad["CQL"] = query
            list_of_graphs.append(_graph)
        # self.graph = _graph
        #print(type(list_of_graphs))
        return list_of_graphs

    def retrieve_by_AnyNameLabels(self, criteria, limit):
        list_of_graphs = []
        for crtr in criteria:
            if limit == -1:
                query = "match (g) where single(label in g.NameLabels WHERE label = '{0}') and g.nodetype='Graph' " \
                        "return g".format(crtr)
            else:
                query = "match (g) where single(label in g.NameLabels WHERE label = '{0}') and g.nodetype='Graph' " \
                        "return g  LIMIT {1}".format(crtr, limit)

            #print(query)
            response = self.db.retrieve(query)
            #print(response)

            rel = []
            # response[0]['n']
            #print(response)
            for graph in response:
                # g = graph['g']
                # properties=dict(g)
                # properties=graph['g']
                properties = graph.data()
                #print(properties)
                for rid in properties['g']['rid']:
                    #print(rid)
                    r = self.__relation.retrieve_by_id(rid)
                    rel += r
                _graph = to_graph(rel, properties)
                _graph.Neo4jID = str(graph['g'].id)
                _graph.SubjectSpecializationOf = set(graph['g'].labels)
                _graph.ScratchPad["CQL"] = query
                list_of_graphs.append(_graph)
            # self.graph = _graph
        #print(type(list_of_graphs))
        return list_of_graphs

    def retrieve_by_Types(self, criteria, limit):
        list_of_graphs = []
        for crtr in criteria:
            if limit == -1:
                query = "match (g) where single(label in g.Type WHERE label = '{0}') and g.nodetype='Graph' return g  ".format(crtr)
            else:
                query = "match (g) where single(label in g.Type WHERE label = '{0}') and g.nodetype='Graph' return g  " \
                        "LIMIT {1}".format(crtr,
                                           limit)
            #print(query)
            response = self.db.retrieve(query)
            #print(response)

            rel = []
            # response[0]['n']
            #print(response)
            for graph in response:
                # g = graph['g']
                # properties=dict(g)
                # properties=graph['g']
                properties = graph.data()
                #print(properties)
                for rid in properties['g']['rid']:
                    #print(rid)
                    r = self.__relation.retrieve_by_id(rid)
                    rel += r
                _graph = to_graph(rel, properties)
                _graph.Neo4jID = str(graph['g'].id)
                _graph.SubjectSpecializationOf = set(graph['g'].labels)
                _graph.ScratchPad["CQL"] = query
                list_of_graphs.append(_graph)
            # self.graph = _graph
        #print(type(list_of_graphs))
        return list_of_graphs

    def retrieve_by_TypeAndSpecialization(self, typecriteria, specializationcriteria, limit):
        if limit == -1:
            query = "match (g:{0}".format(specializationcriteria)
            query += ") where single(label in g.Type WHERE label = '{0}') and g.nodetype='Graph' return g".format(
                typecriteria)
        else:
            query = "match (g:{0}".format(specializationcriteria)
            query += ") where single(label in g.Type WHERE label = '{0}') and g.nodetype='Graph' return g  LIMIT {1}".format(
                typecriteria,
                limit)
        response = self.db.retrieve(query)
        list_of_graphs = []
        rel = []
        # response[0]['n']
        #print(response)
        for graph in response:
            # g = graph['g']
            # properties=dict(g)
            # properties=graph['g']
            properties = graph.data()
            #print(properties)
            for rid in properties['g']['rid']:
                #print(rid)
                r = self.__relation.retrieve_by_id(rid)
                rel += r
            _graph = to_graph(rel, properties)
            _graph.Neo4jID = str(graph['g'].id)
            _graph.SubjectSpecializationOf = set(graph['g'].labels)
            _graph.ScratchPad["CQL"] = query
            list_of_graphs.append(_graph)
        # self.graph = _graph
        #print(type(list_of_graphs))
        return list_of_graphs