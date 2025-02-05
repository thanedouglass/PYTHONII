# Given string
string1 = "John Doe, 999-99-9999, 2-23-2003: 19.8973"

# Find the index of the colon
colon_index = string1.find(":")

# Extract the substring after the colon and strip any leading/trailing whitespace
number_str = string1[colon_index + 1:].strip()

# Convert the extracted string to a float
number = float(number_str)

# Print the result
print(f"Extracted number: {number}")