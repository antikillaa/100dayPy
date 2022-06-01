import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {key: value for (key, value) in students_scores.items() if value > 50}

print(students_scores)

print(passed_students)
