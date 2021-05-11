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
  public partial class TJob : TBase
  {
    private string _Neo4jID;
    private TJobType _JobType;
    private string _JobID;

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

    public TJobType JobType
    {
      get
      {
        return _JobType;
      }
      set
      {
        __isset.JobType = true;
        this._JobType = value;
      }
    }

    public string JobID
    {
      get
      {
        return _JobID;
      }
      set
      {
        __isset.JobID = true;
        this._JobID = value;
      }
    }

    public string ScheduledDateTime { get; set; }

    public string DueDateTime { get; set; }

    public short PriorityLevel { get; set; }


    public Isset __isset;
    #if !SILVERLIGHT
    [Serializable]
    #endif
    public struct Isset {
      public bool Neo4jID;
      public bool JobType;
      public bool JobID;
    }

    public TJob() {
    }

    public TJob(string ScheduledDateTime, string DueDateTime, short PriorityLevel) : this() {
      this.ScheduledDateTime = ScheduledDateTime;
      this.DueDateTime = DueDateTime;
      this.PriorityLevel = PriorityLevel;
    }

    public void Read (TProtocol iprot)
    {
      iprot.IncrementRecursionDepth();
      try
      {
        bool isset_ScheduledDateTime = false;
        bool isset_DueDateTime = false;
        bool isset_PriorityLevel = false;
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
              if (field.Type == TType.Struct) {
                JobType = new TJobType();
                JobType.Read(iprot);
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 3:
              if (field.Type == TType.String) {
                JobID = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 4:
              if (field.Type == TType.String) {
                ScheduledDateTime = iprot.ReadString();
                isset_ScheduledDateTime = true;
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 5:
              if (field.Type == TType.String) {
                DueDateTime = iprot.ReadString();
                isset_DueDateTime = true;
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 6:
              if (field.Type == TType.I16) {
                PriorityLevel = iprot.ReadI16();
                isset_PriorityLevel = true;
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
        if (!isset_ScheduledDateTime)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field ScheduledDateTime not set");
        if (!isset_DueDateTime)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field DueDateTime not set");
        if (!isset_PriorityLevel)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field PriorityLevel not set");
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
        TStruct struc = new TStruct("TJob");
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
        if (JobType != null && __isset.JobType) {
          field.Name = "JobType";
          field.Type = TType.Struct;
          field.ID = 2;
          oprot.WriteFieldBegin(field);
          JobType.Write(oprot);
          oprot.WriteFieldEnd();
        }
        if (JobID != null && __isset.JobID) {
          field.Name = "JobID";
          field.Type = TType.String;
          field.ID = 3;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(JobID);
          oprot.WriteFieldEnd();
        }
        if (ScheduledDateTime == null)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field ScheduledDateTime not set");
        field.Name = "ScheduledDateTime";
        field.Type = TType.String;
        field.ID = 4;
        oprot.WriteFieldBegin(field);
        oprot.WriteString(ScheduledDateTime);
        oprot.WriteFieldEnd();
        if (DueDateTime == null)
          throw new TProtocolException(TProtocolException.INVALID_DATA, "required field DueDateTime not set");
        field.Name = "DueDateTime";
        field.Type = TType.String;
        field.ID = 5;
        oprot.WriteFieldBegin(field);
        oprot.WriteString(DueDateTime);
        oprot.WriteFieldEnd();
        field.Name = "PriorityLevel";
        field.Type = TType.I16;
        field.ID = 6;
        oprot.WriteFieldBegin(field);
        oprot.WriteI16(PriorityLevel);
        oprot.WriteFieldEnd();
        oprot.WriteFieldStop();
        oprot.WriteStructEnd();
      }
      finally
      {
        oprot.DecrementRecursionDepth();
      }
    }

    public override string ToString() {
      StringBuilder __sb = new StringBuilder("TJob(");
      bool __first = true;
      if (Neo4jID != null && __isset.Neo4jID) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Neo4jID: ");
        __sb.Append(Neo4jID);
      }
      if (JobType != null && __isset.JobType) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("JobType: ");
        __sb.Append(JobType== null ? "<null>" : JobType.ToString());
      }
      if (JobID != null && __isset.JobID) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("JobID: ");
        __sb.Append(JobID);
      }
      if(!__first) { __sb.Append(", "); }
      __sb.Append("ScheduledDateTime: ");
      __sb.Append(ScheduledDateTime);
      __sb.Append(", DueDateTime: ");
      __sb.Append(DueDateTime);
      __sb.Append(", PriorityLevel: ");
      __sb.Append(PriorityLevel);
      __sb.Append(")");
      return __sb.ToString();
    }

  }

}
