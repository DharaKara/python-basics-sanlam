from pprint import pprint
import json

# Parse the JSON data
bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""

# Task 1
users = json.loads(bank_data)
for user in users:
    if user["isActive"]:
        user["balance"] *= 1.10
updated_bank_data = json.dumps(users, indent=4)
pprint(updated_bank_data)

# Task 2
users = json.loads(bank_data)
updated_users = [
    {**user, "balance": user["balance"] * 1.10} if user["isActive"] else user
    for user in users
]
updated_bank_data = json.dumps(updated_users, indent=4)
pprint(updated_bank_data)

# converting to json -> dumps
# converting to dict -> loads

# files
with open("bank_accounts.json", "w") as file:
    json.dump(updated_users, file, indent=4)

with open("bank_accounts.json", "r") as file:
    data = json.load(file)
    print(data, type(data))
