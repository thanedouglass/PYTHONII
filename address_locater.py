import re

# 1. Convert lowercase to uppercase
with open('mbox.txt', 'r') as input_file:
    contents = input_file.read()  # Read the entire file
    upper_contents = contents.upper()  # Convert to uppercase

# Write the uppercase content to a new file
with open('mbox-upper-case.txt', 'w') as output_file:
    output_file.write(upper_contents)

print("Uppercase file created: mbox-upper-case.txt")

# 2. Extract and count all email addresses
email_set = set()

# Read the file and extract email addresses
with open('mbox.txt', 'r') as input_file:
    for line in input_file:
        # Use regex to find email addresses
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in emails:
            email_set.add(email)  # Add email to the set (automatically handles duplicates)

# Write all unique email addresses to total-email-count file
with open('total-email-count', 'w') as output_file:
    for email in email_set:
        output_file.write(email + '\n')

# Print the total count of unique email addresses
print(f"Total unique email addresses: {len(email_set)}")

# 3. Extract and sort umich.edu email addresses
umich_set = set()

# Read the file and extract ".umich.edu" email addresses
with open('mbox.txt', 'r') as input_file:
    for line in input_file:
        # Use regex to find email addresses ending with ".umich.edu"
        emails = re.findall(r'[\w\.-]+@umich\.edu', line)
        for email in emails:
            umich_set.add(email)  # Add email to the set (automatically handles duplicates)

# Sort the email addresses alphabetically
sorted_umich_emails = sorted(umich_set)

# Write the sorted ".umich.edu" email addresses to mbox-umich.txt
with open('mbox-umich.txt', 'w') as output_file:
    for email in sorted_umich_emails:
        output_file.write(email + '\n')

# Print the total count of unique ".umich.edu" email addresses
print(f"Total unique '.umich.edu' email addresses: {len(sorted_umich_emails)}")