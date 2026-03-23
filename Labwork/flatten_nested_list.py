lst = [[1, 2], [3, 4], [5]]  #given ist

result = []  #store list
for sublist in lst:  #to take sublist
    for item in sublist:  #to take items from list
        result.append(item)

print(result)  #to display