num=int(input("Enter the number: "))  #input number
ans=num
rev=0   # default 0
while(num>0):   
    rem=num%10  #contains remainder
    rev=(rev*10) + rem   #contains reverse number
    num=num//10  #shortening number in every iteration
# check palindrome or not
if(ans==rev):
    print("Palindrome")
else:
    print("No! Plaindrome")