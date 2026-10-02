from enum import Enum

from pydantic import BaseModel


class InventoryItem(BaseModel):
    id: int
    name: str
    category: str
    stock: int
    image_url: str


class OrderBy(str, Enum):
    asc = "asc"
    desc = "desc"


class GetInventoryQueryParams(BaseModel):
    order_by: OrderBy = OrderBy.asc
