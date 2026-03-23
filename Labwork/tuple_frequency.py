t = (1, 2, 2, 3, 1, 4)

freq = {}  #conatins frequency but initially empty

for item in t:
    if item in freq:   #if element then update frequency
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)