from adapters.file_storage import load_inventory
from modules.inventory.schema import GetInventoryQueryParams, InventoryItem, OrderBy

inventory_item = load_inventory()


def get_inventory(params: GetInventoryQueryParams) -> list[InventoryItem]:
    return sorted(
        inventory_item,
        key=lambda item: item.name,
        reverse=params.order_by == OrderBy.desc,
    )


def create_inventory(item: InventoryItem) -> InventoryItem:
    inventory_item.append(item)
    return item


def delete_inventory(item_id: int) -> None:
    global inventory_item
    inventory_item = [item for item in inventory_item if item.id != item_id]
