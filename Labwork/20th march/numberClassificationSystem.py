# Function to check number properties
def check_number(num):
    
    # Check if number is Positive, Negative, or Zero
    if num > 0:
        print(f"{num} is Positive")
        
        # Nested if to check Even or Odd (inside Positive)
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
    
    elif num < 0:
        print(f"{num} is Negative")
        
        # Nested if to check Even or Odd (inside Negative)
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
    
    else:
        # If number is zero
        print(f"{num} is Zero")
        print(f"{num} is Even")  # Zero is considered even


# List of numbers (you can change this list)
numbers = [10, -5, 0, 7, -8]

# Loop to process all numbers in the list
for num in numbers:
    check_number(num)  # Call function for each number
    print("-----")  # Separator for better readability