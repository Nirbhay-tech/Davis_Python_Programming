marks=int(input("Enter your marks: "))  #input marks

#condition to find grade
if(marks>85):
    print("A")
elif(85>=marks>60):
    print("B")
elif(60>=marks>34):
    print("c")
else:
    print("D")