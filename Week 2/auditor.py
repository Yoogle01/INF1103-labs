inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or enter 'quit' to exit): ")
    #when user types quit
    if user_input.lower() == "quit":
        break
    #when user types string or negative number
    if not user_input.isdigit():
        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error. Negative numbers are not allowed.")   
            failed_entries += 1
        else:
            print("Error. String is not allowed")  
            failed_entries += 1
        continue

    #  accepting stock value as integer 
    num_stock = int(user_input)
    inventory += num_stock
    print("Added", num_stock, "| Current total inventory: ", inventory)
     
    if inventory > 500:
        print("Alert. Total inventory is exceeding 500 units")
        break

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries: ", failed_entries)
     




    
         
          
         
      
            