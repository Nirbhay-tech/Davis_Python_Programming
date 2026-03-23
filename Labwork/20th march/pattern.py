# Number of rows
rows = 4

# Loop for each row
for i in range(1, rows + 1):
    
    # Check if row number is even or odd
    if i % 2 == 0:
        symbol = "*"   # Even row
    else:
        symbol = "#"   # Odd row
    
    # Inner loop to print symbols in triangle form
    for j in range(i):
        print(symbol, end=" ")
    
    # Move to next line after each row
    print()