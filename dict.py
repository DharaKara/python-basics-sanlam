# dict
# person = {
#   "name": "Siya Kolisi",
#   "age": 32,
#   "country": "South Africa",
#   "sport": "Ruby"
# }

# # iterables
# print(person.keys())
# print(person.values())
# print(person.items())

# # loops
# for key, value in person.values():
#   print(key, value)

# books = [
#   {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
#   {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
#   {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
#   {"title": "Sapiens", "rating": 4.9, "genre": "History"},
#   {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
# ]

# Task 1: Highly rated books of 4.7 or more
# highly_rated_books = []
# for book in books:
#     if book["rating"] >= 4.7:
#         highly_rated_books.append(book["title"])
# print(highly_rated_books)

# Task 2: List comprehension
# highly_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
# print(highly_rated_books)

# Task 2: Ascending order
# highly_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
# print(sorted(highly_rated_books)) # <-- will not mutate array, but instead just give a copy version whereas .sort() will mutate list

# Task 1 - create new product only
# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]

# product_name = input("Enter product name: ")
# quantity = int(input("Enter quantity: "))
# price = float(input("Enter price: "))

# inventory.append({"name": product_name, "quantity": quantity, "price": price})
# inventory = [
#   {"name": "Apple", "quantity": 30, "price": 0.50},
#   {"name": "Banana", "quantity": 20, "price": 0.20}
# ]
# -------------------------------

# Task 2 - if product exists then update quantity and price, if does not exist create new product
# product_name = input("Enter product name: ")
# quantity = int(input("Enter quantity: "))
# price = float(input("Enter price: "))

# product_exists = False
# for item in inventory:
#   if item["name"] == product_name:
#       item["quantity"] += quantity
#       item["price"] = price
#       product_exists = True
#       break

# if not product_exists:
#   inventory.append({"name": product_name, "quantity": quantity, "price": price})

# print("Updated Inventory:")
# for item in inventory:
#   print(item)
# -----------------------------------------------------------------------------

# Task 3 - Improvement for ... else
# product_name = input("Enter product name: ")
# quantity = int(input("Enter quantity: "))
# price = float(input("Enter price: "))

# for item in inventory:
#   if item["name"] == product_name:
#       item["quantity"] += quantity
#       item["price"] = price
#       break
# else:
#   inventory.append({"name": product_name, "quantity": quantity, "price": price})

# print("Updated Inventory:")
# for item in inventory:
#   print(item)

# Guest List for Eligible
guests = [{
    "name": "Alice",
    "age": 25,
    "code": "VIP123"
}, {
    "name": "Bob",
    "age": 17,
    "code": "VIP123"
}, {
    "name": "Charlie",
    "age": 30,
    "code": "VIP123"
}, {
    "name": "Dave",
    "age": 22,
    "code": "GUEST"
}, {
    "name": "Eve",
    "age": 29,
    "code": "VIP123"
}]
blacklist = ["Dave", "Eve"]

# Output
# People who are 21 or above and VIP123
# Blacklist are not allowed
# ["Alice", "Charlie"]

# allowed_guests = []
# for guest in guests:
#     if (guest["name"] not in blacklist) and (guest["age"] >= 21) and (guest["code"] == "VIP123"):
#       allowed_guests.append(guest["name"])
# print(allowed_guests)

# allowed_guests = [guest["name"] for guest in guests if guest["age"] >= 21 and guest["code"] == "VIP123" and guest["name"] not in blacklist]
# print(allowed_guests)
# person={
#   "name": "Siya Kolisi",
#   "age": 32,
#   "address": {
#     "city": "Port Elizabeth",
#     "country": "South Africa",
#   },
#   "stats":{}
#   "school": "Grey high school",
#   "height": 186,
#   "sport": "Ruby"
# }
# print(person["address"]["city"])

# list of tuples -- > enumerate
# nums=[90, 50, 80]
# for num in enumerate(nums):
#   print(idx, num)

# Task 1: Increase experience by 1 for each employee
# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]

# updated_employees = [
#   {"name": emp["name"], "experience": emp.get("experience", 0) + 1}
#   for emp in employees
# ]

# print(updated_employees)
# ---------------------------------------------------------------

# Task 2: Determine status
# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]

# updated_employees = [
#   {
#       "name": emp["name"],
#       "experience": emp.get("experience", 0) + 1,
#       "status": "Junior" if emp.get("experience", 0) < 3 else ("Mid level" if emp.get("experience", 0) < 5 else "Senior")
#   }
#   for emp in employees
# ]

# print(updated_employees)
# --------------------------------------------------------------

movie = {"name": "Mr Bones", "year": 2001}

detail = {"actor": "Leon", "director": "Dzithendo"}

movie_details = {**movie, **detail}
print(movie_details)

price = [1000, 1200, 400]
price_copy = [*price]
price_copy1 = [50, 40, *price, 60]
print(price_copy, price_copy1)
