# Prompt the user for pet details.
pet_name = input("Enter your pet's name: ")
pet_type = input("Enter your pet's type: ")# Use input() to collect this data.
pet_age = int(input("Enter your pet's age: "))# Use input() to collect this data.

# Format the pet description using an f-string.
pet_description = f"{pet_name} is a {pet_age}-year-old {pet_type}."# Add f-string here. pet_age pet_type"

# Convert the description to uppercase.
uppercase_description = pet_description.upper()# Use .upper().

# Ask how many treats the pet gets per day.
treats_per_day = int(input("How many treats does your pet get per day? "))# Use input() to collect this data.
treats_per_week = treats_per_day * 7 # Convert to integer and calculate treats per week.

# Replace the pet type.
updated_description = f"{pet_name} is a {pet_age}-year-old {pet_type.replace("dog", "canine")}"# Use .replace() to modify pet type from "dog" to "canine".
updated_description = f"{pet_name} is a {pet_age}-year-old {pet_type.replace("cat", "feline")}"# Use .replace() to modify pet type from "cat" to "feline".

# Display a thank you message.
thank_you_message = "Thanks for visiting! \nCome Again."# Add escape characters here.

# Print all results.
print("\nPet Profile:")
print(pet_description)
print("Uppercase Description:", uppercase_description)
print("Treats per week:", treats_per_week)
print("Updated Description:", updated_description)
print(thank_you_message)