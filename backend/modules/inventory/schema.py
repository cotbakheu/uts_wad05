from enum import Enum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class InventoryItem(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: int
    name: str
    category: str
    stock: int
    image_url: str
    location: str


class CreateInventoryItem(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    name: str
    category: str
    stock: int
    image_url: str
    location: str


class OrderBy(str, Enum):
    asc = "asc"
    desc = "desc"


class GetInventoryQueryParams(BaseModel):
    order_by: OrderBy = OrderBy.asc
    name: str | None = None
