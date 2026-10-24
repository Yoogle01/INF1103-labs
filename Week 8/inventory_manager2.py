import json
import os

class Product:
    def __init__(self, product_id, name,stock, price ):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    #get methods
    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
            
    def get_stock(self):
        return self.__stock 
    """ #set methods    
    def set_product_id(self, product_id):
        self.__product_id = product_id
        
    def set_name(self, name):
        self.__name = name    
        
    def set_price(self, price):
       self.__price = price
       
    def set_stock(self, stock):
        self.__stock = stock         """
        
    #update stock        
    def update_stock(self, new_stock):
        self.stock = new_stock
    
        
    def to_dict(self):
        return {
            "product_id" : self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock" : self.__stock
        }   
        
    def __str__ (self):
        return  f"Product_id: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}"
    
class Inventory:
    def __init__(self):
        self.__items = []  
        
    def get_items(self):
        return self.__items
        
    def add_products(self, product):
        self.__items.append(product)      
        
    def search_product(self, product_id):
        for item in self.__items:
            if item.get_id().lower() == product_id.lower():
                return item
        return None   
    
    def display_products(self):
        print("\nCurrent Inventory")
        print("-" * 46)
        if not self.__items:
            print("Inventory is empty.")
        else:
            for item in self.__items:
                print(item)
        print("-" * 46)    
        
        
          
    
        



















""" import json
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


def save_inventory(inventory, filename=FILENAME):
    print("Saving inventory...")
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)
    print(f"Inventory saved successfully to {filename}.")


def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 46)
    for item in inventory:
        print(
            f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )
    print("-" * 46)


def add_product(inventory):
    print("\nAdd New Product")
    prod_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    price = float(input("Price: ").strip())
    stock = int(input("Stock Quantity: ").strip())

    new_product = {"id": prod_id, "name": name, "price": price, "stock": stock}
    inventory.append(new_product)
    print("\nProduct added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    target = None
    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            target = item
            break

    if target:
        print("\nProduct Found:")
        print(f"Name: {target['name']}")
        print(f"Current Stock: {target['stock']}\n")
        new_stock = int(input("New Stock Quantity: ").strip())
        target["stock"] = new_stock
        print("\nStock updated successfully!")
    else:
        print("\nProduct not found.")


def search_product(inventory):
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    target = None
    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            target = item
            break

    if target:
        print("\nProduct Found")
        print("-" * 46)
        print(f"ID: {target['id']}")
        print(f"Name: {target['name']}")
        print(f"Price: ${target['price']:.2f}")
        print(f"Stock: {target['stock']}")
        print("-" * 46)
    else:
        print("\nProduct not found.")


# --- Startup and Menu Execution ---
print("==================================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("==================================================\n")

inventory = load_inventory()

while True:
    print("\n--------- MENU ---------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------\n")

    option = input("Enter option: ").strip()

    if option == "1":
        display_all(inventory)
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        save_inventory(inventory)
    elif option == "6":
        print("\nSaving inventory before exit...")
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully.\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please try again.") """