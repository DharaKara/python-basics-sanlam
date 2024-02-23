from math import pi
from datetime import datetime

# salary = 420_000_000
# print(salary) #DX readibility

# print(f"Dhara's salary is R{salary:,}")
# print(f"Dhara's salary is R{salary:_}")

# print(f"The PI value is: {round(pi)}")
# print(f"The PI value is: {pi:.2f}")
# print(f"The PI value is: {pi:.3f}")

# name = "Lilitha"
# person = "Quinlan"
# print(f"{name:>20}:")
# print(f"{name:<20}:")
# print(f"{name:^20}:")

# print(f"{person:*>20}:")
# print(f"{person:#>20}:")
# print(f"{person:$>20}:")

# caleb = "0.925"
# print(f"The test results are out and Caleb got {caleb:.2%}") # 0.925 -> 92.5

# now = datetime.now()
# print(now)
# print(f"The Current date is: {now:%d-%m-%Y}")
# print(f"The Current date is: {now:%d/%m/%Y}")

# recipe = {
#   "name": "Spaghetti Carbonara",
#   "servings": 4,
#   "ingredients": ["200g spaghetti", "100g pancetta", "2 eggs", "1/2 cup grated Parmesan", "1 clove garlic"]
# }
# print("{:=^33}".format(recipe['name']))
# for ingredient in recipe["ingredients"]:
#     print(f"- {ingredient}")
# print(f"Serves: {recipe['servings']} people")

# # Task 2 party invite
guests = ["Alice", "Bob", "Charlie"]
party_date = datetime(2024, 3, 14)
# Party Invite Output
for guest in guests:
    print(f"*{guest:^25}*")
    print(f"You are invited to the party on {party_date:%B %d, %Y}!")

classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}

# Task 1
average_grades = {}
for class_name, students in classes.items():
    total_grade = sum(sum(student["grades"]) for student in students)
    average_grade = total_grade / (len(students) * len(students[0]["grades"]))
    average_grades[class_name.lower()] = round(average_grade, 2)
print("Task 1 output:", average_grades)

