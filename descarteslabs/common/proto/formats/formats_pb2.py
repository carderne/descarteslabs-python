# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: descarteslabs/common/proto/formats/formats.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="descarteslabs/common/proto/formats/formats.proto",
    package="descarteslabs.workflows",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=(
        b"\n0descarteslabs/common/proto/formats/formats.proto\x12\x17\x64\x65scarteslabs.workflows\x1a"
        b' google/protobuf/descriptor.proto"\xef\x05\n\x06\x46ormat\x12W\n\x07pyarrow\x18\x01'
        b" \x01(\x0b\x32"
        b" .descarteslabs.workflows.PyarrowB\x1b\xd2\xc9\x01\x17\x61pplication/vnd.pyarrowR\x07pyarrow\x12G\n\x04json\x18\x02"
        b" \x01(\x0b\x32\x1d.descarteslabs.workflows.JSONB\x14\xd2\xc9\x01\x10\x61pplication/jsonR\x04json\x12T\n\x07geojson\x18\x03"
        b" \x01(\x0b\x32"
        b" .descarteslabs.workflows.GeoJSONB\x18\xd2\xc9\x01\x14\x61pplication/geo+jsonR\x07geojson\x12<\n\x03\x63sv\x18\x04"
        b" \x01(\x0b\x32\x1c.descarteslabs.workflows.CSVB\x0c\xd2\xc9\x01\x08text/csvR\x03\x63sv\x12=\n\x03png\x18\x05"
        b" \x01(\x0b\x32\x1c.descarteslabs.workflows.PNGB\r\xd2\xc9\x01\timage/pngR\x03png\x12J\n\x07geotiff\x18\x06"
        b" \x01(\x0b\x32"
        b" .descarteslabs.workflows.GeotiffB\x0e\xd2\xc9\x01\nimage/tiffR\x07geotiff\x12S\n\x07msgpack\x18\x07"
        b" \x01(\x0b\x32"
        b" .descarteslabs.workflows.MsgPackB\x17\xd2\xc9\x01\x13\x61pplication/msgpackR\x07msgpack\x12\x1f\n\x0bhas_pyarrow\x18\x14"
        b" \x01(\x08R\nhasPyarrow\x12\x19\n\x08has_json\x18\x15"
        b" \x01(\x08R\x07hasJson\x12\x1f\n\x0bhas_geojson\x18\x16"
        b" \x01(\x08R\nhasGeojson\x12\x17\n\x07has_csv\x18\x17"
        b" \x01(\x08R\x06hasCsv\x12\x17\n\x07has_png\x18\x18"
        b" \x01(\x08R\x06hasPng\x12\x1f\n\x0bhas_geotiff\x18\x19"
        b" \x01(\x08R\nhasGeotiff\x12\x1f\n\x0bhas_msgpack\x18\x1a"
        b' \x01(\x08R\nhasMsgpack"\xd5\x01\n\x07Pyarrow\x12U\n\x0b\x63ompression\x18\x01'
        b' \x01(\x0e\x32\x33.descarteslabs.workflows.Pyarrow.PyarrowCompressionR\x0b\x63ompression"s\n\x12PyarrowCompression\x12"\n\x1ePYARROWCOMPRESSION_UNSPECIFIED\x10\x00\x12\x1a\n\x16PYARROWCOMPRESSION_LZ4\x10\x01\x12\x1d\n\x19PYARROWCOMPRESSION_BROTLI\x10\x02"\x06\n\x04JSON"\t\n\x07GeoJSON"\x05\n\x03\x43SV"\x05\n\x03PNG"\x81\x05\n\x07Geotiff\x12#\n\rnot_overviews\x18\x01'
        b" \x01(\x08R\x0cnotOverviews\x12U\n\x0b\x63ompression\x18\x02"
        b" \x01(\x0e\x32\x33.descarteslabs.workflows.Geotiff.GeotiffCompressionR\x0b\x63ompression\x12h\n\x12overview_resampler\x18\x03"
        b' \x01(\x0e\x32\x39.descarteslabs.workflows.Geotiff.GeotiffOverviewResamplerR\x11overviewResampler"\x8e\x01\n\x12GeotiffCompression\x12"\n\x1eGEOTIFFCOMPRESSION_UNSPECIFIED\x10\x00\x12\x1a\n\x16GEOTIFFCOMPRESSION_LZW\x10\x01\x12\x1b\n\x17GEOTIFFCOMPRESSION_NONE\x10\x02\x12\x1b\n\x17GEOTIFFCOMPRESSION_JPEG\x10\x03"\xfe\x01\n\x18GeotiffOverviewResampler\x12(\n$GEOTIFFOVERVIEWRESAMPLER_UNSPECIFIED\x10\x00\x12$\n'
        b" GEOTIFFOVERVIEWRESAMPLER_NEAREST\x10\x01\x12$\n"
        b' GEOTIFFOVERVIEWRESAMPLER_AVERAGE\x10\x02\x12%\n!GEOTIFFOVERVIEWRESAMPLER_BILINEAR\x10\x03\x12"\n\x1eGEOTIFFOVERVIEWRESAMPLER_CUBIC\x10\x04\x12!\n\x1dGEOTIFFOVERVIEWRESAMPLER_MODE\x10\x05"\t\n\x07MsgPack::\n\x08mimetype\x12\x1d.google.protobuf.FieldOptions\x18\x9a\x19'
        b" \x01(\tR\x08mimetypeb\x06proto3"
    ),
    dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,],
)


