"""
Menu Driven Program: Student Result System
Enter Marks
Calculate Percentage
Assign Grade
"""
marks = []
percentage = 0

# Enter Marks
def enter_marks():
    global marks
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    print("Marks Entered Successfully!")

# Calculate Percentage
def calculate_percentage():
    global percentage
    if len(marks) == 0:
        print("Please enter marks first!")
    else:
        total = sum(marks)
        percentage = total / len(marks)
        print("Percentage =", percentage)

# Assign Grade
def assign_grade():
    if percentage == 0:
        print("Please calculate percentage first!")
    else:
        if percentage >= 90:
            print("Grade: A+")
        elif percentage >= 75:
            print("Grade: A")
        elif percentage >= 60:
            print("Grade: B")
        elif percentage >= 50:
            print("Grade: C")
        else:
            print("Grade: Fail")

while True:
    print("\n--- Student Result System ---")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enter_marks()
    elif choice == 2:
        calculate_percentage()
    elif choice == 3:
        assign_grade()
    elif choice == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
