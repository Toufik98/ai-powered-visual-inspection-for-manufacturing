# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rgb_image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rgb_image.proto',
  package='ai_powered_visual_inspection_for_manifacturing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0frgb_image.proto\x12.ai_powered_visual_inspection_for_manifacturing\"G\n\tRGB_image\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05image\x18\x04 \x01(\t\".\n\x0fPredicted_label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t2\x97\x01\n\rPredict_label\x12\x85\x01\n\x07Predict\x12\x39.ai_powered_visual_inspection_for_manifacturing.RGB_image\x1a?.ai_powered_visual_inspection_for_manifacturing.Predicted_labelb\x06proto3'
)




_RGB_IMAGE = _descriptor.Descriptor(
  name='RGB_image',
  full_name='ai_powered_visual_inspection_for_manifacturing.RGB_image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ai_powered_visual_inspection_for_manifacturing.RGB_image.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='ai_powered_visual_inspection_for_manifacturing.RGB_image.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='ai_powered_visual_inspection_for_manifacturing.RGB_image.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='ai_powered_visual_inspection_for_manifacturing.RGB_image.image', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=67,
  serialized_end=138,
)


_PREDICTED_LABEL = _descriptor.Descriptor(
  name='Predicted_label',
  full_name='ai_powered_visual_inspection_for_manifacturing.Predicted_label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ai_powered_visual_inspection_for_manifacturing.Predicted_label.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='ai_powered_visual_inspection_for_manifacturing.Predicted_label.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=140,
  serialized_end=186,
)

DESCRIPTOR.message_types_by_name['RGB_image'] = _RGB_IMAGE
DESCRIPTOR.message_types_by_name['Predicted_label'] = _PREDICTED_LABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RGB_image = _reflection.GeneratedProtocolMessageType('RGB_image', (_message.Message,), {
  'DESCRIPTOR' : _RGB_IMAGE,
  '__module__' : 'rgb_image_pb2'
  # @@protoc_insertion_point(class_scope:ai_powered_visual_inspection_for_manifacturing.RGB_image)
  })
_sym_db.RegisterMessage(RGB_image)

Predicted_label = _reflection.GeneratedProtocolMessageType('Predicted_label', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTED_LABEL,
  '__module__' : 'rgb_image_pb2'
  # @@protoc_insertion_point(class_scope:ai_powered_visual_inspection_for_manifacturing.Predicted_label)
  })
_sym_db.RegisterMessage(Predicted_label)



_PREDICT_LABEL = _descriptor.ServiceDescriptor(
  name='Predict_label',
  full_name='ai_powered_visual_inspection_for_manifacturing.Predict_label',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=189,
  serialized_end=340,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='ai_powered_visual_inspection_for_manifacturing.Predict_label.Predict',
    index=0,
    containing_service=None,
    input_type=_RGB_IMAGE,
    output_type=_PREDICTED_LABEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICT_LABEL)

DESCRIPTOR.services_by_name['Predict_label'] = _PREDICT_LABEL

# @@protoc_insertion_point(module_scope)
