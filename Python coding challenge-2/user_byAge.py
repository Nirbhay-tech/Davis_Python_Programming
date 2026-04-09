age=int(input("Enter your age :"))  #input age

#conditions applied

if(age<=0):
    print("Enter your valid age")
elif(age<18):
    print("Minor")
elif(18>=age<40):
    print("Adult")
else:
    print("senior")