from fastapi import APIRouter, Depends
from modules.inventory.service import get_inventory
from modules.inventory.schema import GetInventoryQueryParams

router = APIRouter()


@router.get("/inventory", tags=["Inventory"])
async def read_inventory(
    params: GetInventoryQueryParams = Depends(),
):
    inventory = get_inventory(params)
    return inventory
