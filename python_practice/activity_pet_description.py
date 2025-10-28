# Write a string with pet details.
pet_details = "Buddy is a 3-year-old dog."

# Use an f-string to preface pet_description with "Pet description:".
formatted_description = f"Pet description: {pet_details}"

# Add a string with a newline character and a thank you message.
message = f"{formatted_description}\nThank you for visiting AnyCompany Pet Society"

# Extract the pet's name from pet_details using slicing.
pet_name = pet_details[:5]

# Convert the formatted_description to uppercase.
uppercase_description = formatted_description.upper()

# Replace "dog" with "canine" in the formatted_description.
updated_description = formatted_description.replace("dog", "canine")

# Print the results.
print("Formatted string:", formatted_description)
print("Message with newline:", message)
print("Pet name:", pet_name)
print("Uppercase description:", uppercase_description)
print("Updated description:", updated_description)