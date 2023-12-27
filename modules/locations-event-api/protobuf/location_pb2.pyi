from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LocationItem(_message.Message):
    __slots__ = ["person_id", "latitude", "longitude"]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    person_id: int
    latitude: str
    longitude: str
    def __init__(self, person_id: _Optional[int] = ..., latitude: _Optional[str] = ..., longitude: _Optional[str] = ...) -> None: ...
