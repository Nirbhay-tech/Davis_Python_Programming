num=int(input("Enter a number : ")) # input number

def findEven(num):    #function to check even or not
  if num % 2==0:
    return 1
  else:
    return 0
isEven=findEven(num)  #function call

if(isEven==1):        #check number is even or odd after task of function
  print("Number is even")
else:
  print("Number is odd")