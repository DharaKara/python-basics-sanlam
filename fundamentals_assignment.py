# # Q1. Data Sorting and Ranking
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
# # ---------------------------------
# # Q2. Merging Data from Two Lists
# # Setup Code
# employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
# salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]
# # Expected Task: Merge these lists into a single list of dictionaries by matching the "id" field, including all keys.
# # merged = []
# # for employee in employees:
# #     for salary in salaries:
# #         if employee["id"] == salary["id"]:
# #             merged.append({**employee, **salary})
# # or with list comprehension
# merged = [
#     {**employee, **salary}
#     for employee in employees
#     for salary in salaries
#     if employee["id"] == salary["id"]
# ]
# for item in merged:
#     print(item)
# # ---------------------------------
# # Q3. Advanced Filtering with Multiple Conditions
# # Setup Code
# products = [
#     {"id": 1, "category": "Electronics", "price": 850},
#     {"id": 2, "category": "Furniture", "price": 1200},
#     {"id": 3, "category": "Electronics", "price": 400},
# ]
# # Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.
# filtered_products = [
#     product
#     for product in products
#     if product["category"] == "Electronics" and product["price"] < 500
# ]
# print(filtered_products)
# # ---------------------------------
# # Q4. Complex Data Transformation
# # Setup Code
# orders = [
#     {
#         "order_id": 1,
#         "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
#     },
#     {
#         "order_id": 2,
#         "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
#     },
# ]
# # Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.
# product_quantities = {}
# for order in orders:
#     for item in order["items"]:
#         product = item["product"]
#         quantity = item["quantity"]
#         if product in product_quantities:
#             product_quantities[product] += quantity
#         else:
#             product_quantities[product] = quantity
# print(product_quantities)
# # ---------------------------------
# # Q5. Data Consolidation and Summarization
# # Setup Code
# transactions = [
#     {"date": "2021-01-01", "amount": 100, "category": "Food"},
#     {"date": "2021-01-01", "amount": 200, "category": "Transport"},
#     {"date": "2021-01-02", "amount": 150, "category": "Food"},
# ]
# # Expected Task: Summarize the total amount spent per category.
# category_totals = {transaction["category"]: 0 for transaction in transactions}
# for transaction in transactions:
#     category_totals[transaction["category"]] += transaction["amount"]
# print(category_totals)
# # ---------------------------------
# Q6. Grouping and Aggregating Data
# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.
# ---------------------------------
# Q7. Lambda Functions for Spell Power
# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.
# ---------------------------------
# Q8. Map Transformation for Potion Ingredients
# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.
# ---------------------------------
# Q9. Magical Book Filter and Formatter
# Setup Code
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.
# ---------------------------------
# Q10. Wizard Duel Game Class
# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.
# ---------------------------------
# Q11. Custom Error Handling in Potion Making
# Setup Code
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.
# ---------------------------------
# Q12. Hogwarts Library Database Query
# Setup Code
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.
# ---------------------------------
# Q13. Hogwarts House Points Calculator
# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.
# ---------------------------------
# Q14. Class Inheritance for Magical Creatures
# Setup Code
# Expected Task: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.
# ---------------------------------
# Q15. Custom Sorting with Lambda for Magical Artifacts
# Setup Code
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.
# ---------------------------------
# Q16. Wizard Profile Generator with f-strings
# Setup Code
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.
# ---------------------------------
# Q17. Magical Creature Adoption Matching
# Setup Code
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.
# ---------------------------------
# Q18. Advanced Potion Making with Nested Loops
# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.
# ---------------------------------
# Q19. Nested Data Manipulation
# Setup Code
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.
# ---------------------------------
# Q20. Implementing a Custom Sort Function
# Setup Code
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False},
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").
