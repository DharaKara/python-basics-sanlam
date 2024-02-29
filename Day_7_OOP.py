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


# Encapsulation | putting in all together in one container | giving access
# Bank Account
class Bank:
    interest_rate = 0.2
    total_accounts = 0

    def __init__(self, acc_no, name, balance):
        # instance variables
        self.acc_no = acc_no  # public variable
        self.name = name
        self._balance = (
            balance  # private variable - can't change and access __ -> protected _
        )
        self.transactions = []
        self.last_interest_applied = datetime.now()
        Bank.total_accounts += 1

    def display_balance(self):
        return f"Your balance is: R{self._balance:,}"

    @classmethod  # cls --> Class
    def update_interest_rate(cls, rate):
        Bank.interest_rate = rate

    # @staticmethod # holds things together inside but can be called outside of class
    # doesnt need updating or changing | no cls, self just call classname. | normal func
    @classmethod
    def get_total_no_accounts(cls):
        return f"In total we have {cls.total_accounts} accounts."

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.transactions.append(("withdraw", amount, datetime.now()))
            return f"Success. {self.display_balance()}"
        else:
            return "Failure. Insufficient funds."

    def deposit(self, amount):
        if amount > 0:
            self._balancebalance += amount
            self.transactions.append(("deposit", amount, datetime.now()))
            return f"Success. {self.display_balance()}"
        else:
            return "Failure. Invalid deposit amount."

    def print_statement(self):
        if not self.transactions:
            print("No transactions.")
        print("{:<3}  {:<10}  {:<9}  {}".format("id", "Date", "Type", "Amount"))
        for i, (trans_type, amount, date) in enumerate(self.transactions, start=1):
            print(
                "{:<3}  {:<10}  {:<9}  R{:<,.2f}".format(
                    i, date.strftime("%d %b"), trans_type.capitalize(), amount
                )
            )

    def apply_interest(self):
        self.__balance += self.__balance * Bank.interest_rate


class SavingsAccount(Bank):
    interest_rate = 0.05


# the below code wasn't needed | overiding not needed
# def __init__(self, acc_no, name, balance): # <- call when adding variables
#     super().__init__(acc_no, name, balance)

# def apply_interest(self):
#     interest_amount = self._Bank__balance * SavingsAccount.interest_rate
#     self._Bank__balance += interest_amount


# Magic methods - 1. __repr__, 2. __str__
class CheckingAccount(Bank):
    transaction_fee = 1

    def withdraw(self, amount):
        total_amount = amount + CheckingAccount.transaction_fee
        return super().withdraw(total_amount)

    def __str__(self):
        return f"This account belongs to {self.name} and has a balance of {self._balance:,}"

    def __repr__(self):  # -> repr(alex) reconstructing
        """DX: String --> Class"""
        return f"CheckingAccount({self.acc_no}, '{self.name}', {self._balance})"

    def __add__(self, other):  # -> alex + caleb
        return self._balance + other._balance


# Task 1
# gemma = SavingsAccount(123, "Gemma Porrill", 1000)
# gemma.apply_interest()
# print(gemma.display_balance())  # Output: Your balance is: R1,050.00

# # Task 2
# alex = CheckingAccount(126, "Alex Lazarus", 100)
# print(alex.withdraw(50))  # Output: Remaining balance: R50.00

# Task 1 - objects/instances of class
# gemma = Bank(123, "Gemma Porrill", 15_000)
# dhara = Bank(124, "Dhara Kara", 50_001)
# caleb = Bank(125, "Caleb Potts", 100_000)
# alex = Bank(126, "Alex Lazarus", 100)

# Task 2 display balance and 3 withdraw
# print(caleb.withdraw(2_000))

# # Task 4 deposit
# print(dhara.deposit(10_000))
# print(dhara.withdraw(2_000))
# print(dhara.withdraw(8_000))

# PEP 8: Python Enhancement Proposals
# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000
# print(dhara.print_statement())

# print(gemma.display_balance())

# Bank.update_interest_rate(0.10)
# alex.apply_interest()
# print(alex.display_balance())

# Task
# print(Bank.get_total_no_accounts())  # output: In total we have 4 accounts

# -----------------------------------------------------

# # Task 1 perimeter func static, Task 2 the rest
# class Circle:
#     pi = 3.14159  # Class variable

#     def __init__(self, radius):
#         self.radius = radius

#     @staticmethod
#     def perimeter(radius):
#         return round(2 * Circle.pi * radius, 2)

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

#     def calculate_area(self):
#         return Circle.pi * self.radius**2


# print(Circle.perimeter(10))  # 10 --> radius

# circle1 = Circle(2)  # radius
# print(circle1.calculate_area())

# # the below 2 lines says you need to use a class method
# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())

# -----------------------------------------------------------


# Inheritance
# class Animal:  # base
#     def __init__(self, name):
#         self.name = name

#     # methods/attributes
#     def speak(self):
#         return "Some sound"


# class Dog(Animal):  # child
#     def __init__(self, name, speed):
#         super().__init__(name)
#         self.speed = speed

#     def run(self):
#         return "🐶 wags tails!!"

#     # Overiding methods -> Polymorphism
#     def speak(self):
#         return "Woof!! 🐕‍🦺"

#     def speed_bonus(self):
#         return f"Running at {self.speed * 2}Km/hr"


# toby = Animal("toby")
# maxy = Dog("maxy", 20)

# print(toby.speak())
# print(maxy.name)
# print(maxy.speak())
# print(maxy.run())


# ---------------------------------------------------------
