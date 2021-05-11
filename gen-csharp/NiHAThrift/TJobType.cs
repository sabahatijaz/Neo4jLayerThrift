/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using Thrift;
using Thrift.Collections;
using System.Runtime.Serialization;
using Thrift.Protocol;
using Thrift.Transport;

namespace NiHAThrift
{

  #if !SILVERLIGHT
  [Serializable]
  #endif
  public partial class TJobType : TBase
  {
    private string _Neo4jID;
    private THashSet<TFile> _Attachments;
    private THashSet<string> _CodeletsToBeUsed;
    private THashSet<string> _SensorsToBeUsed;
    private THashSet<string> _ActuatorsToBeUsed;

    public string Neo4jID
    {
      get
      {
        return _Neo4jID;
      }
      set
      {
        __isset.Neo4jID = true;
        this._Neo4jID = value;
      }
    }

    public string Name { get; set; }

    public THashSet<TFile> Attachments
    {
      get
      {
        return _Attachments;
      }
      set
      {
        __isset.Attachments = true;
        this._Attachments = value;
      }
    }

    public THashSet<string> CodeletsToBeUsed
    {
      get
      {
        return _CodeletsToBeUsed;
      }
      set
      {
        __isset.CodeletsToBeUsed = true;
        this._CodeletsToBeUsed = value;
      }
    }

    public THashSet<string> SensorsToBeUsed
    {
      get
      {
        return _SensorsToBeUsed;
      }
      set
      {
        __isset.SensorsToBeUsed = true;
        this._SensorsToBeUsed = value;
      }
    }

    public THashSet<string> ActuatorsToBeUsed
    {
      get
      {
        return _ActuatorsToBeUsed;
      }
      set
      {
        __isset.ActuatorsToBeUsed = true;
        this._ActuatorsToBeUsed = value;
      }
    }


    public Isset __isset;
    #if !SILVERLIGHT
    [Serializable]
    #endif
    public struct Isset {
      public bool Neo4jID;
      public bool Attachments;
      public bool CodeletsToBeUsed;
      public bool SensorsToBeUsed;
      public bool ActuatorsToBeUsed;
    }

    public TJobType() {
    }

    public TJobType(string Name) : this() {
      this.Name = Name;
    }

