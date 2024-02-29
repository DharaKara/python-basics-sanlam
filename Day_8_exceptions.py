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
        year_input = input("Please tell me your year of birth: ")
        year = int(year_input)
        current_year = datetime.now().year
        age = current_year - year
        print(f"Your age is {age}")
    except ValueError as ve:
        print(f"Error: {ve}")
        print("Please enter a valid year.")
    except TypeError as te:
        print(f"Error: {te}")
        print("Unexpected error occurred. Please try again.")
    except (
        Exception
    ) as e:  # use only for worse case scenarios when you dont know what to expect, catches all errors
        print(f"Unexpected error: {e}")
    finally:
        print("Done")


calculate_age()


# Create your own Error Class


class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} --> {self.value}"


def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)
    # match what type of error
    except NegativeNumberError as e:
        print(e)


only_positive_num()

# # Task 1
# # Please tell me your year of birth -> 2000
# # Your age is 24
