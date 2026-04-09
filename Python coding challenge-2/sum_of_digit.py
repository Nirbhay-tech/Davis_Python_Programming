num=int(input("Enter the number: ")) #input
sumofdigit=0   # default 0
while(num>0):   
    rem=num%10  #contains remainder
    sumofdigit=sumofdigit + rem   #add the digits
    num=num//10  #shortening number in every iteration
print(sumofdigit)  #display sum of digit 