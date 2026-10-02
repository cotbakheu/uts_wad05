from http.client import HTTPException

from fastapi import APIRouter, Depends
from modules.inventory.service import (
    get_inventory,
    create_inventory as create_inventory_service,
    delete_inventory as delete_inventory_service,
    get_inventory_by_id as get_inventory_by_id_service,
    update_inventory as update_inventory_service,
)
from modules.inventory.schema import GetInventoryQueryParams, CreateInventoryItem
from models.response_model import ResponseModel

router = APIRouter()


@router.get(
    "/inventory",
    response_model=ResponseModel,
    response_model_by_alias=True,
    tags=["Inventory"],
)
async def read_inventory(
    params: GetInventoryQueryParams = Depends(),
):
    inventory = get_inventory(params)
    return ResponseModel(
        status="success", message="Inventory retrieved successfully", data=inventory
    )


@router.get(
    "/inventory/{item_id}",
    response_model=ResponseModel,
    response_model_by_alias=True,
    tags=["Inventory"],
)
def read_inventory_by_id(item_id: int):
    item = get_inventory_by_id_service(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ResponseModel(
        status="success", message="Item retrieved successfully", data=item
    )


@router.post("/inventory", tags=["Inventory"])
async def create_inventory(item: CreateInventoryItem):
    item = create_inventory_service(item)
    return ResponseModel(
        status="success", message="Item created successfully", data=item
    )


@router.patch("/inventory/{item_id}", tags=["Inventory"])
async def update_inventory(item_id: int, item: CreateInventoryItem):
    updated_item = update_inventory_service(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ResponseModel(
        status="success", message="Item updated successfully", data=updated_item
    )


@router.delete("/inventory/{item_id}", tags=["Inventory"])
async def delete_inventory(item_id: int):
    delete_inventory_service(item_id)
    return ResponseModel(
        status="success", message="Item deleted successfully", data=None
    )
