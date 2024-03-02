# # Q1 - data sorting and ranking
# # Setup Code
# students = [
#     {"name": "Alice", "grade": 88},
#     {"name": "Bob", "grade": 75},
#     {"name": "Charlie", "grade": 93},
# ]
# # Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.
# sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
# for i, student in enumerate(sorted_students):
#     student["rank"] = i + 1
# for student in sorted_students:
#     print(student)

# Q2 - merging data from two lists
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.
# merged = []
# for employee in employees:
#     for salary in salaries:
#         if employee["id"] == salary["id"]:
#             merged.append({**employee, **salary})
# or with list comprehension
merged = [
    {**employee, **salary}
    for employee in employees
    for salary in salaries
    if employee["id"] == salary["id"]
]
for item in merged:
    print(item)
