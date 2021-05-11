namespace csharp NiHAThrift
namespace py niha_thrift


enum TESystemLevelType {
    INT16,  
    INT32, 
    INT64,
    DOUBLE,
    BOOL,
    STRING,
    DATETIME,
    IMAGE,
    AUDIO,
    VIDEO,
    GRAPH,
    DATAFILE,
    DATASOURCE
}   

enum TEAbstractionLevel
{
    SEMANTIC_NODE,
    CONCEPT_NODE,
    INSTANCE_NODE,
}

enum TERepresentationType
{
    SEMANTIC_NETWORK,
    CONCEPTUAL_GRAPH
}



struct TUser
{
    1: string UserID;
    2: string UserName;
    3: string AppKey;
    4: list<string> RegisteredDevices
}

struct TEndPoint
{
    1: required string Host;
    2: required i32 Port;
    3: required string NodeName;
}

enum TESiginStatus
{
    SIGNIN_SUCCESSFUL,
    SIGNIN_NOT_SUCCESSFUL,
    SIGNOUT_SUCCESSFUL,
    SIGNOUT_NOT_SUCCESSFUL,
}

//post demo 1
//ATV, Side-by-Side & UTV Parts & Accessories https://www.ebay.com/b/ATV-Side-by-Side-UTV-Parts-

//SubjectSpecializationOf=link:ATV__Side-by-Side__UTV__arts__Accessories:MenWear
//nameLabel = ATV__Side-by-Side__UTV__arts__Accessories, ATV, Side-By-Side, UTV,ARTS, Accessories
//ScratchPad = ["link", https://www.ebay.com/b/ATV-Side-by-Side-UTV-Parts-]

struct TNode
{
    //CREATE (node:label1:label2:label3...{ key1: value, key2: value, . . . . . . . . .  })
    1: string Neo4jID; 
    2: required set<string> GraphID;
    3: required set<string> AoKID;//as property
    4: required list<string> SubjectSpecializationOf; //OS:Computer:Electronics:Product:Object
    5: required set<string> NameLabels; //as property label and akas, Windows,Win,MS_Win,MS_Windows,Micorsoft_Windows
    6: required TESystemLevelType SystemLevelType;//as property, example 'SystemType:INT16' as enum number value
    7: required TEAbstractionLevel AbstractionLevel;//
    8: string Validity;//as property, example 'validity: Not > 20'
    9: map<string, double> TruthValue;//as property
    10: double Evaluation;//as property
    11: string DateTimeStamp; //as property
    12: i64 AgeInMilliseconds;//as property
    13: double AttentionLevel;
    14: map<string, string> ScratchPad;
    15: TUser SignedInUser;  //input
    16: bool HasUserCreatedTheNode;
    17: map<string, set<string>> Type;  // key: "isA", value:[isA, Dictionary]
                                        // key: "hasA", value:[hasA, Dictionary]
                                        // key: "Product", value:[Product, RetailItem, Description]
}



enum TEGraphComponent
{
    Node,
    Relation,
    Graph
}

struct TRelation
{
    1: string Neo4jID; 
    2: required set<string> GraphID;
    3: required set<string> AoKID;
    4: required list<string> SubjectSpecializationOf;
    5: required set<string> NameLabels; 
    6: string RelationType; 
    7: TNode SourceNode;
    8: TNode TargetNode;
    9: double AttentionLevel;
    10: map<string, double> TruthValue;//as property
    11: map<string, string> ScratchPad;
    12: string DateTimeStamp; //as property
    13: i64 AgeInMilliseconds;//as property
    14: TUser SignedInUser;
    15: bool HasUserCreatedTheRelation;
    16: set<string> Type;
}

struct TGraph
{
    1: string Neo4jID; 
    2: required string GraphID;
    3: required set<string> AoKID;
    4: required list<string> SubjectSpecializationOf; //Laptop:Computers
    5: required set<string> NameLabels; 
    6: map<string, TNode> Nodes;
    7: map<string, TRelation> Relations;
    8: TERepresentationType RepresentationType;
    9: set<string> Type;//example: IsA, Dictionary
    10: map<string, string> ScratchPad;
    11: string DateTimeStamp; //as property
    12: i64 AgeInMilliseconds;//as property
    13: TUser SignedInUser;
    14: bool HasUserCreatedTheGraph;
}

