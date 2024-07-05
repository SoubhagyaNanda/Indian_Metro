# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c2c.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='c2c.proto',
  package='de.tu_darmstadt.seemoo.nfcgate.network.c2c',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tc2c.proto\x12*de.tu_darmstadt.seemoo.nfcgate.network.c2c\"\x9f\x02\n\x07NFCData\x12S\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0e\x32>.de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.DataSource\x12O\n\tdata_type\x18\x02 \x01(\x0e\x32<.de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.DataType\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\"\n\nDataSource\x12\n\n\x06READER\x10\x00\x12\x08\n\x04\x43\x41RD\x10\x01\")\n\x08\x44\x61taType\x12\x0b\n\x07INITIAL\x10\x00\x12\x10\n\x0c\x43ONTINUATION\x10\x01\x62\x06proto3'
)



_NFCDATA_DATASOURCE = _descriptor.EnumDescriptor(
  name='DataSource',
  full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.DataSource',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=268,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_NFCDATA_DATASOURCE)

_NFCDATA_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.DataType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INITIAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONTINUATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=304,
  serialized_end=345,
)
_sym_db.RegisterEnumDescriptor(_NFCDATA_DATATYPE)


_NFCDATA = _descriptor.Descriptor(
  name='NFCData',
  full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_source', full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.data_source', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.timestamp', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData.data', index=3,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NFCDATA_DATASOURCE,
    _NFCDATA_DATATYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=345,
)

_NFCDATA.fields_by_name['data_source'].enum_type = _NFCDATA_DATASOURCE
_NFCDATA.fields_by_name['data_type'].enum_type = _NFCDATA_DATATYPE
_NFCDATA_DATASOURCE.containing_type = _NFCDATA
_NFCDATA_DATATYPE.containing_type = _NFCDATA
DESCRIPTOR.message_types_by_name['NFCData'] = _NFCDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NFCData = _reflection.GeneratedProtocolMessageType('NFCData', (_message.Message,), {
  'DESCRIPTOR' : _NFCDATA,
  '__module__' : 'c2c_pb2'
  # @@protoc_insertion_point(class_scope:de.tu_darmstadt.seemoo.nfcgate.network.c2c.NFCData)
  })
_sym_db.RegisterMessage(NFCData)


# @@protoc_insertion_point(module_scope)
