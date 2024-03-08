import json

# data = {
#     "employees": [
#         {"name": "Alice", "age": 30, "department": "Sales"},
#         {"name": "Bob", "age": 25, "department": "Marketing"},
#     ]
# }

# print(type(data))
# print(data["employees"][0]["age"])
# data_json = json.dumps(data, indent=4)
# print(data_json, type(data_json)) # data_json is a string
# # print(data_json["employees"]) # Error

student1_json = """
        {
            "name":"gemma",
            "gender":"female"
    }
"""
# # JSON - JavaScript Object Notation
student = json.loads(student1_json)
print(student, type(student), student["name"])
# print(student1_json)

# # First-Class Function -> Function treated as a value
# sport = {"name": "Dhoni", "dbl": lambda x: x * 2}  # valid dictionary
# print(sport["dbl"](100))
# # sport_json = json.dumps(sport) # JSON serializable (convert) | cant convert dict to json because it contains funcs
# # print(sport_json) # invalid JSON
