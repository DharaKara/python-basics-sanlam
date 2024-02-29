# def math_divide(n1, n2):
#     try:
#         result = n1 / n2
#         print("The answer is ", result)
#     except ZeroDivisionError:
#         # when error happens
#         print("You cannot divide by zero! 💀")
#     else:
#         # when no error
#         print("Division was successful ✅")
#     finally:
#         # no error or error, regardless will run
#         print("Operation done 🙂✌️")


# print("Hiii")
# math_divide(10, 5)
# math_divide("anb", 1) # type error

from datetime import datetime


def calculate_age():
    try:
        year = int(input("Please tell me your year of birth: "))
        current_year = datetime.now().year
        age = current_year - year
        print(f"Your age is {age}")
    except ValueError:
        print("Incorrect input. Please enter a valid year.")
    finally:
        print("Done")


calculate_age()

# # Task 1
# # Please tell me your year of birth -> 2000
# # Your age is 24

# # Assignment
# # 1. @property,  @balance.setter
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self._balance = value


# # Example usage
# acc = BankAccount(100)
# print(acc.balance)  # Output: 100
# acc.balance = 150
# print(acc.balance)  # Output: 150
# acc.balance = -50  # Raises ValueError


# # 2. Creating you own decorator
# # Using function
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")


# say_hello()


# # Using classes
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = self.func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result


# @MyDecorator
# def say_hello():
#     print("Hello!")


# say_hello()
