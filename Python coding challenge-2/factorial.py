num=int(input("Enter the number: "))  #input number
fact=1   
if(num==0 or num==1):      #condition base
    print("Factorial of",num,"is",fact)
else:   
  for i in range(1,num+1):    #iterate to calculate factorial
    fact=fact*i
  print("Factorial of",num,"is",fact)