# Take input for sets
set1 = set(map(int, input("Enter elements of set1: ").split()))
set2 = set(map(int, input("Enter elements of set2: ").split()))

# Find union
result = set1.union(set2)

# Print result
print("Union:", result)