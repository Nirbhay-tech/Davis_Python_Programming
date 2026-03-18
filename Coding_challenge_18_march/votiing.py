age=int(input("Enter Your age : "))  #users age

def checkEligibility(age):
   if(age<18):  #for eligible
       return 0
   else:      #for not eligibile
       return 1

eligibility=checkEligibility(age)
if(eligibility==0):
    print("Not Eligible")
else:
    print("Eligible")

