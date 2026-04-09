# Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Remove duplicates first (important for correct result)
unique_lst = list(set(lst))

# Assume first element as largest and second largest
largest = second = float('-inf')

# Loop through list
for num in unique_lst:
    
    # Update largest and second largest
    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num

# Print second largest
print("Second largest element:", second)