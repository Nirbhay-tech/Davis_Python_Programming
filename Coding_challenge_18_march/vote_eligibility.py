age=int(input("Enter Your age : "))  #users age

if(age==0 or age<0):
    print("enter valid age")
elif(age<18):  #for eligible
    print("Not Eligible")
else:      #for not eligibile
    print("Eligible")
