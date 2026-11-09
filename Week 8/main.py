from Inventory import load_inventory, save_inventory
from CanBeShipped import CanBeShipped
from physicalProduct import physicalProduct
from digitalProduct import digitalProduct
from Supplier import Supplier

print("=" * 46)
print("Inventory Management System")
print("=" * 46)

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
    
    choice = input("Enter option: ").strip()
    
    if choice == "1":
        inventory.display_products()
        
    elif choice == "2":
        print("\nAdd New Product")
        digiOrPhy = input("Digital or Physical Product? ").strip().lower()
        
        if digiOrPhy not in ["digital", "physical"]:
            print("Invalid product type entered. Please type 'digital' or 'physical'.")
            continue
            
        p_id = input("Product ID: ").strip()  
        name = input("Name: ").strip()
        
        # --- Prompt for Supplier Details ---
        print("\n--- Enter Supplier Details ---")
        supp_id = input("Supplier ID: ").strip()
        supp_name = input("Supplier Name: ").strip()
        supp_email = input("Supplier Email: ").strip()
        
        # Create the Supplier object from user input
        user_supplier = Supplier(supp_id, supp_name, supp_email)
        print("------------------------------")
        
        if digiOrPhy == "digital":
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                download_size = float(input("Download size (MB): "))
            except ValueError:
                print("Error: Invalid numeric input format.")
                continue
                
            # Pass the user_supplier as the final argument
            digital_product = digitalProduct(p_id, name, price, stock, download_size, user_supplier)
            inventory.add_products(digital_product)
            print("\nDigital Product added successfully!")
            
        elif digiOrPhy == "physical":
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                weight = float(input("Weight (kg): "))
            except ValueError:
                print("Error: Invalid numeric input format.")
                continue
                
            # Pass the user_supplier as the final argument
            physical_product = physicalProduct(p_id, name, price, stock, weight, user_supplier)
            inventory.add_products(physical_product)  
            print("\nPhysical Product added successfully!")
          
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
        save_inventory(inventory)

    elif choice == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")