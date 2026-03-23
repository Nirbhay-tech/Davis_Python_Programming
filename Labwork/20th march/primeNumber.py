# Function to check if a number is prime
def is_prime(n):
    
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Loop to check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:   # If divisible by any number
            return False
    
    # If no divisors found, number is prime
    return True


# Take input from user
num = int(input("Enter a number: "))

# Use if-else to display result
if is_prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")