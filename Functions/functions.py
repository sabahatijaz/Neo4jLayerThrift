import json
# from niha_thrift.ttypes import TGraph, TNode, TRelation, TMemoryChunk
import os
from genpy.niha_thrift.ttypes import *

def load_config():
    path = os.getcwd()

    with open(r"C:\Users\User\Desktop\thrift_server_test\thrift_server_test\Functions\config.json") as json_data_file:
        data = json.load(json_data_file)
    conf = data["neo4j"]
    scheme = conf["scheme"]
    host = conf["host"]
    port = conf["port"]
    user = conf["user"]
    password = conf["password"]
    url = "{scheme}://{host_name}:{port}".format(scheme=scheme, host_name=host, port=port)
    return url, user, password


def to_relation(_id, source, target, _relation, rel_properties):
    relation = TRelation()
    relation.SubjectSpecializationOf = set(rel_properties['SubjectSpecializationOf'])
    relation.Neo4jID = str(_id)
    relation.NameLabels=set(rel_properties['NameLabels'])
    relation.AoKID = set(rel_properties['AoKID'])
    relation.GraphID= set(rel_properties['GraphID'])
    relation.RelationType = str(rel_properties['RelationType'])
    relation.SourceNode = source
    relation.TargetNode = target
    #relation.IsBiDirectional = False
    # relation.Properties = rel_properties
    relation.AttentionLevel = float(rel_properties['AttentionLevel'])
    #relation.AttentionLevel = 0.0
    relation.DateTimeStamp=rel_properties['DateTimeStamp']
    #relation.SignedInUser=rel_properties['SignedInUser']
    relation.HasUserCreatedTheRelation=rel_properties['HasUserCreatedTheRelation']
    username=str(rel_properties['UserName'])
    userid=str(rel_properties['UserID'])
    appkey=str(rel_properties['AppKey'])
    RegisteredDevices = []
    #print(rel_properties['RegisteredDevices'])
    for rd in rel_properties['RegisteredDevices']:
        RegisteredDevices.append(rd)
    #print(RegisteredDevices)
    relation.SignedInUser=TUser(UserID=userid,UserName=username,AppKey=appkey, RegisteredDevices= RegisteredDevices)
    Type=set()
    for key in rel_properties['Type']:
        Type.add(key)
    relation.Type = Type
    tv_dict = dict()
    for key in rel_properties['tv_Keys']:
        tv_dict[key] = float(rel_properties[key])
    relation.TruthValue = tv_dict
    sp_dict = dict()
    for key in rel_properties['sp_Keys']:
        sp_dict[key] = rel_properties[key]
    relation.ScratchPad = sp_dict
    return relation


def to_graph(response, gproperties):
    graph = TGraph()
    _nodes = dict()
    _edges = dict()
    #print(gproperties)
    for node in response:
        source_node = to_tnode(node['r'].nodes[0])
        target_node = to_tnode(node['r'].nodes[1])
        _id = node['r'].id
        _type = node['r'].type
        properties = dict(node['r'])
        relation = to_relation(_id, source_node, target_node, _type, properties)
        _nodes[source_node.Neo4jID] = source_node
        _nodes[target_node.Neo4jID] = target_node
        _edges[str(_id)] = relation
    graph.Nodes = _nodes
    graph.Relations = _edges
    graph.GraphID=str(gproperties['g']['GraphID'])
    graph.AoKID=set(gproperties['g']['AoKID'])
    #graph.SubjectSpecializationOf=gproperties['g'].labels
    graph.NameLabels=set(gproperties['g']['NameLabels'])
    graph.Type=set(gproperties['g']['Type'])
    graph.RepresentationType=gproperties['g']['RepresentationType']
    graph.DateTimeStamp=str(gproperties['g']['DateTimeStamp'])
    #graph.SignedInUser=gproperties['g']['SignedInUser']
    graph.HasUserCreatedTheGraph=gproperties['g']['HasUserCreatedTheGraph']
    username = str(gproperties['g']['UserName'])
    userid = str(gproperties['g']['UserID'])
    appkey = str(gproperties['g']['AppKey'])
    RegisteredDevices = []
    for rd in gproperties['g']['RegisteredDevices']:
        RegisteredDevices.append(rd)
    #print("g",RegisteredDevices)
    graph.SignedInUser = TUser(UserID=userid,UserName= username, AppKey=appkey, RegisteredDevices=RegisteredDevices)
    sp_dict = dict()
    for key in gproperties['g']['sp_Keys']:
        sp_dict[key] = str(gproperties['g'][key])
    graph.ScratchPad = sp_dict
    return graph


