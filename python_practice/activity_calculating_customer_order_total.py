# Assign values to variables.
pet_type = "Iguana" # The type of the pet (string)
pet_price = 79.99 # The price of the pet (float)
quantity = "2" # The number of pets the customer wants to buy (string)

# Convert quantity to an integer.
quantity_int = int(quantity) # Cast the quantity to an integer

# Calculate the total cost.
total_cost = pet_price * quantity_int # Multiply pet_price by quantity_int

# Convert the total cost to a string.
total_cost_str = str(total_cost)# Cast total_cost to a string

# Print the receipt.
print("Receipt:")
print("Pet Type:", pet_type)
print("Quantity:", quantity_int)
print("Total Cost: $" + total_cost_str)