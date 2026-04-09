# Program to check if two strings are anagrams

# Take input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert both strings to lowercase
# This ensures comparison is case-insensitive and ignores spaces
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Sort both strings
# If they are anagrams, sorted characters will be the same
if sorted(str1) == sorted(str2):
    print("True")   # Strings are anagrams
else:
    print("False")  # Strings are not anagrams