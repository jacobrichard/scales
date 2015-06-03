#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from test.gen_py.fb303 import ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ResultCode(object):
  OK = 0
  TRY_LATER = 1

  _VALUES_TO_NAMES = {
    0: "OK",
    1: "TRY_LATER",
  }

  _NAMES_TO_VALUES = {
    "OK": 0,
    "TRY_LATER": 1,
  }


class LogEntry(object):
  """
  Attributes:
   - category
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.UTF8, 'category', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
  )

  def __init__(self, category=None, message=None,):
    self.category = category
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.UTF8:
          self.category = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LogEntry')
    if self.category is not None:
      oprot.writeFieldBegin('category', TType.UTF8, 1)
      oprot.writeString(self.category.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

  def iteritems(self):
    return self.__dict__.iteritems()

  def __getitem__(self, key):
    return self.__dict__[key]

  def __setitem__(self, key, value):
    self.__dict__[key] = value
