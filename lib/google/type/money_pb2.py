# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/money.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/type/money.proto',
  package='google.type',
  syntax='proto3',
  serialized_options=_b('\n\017com.google.typeB\nMoneyProtoP\001Z6google.golang.org/genproto/googleapis/type/money;money\370\001\001\242\002\003GTP'),
  serialized_pb=_b('\n\x17google/type/money.proto\x12\x0bgoogle.type\"<\n\x05Money\x12\x15\n\rcurrency_code\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\x03\x12\r\n\x05nanos\x18\x03 \x01(\x05\x42`\n\x0f\x63om.google.typeB\nMoneyProtoP\x01Z6google.golang.org/genproto/googleapis/type/money;money\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3')
)




_MONEY = _descriptor.Descriptor(
  name='Money',
  full_name='google.type.Money',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.type.Money.currency_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='google.type.Money.units', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nanos', full_name='google.type.Money.nanos', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['Money'] = _MONEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Money = _reflection.GeneratedProtocolMessageType('Money', (_message.Message,), dict(
  DESCRIPTOR = _MONEY,
  __module__ = 'google.type.money_pb2'
  # @@protoc_insertion_point(class_scope:google.type.Money)
  ))
_sym_db.RegisterMessage(Money)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
