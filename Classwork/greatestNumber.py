#given number
num=3723
max=0
while(num>0):
  digit=num%10 #get last digit
  if(digit>max):#checking digit is greater or not
    max=digit
  num=num//10   #remove last digit 
print("greatest digit is :",max)