lst = [{1, 2}, set(), {3, 4}, set()]  #conations empty set

while set() in lst: #checking empty set
    lst.remove(set()) #if present then remove

print(lst)