# conditionals in python - if, elif and else statements
# basic comparison, handling equal values
number1 = 10 # check for equality
number2 = 10
# comparing two numbers and printing the result
if number1>number2:
  print("number1 is greater")
elif number1==number2: # to handle equal values
  print("both numbers are equal")
else:
  print("number2 is greater")

# applying conditionals to user input
p1= input('Please give your name: ')
h1= int(input('Please provide height in cm: '))
p2= input('Please give your name: ')
h2= int(input('Please provide height in cm: '))
# implementing conditional logic based on user input
if (h1>h2):
  print(f"{p1} is taller")
elif (h1==h2):
  print(f"{p1} and {p2} is of the same height")
else:
  print(f"{p2} is taller")

# understanding/demonstrating elif and else
choice = input ("Choose one option: A, B, or C: ")
# elif for multiple conditions and else for final default condition
if choice == 'A':
  print("You chose A.")
elif (choice == "B"):
  print("You chose B.")
else:
  print("You chose C.")

# exercise 1: ice cream stock checker
# V1 - initial approach with multiple if/elif statements
fav_flavour = input("Enter flavour: ")
stock1="vanilla"
stock2="lime"
stock3="chocolate"
if (fav_flavour == stock1):
  print(f'yes, we do have the flavour {stock1} you want')
elif (fav_flavour == stock2):
  print(f'yes, we do have the flavour {stock2} you want')
elif (fav_flavour == stock3):
  print(f'yes, we do have the flavour {stock3} you want')
else: 
  print('sorry! we ran out of stock')

# V2 - simplified approach using logical or
if (fav_flavour == stock1) or (fav_flavour == stock2) or (fav_flavour == stock3):
  print("Yes, we do have it.")
else:
  print("Sorry, we are out of stock.")

# V3 - improving it further with membership operator (in)
stocks = "vanilla, lime, chocolate"
if fav_flavour in stocks:
  print("Yes, we do have it.")
else:
  print("Sorry, we are out of stock.")

# V4 - applying ternary operator for conciseness
result = "Yes, we do have it" if fav_flavour in stocks else "Sorry, we are out of stock."
print(result)

# operators - unary (single operand: not, bitwise)
# binary (two operands: arithmetic, comparison, logical)
# ternary (concise if-else in one line)

# exercise: secret code extractor
# V1 finding the key
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

keyID = message.find("🔑") # <- returns index val
secretMsg = message[(keyID + 1):] # <- slicing to get code
output = secretMsg.upper() # <- without changing original capitilizing
print(output) # SECRET_CODE✌️
if (output == code):
  print("You are an hacker 🎊")
else:
  print("Try again")

# V2 handling the absense if no key
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

keyID = message.find("🔑") # <- returns index val
if (keyID != -1):
  secretMsg = message[(keyID + 1):] # <- slicing to get code
  output = secretMsg.upper() # <- without changing original capitilizing
  print(output) # SECRET_CODE✌️
  if (output == code):
    print("You are an hacker 🎊")
  else:
    print("Try again")
else:
  print("No, secret is present")

# V3 adjusted for correct conditional task in V2
message = "    🚨🔍📱🔑****secret_code✌️(((("
code = "SECRET_CODE✌️"

keyID = message.find("🔑") # <- returns index val
if (keyID != -1):
  secretMsg = message[(keyID + 1):] # <- slicing to get code
  output = secretMsg.upper().strip("*").strip("(") # <- without changing original capitilizing
  print(output) # SECRET_CODE✌️
  if (output == code):
    print("You are an hacker 🎊")
  else:
    print("Try again")
else:
  print("No, secret is present")

# V4 adjusted for correct logical flow from V2
message = "    🚨🔍📱🔑****secret_code✌️(((("
code = "SECRET_CODE✌️"

keyID = message.find("🔑") # <- returns index val
if (keyID != -1):
  output = message[(keyID + 1):].upper().strip("*").strip("(") 
  print(output) # SECRET_CODE✌️
  if (output == code):
    print("You are an hacker 🎊")
  else:
    print("Try again")
else:
  print("No, secret is present")
