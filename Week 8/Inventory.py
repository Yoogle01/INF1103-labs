import csv
import json
import os
from CanBeShipped import CanBeShipped
from Product import Product
from ProductFactory import ProductFactory
from Supplier import Supplier

FILENAME = "inventory.json"


class Inventory:
    def __init__(self):
        self.__items: list[Product] = []

    def get_items(self):
        return self.__items

    def add_products(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise ValueError("Item must be a valid Product instance.")
        self.__items.append(product)

    def search_product(self, product_id: str) -> Product | None:
        for item in self.__items:
            if item.get_product_id().lower() == product_id.lower():
                return item
        return None

    def remove_product(self, product_id: str) -> None:
        for item in self.__items:
            if item.get_product_id().lower() == product_id.lower():
                self.__items.remove(item)
                return

    def display_products(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 55)
        if not self.__items:
            print("Inventory is empty.")
        else:
            for item in self.__items:
                print(item.display_information())
                print(f"Fulfilment: {item.get_fulfilment_info()}")
                if isinstance(item, CanBeShipped):
                    print(f"Shipping Cost: ${item.calculate_shipping_cost()}")
                print("-" * 55)


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for row in reader:
                if not row:
                    continue
                try:
                    prod_type = row[0].strip()
                    p_id = row[1].strip()
                    name = row[2].strip()
                    price = float(row[3].strip())
                    stock = int(row[4].strip())

                    weight = 1.0 if prod_type.lower() == "physical" else 0
                    download_size = 1.0 if prod_type.lower() == "digital" else 0

                    product = ProductFactory.create(
                        prod_type,
                        p_id,
                        name,
                        price,
                        stock,
                        weight,
                        download_size,
                        supplier,
                    )
                    inventory.add_products(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Invalid row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")


def load_inventory(filename=FILENAME):
    inv = Inventory()
    default_supplier = Supplier("S001", "Global Hardware Inc.", "contact@globalhardware.com")

    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    prod_type = item.get("type", "")
                    p_id = item.get("product_id", "")
                    name = item.get("name", "")
                    price = float(item.get("price"))
                    stock = int(item.get("stock"))
                    weight = float(item.get("weight", 0))
                    download_size = float(item.get("download_size", 0))

                    try:
                        new_prod = ProductFactory.create(
                            prod_type,
                            p_id,
                            name,
                            price,
                            stock,
                            weight,
                            download_size,
                            default_supplier,
                        )
                    except ValueError:
                        continue
                    inv.add_products(new_prod)

            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inv
        except (json.JSONDecodeError, OSError) as e:
            print(f"Error loading inventory file: {e}")

    # Default initial inventory created via ProductFactory
    inv.add_products(
        ProductFactory.create("physical", "P1001", "Laptop", 1200.00, 15, 2.5, 0, default_supplier)
    )
    inv.add_products(
        ProductFactory.create("physical", "P002", "Mouse", 25.50, 40, 0.2, 0, default_supplier)
    )
    inv.add_products(
        ProductFactory.create("digital", "D001", "Antivirus Software", 49.99, 100, 0, 250.0, default_supplier)
    )
    return inv


def save_inventory(inventory, filename=FILENAME):
    print("Saving inventory...")
    data = [item.to_dict() for item in inventory.get_items()]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved successfully to {filename}.")