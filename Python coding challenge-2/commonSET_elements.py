# Take input for sets
set1 = set(map(int, input("Enter elements of set1: ").split()))
set2 = set(map(int, input("Enter elements of set2: ").split()))

# Find intersection
result = set1.intersection(set2)

# Print result
print("Intersection:", result)