MIMETYPE_FIELD_NUMBER = 3226
mimetype = _descriptor.FieldDescriptor(
    name="mimetype",
    full_name="descarteslabs.workflows.mimetype",
    index=0,
    number=3226,
    type=9,
    cpp_type=9,
    label=1,
    has_default_value=False,
    default_value=b"".decode("utf-8"),
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    json_name="mimetype",
    file=DESCRIPTOR,
)

_PYARROW_PYARROWCOMPRESSION = _descriptor.EnumDescriptor(
    name="PyarrowCompression",
    full_name="descarteslabs.workflows.Pyarrow.PyarrowCompression",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PYARROWCOMPRESSION_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PYARROWCOMPRESSION_LZ4",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PYARROWCOMPRESSION_BROTLI",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=964,
    serialized_end=1079,
)
_sym_db.RegisterEnumDescriptor(_PYARROW_PYARROWCOMPRESSION)

_GEOTIFF_GEOTIFFCOMPRESSION = _descriptor.EnumDescriptor(
    name="GeotiffCompression",
    full_name="descarteslabs.workflows.Geotiff.GeotiffCompression",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFCOMPRESSION_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFCOMPRESSION_LZW",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFCOMPRESSION_NONE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFCOMPRESSION_JPEG",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1357,
    serialized_end=1499,
)
_sym_db.RegisterEnumDescriptor(_GEOTIFF_GEOTIFFCOMPRESSION)

_GEOTIFF_GEOTIFFOVERVIEWRESAMPLER = _descriptor.EnumDescriptor(
    name="GeotiffOverviewResampler",
    full_name="descarteslabs.workflows.Geotiff.GeotiffOverviewResampler",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFOVERVIEWRESAMPLER_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFOVERVIEWRESAMPLER_NEAREST",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFOVERVIEWRESAMPLER_AVERAGE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFOVERVIEWRESAMPLER_BILINEAR",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFOVERVIEWRESAMPLER_CUBIC",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="GEOTIFFOVERVIEWRESAMPLER_MODE",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1502,
    serialized_end=1756,
)
_sym_db.RegisterEnumDescriptor(_GEOTIFF_GEOTIFFOVERVIEWRESAMPLER)


