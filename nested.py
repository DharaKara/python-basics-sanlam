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
# Task 1 - 5mins organise average by class
# averages = {}
# for class_name, students in classes.items():
#     total_grades = 0
#     total_students = len(students)
#     for student in students:
#         total_grades += sum(student["grades"])
#     class_average = total_grades / (total_students * len(student["grades"]))
#     averages[class_name] = "{:.2f}".format(class_average)
# # interpolation and fstring
# print(averages)

# ragavs answer
def find_avg(nums):
  return round(sum(nums) / len(nums), 2)

# classes_avg = {}
# for cls_name, students in classes.items():
#   class_students_avg = []
#   for student in students:
#     class_students_avg.append(find_avg(student['grades']))
#   classes_avg[cls_name] = find_avg(class_students_avg)

# print(classes_avg)
# --------------------------------------------
# Task 2 - Student name's unique
# student_averages = {}
# for class_name, students in classes.items():
#     for student in students:
#         name = student["name"]
#         grades = student["grades"]
#         avg_grade = round(sum(grades) / len(grades), 2)
#         if class_name not in student_averages:
#             student_averages[class_name] = {}
#         student_averages[class_name][name] = avg_grade
# print(student_averages)

# ragavs answer
# students_avg_dict = {}
# for cls_name, students in classes.items():
#   students_dict = {}
#   for student in students:
#     students_dict[student['name']] = find_avg(student['grades'])
#   students_avg_dict[cls_name] = students_dict
# pprint(students_avg_dict)

# students_avg_dict = {}
# for cls_name, students in classes.items():
#   students_avg_dict[cls_name] = {student['name']: find_avg(student['grades'])  for student in students}
# pprint(students_avg_dict)
# ---------------------------------------------
# Task 3 - Task 2 with dictionary comprehension
# students_avg_dict = {
#     cls_name: {student['name']: find_avg(student['grades']) for student in students}
#     for cls_name, students in classes.items()
# }
# pprint(students_avg_dict) 

# students_avg_dict = {cls_name: {student['name']: find_avg(student['grades']) for student in students} for cls_name, students in classes.items()}
# pprint(students_avg_dict)

# f5 for debugging
# f2 for renaming variable
# pprint for neatening output


