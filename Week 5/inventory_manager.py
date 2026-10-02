import json
import os

FILENAME = "inventory.json"


def load_inventory(filename=FILENAME):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                inventory = json.load(file)
                print("inventory.json found.")
                print("Inventory loaded successfully.")
                return inventory
        except (json.JSONDecodeError, OSError):
            pass

    # Default starter data if file doesn't exist yet
    return [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]


