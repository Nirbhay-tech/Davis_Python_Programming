vowels=["a","e","i","o","u"]  #list contains vowel

char=input("Enter a charcter: ")  #input character

if char.lower() in vowels:  #condition to check vowel or not
    print("Vowel")
else:
    print("It is not vowel")