# Program to replace all vowels in a string with '*'

def replace_vowels_with_star(text):
    """
    Replaces all vowels (both uppercase and lowercase) in the given text with '*'.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The modified string with vowels replaced by '*'.
    """
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    result = ""  # Initialize an empty string to store the result
    
    # Iterate over each character in the input text
    for char in text:
        if char in vowels:
            result += "*"  # Replace vowel with '*'
        else:
            result += char  # Keep consonants and other characters unchanged
    
    return result


# Main program execution
if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter a string: ").strip()
    
    # Validate input (ensure it's not empty)
    if not user_input:
        print("Error: Empty string entered.")
    else:
        # Call the function and display the result
        modified_string = replace_vowels_with_star(user_input)
        print("Modified string:", modified_string)