_FORMAT = _descriptor.Descriptor(
    name="Format",
    full_name="descarteslabs.workflows.Format",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="pyarrow",
            full_name="descarteslabs.workflows.Format.pyarrow",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\027application/vnd.pyarrow",
            json_name="pyarrow",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="json",
            full_name="descarteslabs.workflows.Format.json",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\020application/json",
            json_name="json",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="geojson",
            full_name="descarteslabs.workflows.Format.geojson",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\024application/geo+json",
            json_name="geojson",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="csv",
            full_name="descarteslabs.workflows.Format.csv",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\010text/csv",
            json_name="csv",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="png",
            full_name="descarteslabs.workflows.Format.png",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\timage/png",
            json_name="png",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="geotiff",
            full_name="descarteslabs.workflows.Format.geotiff",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\nimage/tiff",
            json_name="geotiff",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="msgpack",
            full_name="descarteslabs.workflows.Format.msgpack",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\322\311\001\023application/msgpack",
            json_name="msgpack",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_pyarrow",
            full_name="descarteslabs.workflows.Format.has_pyarrow",
            index=7,
            number=20,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasPyarrow",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_json",
            full_name="descarteslabs.workflows.Format.has_json",
            index=8,
            number=21,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasJson",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_geojson",
            full_name="descarteslabs.workflows.Format.has_geojson",
            index=9,
            number=22,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasGeojson",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_csv",
            full_name="descarteslabs.workflows.Format.has_csv",
            index=10,
            number=23,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasCsv",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_png",
            full_name="descarteslabs.workflows.Format.has_png",
            index=11,
            number=24,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasPng",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_geotiff",
            full_name="descarteslabs.workflows.Format.has_geotiff",
            index=12,
            number=25,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasGeotiff",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="has_msgpack",
            full_name="descarteslabs.workflows.Format.has_msgpack",
            index=13,
            number=26,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="hasMsgpack",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=112,
    serialized_end=863,
)


_PYARROW = _descriptor.Descriptor(
    name="Pyarrow",
    full_name="descarteslabs.workflows.Pyarrow",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="compression",
            full_name="descarteslabs.workflows.Pyarrow.compression",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="compression",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_PYARROW_PYARROWCOMPRESSION,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=866,
    serialized_end=1079,
)


_JSON = _descriptor.Descriptor(
    name="JSON",
    full_name="descarteslabs.workflows.JSON",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1081,
    serialized_end=1087,
)


_GEOJSON = _descriptor.Descriptor(
    name="GeoJSON",
    full_name="descarteslabs.workflows.GeoJSON",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1089,
    serialized_end=1098,
)


_CSV = _descriptor.Descriptor(
    name="CSV",
    full_name="descarteslabs.workflows.CSV",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1100,
    serialized_end=1105,
)


_PNG = _descriptor.Descriptor(
    name="PNG",
    full_name="descarteslabs.workflows.PNG",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1107,
    serialized_end=1112,
)


_GEOTIFF = _descriptor.Descriptor(
    name="Geotiff",
    full_name="descarteslabs.workflows.Geotiff",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="not_overviews",
            full_name="descarteslabs.workflows.Geotiff.not_overviews",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="notOverviews",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="compression",
            full_name="descarteslabs.workflows.Geotiff.compression",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="compression",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="overview_resampler",
            full_name="descarteslabs.workflows.Geotiff.overview_resampler",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            json_name="overviewResampler",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_GEOTIFF_GEOTIFFCOMPRESSION, _GEOTIFF_GEOTIFFOVERVIEWRESAMPLER,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1115,
    serialized_end=1756,
)


_MSGPACK = _descriptor.Descriptor(
    name="MsgPack",
    full_name="descarteslabs.workflows.MsgPack",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1758,
    serialized_end=1767,
)

