# Function to calculate grade based on marks
def calculate_grade(marks):
    # Check if marks are 90 or above
    if marks >= 90:
        return "A"
    
    # Check if marks are between 75 and 89
    elif marks >= 75:
        return "B"
    
    # Check if marks are between 50 and 74
    elif marks >= 50:
        return "C"
    
    # If marks are below 50
    else:
        return "Fail"


# Loop to process marks of 5 students
for i in range(1, 6):
    
    # Take input from user for each student
    marks = int(input(f"Enter marks for student {i}: "))
    
    # Call the function to get grade
    grade = calculate_grade(marks)
    
    # Display the result
    print(f"Student {i} Grade: {grade}")