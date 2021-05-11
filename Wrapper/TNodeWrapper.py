from Neo4JLayer.Neo4j import Neo4Niha
# from Node import Node
from Functions.functions import to_tnode
import datetime
import pandas as pd
from genpy.niha_thrift.ttypes import TNode
import sys

class Neo4jNode:
    def __init__(self, _node=None):
        self.node = _node
        self.db = Neo4Niha()

    def set_node(self, value):
        self.node = value

    def create_node_query(self):
        global label
        query = "CREATE (n"
        # self.node.SubjectSpecializationOf = [''.join(e for e in string if e.isalnum()) for string in
        #                                                       self.node.SubjectSpecializationOf]
        subjectlength = len(self.node.SubjectSpecializationOf)
        for node in range(subjectlength):
            strrep = self.node.SubjectSpecializationOf[node]
            strrep = strrep.replace(" ", "_")
            strrep = strrep.replace("&", "_")
            strrep = strrep.replace("/", "_")
            strrep = strrep.replace("#", "_")
            strrep = strrep.replace("@", "_")
            strrep = strrep.replace("!", "_")
            strrep = strrep.replace("(", "_")
            strrep = strrep.replace(")", "_")
            strrep = strrep.replace("*", "_")
            strrep = strrep.replace("-", "_")
            strrep = strrep.replace("'", "")
            strrep = strrep.replace(",", "_")
            strrep = strrep.replace(":", "_")
            strrep = strrep.replace(";", "_")
            strrep = strrep.replace("-", "_")
            self.node.SubjectSpecializationOf[node] = strrep

        for label in self.node.SubjectSpecializationOf:
            query += ":`{label}`".format(label=label)
        query += " {"
        # for label in self.__relation.SourceNode.NameLabels:
        #     label=label
        #     break
        query += "nodetype:'{0}', name:'{1}'".format("Node", self.node.SubjectSpecializationOf[0])
        namelist = []
        for labels in self.node.NameLabels:
            namelist.append(labels)
        query += ", NameLabels:{0}".format(list(namelist))
        aoklist = []
        for aokid in self.node.AoKID:
            aoklist.append(aokid)
        Graphidlist = []
        for gid in self.node.AoKID:
            Graphidlist.append(gid)
        query += ", AoKID:{0} , SystemLevelType:{1} , AbstractionLevel:{2}, Validity:'{3}', Evaluation:{4}, " \
                  "AgeInMilliseconds:{5}, AttentionLevel:{6}, GraphID:{7}, DateTimeStamp:'{8}', HasUserCreatedTheNode:{9},UserID:'{10}', UserName:'{11}',AppKey:'{12}',RegisteredDevices:{13}".format(
            list(aoklist),
            self.node.SystemLevelType, self.node.AbstractionLevel,
            self.node.Validity,
            self.node.Evaluation,
            self.node.AgeInMilliseconds, self.node.AttentionLevel, list(Graphidlist),
            self.node.DateTimeStamp,
            self.node.HasUserCreatedTheNode, self.node.SignedInUser.UserID,
            self.node.SignedInUser.UserName, self.node.SignedInUser.AppKey,
            list(self.node.SignedInUser.RegisteredDevices))
        # for domain in self.node.Domains:+
        #     query += "{domain},".format(domain=domain)

        if self.node.TruthValue is not None:
            Keylis = []
            for key in self.node.TruthValue.keys():
                Keylis.append(key)
            query += ", tv_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.node.TruthValue.keys(),
                                  self.node.TruthValue.values()):
                query += ",{0} :{1}".format(key, value)

        if self.node.ScratchPad is not None:
            Keylis = []
            for key in self.node.ScratchPad.keys():
                Keylis.append(key)
            query += ", sp_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.node.ScratchPad.keys(),
                                  self.node.ScratchPad.values()):
                query += ",{0} :'{1}'".format(key, value)

        if self.node.Type is not None:
            Keylis = []
            for key in self.node.Type.keys():
                Keylis.append(key)
            query += ", type_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.node.Type.keys(), self.node.Type.values()):
                vallis = []
                # for val in value:
                #  Keylis.append(val)
                query += ",{0} :{1}".format(key, list(value))

        query += "}) RETURN ID(n) as id"
        #print(query)
        return query

    def delete_node_query(self, n_id):
        return "match (n) where ID(n)={0} detach delete n return 1".format(n_id)

    def retrieve_node_queryId(self, n_id):
        return "match (n) where ID(n)={0} return n".format(n_id)

    def retrieve_node_by_AnySubjectSpecializationOf(self, criteria, limit):
        return "match (n:{0}) return n limit {1}".format(criteria, limit)

    def retrieve_node_by_AnyNameLabels(self, criteria, limit):
        return "match (n) where single(label in n.NameLabels WHERE label = '{0}')  return n LIMIT {1}".format(criteria, limit)

    def retrieve_node_by_UniqueListOfAllSpecializationLabels(self, limit):
        return "match (n) return DISTINCT labels(n) limit {0}".format(limit)

    def update_node_query(self, n_id):
        query = "MATCH (n) where ID(n)=" + n_id + " SET "
        namelist = []
        for labels in self.node.NameLabels:
            namelist.append(labels)
        query += "n.NameLabels={0}".format(list(namelist))
        aoklist = []
        for aokid in self.node.AoKID:
            aoklist.append(aokid)
        Graphidlist = []
        for gid in self.node.GraphID:
            Graphidlist.append(gid)
        query += ", n.AoKID={0} , n.SystemLevelType={1} , n.AbstractionLevel={2}, n.Validity='{3}', n.Evaluation={4}, " \
                 "n.AgeInMilliseconds={5}, n.AttentionLevel={6}, n.GraphID={7}, n.DateTimeStamp='{8}', n.HasUserCreatedTheNode={9},n.UserID='{10}', n.UserName='{11}',n.AppKey='{12}',n.RegisteredDevices={13}".format(
            list(aoklist),
            self.node.SystemLevelType, self.node.AbstractionLevel,
            self.node.Validity,
            self.node.Evaluation,
            self.node.AgeInMilliseconds, self.node.AttentionLevel, list(Graphidlist), self.node.DateTimeStamp,
            self.node.HasUserCreatedTheNode, self.node.SignedInUser.UserID, self.node.SignedInUser.UserName,
            self.node.SignedInUser.AppKey, list(self.node.SignedInUser.RegisteredDevices))
        # for domain in self.node.Domains:+
        if self.node.TruthValue is not None:
            Keylis = []
            for key in self.node.TruthValue.keys():
                Keylis.append(key)
            query += ", n.tv_Keys={0}".format(list(Keylis))
            for key, value in zip(self.node.TruthValue.keys(), self.node.TruthValue.values()):
                # print(key, value)
                query += ",n.{0} ={1}".format(key, value)
                #query += ", n." + key + "=" + value

        if self.node.ScratchPad is not None:
            Keylis = []
            for key in self.node.ScratchPad.keys():
                Keylis.append(key)
            query += ", n.sp_Keys={0}".format(list(Keylis))
            for key, value in zip(self.node.ScratchPad.keys(), self.node.ScratchPad.values()):
                # print(key, value)
                query += ",n.{0} ={1}".format(key, value)
                #query += ", n." + key + "=" + value


        if self.node.Type is not None:
            Keylis = []
            for key in self.node.Type.keys():
                Keylis.append(key)
            query += ", n.type_Keys={0}".format(list(Keylis))
            for key, value in zip(self.node.Type.keys(), self.node.Type.values()):
                vallist = []
                for val in value:
                    vallist.append(val)
                query += ",n.{0} ={1}".format(key, list(vallist))
                #query += ", n." + key + "=" + value

        query += " return 1"
        return query

    def create_node(self):
        query = self.create_node_query()
        response = self.db.create(query)
        self.node.Neo4jID = response[0]
        _id=""
        for record in response:
            _id=record['id']
        #print(str(_id))
        return str(_id)

    def retrieve_node_by_neo4jid(self, n_id):
        query = self.retrieve_node_queryId(n_id)
        response = self.db.retrieve(query)
        node=to_tnode(response[0]['n'])
        #print(node)
        return node

    def retrieve_by_AnySubjectSpecializationOf(self, criteria, limit):
        query = self.retrieve_node_by_AnySubjectSpecializationOf(criteria, limit)
        response = self.db.retrieve(query)
        list_of_nodes = []
        for node in response:
            list_of_nodes += [to_tnode(node['n'])]
        #print(list_of_nodes)
        return list_of_nodes

    def retrieve_by_AnyNameLabels(self, criteria, limit):
        query = self.retrieve_node_by_AnyNameLabels(criteria, limit)
        response = self.db.retrieve(query)
        list_of_nodes = []
        for node in response:
            list_of_nodes += [to_tnode(node['n'])]
        #print(list_of_nodes)
        return list_of_nodes

    def retrieve_by_UniqueListOfAllSpecializationLabels(self, limit):
        query = self.retrieve_node_by_UniqueListOfAllSpecializationLabels(limit)
        response = self.db.retrieve(query)
        list_of_SpecializationLabels = []
        #print(response)
        for node in response:
            list_of_SpecializationLabels += node
        #print(list_of_SpecializationLabels)
        return list_of_SpecializationLabels[0]

    def retrieve_nodes(self, query):
        #query = "match (n) return n"
        nodes = self.db.retrieve(query)
        list_of_nodes = []
        for node in nodes:
            list_of_nodes += [to_tnode(node['n'])]
        #print(list_of_nodes)
        return list_of_nodes

    def delete_node(self, n_id):
        query = self.delete_node_query(n_id)
        response = self.db.delete(query)
        if response==1:
            return True
        else:
            return False

    def update_node(self, n_id):
        query = self.update_node_query(n_id)
        #print(query)
        response = self.db.update(query)
        #print(response)
        if response == '1':
            return True
        else:
            return False
    def updation(self,label,ebayid,link):
        query = "MATCH (n:`{0}`)".format(label)
        query+=" where n.EbayID='{0}'".format(str(ebayid))
        query+=" SET n.link='{0}'".format(link)
        query+=" return 1"
        response = self.db.update(query)
        # print(response)
        if response == '1':
            return True
        else:
            return False

# if __name__ == '__main__':
#     n4j=Neo4jNode()
#     data = pd.read_csv(r"C:\Users\User\Desktop\thrift_server_test\thrift_server_test\cat_Id.csv").values
#     for i in range(data.shape[0]):
#        print(str(data[i,1]))
#         strrep = data[i,0]
#         strrep = strrep.replace(" ", "_")
#         strrep = strrep.replace("&", "_")
#         strrep = strrep.replace("/", "_")
#         strrep = strrep.replace("#", "_")
#         strrep = strrep.replace("@", "_")
#         strrep = strrep.replace("!", "_")
#         strrep = strrep.replace("(", "_")
#         strrep = strrep.replace(")", "_")
#         strrep = strrep.replace("*", "_")
#         strrep = strrep.replace("-", "_")
#         strrep = strrep.replace("'", "")
#         strrep = strrep.replace(",", "_")
#         strrep = strrep.replace(":", "_")
#         strrep = strrep.replace(";", "_")
#         strrep = strrep.replace("-", "_")
#         data[i,0]=strrep
#         response=n4j.updation(data[i,0],data[i,2],data[i,1])
#         print(response)