service TGSpace
{
    i32 GetFrequency();
    i32 GetFrequencyByUser(1: TUser user);

    TESiginStatus SignIn(1: TUser user, 2: string Password);
    TESiginStatus SignOut(1: TUser user);
    void Ping();        //1- Just an empty function

    string CreateGraph(1: TGraph graph); //1- //it should return id //Done
    bool UpdateGraph(1: TGraph graph); //Done
    bool DeleteGraph(1: string criteria); //Done
    list<TGraph> RetrieveGraphs(1: string query);//1- //if limits is neg then no limit is assign
    TGraph RetrieveGraphByGraphID(1: string graphid, 2: i32 limit); //Done
    list<TGraph> RetrieveGraphsByAoKID(1: string id, 2: i32 limit); //applies to both nodes and relations
    
    list<TGraph> RetrieveGraphsByAllSubjectSpecializationOf(1: string criteria, 2: i32 limit);
    list<TGraph> RetrieveGraphsByAnySubjectSpecializationOf(1: string criteria, 2: i32 limit);//1-
    
    list<TGraph> RetrieveGraphsByAllNameLabels(1: set<string> criteria,2: i32 limit);
    list<TGraph> RetrieveGraphsByAnyNameLabels(1: set<string> criteria,2: i32 limit);//1-
    
    list<TGraph> RetrieveGraphsByTypes(1: set<string> types,2: i32 limit);//1-
    list<TGraph> RetrieveGraphsByTypeAndName(1: string type, 2: string name, 3: i32 limit);//([dictionary, isa], Laptop)
    list<TGraph> GetGraphByTypeAndSpecialization(1: string type, 2: string specialization_criteria, 3: i32 limit);//1- //alias for RetrieveGraphBySpecializationOf

    list<TGraph> RetrieveGraphsCreatedByNiHA(1: i32 limit);
    list<TGraph> RetrieveGraphsCreatedByNiHAWithUser(1: string when_this_user_was_signedin,2: i32 limit);
    list<TGraph> RetrieveGraphsCreatedByNiHAWithCriteria(1: string criteria,2: i32 limit);
    list<string> RetriveGraphsUniqueListOfAllSubjectSpecializationLabels(1: i32 limit);



    map<string, string> CreateRelation(1: TRelation relations); //1- //return list rid, sid, tid
    string CreateRelationWithNodes(1: TNode source_node, 2: TNode target_node);
    bool UpdateRelation(1: TRelation relation);
    bool DeleteRelation(1: string criteria);
    TRelation RetrieveRelationByNeo4jId(1: string id, 2: i32 limit);
    list<TRelation> RetrieveRelations(1: string criteria, 2: i32 limit);
    list<TRelation> RetrieveRelationsByGraphID(1: string graphid, 2: i32 limit); //1-
    list<TRelation> RetrieveRelationsByAoKID(1: string id, 2: i32 limit); //applies to both nodes and relations
    list<TRelation> RetrieveRelationsBySpecializationOf(1: string subject_specialization, 2: i32 limit); 
    list<TRelation> RetrieveRelationsNameLabels(1: string criteria, 2: i32 limit); //1-
    list<TRelation> RetrieveRelationsTruthValue(1: string criteria, 2: i32 limit);
    list<TRelation> RetrieveRelationsByDateTime(1: string criteria, 2: i32 limit);
    list<TRelation> RetrieveRelationsByAge(1: string criteria, 2: i32 limit);
    list<TRelation> RetrieveRelationsAttentionLevel(1: string criteria, 2: i32 limit);
    list<TRelation> RetrieveRelationsScratchPad(1: string criteria, 2: i32 limit);
    list<TRelation> RetrieveRelationsByUser(1: string userid, 2: i32 limit);
    list<TRelation> RetrieveRelationsCreateByUser(1: string userid, 2: i32 limit);
    list<TRelation> RetrieveRelationsCreatedByNiHA(1: i32 limit);
    list<TRelation> RetrieveRelationsCreatedByNiHAWithUser(1: string when_this_user_was_signedin, 2: i32 limit);
    list<TRelation> RetrieveRelationsCreatedByNiHAWithCriteria(1: string criteria, 2: i32 limit);
    list<string> RetrieveRelationsUniqueListOfAllSpecializationLabels(1: i32 limit); //1-  //list string




    string CreateNodes(1: TNode node);//1- //return neojid
    TNode RetrieveByNeo4jId(1: string id);
    list<TNode> RetrieveNodes(1: string query); //1-
    list<TNode> RetrieveNodesByGraphID(1: string graphid, 2: i32 limit);
    list<TNode> RetrieveNodesByAoKID(1: string id, 2: i32 limit); //applies to both nodes and relations

    list<TNode> RetrieveNodesByAllSubjectSpecializationOf(1: string criteria, 2: i32 limit); 
    list<TNode> RetrieveNodesByAnySubjectSpecializationOf(1: string criteria, 2: i32 limit); //1-

    list<TNode> RetrieveNodesByAnyNameLabels(1: string criteria, 2: i32 limit); //1-
    list<TNode> RetrieveNodesByAllNameLabels(1: string criteria, 2: i32 limit);

    list<TNode> RetrieveNodesTruthValue(1: string criteria, 2: i32 limit);
    list<TNode> RetrieveNodesByEvaluation(1: string criteria,2: i32 limit);
    list<TNode> RetrieveNodesByDateTime(1: string criteria,2: i32 limit);
    list<TNode> RetrieveNodesByAge(1: string criteria,2: i32 limit);
    list<TNode> RetrieveNodesAttentionLevel(1: string criteria,2: i32 limit);
    list<TNode> RetrieveNodesByScratchPad(1: string criteria,2: i32 limit);
    list<TNode> RetrieveNodesByUser(1: string userid,2: i32 limit);
    list<TNode> RetrieveNodesCreateByUser(1: string userid,2: i32 limit);
    
    list<TNode> RetrieveNodesCreatedByNiHA(1: i32 limit);
    list<TNode> RetrieveNodesCreatedByNiHAWithUser(1: string when_this_user_was_signedin,2: i32 limit);
    list<TNode> RetrieveNodesCreatedByNiHAWithCriteria(1: string criteria,2: i32 limit);
    list<string> RetriveNodesUniqueListOfAllSpecializationLabels(1: i32 limit); //1-
    bool UpdateNode(1: TNode node);//, 2: string neo4Id);
    bool DeleteNode(1: string criteria);//
}

