# Function to print multiplication table
def print_table(num):
    
    # Check if number is negative
    if num < 0:
        print("Negative numbers are not allowed")
        return  # Exit function
    
    # Print table from 1 to 10
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# Take input from user
number = int(input("Enter a number: "))

# Call the function
print_table(number)