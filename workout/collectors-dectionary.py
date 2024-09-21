students = {
    'student1': {
        'name': 'Alice',
        'age': 20,
        'courses': ['Math', 'Physics'],
    },
    'student2': {
        'name': 'Bob',
        'age': 22,
        'courses': ['Chemistry', 'Biology'],
    },
    'student3': {
        'name': 'Charlie',
        'age': 19,
        'courses': ['History', 'Literature'],
    },
}
# -------------------------------Accessing data from the nested dictionary
print(students['student1']['name'])  # Output: Alice
print(students['student2']['courses'])  # Output: ['Chemistry', 'Biology']

# --------------------------------Adding a new student
students['student4'] = {
    'name': 'David',
    'age': 21,
    'courses': ['Computer Science', 'Art'],
}

# ----------------------------------Updating a student's data
students['student1']['age'] = 21

# ------------------------------------Iterating through the nested dictionary
for student_id, student_info in students.items():
    print(f"\n{student_id}:")
    for key, value in student_info.items():
        print(f"{key}: {value}")
#  Outer Loop: for student_id, student_info in students.items():
# Purpose: This loop iterates over the outer dictionary (students).
# students.items(): This method returns a view object that displays --
# list of the dictionary's key-value tuple pairs. In this case, each item is a tuple where:
# student_id is the key (e.g., 'student1', 'student2').
# student_info is the value, which is another dictionary containing that student's details.

# Outer loop: Iterates through each student in the students dictionary.
# Inner loop: Iterates through each attribute of the student (like name, age, and courses).