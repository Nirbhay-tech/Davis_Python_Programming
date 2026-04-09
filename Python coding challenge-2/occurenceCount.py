string=input("Enter any string: ").lower()   #input string
char=input("Enter any string: ").lower()  #input char to find its occurence

count=0  #default 0

for i in string:      #iterate
    if char == i:   #checking charcter is occur or not
        count+=1      #if occurs count increase by 1
print(count)    #display count