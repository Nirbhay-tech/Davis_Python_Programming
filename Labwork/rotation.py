lst = [10, 20, 30, 40, 50]
k = 2

k = k % len(lst)   # handle k > length  #handling k length so it remains in list
rotated = lst[-k:] + lst[:-k]

print(rotated)