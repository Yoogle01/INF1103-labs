import json
import os
from abc import ABC, abstractmethod
FILENAME = "inventory.json"

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
    
class Product(ABC):
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
    
    @abstractmethod    
    def to_dict(self):
        pass  
        
    @abstractmethod
    def get_fulfilment_info(self):
        pass
        
    def display_information(self):
        return  f"Product_id: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}"
            
    def __str__ (self):
        return self.display_information()

class physicalProduct(Product, CanBeShipped):
    def __init__(self, weight, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock)
        self.weight = weight
        
    def get_fulfilment_info():
        print("Product requires physical shipping")   
    
    def calculate_shipping_cost(self):
        base_fee = 5.00
        cost_per_kg = 2.00
        return base_fee + (self.weight * cost_per_kg)
        
    def to_dict(self):
        return {
            "type": "physical",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.weight
        }    
        
    def display_information(self):
        product_info = super().display_information()
        return  f"{product_info} | weight: {self.weight}"
        
class digitalProduct(Product):
    def __init__(self, download_size, product_id, name, price, stock):
        super().__init__(download_size, product_id, name, price, stock)
        self.download_size = download_size
    
    def get_fulfilment_info():
        print("Product is delivered digitally")    
    
    def to_dict(self):
        return {
            "type": "digital",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.download_size
        }
        
    def display_information(self):
        product_info = super().display_information()
        return  f"{product_info} | Download size: {self.download_size}"    

    
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
        print("-" * 55)
        if not self.__items:
            print("Inventory is empty.")
        else:
            for item in self.__items:
                print(item)
                print(f"Fulfilment: {item.get_fulfilment_info()}")
                if isinstance(item, CanBeShipped):
                    print(f"Shipping Cost: ${item.calculate_shipping_cost():.2f}")
                print("-" * 55)
        
def load_inventory(filename=FILENAME):
    inv = Inventory()

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
                    
                    if prod_type == "physical":
                        weight = float(item.get("weight"))
                        new_prod = PhysicalProduct(p_id, name, price, stock, weight)
                    elif prod_type == "digital":
                        download_size = float(item.get("download_size"))
                        new_prod = DigitalProduct(p_id, name, price, stock, download_size)
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
    inv.add_products(PhysicalProduct("P1001", "Laptop", 1200.00, 15, 2.5))
    inv.add_products(PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2))
    inv.add_products(DigitalProduct("D001", "Antivirus Software", 49.99, 100, 250.0))
    return inv   
   
def save_inventory(inventory, filename=FILENAME):
    print("Saving inventory...")
    data = [item.to_dict() for item in inventory.get_items()]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved successfully to {filename}.") 
    
print("=" * 46)
print("Inventory Management System")
print("=" * 46)

inventory = load_inventory(FILENAME)

while True:
    print("\n--------- MENU ---------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------\n")
    
    choice = input("Enter option: ").strip()
    
    if choice == "1":
        inventory.display_products()
        
    elif choice == "2":
        print("\nAdd New Product")
        digiOrPhy = input("Digital or Physical Product? ").strip().lower()
        
        if digiOrPhy == "digital":
            p_id = input("Product ID: ").strip()  
            name = input("Name: ").strip()
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                download_size = float(input("Download size (MB): "))
            except ValueError:
                print("Error: Invalid numeric input format.")
                continue
                
            digital_product = DigitalProduct(p_id, name, price, stock, download_size)
            inventory.add_products(digital_product)
            print("\nDigital Product added successfully!")
            
        elif digiOrPhy == "physical":
            p_id = input("Product ID: ").strip()  
            name = input("Name: ").strip()
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                weight = float(input("Weight (kg): "))
            except ValueError:
                print("Error: Invalid numeric input format.")
                continue
                
            physical_product = PhysicalProduct(p_id, name, price, stock, weight)
            inventory.add_products(physical_product)  
            print("\nPhysical Product added successfully!")
        else:
            print("Invalid product type entered. Please type 'digital' or 'physical'.")
          
    elif choice == "3":
        p_id = input("Product ID: ").strip()
        target = inventory.search_product(p_id)
        
        if target:
            print("\nProduct found")
            print(f"Name: {target.get_name()}") 
            print(f"Current Stock: {target.get_stock()}")
            try:
                new_stock = int(input("New Stock Quantity: "))
                target.update_stock(new_stock)
                print("Stock updated successfully!")
            except ValueError:
                print("Error: Stock must be an integer.")
        else:
            print("\nProduct not found.")
            
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
            print(f"Fulfilment: {target.get_fulfilment_info()}")
            if isinstance(target, CanBeShipped):
                print(f"Shipping Cost: ${target.calculate_shipping_cost():.2f}")
            print("-" * 46)
        else:
            print("\nProduct not found.")

    elif choice == "5":
        save_inventory(inventory, FILENAME)

    elif choice == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory, FILENAME)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")