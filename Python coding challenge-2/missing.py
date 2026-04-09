# Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Find max number
n = max(lst)

# Expected sum of numbers from 1 to n
total = n * (n + 1) // 2

# Actual sum of list
actual = sum(lst)

# Missing number
missing = total - actual

# Print result
print("Missing number:", missing)