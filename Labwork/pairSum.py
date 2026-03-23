Tuple = (1, 2, 3, 4, 5)
Sum = 5

pairs = []

for i in range(len(Tuple)): #to get first element
    for j in range(i + 1, len(Tuple)):   #to get next element to first
        if Tuple[i] + Tuple[j] == Sum:
            pairs.append((Tuple[i], Tuple[j]))

print(pairs)