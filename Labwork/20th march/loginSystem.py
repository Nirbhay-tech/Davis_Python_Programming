# Function for login system
def login():
    # Correct credentials
    correct_username = "admin"
    correct_password = "1234"
    
    attempts = 0  # Counter for number of attempts
    
    # Allow maximum 3 attempts
    while attempts < 3:
        
        # Take input from user
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Check credentials using if-else
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return  # Exit function if login is successful
        
        else:
            attempts += 1  # Increase attempt count
            print("Invalid credentials")
    
    # If 3 attempts are used
    print("Account Locked")


# Call the function
login()