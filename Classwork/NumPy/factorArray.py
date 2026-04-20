import numpy as np
# create a numpy array from the even factors of a given number
num=int(input("enter the number: "))
# if(num<0):
#     num=abs(num)
# elif(num==0):
#     print("no factor found")
# else:
array=np.arange(2,num+1,2)
factors=array[num % array==0]
print(factors)