def to_tnode(_node):
    node = TNode()
    properties = dict(_node)
    #print(properties)
    node.SubjectSpecializationOf = set(_node.labels)
    node.Neo4jID = str(_node.id)
    node.AoKID = set(properties['AoKID'])
    node.GraphID=set(properties['GraphID'])
    node.NameLabels=set(properties['NameLabels'])
    node.AbstractionLevel = properties['AbstractionLevel']
    node.AgeInMilliseconds = properties['AgeInMilliseconds']
    node.AttentionLevel = properties['AttentionLevel']
    #node.Value = str(properties['Value'])
    node.Validity = properties['Validity']
    #node.Tag = properties['Tag']
    node.Evaluation = properties['Evaluation']
    #node.ProcessingTag = properties['ProcessingTag']
    node.SystemLevelType = properties['SystemLevelType']
    node.DateTimeStamp=properties['DateTimeStamp']
   # node.SignedInUser=properties['SignedInUser']
    node.HasUserCreatedTheNode=properties['HasUserCreatedTheNode']
    username = str(properties['UserName'])
    userid = str(properties['UserID'])
    appkey = str(properties['AppKey'])
    RegisteredDevices=[]
    for rd in properties['RegisteredDevices']:
        #print("n",rd)
        RegisteredDevices.append(str(rd))
    #print("n",RegisteredDevices)
    node.SignedInUser = TUser(UserID=userid, UserName=username, AppKey=appkey, RegisteredDevices=RegisteredDevices)
    tv_dict = dict()
    for key in properties['tv_Keys']:
        tv_dict[key] = properties[key]
    node.TruthValue = tv_dict
    sp_dict = dict()
    for key in properties['sp_Keys']:
        sp_dict[key] = properties[key]
    node.ScratchPad = sp_dict
    type_dict = dict()
    for key in properties['type_Keys']:
        type_dict[key] = properties[key]
    node.Type = type_dict
    #domains = list()
    #node.Domains = set(properties['Domains'])
   # print(node.Domains)
    return node

''''
def to_memoryChunk(response):
    memory_chunk = TMemoryChunk()
    properties = dict(response)
    memory_chunk.Neo4jID = str(response.id)
    memory_chunk.ID = str(response.id)
    #    memory_chunk.Graph = properties['Graph']
    memory_chunk.Capacity = properties['Capacity']
    memory_chunk.TimeStamp = properties['TimeStamp']
    memory_chunk.DecayLevel = properties['DecayLevel']
    memory_chunk.AttentionLevel = properties['AttentionLevel']
    memory_chunk.Evaluation = properties['Evaluation']
    memory_chunk.Importance = properties['Importance']
    return memory_chunk

'''
def merge_node(t_node):
    query = "Merge (n"
    for label in t_node.node.Labels:
        query += ":{label}".format(label=label)
    query += " {AoKID:" + t_node.node.AoKID + ", Value:" + t_node.node.Value + ", SystemLevelType:" + t_node.node.SystemLevelType + ", AbstractionLevel:" + t_node.node.AbstractionLevel + ", Tag:" + t_node.node.Tag + ", Validity:" + t_node.node.Validity + ", ProcessingTag:" + t_node.node.ProcessingTag + ", Evaluation:" + t_node.node.Evaluation + ", DateTimeStamp:" + t_node.node.DateTimeStamp + ", AgeInMilliseconds:" + t_node.node.AgeInMilliseconds + ", AttentionLevel:" + t_node.node.AttentionLevel
    for key, value in zip(t_node.node.TruthValue.keys(), t_node.node.TruthValue.values()):
        # print(key, value)
        query += ", TV_" + key + ":" + value
    query += "})"
    return query
