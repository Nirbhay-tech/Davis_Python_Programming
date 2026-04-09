vowels=["a","e","i","o","u"]  #contains vowels

string=input("Enter any string: ").lower()   #input string

count=0  #default 0

for i in string:    #iterate
    if i in vowels:   #checking vowles or not
        count+=1      #if vowel count increase by 1
print(count)    #display count