_FORMAT.fields_by_name["pyarrow"].message_type = _PYARROW
_FORMAT.fields_by_name["json"].message_type = _JSON
_FORMAT.fields_by_name["geojson"].message_type = _GEOJSON
_FORMAT.fields_by_name["csv"].message_type = _CSV
_FORMAT.fields_by_name["png"].message_type = _PNG
_FORMAT.fields_by_name["geotiff"].message_type = _GEOTIFF
_FORMAT.fields_by_name["msgpack"].message_type = _MSGPACK
_PYARROW.fields_by_name["compression"].enum_type = _PYARROW_PYARROWCOMPRESSION
_PYARROW_PYARROWCOMPRESSION.containing_type = _PYARROW
_GEOTIFF.fields_by_name["compression"].enum_type = _GEOTIFF_GEOTIFFCOMPRESSION
_GEOTIFF.fields_by_name[
    "overview_resampler"
].enum_type = _GEOTIFF_GEOTIFFOVERVIEWRESAMPLER
_GEOTIFF_GEOTIFFCOMPRESSION.containing_type = _GEOTIFF
_GEOTIFF_GEOTIFFOVERVIEWRESAMPLER.containing_type = _GEOTIFF
DESCRIPTOR.message_types_by_name["Format"] = _FORMAT
DESCRIPTOR.message_types_by_name["Pyarrow"] = _PYARROW
DESCRIPTOR.message_types_by_name["JSON"] = _JSON
DESCRIPTOR.message_types_by_name["GeoJSON"] = _GEOJSON
DESCRIPTOR.message_types_by_name["CSV"] = _CSV
DESCRIPTOR.message_types_by_name["PNG"] = _PNG
DESCRIPTOR.message_types_by_name["Geotiff"] = _GEOTIFF
DESCRIPTOR.message_types_by_name["MsgPack"] = _MSGPACK
DESCRIPTOR.extensions_by_name["mimetype"] = mimetype
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Format = _reflection.GeneratedProtocolMessageType(
    "Format",
    (_message.Message,),
    {
        "DESCRIPTOR": _FORMAT,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Format)
    },
)
_sym_db.RegisterMessage(Format)

Pyarrow = _reflection.GeneratedProtocolMessageType(
    "Pyarrow",
    (_message.Message,),
    {
        "DESCRIPTOR": _PYARROW,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Pyarrow)
    },
)
_sym_db.RegisterMessage(Pyarrow)

JSON = _reflection.GeneratedProtocolMessageType(
    "JSON",
    (_message.Message,),
    {
        "DESCRIPTOR": _JSON,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.JSON)
    },
)
_sym_db.RegisterMessage(JSON)

GeoJSON = _reflection.GeneratedProtocolMessageType(
    "GeoJSON",
    (_message.Message,),
    {
        "DESCRIPTOR": _GEOJSON,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GeoJSON)
    },
)
_sym_db.RegisterMessage(GeoJSON)

CSV = _reflection.GeneratedProtocolMessageType(
    "CSV",
    (_message.Message,),
    {
        "DESCRIPTOR": _CSV,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CSV)
    },
)
_sym_db.RegisterMessage(CSV)

PNG = _reflection.GeneratedProtocolMessageType(
    "PNG",
    (_message.Message,),
    {
        "DESCRIPTOR": _PNG,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.PNG)
    },
)
_sym_db.RegisterMessage(PNG)

Geotiff = _reflection.GeneratedProtocolMessageType(
    "Geotiff",
    (_message.Message,),
    {
        "DESCRIPTOR": _GEOTIFF,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Geotiff)
    },
)
_sym_db.RegisterMessage(Geotiff)

MsgPack = _reflection.GeneratedProtocolMessageType(
    "MsgPack",
    (_message.Message,),
    {
        "DESCRIPTOR": _MSGPACK,
        "__module__": "descarteslabs.common.proto.formats.formats_pb2"
        # @@protoc_insertion_point(class_scope:descarteslabs.workflows.MsgPack)
    },
)
_sym_db.RegisterMessage(MsgPack)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(mimetype)

_FORMAT.fields_by_name["pyarrow"]._options = None
_FORMAT.fields_by_name["json"]._options = None
_FORMAT.fields_by_name["geojson"]._options = None
_FORMAT.fields_by_name["csv"]._options = None
_FORMAT.fields_by_name["png"]._options = None
_FORMAT.fields_by_name["geotiff"]._options = None
_FORMAT.fields_by_name["msgpack"]._options = None
# @@protoc_insertion_point(module_scope)
