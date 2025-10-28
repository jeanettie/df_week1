# Prompt the user for pet details.
pet_name = input("Enter your pet's name: ")
pet_type = input("What type of pet is it? ")
pet_age = input("How old is your pet? ")

# Format the pet description using an f-string.
pet_description = f"{pet_name} is a {pet_age}-year-old {pet_type}."

# Convert the description to uppercase.
uppercase_description = pet_description.upper()

# Ask how many treats the pet gets per day.
treats_per_day = input("How many treats does your pet get per day? ")
# Convert to integer and calculate treats per week.
treats_per_week = int(treats_per_day) * 7 

# Replace the pet type.
# Use .replace() to modify pet type from "dog" to "canine"
updated_description = pet_description.replace("dog", "canine") 
# Use .replace() to modify pet type from "cat" to "feline"
updated_description = updated_description.replace("cat", "feline") 

# Display a thank you message.
thank_you_message = "\nThank you for sharing your pet's profile!\nVisit us again soon!"

# Print all results.
print("\nPet Profile:")
print(pet_description)
print("Uppercase Description:", uppercase_description)
print("Treats per week:", treats_per_week)
print("Updated Description:", updated_description)
print(thank_you_message)