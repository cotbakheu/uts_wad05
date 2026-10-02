from adapters.file_storage import load_inventory
from modules.inventory.schema import (
    CreateInventoryItem,
    GetInventoryQueryParams,
    InventoryItem,
    OrderBy,
)

inventory_item = load_inventory()


def get_inventory(params: GetInventoryQueryParams) -> list[InventoryItem]:
    items = inventory_item
    if params.name:
        items = [item for item in items if params.name.lower() in item.name.lower()]
    return sorted(
        items,
        key=lambda item: item.name,
        reverse=params.order_by == OrderBy.desc,
    )


def get_inventory_by_id(item_id: int) -> InventoryItem | None:
    for item in inventory_item:
        if item.id == item_id:
            return item
    return None


def create_inventory(item: CreateInventoryItem) -> InventoryItem:
    global inventory_item
    next_id = max((item.id for item in inventory_item), default=0) + 1
    inventory = InventoryItem(id=next_id, **item.model_dump())
    inventory_item.append(inventory)
    return inventory


def delete_inventory(item_id: int) -> None:
    global inventory_item
    inventory_item = [item for item in inventory_item if item.id != item_id]
