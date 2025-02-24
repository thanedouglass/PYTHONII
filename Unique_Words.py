# Open the file and read its contents
filename = "Romeo-full.txt"
try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
    exit()

# Process the text to find unique words
# Convert to lowercase and split into words
words = text.lower().split()

# Remove punctuation and clean words
clean_words = []
for word in words:
    # Remove punctuation at start and end of words
    word = word.strip(".,;:!?-\"'()[]{}")
    if word:  # Only add non-empty strings
        clean_words.append(word)

# Find unique words
unique_words = sorted(set(clean_words))

# Write unique words to a new file
output_filename = "Shakespeare - Unique Words.txt"
with open(output_filename, 'w') as output_file:
    for word in unique_words:
        output_file.write(word + '\n')

print(f"Found {len(unique_words)} unique words.")
print(f"Unique words have been saved to {output_filename}")