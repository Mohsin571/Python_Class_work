# Function to calculate grade
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# List to store student data
students = []

# Collect data for 10 students
for i in range(10):
    name = input(f"Enter name of student {i + 1}: ")
    score = float(input(f"Enter score of {name}: "))
    grade = calculate_grade(score)
    students.append({'name': name, 'score': score, 'grade': grade})

# Display student data
print("\nStudent Grades:")
for student in students:
    print(f"Name: {student['name']}, Score: {student['score']}, Grade: {student['grade']}")
