from pprint import pprint
classes = {
    "Class A": [{
        "name": "Alice",
        "grades": [82, 90, 88]
    }, {
        "name": "Bob",
        "grades": [78, 81, 86]
    }, {
        "name": "Charlie",
        "grades": [85, 85, 87]
    }],
    "Class B": [{
        "name": "Dave",
        "grades": [92, 93, 88]
    }, {
        "name": "Eve",
        "grades": [76, 88, 91]
    }, {
        "name": "Frank",
        "grades": [88, 90, 92]
    }]

}

# Find average of each class
# Task 1 - 5mins
averages = {}

for class_name, students in classes.items():
    total_grades = 0
    total_students = len(students)
    for student in students:
        total_grades += sum(student["grades"])
    class_average = total_grades / (total_students * len(student["grades"]))
    averages[class_name] = "{:.2f}".format(class_average)

print(averages)

# Task 2
# Student name's unique
# output = {
#     "Class A": {
#         "Alice": 90.5,
#         "Bob": 84.5,
#         "Charlie": 90
#     },
#     "Class B": {
#         "Dave": 92.5,
#         "Eve": 86.5,
#         "Frank": 95
#     }
# }

# Task 3 - Task 1 with last comprehension
averages = {}
for class_name, students in classes.items():
    class_average = sum(sum(student["grades"]) for student in students) / (len(students) * len(students[0]["grades"]))
    averages[class_name] = "{:.2f}".format(class_average)

pprint(averages)


