# Function to calculate bonus based on experience
def calculate_bonus(salary, years):
    
    # Check experience and apply bonus
    if years >= 10:
        bonus = salary * 0.20   # 20% bonus
    elif years >= 5:
        bonus = salary * 0.10   # 10% bonus
    else:
        bonus = salary * 0.05   # 5% bonus
    
    return bonus


# Loop to process multiple employees
n = int(input("Enter number of employees: "))

for i in range(1, n + 1):
    
    print(f"\nEmployee {i}")
    
    # Take input
    salary = float(input("Enter salary: "))
    years = int(input("Enter years of experience: "))
    
    # Calculate bonus
    bonus = calculate_bonus(salary, years)
    
    # Display result
    print(f"Bonus: {bonus}")
    print(f"Total Salary after bonus: {salary + bonus}")