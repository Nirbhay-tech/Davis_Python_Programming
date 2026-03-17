num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if num % i == 0 and i % 2 == 0:
        print("Even factors of", num, "are:")
        print(i)
    else:
        print("No even factors found!")
        break