import json
from pathlib import Path
from typing import Union
from modules.inventory.schema import InventoryItem

DEFAULT_FILE = Path("./seeds/inventory.json")


def load_inventory(file_path: Union[Path, str] = DEFAULT_FILE) -> list[InventoryItem]:
    path = Path(file_path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        inventory_data = json.load(file)
        return [InventoryItem(**item) for item in inventory_data["data"]]
