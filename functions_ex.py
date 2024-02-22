library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Advance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]

# Task 1: Add Book Function
# def add_book(library, new_book):
#     library.append(new_book)

# new_book = {"title": "You", "author": "Mark Lutz", "year": 2023, "available": True}
# print(add_book(library, new_book))

# Task 2: Search Books by Author Function
# def search_by_author(library, author_name):
#     result = []
#     for book in library:
#         if book["author"] == author_name:
#             result.append(book)
#     return result

# result = search_by_author(library, "Mark Lutz")
# print(result)

# Task 3: Check out book function
# def check_out_book(library,title):
#   result = []
#   for book in library:
#     if (book["title"] == title) and (book["available"] == "True"):
#       result = "Book is available"
#     else:
#       result = "Book is not available"
#     return result

# result = check_out_book(library, "Learning Pythin I")

# Task 3 Check-out book function
# def check_out_book(library, title):
#   for book in library:
#     if book["title"] == title and book["available"]:
#       book["available"] = False
#       return f"{title} has been checked out."
#   return f"{title} is not available."

# print(check_out_book(library, "Fluent Python"))  


      
