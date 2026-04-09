text = input("Enter string: ")
result = ""

for ch in text:
    if 'a' <= ch <= 'z':   # check lowercase
        result += chr(ord(ch) - 32)
    else:
        result += ch

print("Uppercase:", result)