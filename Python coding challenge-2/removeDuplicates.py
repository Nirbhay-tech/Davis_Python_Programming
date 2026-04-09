# Take input from user
text = input("Enter a string: ")

# List to store characters that are already seen
seen = []

# List to store duplicate characters
duplicates = []

# Loop through each character in the string
for ch in text:
    
    # If character is already seen and not already added in duplicates
    if ch in seen and ch not in duplicates:
        duplicates.append(ch)   # Add to duplicates list
    
    else:
        seen.append(ch)         # Add to seen list

# Print duplicate characters separated by space
print("Duplicate characters:", " ".join(duplicates))