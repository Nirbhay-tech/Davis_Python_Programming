num=int(input("Enter the number: "))  #input number
rev=0   # default 0
while(num>0):   
    rem=num%10  #contains remainder
    rev=(rev*10) + rem   #contains reverse number
    num=num//10  #shortening number in every iteration
print(rev)  #display reverse number