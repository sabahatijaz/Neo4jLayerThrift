#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#
import csv
import sys
import glob

sys.path.append('genpy')

from genpy.niha_thrift.TGSpace import *
from genpy.niha_thrift.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import pandas as pd

def Reverse(lst):
    lst.reverse()
    return lst
def main():
    # Make socket
    global ebayid
    transport = TSocket.TSocket('localhost', 9092)  # 116.58.56.42

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Client(protocol)

    # Connect!
    transport.open()

    # TS = TESystemLevelType.STRING
    # TA = TEAbstractionLevel.INSTANCE_NODE
    # SU = TUser(UserID="1", UserName="Sabahat", AppKey="123", RegisteredDevices=['Neo4Niha'])
    # Node1 = TNode(AoKID="5", GraphID="1", SubjectSpecializationOf=special1,
    #                     NameLabels={special1[0]}, SystemLevelType=TS, AbstractionLevel=TA,
    #                     Validity='Not > 20', TruthValue={'Key1': 1234.0, 'Key2': 125.0}, Evaluation=0.0,
    #                     DateTimeStamp="10 April", AttentionLevel=1.0, AgeInMilliseconds=0,
    #                     HasUserCreatedTheNode=True, ScratchPad={'EbayID': "Null"},
    #                     Type={"isA": ['isA', 'Dictionary'], "hasA": ["hasA", "Dictionary"],
    #                         "Product": ["Product", "RetailItem", "Description"]}, SignedInUser=SU)
    #
    # Node2 = TNode(AoKID="5", GraphID="1", SubjectSpecializationOf=special2,
    #                           NameLabels={special2[0]}, SystemLevelType=TS, AbstractionLevel=TA,
    #                           Validity='Not > 20', TruthValue={'Key1': 1234.0, 'Key2': 125.0}, Evaluation=0.0,
    #                           DateTimeStamp="10 April", AttentionLevel=1.0, AgeInMilliseconds=0,
    #                           HasUserCreatedTheNode=True, ScratchPad={'EbayID': ebayid},
    #                           Type={"isA": ['isA', 'Dictionary'], "hasA": ["hasA", "Dictionary"],
    #                                 "Product": ["Product", "RetailItem", "Description"]}, SignedInUser=SU)
    #             # print(Node1)
    #             # print(Node2)
    #             rel = TRelation(GraphID={"1"}, AoKID={"7"}, SubjectSpecializationOf={"has_category"},
    #                             NameLabels={"Win", "Windows", "MS_WIN", "MS_Windows"},
    #                             RelationType="Rel", SourceNode=Node1, TargetNode=Node2, AttentionLevel=0.0,
    #                             TruthValue={'Key1': 1234.0, 'Key2': 125.0},
    #                             ScratchPad={'OS': 'Operating_System', 'RAM': 'Memory'},
    #                             DateTimeStamp="10 April", AgeInMilliseconds=0, HasUserCreatedTheRelation=True,
    #                             Type={"isA", "hasA",
    #                                   "Product"}, SignedInUser=SU)
    #
    #             rel2 = TRelation(GraphID={"1"}, AoKID={"7"}, SubjectSpecializationOf={"subcategory_of"},
    #                              NameLabels={"Win", "Windows", "MS_WIN", "MS_Windows"},
    #                              RelationType="Rel", SourceNode=Node2, TargetNode=Node1, AttentionLevel=0.0,
    #                              TruthValue={'Key1': 1234.0, 'Key2': 125.0},
    #                              ScratchPad={'OS': 'Operating_System', 'RAM': 'Memory'},
    #                              DateTimeStamp="10 April", AgeInMilliseconds=0, HasUserCreatedTheRelation=True,
    #                              Type={"isA", "hasA",
    #                                    "Product"}, SignedInUser=SU)
                # TR = TERepresentationType.SEMANTIC_NETWORK
                # graph = TGraph(GraphID="1", AoKID={"8"}, SubjectSpecializationOf={"Computer", "Electronics"},
                #                NameLabels={"Win", "Windows", "MS_WIN", "MS_Windows"}, Relations={'relation': rel},
                #                RepresentationType=TR, Type={"isA", "hasA",
                #                                             "Product"}, ScratchPad={'OS': 'Operating_System', 'RAM': 'Memory'},
                #                DateTimeStamp="10 April", AgeInMilliseconds=0, HasUserCreatedTheGraph=True, SignedInUser=SU)
                # response1 = client.CreateGraph(graph)
                # print("response : ", response1)
                # response1 = client.RetrieveGraphs("MATCH(g) where g.nodetype='Graph' return g")
                # print("response : ", response1)
                # response1 = client.RetrieveGraphsByAnySubjectSpecializationOf("Computer", 10)
                # print("response : ", response1)
                # response1 = client.RetrieveGraphsByAnyNameLabels({"MS_WIN"}, 10)
                # print("response : ", response1)
                # response1 = client.RetrieveGraphsByTypes({"isA"}, 10)
                # print("response : ", response1)
                # response1 = client.GetGraphByTypeAndSpecialization("isA", "Computer", 10)
                # print("response : ", response1)
                # response1 = client.GetGraphByTypeAndSpecialization("isA", "Computer", 10)
                # print("response : ", response1)

                # response1 = client.CreateRelation(rel)
                # print("response : ", response1)
                # response1 = client.CreateRelation(rel2)
                # print("response : ", response1)
                # print("####################################################")
                #
                # # response1 = client.RetrieveRelationsByGraphID('1', 10)
                # # print("response : ", response1)
                # # response1 = client.RetrieveRelationsNameLabels("Win", 2)
                # # print("response : ", response1)
    response1 = client.RetrieveRelationsUniqueListOfAllSpecializationLabels(10)  # should return list string
    print("response : ", response1)
                #
                # # response1 = client.CreateNodes(Node1)
                # # print("response : ", response1)
                # # response2 = client.CreateNodes(Node2)
                # # print("response : ", response2)
    response = client.RetrieveNodes("MATCH(n) where n.nodetype='Node' RETURN n")
    print(response)
                # # response = client.RetrieveNodesByAnySubjectSpecializationOf("Electronics", 1)
                # # print(response)
                # # response = client.RetrieveNodesByAnyNameLabels("Win", 2)
                # # print(response)
    response = client.RetriveNodesUniqueListOfAllSpecializationLabels(-1)
    print(response)
                #


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
