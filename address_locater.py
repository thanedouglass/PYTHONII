import re
# Read the file, convert lowercase to uppercase, and write to a new file
with open('mbox.txt', 'r') as f:
    contents = f.read()  # Read the entire file
    upper_contents = contents.upper()  # Convert to uppercase

# Write the uppercase content to a new file
with open('mbox.txt', 'w') as f:
    f.write(upper_contents)

print("Uppercase file created: mbox-short-upper-case.txt")

# Set to store unique email addresses
email_set = set()

# Read the file and extract email addresses
with open('mbox.txt', 'r') as f:
    for line in f:
        # Use regex to find email addresses
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in emails:
            email_set.add(email)  # Add email to the set (automatically handles duplicates)

# Write all unique email addresses to a new file
with open('mbox.txt', 'w') as f:
    for email in email_set:
        f.write(email + '\n')

# Print the total count of unique email addresses
print(f"Total unique email addresses: {len(email_set)}")

# Set to store unique ".umich.edu" email addresses
umich_set = set()

# Read the file and extract ".umich.edu" email addresses
with open('mbox.txt', 'r') as f:
    for line in f:
        # Use regex to find email addresses ending with ".umich.edu"
        emails = re.findall(r'[\w\.-]+@umich\.edu', line)
        for email in emails:
            umich_set.add(email)  # Add email to the set (automatically handles duplicates)

# Sort the email addresses alphabetically
sorted_umich_emails = sorted(umich_set)

# Write the sorted ".umich.edu" email addresses to a new file
with open('mbox.txt', 'w') as f:
    for email in sorted_umich_emails:
        f.write(email + '\n')

# Print the total count of unique ".umich.edu" email addresses
print(f"Total unique '.umich.edu' email addresses: {len(sorted_umich_emails)}")