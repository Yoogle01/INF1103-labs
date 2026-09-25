

FILENAME = "orders.txt"


def load_orders(filename=FILENAME):
    orders = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) == 3:
                        orders.append({
                            "id": int(parts[0]),
                            "name": parts[1],
                            "quantity": int(parts[2])
                        })
    except FileNotFoundError:
        return []

    return orders

def save_orders(orders, filename=FILENAME):
    """Saves all individual orders to the file."""
    with open(filename, "w") as file:
        for order in orders:
            file.write(f"{order['id']},{order['name']},{order['quantity']}\n")


def display_orders(orders):
    #Displays current orders loaded from the file.
    print("Current Orders:\n")
    if orders:
        for order in orders:
            print(f"{order['id']}, {order['name']}, {order['quantity']}")
    print()


def generate_report(total_transactions, total_units, failed_attempts):
    """Prints the final summary report."""
    print("\n--- Audit Report ---")
    print(f"Total Transactions: {total_transactions}")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


orders = load_orders()


display_orders(orders)


failed_entries = 0

# 4. Main entry loop until user types 'quit'
while True:
    product_name = input("Enter Product Name (or 'quit' to exit): ").strip()

    if product_name.lower() == "quit":
       
        save_orders(orders)

        
        total_quantity = sum(order["quantity"] for order in orders)
        total_transactions = len(orders)

        print(f"\nOrders successfully saved to {FILENAME}")

       
        generate_report(total_transactions, total_quantity, failed_entries)
        break

    if not product_name:
        print("Product name cannot be empty.\n")
        failed_entries += 1
        continue

    quantity_input = input("Enter Quantity: ").strip()
    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("Invalid quantity. Please enter a positive integer.\n")
        failed_entries += 1
        continue

    quantity = int(quantity_input)

    
    next_id = orders[-1]["id"] + 1 if orders else 1001

    
    new_order = {
        "id": next_id,
        "name": product_name,
        "quantity": quantity
    }
    orders.append(new_order)

   
    print("\nNew Order Added:")
    print(f"{new_order['id']},{new_order['name']},{new_order['quantity']}\n")
    
    
    
'''
def get_valid_input():
    """Handles prompt, input validation, and returns an integer, 'quit', or 'invalid'."""
    user_input = input("Enter stock quantity (or enter 'quit' to exit): ").strip()
    
    if user_input.lower() == "quit":
        return "quit"
        
    if user_input.isdigit():
        return int(user_input)
        
    if user_input.startswith("-") and user_input[1:].isdigit():
        print("Error. Negative numbers are not allowed.")
    else:
        print("Error. String is not allowed.")
        
    return "invalid"


def process_delivery(current_total, new_value):
    """Calculates and returns the new inventory total."""
    return current_total + new_value


def calculate_tax(amount):
    """Calculates 10% tax for a specific delivery amount."""
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    """Prints the final summary report."""
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


# 1. Initialize inventory and counters at the start
inventory = 0
failed_entries = 0

# 2. Continuous loop
while True:
    value = get_valid_input()

    if value == "quit":
        break

    if value == "invalid":
        failed_entries += 1
        continue

    # 3. Process valid input
    inventory = process_delivery(inventory, value)
    tax = calculate_tax(value)
    
    print("Added", value,
          "| Tax for this delivery:", tax, 
          "| Current total inventory:", inventory)

# 4. Reporting
generate_report(inventory, failed_entries)'''