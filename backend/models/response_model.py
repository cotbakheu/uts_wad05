from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    status: str
    message: str
    data: T
