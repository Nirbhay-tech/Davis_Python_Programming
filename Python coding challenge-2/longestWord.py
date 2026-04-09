# Program to find the longest word in a sentence

# Take input from user
sentence = input("Enter a sentence: ")

# Split the sentence into words using space
words = sentence.split()

# Assume first word is the longest initially
longest_word = words[0]

# Loop through each word in the list
for word in words:
    # Check if current word length is greater than longest_word
    if len(word) > len(longest_word):
        longest_word = word  # Update longest_word

# Display the result
print("Longest word is:", longest_word)
