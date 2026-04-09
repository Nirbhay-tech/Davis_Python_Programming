# Take list input
lst = list(map(int, input("Enter elements: ").split()))

# Rotate list (last element moves to front)
rotated = [lst[-1]] + lst[:-1]

# Print result
print("Rotated list:", rotated)