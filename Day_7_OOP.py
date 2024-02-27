from datetime import datetime
#  How not to do it 
# class Car0:
#     Car0.name="Toyata"
#     ca

# Car --> blueprint | class blueprint object
# DRY
# class Car:
#     def __init__(self, name, engine, wheels, doors):
#         self.name = "Ferrari"
#         self.engine = "v4"
#         self.wheels = 4
#         self.doors = 4
# self --> to the object created
# ferrari --> object

# ferrari = Car("Ferrari", "v8", 4, 2)
# print(ferrari.name, ferrari.wheels)

# Bank Account
class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("withdraw", amount, datetime.now()))
            return f"Success. {self.display_balance()}"
        else:
            return "Failure. Insufficient funds."

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(("deposit", amount, datetime.now()))
            return f"Success. {self.display_balance()}"
        else:
            return "Failure. Invalid deposit amount."

    def print_statement(self):
        if not self.transactions:
            print("No transactions.")
        print("{:<3}  {:<10}  {:<9}  {}".format("id", "Date", "Type", "Amount"))
        for i, (trans_type, amount, date) in enumerate(self.transactions, start=1):
            print("{:<3}  {:<10}  {:<9}  R{:<,.2f}".format(i, date.strftime('%d %b'), trans_type.capitalize(), amount))

# Task 1
gemma = Bank(123, "Gemma Porrill", 15_000)
dhara = Bank(124, "Dhara Kara", 50_001) 
caleb = Bank(125, "Caleb Potts", 100_000)    

# Task 2 and 3
print(caleb.withdraw(2_000))

# Task 4
print(dhara.deposit(10_000))
print(dhara.withdraw(2_000))
print(dhara.withdraw(8_000))

# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount  
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000
print(dhara.print_statement())