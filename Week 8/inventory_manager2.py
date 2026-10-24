import json
import os
FILENAME = "inventory.json"

class Product:
    def __init__(self, product_id, name,price, stock ):
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
        
    #update stock        
    def update_stock(self, new_stock):
        self.__stock = new_stock
    
        
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
            if item.get_product_id().lower() == product_id.lower():
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
        
def load_inventory_data(filename=FILENAME):
    inv = Inventory()

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    new_prod = Product(item["id"], item["name"], item["price"], item["stock"])
                    inv.add_products(new_prod)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inv
        except (json.JSONDecodeError, OSError):
            pass        
          
    inv.add_products(Product("P1001", "laptop", 1200.00, 15 ))
    inv.add_products(Product("P002", "Mouse", 25.50, 40))
    inv.add_products(Product("P003", "Keyboard", 45.00, 25))
    return inv    
   
def save_inventory_data(inventory, filename=FILENAME):
    print("Saving inventory...")
    data = [item.to_dict() for item in inventory.get_items()]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved successfully to {filename}.") 
    
print("=" *  46)
print("Inventory Management System")
print("=" * 46)

inventory = load_inventory_data(FILENAME)

while True:
    print("\n--------- MENU ---------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------\n")
    
    choice = input("Enter option: ")
    
    if choice == "1":
        inventory.display_products()
        
    elif choice == "2":
        print("\nAdd New Product")
        p_id = input("Product ID: ")  
        name = input("Name: ")
        price = input("Price: ")
        stock= input("Stock: ")
          
        new_product = Product(p_id, name, price, stock)
        inventory.add_products(new_product)
        print("\nProduct added sucessfully!")
          
    elif choice == "3":
        p_id = input("Product ID: ")
        target = inventory.search_product(p_id)
        
        if target:
            print("\nProduct found")
            print(f"Name: {target.get_name()}") 
            print(f"Current Stock: {target.get_stock()}")
            
            new_stock = int(input("New Stock Quantity: "))
            target.update_stock(new_stock)
            print("Stock updated successfully!")
            
    elif choice == "4":
        print("\nSearch Product")
        p_id = input("Enter Product ID: ").strip()
        target = inventory.search_product(p_id)

        if target:
            print("\nProduct Found")
            print("-" * 46)
            print(f"ID: {target.get_product_id()}")
            print(f"Name: {target.get_name()}")
            print(f"Price: ${target.get_price():.2f}")
            print(f"Stock: {target.get_stock()}")
            print("-" * 46)
        else:
            print("\nProduct not found.")

    elif choice == "5":
        save_inventory_data(inventory, FILENAME)

    elif choice == "6":
        print("\nSaving inventory before exit...")
        save_inventory_data(inventory, FILENAME)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")       