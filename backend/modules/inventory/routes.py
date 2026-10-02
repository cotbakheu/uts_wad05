from fastapi import APIRouter, Depends
from modules.inventory.service import get_inventory, create_inventory
from modules.inventory.schema import GetInventoryQueryParams, InventoryItem

router = APIRouter()


@router.get("/inventory", tags=["Inventory"])
async def read_inventory(
    params: GetInventoryQueryParams = Depends(),
):
    inventory = get_inventory(params)
    return inventory


@router.post("/inventory", tags=["Inventory"])
async def create_inventory(item: InventoryItem):
    item = create_inventory(item)
    return item
