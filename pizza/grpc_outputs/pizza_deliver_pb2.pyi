from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PizzaRequest(_message.Message):
    __slots__ = ("customer",)
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: str
    def __init__(self, customer: _Optional[str] = ...) -> None: ...

class PizzaResponse(_message.Message):
    __slots__ = ("rsp",)
    RSP_FIELD_NUMBER: _ClassVar[int]
    rsp: str
    def __init__(self, rsp: _Optional[str] = ...) -> None: ...
