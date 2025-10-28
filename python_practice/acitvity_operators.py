# Arithmetic operators.
total_dogs = 8
total_cats = 7

# Addition: Total number of pets.
total_pets = total_dogs + total_cats

# Multiplication: Number of treats per dog and per cat.
treats_per_dog = 4
treats_per_cat = 3
total_dog_treats_needed = treats_per_dog * total_dogs
total_cat_treats_needed = treats_per_cat * total_cats
total_treats_needed = total_dog_treats_needed+total_cat_treats_needed

# Division: Average treats per pet.
average_treats_per_pet = total_treats_needed / total_pets

# Modulus: Leftover treats after dividing evenly among pets.
leftover_treats = total_treats_needed % total_pets

# String concatenation.
store_greeting = "Welcome to " + "AnyCompany Pet Society!"

# Printing results.
print(store_greeting)
print("We have a total of", total_pets, "pets.")
print("We need", total_dog_treats_needed, "treats for the dogs.")
print("Each pet gets an average of", average_treats_per_pet, "treats.")
print("Leftover treats:", leftover_treats)

# Assign values for the number of pets and treats per pet.
total_rabbits = 15
total_birds = 20
treats_per_pet = 2

# Calculate the total number of pets.
total_pets = total_rabbits + total_birds # Use an arithmetic operator to calculate total pets

# Calculate the total number of treats needed.
total_treats_needed = total_pets * treats_per_pet # Use an arithmetic operator to calculate total treats needed

# Calculate the number of leftover treats (assume 100 treats available).
available_treats = 100
leftover_treats = available_treats - total_treats_needed # Use an arithmetic operator to calculate leftover treats

# Print the results.
print("Total pets:", total_pets)
print("Total treats needed:", total_treats_needed)
print("Leftover treats:", leftover_treats)