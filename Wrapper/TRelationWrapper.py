import datetime
import string

from Neo4JLayer.Neo4j import Neo4Niha
from genpy.niha_thrift.ttypes import *
from Functions.functions import *
from Wrapper.TNodeWrapper import Neo4jNode


class Neo4jRelation:
    def __init__(self, _relation=None):
        self.__relation = _relation
        self.db = Neo4Niha()

    def set_relation(self, value):
        self.__relation = value

    def create_query(self):
        global label, label2
        query1 = "MERGE (n"
        #self.__relation.SourceNode.SubjectSpecializationOf=['_'.join(e for e in string if e.isalnum()) for string in self.__relation.SourceNode.SubjectSpecializationOf]
        subjectlength=len(self.__relation.SourceNode.SubjectSpecializationOf)
        for node in range(subjectlength):
            strrep=self.__relation.SourceNode.SubjectSpecializationOf[node]
            strrep=strrep.replace(" ","_")
            strrep = strrep.replace("&", "_")
            strrep = strrep.replace("/", "_")
            strrep = strrep.replace("#", "_")
            strrep = strrep.replace("@", "_")
            strrep = strrep.replace("!", "_")
            strrep = strrep.replace("(", "_")
            strrep = strrep.replace(")", "_")
            strrep = strrep.replace("*", "_")
            strrep = strrep.replace("'", "")
            strrep = strrep.replace(",", "_")
            strrep = strrep.replace(":", "_")
            strrep = strrep.replace(";", "_")
            strrep = strrep.replace("-", "_")
            self.__relation.SourceNode.SubjectSpecializationOf[node]=strrep

        for label in self.__relation.SourceNode.SubjectSpecializationOf:
            query1 += ":`{label}`".format(label=label)
        query1 += " {"
        # for label in self.__relation.SourceNode.NameLabels:
        #     label=label
        #     break
        query1 += "nodetype:'{0}', name:'{1}'".format("Node", self.__relation.SourceNode.SubjectSpecializationOf[0])
        namelist = []
        for labels in self.__relation.SourceNode.NameLabels:
            namelist.append(labels)
        query1 += ", NameLabels:{0}".format(list(namelist))
        aoklist = []
        for aokid in self.__relation.SourceNode.AoKID:
            aoklist.append(aokid)
        Graphidlist = []
        for gid in self.__relation.SourceNode.AoKID:
            Graphidlist.append(gid)
        query1 += ", AoKID:{0} , SystemLevelType:{1} , AbstractionLevel:{2}, Validity:'{3}', Evaluation:{4}, " \
                  "AgeInMilliseconds:{5}, AttentionLevel:{6}, GraphID:{7}, DateTimeStamp:'{8}', HasUserCreatedTheNode:{9},UserID:'{10}', UserName:'{11}',AppKey:'{12}',RegisteredDevices:{13}".format(
            list(aoklist),
            self.__relation.SourceNode.SystemLevelType, self.__relation.SourceNode.AbstractionLevel,
            self.__relation.SourceNode.Validity,
            self.__relation.SourceNode.Evaluation,
            self.__relation.SourceNode.AgeInMilliseconds, self.__relation.SourceNode.AttentionLevel, list(Graphidlist),
            self.__relation.SourceNode.DateTimeStamp,
            self.__relation.SourceNode.HasUserCreatedTheNode, self.__relation.SourceNode.SignedInUser.UserID,
            self.__relation.SourceNode.SignedInUser.UserName, self.__relation.SourceNode.SignedInUser.AppKey,
            list(self.__relation.SourceNode.SignedInUser.RegisteredDevices))
        # for domain in self.node.Domains:+
        #     query += "{domain},".format(domain=domain)

        if self.__relation.SourceNode.TruthValue is not None:
            Keylis = []
            for key in self.__relation.SourceNode.TruthValue.keys():
                Keylis.append(key)
            query1 += ", tv_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.SourceNode.TruthValue.keys(),
                                  self.__relation.SourceNode.TruthValue.values()):
                query1 += ",{0} :{1}".format(key, value)

        if self.__relation.SourceNode.ScratchPad is not None:
            Keylis = []
            for key in self.__relation.SourceNode.ScratchPad.keys():
                Keylis.append(key)
            query1 += ", sp_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.SourceNode.ScratchPad.keys(),
                                  self.__relation.SourceNode.ScratchPad.values()):
                query1 += ",{0} :'{1}'".format(key, value)

        if self.__relation.SourceNode.Type is not None:
            Keylis = []
            for key in self.__relation.SourceNode.Type.keys():
                Keylis.append(key)
            query1 += ", type_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.SourceNode.Type.keys(), self.__relation.SourceNode.Type.values()):
                vallis = []
                # for val in value:
                #  Keylis.append(val)
                query1 += ",{0} :{1}".format(key, list(value))

        query1 += "})"

        query2 = " MERGE (m"
        #self.__relation.TargetNode.SubjectSpecializationOf=['_'.join(e for e in string if e.isalnum()) for string in self.__relation.TargetNode.SubjectSpecializationOf]
        subjectlength = len(self.__relation.TargetNode.SubjectSpecializationOf)
        for node in range(subjectlength):
            strrep = self.__relation.TargetNode.SubjectSpecializationOf[node]
            # ''.join(e for e in strrep if e.isalnum())
            strrep = strrep.replace(" ", "_")
            strrep = strrep.replace("&", "_")
            strrep = strrep.replace("/", "_")
            strrep = strrep.replace("#", "_")
            strrep = strrep.replace("@", "_")
            strrep = strrep.replace("!", "_")
            strrep = strrep.replace("(", "_")
            strrep = strrep.replace(")", "_")
            strrep = strrep.replace("*", "_")
            strrep = strrep.replace("'", "")
            strrep = strrep.replace(",", "_")
            strrep = strrep.replace(":", "_")
            strrep = strrep.replace(";", "_")
            strrep = strrep.replace("-", "_")
            self.__relation.TargetNode.SubjectSpecializationOf[node] = strrep

        for label in self.__relation.TargetNode.SubjectSpecializationOf:
            query2 += ":`{label}`".format(label=label)
        query2 += " {"
        # for label in self.__relation.TargetNode.NameLabels:
        #     label=label
        #     break
        query2 += "nodetype:'{0}', name:'{1}'".format("Node", self.__relation.TargetNode.SubjectSpecializationOf[0])
        namelist = []
        for labels in self.__relation.TargetNode.NameLabels:
            namelist.append(labels)
        query2 += ", NameLabels:{0}".format(list(namelist))
        aoklist = []
        for aokid in self.__relation.TargetNode.AoKID:
            aoklist.append(aokid)
        Graphidlist = []
        for gid in self.__relation.TargetNode.AoKID:
            Graphidlist.append(gid)
        query2 += ", AoKID:{0} , SystemLevelType:{1} , AbstractionLevel:{2}, Validity:'{3}', Evaluation:{4}, " \
                  "AgeInMilliseconds:{5}, AttentionLevel:{6}, GraphID:{7}, DateTimeStamp:'{8}', HasUserCreatedTheNode:{9},UserID:'{10}', UserName:'{11}',AppKey:'{12}',RegisteredDevices:{13}".format(
            list(aoklist),
            self.__relation.TargetNode.SystemLevelType, self.__relation.TargetNode.AbstractionLevel,
            self.__relation.TargetNode.Validity,
            self.__relation.TargetNode.Evaluation,
            self.__relation.TargetNode.AgeInMilliseconds, self.__relation.TargetNode.AttentionLevel, list(Graphidlist),
            self.__relation.TargetNode.DateTimeStamp,
            self.__relation.TargetNode.HasUserCreatedTheNode, self.__relation.TargetNode.SignedInUser.UserID,
            self.__relation.TargetNode.SignedInUser.UserName, self.__relation.TargetNode.SignedInUser.AppKey,
            list(self.__relation.TargetNode.SignedInUser.RegisteredDevices))

        # for domain in self.node.Domains:+
        #     query += "{domain},".format(domain=domain)

        if self.__relation.TargetNode.TruthValue is not None:
            Keylis = []
            for key in self.__relation.TargetNode.TruthValue.keys():
                Keylis.append(key)
            query2 += ", tv_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.TargetNode.TruthValue.keys(),
                                  self.__relation.TargetNode.TruthValue.values()):
                query2 += ",{0} :{1}".format(key, value)

        if self.__relation.TargetNode.ScratchPad is not None:
            Keylis = []
            for key in self.__relation.TargetNode.ScratchPad.keys():
                Keylis.append(key)
            query2 += ", sp_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.TargetNode.ScratchPad.keys(),
                                  self.__relation.TargetNode.ScratchPad.values()):
                query2 += ",{0} :'{1}'".format(key, value)

        if self.__relation.TargetNode.Type is not None:
            Keylis = []
            for key in self.__relation.TargetNode.Type.keys():
                Keylis.append(key)
            query2 += ", type_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.TargetNode.Type.keys(), self.__relation.TargetNode.Type.values()):
                vallis = []
                # for val in value:
                #  Keylis.append(val)
                query2 += ",{0} :{1}".format(key, list(value))

        query2 += "})"
        query = query1 + query2 + " Merge (n)-[r"
        #self.__relation.SubjectSpecializationOf=['_'.join(e for e in string if e.isalnum()) for string in self.__relation.SubjectSpecializationOf]
        subjectlength=len(self.__relation.SubjectSpecializationOf)
        for node in range(subjectlength):
            strrep=self.__relation.SubjectSpecializationOf[node]
            strrep=strrep.replace(" ","_")
            strrep = strrep.replace("&", "_")
            strrep = strrep.replace("/", "_")
            strrep = strrep.replace("#", "_")
            strrep = strrep.replace("@", "_")
            strrep = strrep.replace("!", "_")
            strrep = strrep.replace("(", "_")
            strrep = strrep.replace(")", "_")
            #strrep = strrep.replace("*", "_")
            strrep = strrep.replace("-", "_")
            strrep = strrep.replace("'", "")
            strrep = strrep.replace(",", "_")
            strrep = strrep.replace(":", "_")
            strrep = strrep.replace(";", "_")
            strrep = strrep.replace("-", "_")
            self.__relation.SubjectSpecializationOf[node]=strrep

        for label in self.__relation.SubjectSpecializationOf:
            query += ":`{label}`".format(label=label)
            break
        subjectlist = []
        for label in self.__relation.SubjectSpecializationOf:
            subjectlist.append(label)
        query += " {"
        query += "SubjectSpecializationOf:{0} ".format(list(subjectlist))
        namelist = []
        for labels in self.__relation.NameLabels:
            namelist.append(labels)
        query += ", NameLabels:{0}, GraphID:{1}".format(list(namelist), list(self.__relation.GraphID))
        query += ",AoKID:{0}, RelationType:'{1}', AttentionLevel:{2}, DateTimeStamp:'{3}', AgeInMilliseconds:{4}, " \
                 "HasUserCreatedTheRelation:{5},UserID:'{6}', UserName:'{7}',AppKey:'{8}',RegisteredDevices:{9}".format(
            list(self.__relation.AoKID),
            self.__relation.RelationType,
            self.__relation.AttentionLevel,
            self.__relation.DateTimeStamp,
            self.__relation.AgeInMilliseconds, self.__relation.HasUserCreatedTheRelation,
            self.__relation.SignedInUser.UserID, self.__relation.SignedInUser.UserName,
            self.__relation.SignedInUser.AppKey, list(self.__relation.SignedInUser.RegisteredDevices)
        )
        typelist = []
        for type in self.__relation.Type:
            typelist.append(type)
        query += ", Type:{0}".format(list(typelist))
        if self.__relation.TruthValue is not None:
            Keylis = []
            for key in self.__relation.TruthValue.keys():
                Keylis.append(key)
            query += ", tv_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.TruthValue.keys(), self.__relation.TruthValue.values()):
                query += ",{0} :{1}".format(key, value)

        if self.__relation.ScratchPad is not None:
            Keylis = []
            for key in self.__relation.ScratchPad.keys():
                Keylis.append(key)
            query += ", sp_Keys:{0}".format(list(Keylis))
            for key, value in zip(self.__relation.ScratchPad.keys(), self.__relation.ScratchPad.values()):
                query += ",{0} :'{1}'".format(key, value)
        query += "}]-(m) return ID(n) as sid,ID(r) as rid,ID(m) as tid"
        return query

    def update_query(self, r_id):
        query = "match ()-[r]-() where ID(r)={0} set ".format(r_id)
        namelist = []
        for labels in self.__relation.NameLabels:
            namelist.append(labels)
        query += " r.NameLabels={0}, r.GraphID={1}".format(list(namelist), list(self.__relation.GraphID))
        query += ",r.AoKID={0}, r.RelationType='{1}', r.AttentionLevel={2}, r.DateTimeStamp='{3}', " \
                 "r.AgeInMilliseconds={4}, " \
                 "r.HasUserCreatedTheRelation={5},r.UserID='{6}', r.UserName='{7}',r.AppKey='{8}'," \
                 "r.RegisteredDevices={9}".format(
            list(self.__relation.AoKID),
            self.__relation.RelationType,
            self.__relation.AttentionLevel,
            self.__relation.DateTimeStamp,
            self.__relation.AgeInMilliseconds, self.__relation.HasUserCreatedTheRelation,
            self.__relation.SignedInUser.UserID, self.__relation.SignedInUser.UserName,
            self.__relation.SignedInUser.AppKey, list(self.__relation.SignedInUser.RegisteredDevices)
        )
        typelist = []
        for type in self.__relation.TargetNode.Type:
            typelist.append(type)
        query += ", r.Type={0}".format(list(typelist))
        if self.__relation.TruthValue is not None:
            keylis = []
            for key in self.__relation.TruthValue.keys():
                keylis.append(key)
            query += ", r.tv_Keys={0}".format(list(keylis))
            for key, value in zip(self.__relation.TruthValue.keys(), self.__relation.TruthValue.values()):
                query += ",r.{0} ={1}".format(key, value)

        if self.__relation.ScratchPad is not None:
            Keylis = []
            for key in self.__relation.ScratchPad.keys():
                Keylis.append(key)
            query += ", r.sp_Keys={0}".format(list(Keylis))
            for key, value in zip(self.__relation.ScratchPad.keys(), self.__relation.ScratchPad.values()):
                query += ",{0} ={1}".format(key, value)

        query += " return 1"
        return query

    def retrieve_query_id(self, r_id):
        return "match (s)-[r]-(t) where ID(r)={0} return s,r,t".format(r_id)

    def retrieve_query_GraphId(self, r_id, limit):
        return "match (s)-[r]-(t) where single(gid in r.GraphID WHERE gid = '{0}') return s,r,t limit {1}".format(r_id,
                                                                                                                  limit)

    def retrieve_query_NameLabel(self, criteria, limit):
        return "match (s)-[r]-(t) where single(namelabel in r.NameLabels WHERE namelabel = '{0}') return s,r,t limit {1}".format(
            criteria, limit)

    def retrieve_query_UniqueListOfAllSpecializationLabels(self, limit):
        return "match (s)-[r]-(t) return DISTINCT r.SubjectSpecializationOf limit {0}".format(limit)

    def delete_relation_query(self, r_id):
        return "match ()-[r]-() where ID(r)={0} delete r".format(r_id)

    def create_relation(self):
        query = self.create_query()
        # print(query)
        response = self.db.create(query)
        _id_dictionary = [{"sid": str(record['sid']), "rid": str(record['rid']), "tid": str(record['tid'])}
                          for record in response]
        # print(_id_dictionary[0])
        return _id_dictionary[0]
        # update logic here because graph is already generated on just assign neo4j id
        # ids after generated graph physically

    def retrieve_relation_by_id(self, r_id):
        query = self.retrieve_query_id(r_id)
        response = self.db.retrieve(query)
        relation = None
        for node in response:
            source_node = to_tnode(node['r'].nodes[0])
            target_node = to_tnode(node['r'].nodes[1])
            _id = node['r'].id
            _type = node['r'].type
            properties = dict(node['r'])
            relation = to_relation(_id, source_node, target_node, _type, properties)
        return relation

    def retrieve_relation_by_Graphid(self, r_id, limit):
        query = self.retrieve_query_GraphId(r_id, limit)
        response = self.db.retrieve(query)
        list_of_relations = []
        for rel in response:
            # print(rel)
            for node in response:
                source_node = to_tnode(node['r'].nodes[0])
                target_node = to_tnode(node['r'].nodes[1])
                _id = node['r'].id
                _type = node['r'].type
                # print(_type)
                properties = dict(node['r'])
                relation = to_relation(_id, source_node, target_node, _type, properties)
                list_of_relations.append(relation)
        # print(type(list_of_relations[0]))
        # print(list_of_relations[0])
        return list_of_relations

    def retrieve_relation_by_NameLabels(self, criteria, limit):
        query = self.retrieve_query_NameLabel(criteria, limit)
        response = self.db.retrieve(query)
        # print(response)
        list_of_relations = []
        for rel in response:
            # print(rel)
            for node in response:
                source_node = to_tnode(node['r'].nodes[0])
                target_node = to_tnode(node['r'].nodes[1])
                _id = node['r'].id
                _type = node['r'].type
                properties = dict(node['r'])
                relation = to_relation(_id, source_node, target_node, _type, properties)
                list_of_relations.append(relation)
        # print(type(list_of_relations))
        return list_of_relations

    def retrieve_relation_by_UniqueListOfAllSpecializationLabels(self, limit):
        query = self.retrieve_query_UniqueListOfAllSpecializationLabels(limit)
        response = self.db.retrieve(query)
        list_of_SpecializationLabels = []
        # print(response)
        for node in response:
            list_of_SpecializationLabels += node
        # print(type(list_of_SpecializationLabels))
        return list_of_SpecializationLabels[0]

    def retrieve_relation(self):
        query = "match (s)-[r]-(t) return s,r,t"
        response = self.db.retrieve(query)
        relation = []
        for node in response:
            source_node = to_tnode(node['r'].nodes[0])
            target_node = to_tnode(node['r'].nodes[1])
            _id = node['r'].id
            _type = node['r'].type
            properties = dict(node['r'])
            relation += [to_relation(_id, source_node, target_node, _type, properties)]
        return relation

    def delete_relation(self, r_id):
        query = self.delete_relation_query(r_id)
        response = self.db.delete(query)
        return response

    def update_relation(self, r_id):
        query = self.update_query(r_id)
        # print(query)
        response = self.db.update(query)
        return response

    def retrieve_by_id(self, _id):
        query = "match (m)-[r]-(n) where ID(r)={0} return m,r,n".format(_id)
        return self.db.retrieve(query)
