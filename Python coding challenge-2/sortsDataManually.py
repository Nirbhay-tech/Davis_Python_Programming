# Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Bubble Sort Algorithm
n = len(lst)

# Outer loop for passes
for i in range(n):
    
    # Inner loop for comparison
    for j in range(0, n - i - 1):
        
        # Swap if elements are in wrong order
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Print sorted list
print("Sorted list:", lst)