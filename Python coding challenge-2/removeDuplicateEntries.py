# Take list input from user (space separated numbers)
lst = list(map(int, input("Enter elements: ").split()))

# New list to store unique elements
unique_list = []

# Loop through each element in original list
for item in lst:
    
    # Check if element is not already in unique_list
    if item not in unique_list:
        unique_list.append(item)   # Add only unique elements

# Print result
print("List after removing duplicates:", unique_list)