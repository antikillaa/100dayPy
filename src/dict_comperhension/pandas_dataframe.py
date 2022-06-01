import pandas

student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

data = pandas.DataFrame(student_dict)

# for (key, value) in data.items():
#     print(value)

for (index, row) in data.iterrows():
    print(row.student)
