# Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Convert list to set to remove duplicates
unique_elements = set(lst)

# Count unique elements
count = len(unique_elements)

# Print result
print("Number of unique elements:", count)