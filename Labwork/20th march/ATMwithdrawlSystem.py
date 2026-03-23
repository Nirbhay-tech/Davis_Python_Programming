# Function for withdrawal system
def withdrawal_system():
    
    balance = 10000  # Initial balance
    
    # Run loop until user chooses to exit
    while True:
        
        print(f"\nCurrent Balance: {balance}")
        
        # Take withdrawal amount
        amount = float(input("Enter amount to withdraw (or 0 to exit): "))
        
        # Exit condition
        if amount == 0:
            print("Exiting... Thank you!")
            break
        
        # Check for invalid amount
        if amount < 0:
            print("Invalid amount! Please enter a positive value.")
        
        # Check for insufficient balance
        elif amount > balance:
            print("Insufficient balance!")
        
        # Successful withdrawal
        else:
            balance -= amount
            print(f"Withdrawal successful! Remaining balance: {balance}")


# Call the function
withdrawal_system()