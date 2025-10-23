name = str(input("What is your name? "))

subjects = []
grades = []

for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    grade = float(input(f"What is your grade in {subject} out of 100: "))
    subjects.append(subject)
    grades.append(grade)