

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
generate_report(inventory, failed_entries)