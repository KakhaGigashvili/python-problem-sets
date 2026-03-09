students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    if student["house"] == "Slytherin":
            print(student["name"])


# print(students[2]["patronus"])

# for student in students:
#     print(student, students[student], sep=": ")

# for k, v in students.items():
#     print(k, v)

"""

|#    |   name    |    house     |  partniors  |
------------------------------------------------
|0    | Hermione  |  griffindor  |   Otter     |
|1    |  Harry    |  Griffindor  |   stag

"""