    public void Read (TProtocol iprot)
    {
      iprot.IncrementRecursionDepth();
      try
      {
        bool isset_Name = false;
        TField field;
        iprot.ReadStructBegin();
        while (true)
        {
          field = iprot.ReadFieldBegin();
          if (field.Type == TType.Stop) { 
            break;
          }
          switch (field.ID)
          {
            case 1:
              if (field.Type == TType.String) {
                Neo4jID = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 2:
              if (field.Type == TType.String) {
                Name = iprot.ReadString();
                isset_Name = true;
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 3:
              if (field.Type == TType.Set) {
                {
                  Attachments = new THashSet<TFile>();
                  TSet _set0 = iprot.ReadSetBegin();
                  for( int _i1 = 0; _i1 < _set0.Count; ++_i1)
                  {
                    TFile _elem2;
                    _elem2 = new TFile();
                    _elem2.Read(iprot);
                    Attachments.Add(_elem2);
                  }
                  iprot.ReadSetEnd();
                }
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 4:
              if (field.Type == TType.Set) {
                {
                  CodeletsToBeUsed = new THashSet<string>();
                  TSet _set3 = iprot.ReadSetBegin();
                  for( int _i4 = 0; _i4 < _set3.Count; ++_i4)
                  {
                    string _elem5;
                    _elem5 = iprot.ReadString();
                    CodeletsToBeUsed.Add(_elem5);
                  }
                  iprot.ReadSetEnd();
                }
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 5:
              if (field.Type == TType.Set) {
                {
                  SensorsToBeUsed = new THashSet<string>();
                  TSet _set6 = iprot.ReadSetBegin();
                  for( int _i7 = 0; _i7 < _set6.Count; ++_i7)
                  {
                    string _elem8;
                    _elem8 = iprot.ReadString();
                    SensorsToBeUsed.Add(_elem8);
                  }
                  iprot.ReadSetEnd();
                }
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 6:
              if (field.Type == TType.Set) {
                {
                  ActuatorsToBeUsed = new THashSet<string>();
                  TSet _set9 = iprot.ReadSetBegin();
                  for( int _i10 = 0; _i10 < _set9.Count; ++_i10)
                  {
                    string _elem11;
                    _elem11 = iprot.ReadString();
                    ActuatorsToBeUsed.Add(_elem11);
                  }
                  iprot.ReadSetEnd();
                }
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            default: 
              TProtocolUtil.Skip(iprot, field.Type);
              break;
          }
          iprot.ReadFieldEnd();
        }
        iprot.ReadStructEnd();
        if (!isset_Name)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field Name not set");
      }
      finally
      {
        iprot.DecrementRecursionDepth();
      }
    }

    public void Write(TProtocol oprot) {
      oprot.IncrementRecursionDepth();
      try
      {
        TStruct struc = new TStruct("TJobType");
        oprot.WriteStructBegin(struc);
        TField field = new TField();
        if (Neo4jID != null && __isset.Neo4jID) {
          field.Name = "Neo4jID";
          field.Type = TType.String;
          field.ID = 1;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Neo4jID);
          oprot.WriteFieldEnd();
        }
        if (Name == null)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field Name not set");
        field.Name = "Name";
        field.Type = TType.String;
        field.ID = 2;
        oprot.WriteFieldBegin(field);
        oprot.WriteString(Name);
        oprot.WriteFieldEnd();
        if (Attachments != null && __isset.Attachments) {
          field.Name = "Attachments";
          field.Type = TType.Set;
          field.ID = 3;
          oprot.WriteFieldBegin(field);
          {
            oprot.WriteSetBegin(new TSet(TType.Struct, Attachments.Count));
            foreach (TFile _iter12 in Attachments)
            {
              _iter12.Write(oprot);
            }
            oprot.WriteSetEnd();
          }
          oprot.WriteFieldEnd();
        }
        if (CodeletsToBeUsed != null && __isset.CodeletsToBeUsed) {
          field.Name = "CodeletsToBeUsed";
          field.Type = TType.Set;
          field.ID = 4;
          oprot.WriteFieldBegin(field);
          {
            oprot.WriteSetBegin(new TSet(TType.String, CodeletsToBeUsed.Count));
            foreach (string _iter13 in CodeletsToBeUsed)
            {
              oprot.WriteString(_iter13);
            }
            oprot.WriteSetEnd();
          }
          oprot.WriteFieldEnd();
        }
        if (SensorsToBeUsed != null && __isset.SensorsToBeUsed) {
          field.Name = "SensorsToBeUsed";
          field.Type = TType.Set;
          field.ID = 5;
          oprot.WriteFieldBegin(field);
          {
            oprot.WriteSetBegin(new TSet(TType.String, SensorsToBeUsed.Count));
            foreach (string _iter14 in SensorsToBeUsed)
            {
              oprot.WriteString(_iter14);
            }
            oprot.WriteSetEnd();
          }
          oprot.WriteFieldEnd();
        }
        if (ActuatorsToBeUsed != null && __isset.ActuatorsToBeUsed) {
          field.Name = "ActuatorsToBeUsed";
          field.Type = TType.Set;
          field.ID = 6;
          oprot.WriteFieldBegin(field);
          {
            oprot.WriteSetBegin(new TSet(TType.String, ActuatorsToBeUsed.Count));
            foreach (string _iter15 in ActuatorsToBeUsed)
            {
              oprot.WriteString(_iter15);
            }
            oprot.WriteSetEnd();
          }
          oprot.WriteFieldEnd();
        }
        oprot.WriteFieldStop();
        oprot.WriteStructEnd();
      }
      finally
      {
        oprot.DecrementRecursionDepth();
      }
    }

    public override string ToString() {
      StringBuilder __sb = new StringBuilder("TJobType(");
      bool __first = true;
      if (Neo4jID != null && __isset.Neo4jID) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Neo4jID: ");
        __sb.Append(Neo4jID);
      }
      if(!__first) { __sb.Append(", "); }
      __sb.Append("Name: ");
      __sb.Append(Name);
      if (Attachments != null && __isset.Attachments) {
        __sb.Append(", Attachments: ");
        __sb.Append(Attachments);
      }
      if (CodeletsToBeUsed != null && __isset.CodeletsToBeUsed) {
        __sb.Append(", CodeletsToBeUsed: ");
        __sb.Append(CodeletsToBeUsed);
      }
      if (SensorsToBeUsed != null && __isset.SensorsToBeUsed) {
        __sb.Append(", SensorsToBeUsed: ");
        __sb.Append(SensorsToBeUsed);
      }
      if (ActuatorsToBeUsed != null && __isset.ActuatorsToBeUsed) {
        __sb.Append(", ActuatorsToBeUsed: ");
        __sb.Append(ActuatorsToBeUsed);
      }
      __sb.Append(")");
      return __sb.ToString();
    }

  }

}