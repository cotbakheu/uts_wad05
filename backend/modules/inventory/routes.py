from fastapi import APIRouter, Depends
from modules.inventory.service import get_inventory, create_inventory, delete_inventory
from modules.inventory.schema import GetInventoryQueryParams, InventoryItem
from models.response_model import ResponseModel

router = APIRouter()


@router.get("/inventory", tags=["Inventory"])
async def read_inventory(
    params: GetInventoryQueryParams = Depends(),
):
    inventory = get_inventory(params)
    return ResponseModel(
        status="success", message="Inventory retrieved successfully", data=inventory
    )


@router.post("/inventory", tags=["Inventory"])
async def create_inventory(item: InventoryItem):
    item = create_inventory(item)
    return ResponseModel(
        status="success", message="Item created successfully", data=item
    )


@router.delete("/inventory/{item_id}", tags=["Inventory"])
async def delete_inventory(item_id: int):
    delete_inventory(item_id)
    return ResponseModel(
        status="success", message="Item deleted successfully", data=None
    )
