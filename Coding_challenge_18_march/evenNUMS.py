# n=int(input("Enter the last value till u want even nummber : "))
# num=1
# even_list=[]
# def findEven(num,n,even_list):
#   while(num<n):    #iteration to find even numbers
#       if num%2==0:    #logic to check even or not
#         even_list=even_list.append(num)  #if even print numbers
#       num=num+1 
#   return even_list

# even_num=findEven(num,n,even_list)
# print(even_num)

n=int(input("Enter the last value till u want even nummber : "))
num=1
while(num<n):    #iteration to find even numbers
    if num%2==0:    #logic to check even or not
        print(num)  #if even print numbers
    num=num+1 

