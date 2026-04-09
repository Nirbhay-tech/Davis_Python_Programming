username="admin" # default username 
password=1234    # default password

user_name=input("Enter your user name: ").lower() #username that enter by user
pas=int(input("Enter your password: "))  #password that enter by user 

if((username==user_name)and (password==pas)):  #condition that login successfully
    print("Login Successful")
else:
    print("Login Failed")
