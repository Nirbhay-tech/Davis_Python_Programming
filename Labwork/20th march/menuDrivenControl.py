# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle divide by zero
    if b == 0:
        return "Error! Division by zero not allowed."
    return a / b


# Main calculator function
def calculator():
    
    while True:  # Loop for continuous use
        
        # Display menu
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Take user choice
        choice = int(input("Enter your choice (1-5): "))
        
        # Exit condition
        if choice == 5:
            print("Exiting calculator...")
            break
        
        # Take numbers for operations
        if choice in [1, 2, 3, 4]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            # Perform operation using if-elif-else
            if choice == 1:
                print("Result:", add(a, b))
            
            elif choice == 2:
                print("Result:", subtract(a, b))
            
            elif choice == 3:
                print("Result:", multiply(a, b))
            
            elif choice == 4:
                print("Result:", divide(a, b))
        
        else:
            print("Invalid choice! Please select between 1-5.")


# Call the calculator
calculator()