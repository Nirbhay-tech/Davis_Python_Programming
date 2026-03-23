list=[1,2,3,2,4,5,1] #given list
duplicates=[]  #empty list of duplicates

for i in list:  #for loop
    if list.count(i)>1 and i not in duplicates:  #condition for checking duplicates
        duplicates.append(i)   #add duplicates in list
print(duplicates)  #to display