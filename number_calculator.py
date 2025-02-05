# Initialize variables
total = 0
count = 0
numbers = []

# Loop to read numbers
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input.lower() == "done":
        break  # Exit the loop if the user enters "done"
    
    try:
        number = float(user_input)  # Convert input to a float
        total += number  # Add to total
        count += 1  # Increment count
        numbers.append(number)  # Add to the list of numbers
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-numeric input

# Calculate average (if count > 0 to avoid division by zero)
if count > 0:
    average = total / count
    max_num = max(numbers)
    min_num = min(numbers)
else:
    average = max_num = min_num = 0  # Default values if no numbers were entered

# Print results
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")