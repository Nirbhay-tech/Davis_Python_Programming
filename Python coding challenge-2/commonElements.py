# Take input for first list
list1 = list(map(int, input("Enter elements of list1: ").split()))

# Take input for second list
list2 = list(map(int, input("Enter elements of list2: ").split()))

# List to store common elements
common = []

# Loop through elements of first list
for item in list1:
    
    # Check if element is present in second list and not already added
    if item in list2 and item not in common:
        common.append(item)   # Add to common list

# Print result
print("Common elements:", common)