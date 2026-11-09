import json
import os
from CanBeShipped import CanBeShipped
from physicalProduct import physicalProduct
from digitalProduct import digitalProduct
from Product import Product
from Supplier import Supplier

FILENAME = "inventory.json"

class Inventory:
    def __init__(self):
        self.__items: list[Product] = [] 
        
    def get_items(self):
        return self.__items
        
    def add_products(self, product: Product) -> None:
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
                
def load_inventory(filename=FILENAME):
    inv = Inventory()
    
    default_supplier = Supplier("S001", "Global Hardware Inc.", "contact@globalhardware.com")

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    prod_type = item.get("type")
                    p_id = item.get("product_id")
                    name = item.get("name")
                    price = float(item.get("price"))
                    stock = int(item.get("stock"))
                    supplier = item.get("supplier")
                    
                    if prod_type == "physical":
                        weight = float(item.get("weight"))
                        new_prod = physicalProduct(p_id, name, price, stock, weight, default_supplier)
                    elif prod_type == "digital":
                        download_size = float(item.get("download_size"))
                        new_prod = digitalProduct(p_id, name, price, stock, download_size, default_supplier)
                    else:
                        continue
                    inv.add_products(new_prod)
                    
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inv
        except (json.JSONDecodeError, OSError) as e:
            print(f"Error loading inventory file: {e}")
            pass         
         
    # Default initial inventory using concrete subclasses
    inv.add_products(physicalProduct("P1001", "Laptop", 1200.00, 15, 2.5, default_supplier))
    inv.add_products(physicalProduct("P002", "Mouse", 25.50, 40, 0.2, default_supplier))
    inv.add_products(digitalProduct("D001", "Antivirus Software", 49.99, 100, 250.0, default_supplier))
    return inv   
   
def save_inventory(inventory, filename=FILENAME):
    print("Saving inventory...")
    data = [item.to_dict() for item in inventory.get_items()]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved successfully to {filename}.") 