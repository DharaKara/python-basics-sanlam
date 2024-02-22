# declaring variables
name = "John Doe"  # string - text
age = 30  # integer - whole numbers
height = 5.11  # float - decimal numbers
is_adult = True  # boolean - truth values

# type conversions
age_str = str(age)  # int to string
height_str = "5.11"
height_float = float(height_str)  # str to float

# user input
name = input("Enter your name: ")
print(f"Hello, {name}!")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")
favourite_color = input("What's your favourite color? ")
print(f"Hello, {name}! You are {age} years old and love {favourite_color}.")

# string formatting
print(f"Hello, {name}! Next year, you will be {int(age)+1} years old.")

# arithmetic operators
print(5 + 3)  # addition
print(10 - 2)  # subtraction
print(4 * 2)  # multiplication
print(16 / 2)  # division
print(9 % 2)  # modulus
print(2**3)  # exponentiation
print(7 // 2)  # floor division

# comparision operators
print(5 == 5)  # equal
print(5 != 3)  # not equal
print(5 > 3)  # greater than
print(3 < 5)  # less than
print(5 >= 5)  # greater than or equal to
print(3 <= 5)  # less than or equal to

# logical operators
print(True and True)  # and
print(True or False)  # or
print(not True)  # not

# bitwise operators
print(5 & 3)  # and
print(5 | 3)  # or
print(5 ^ 3)  # xor
print(~5)  # not
print(5 << 1)  # left shift
print(5 >> 1)  # right shift

# exercise 1: calculate area of a circle
radius = int(input("Radius: "))
area = 3.14 * radius**2
print = (f"Area of the circle: {area}.")
