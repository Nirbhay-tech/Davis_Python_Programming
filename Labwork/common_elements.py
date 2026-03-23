l1 = [1, 2, 3]  #list 1
l2 = [2, 3, 4]  #list 2
l3 = [2, 5, 3]  #list 3

result = list(set(l1) & set(l2) & set(l3))  #method to find common element using set

print(result)