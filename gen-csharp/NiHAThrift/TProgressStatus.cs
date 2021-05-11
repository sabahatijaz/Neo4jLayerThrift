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
  public partial class TProgressStatus : TBase
  {
    private string _Source;
    private string _Status;
    private double _Progress;

    public string Source
    {
      get
      {
        return _Source;
      }
      set
      {
        __isset.Source = true;
        this._Source = value;
      }
    }

    public string Status
    {
      get
      {
        return _Status;
      }
      set
      {
        __isset.Status = true;
        this._Status = value;
      }
    }

    public double Progress
    {
      get
      {
        return _Progress;
      }
      set
      {
        __isset.Progress = true;
        this._Progress = value;
      }
    }


    public Isset __isset;
    #if !SILVERLIGHT
    [Serializable]
    #endif
    public struct Isset {
      public bool Source;
      public bool Status;
      public bool Progress;
    }

    public TProgressStatus() {
    }

    public void Read (TProtocol iprot)
    {
      iprot.IncrementRecursionDepth();
      try
      {
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
                Source = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 2:
              if (field.Type == TType.String) {
                Status = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 3:
              if (field.Type == TType.Double) {
                Progress = iprot.ReadDouble();
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
        TStruct struc = new TStruct("TProgressStatus");
        oprot.WriteStructBegin(struc);
        TField field = new TField();
        if (Source != null && __isset.Source) {
          field.Name = "Source";
          field.Type = TType.String;
          field.ID = 1;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Source);
          oprot.WriteFieldEnd();
        }
        if (Status != null && __isset.Status) {
          field.Name = "Status";
          field.Type = TType.String;
          field.ID = 2;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(Status);
          oprot.WriteFieldEnd();
        }
        if (__isset.Progress) {
          field.Name = "Progress";
          field.Type = TType.Double;
          field.ID = 3;
          oprot.WriteFieldBegin(field);
          oprot.WriteDouble(Progress);
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
      StringBuilder __sb = new StringBuilder("TProgressStatus(");
      bool __first = true;
      if (Source != null && __isset.Source) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Source: ");
        __sb.Append(Source);
      }
      if (Status != null && __isset.Status) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Status: ");
        __sb.Append(Status);
      }
      if (__isset.Progress) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("Progress: ");
        __sb.Append(Progress);
      }
      __sb.Append(")");
      return __sb.ToString();
    }

  }

}