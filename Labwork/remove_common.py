list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

for i in list2:
    if i in list1:  #checking common element
        list1.remove(i)  #if it present then remove

print(list1)