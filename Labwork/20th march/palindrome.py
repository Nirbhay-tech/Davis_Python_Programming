# Function to check palindrome
def is_palindrome(value):
    
    # Convert input to string (works for both number & string)
    value = str(value)
    
    reversed_value = ""  # To store reversed string
    
    # Loop to reverse the string
    for ch in value:
        reversed_value = ch + reversed_value
    
    # Check if original and reversed are same
    if value == reversed_value:
        print(f"{value} is a Palindrome")
    else:
        print(f"{value} is NOT a Palindrome")


# Take input from user
data = input("Enter a number or string: ")

# Call the function
is_palindrome(data)