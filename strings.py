# immutable (cannot be changed once created)
# accessing characters
quote = "I love python"
# demonstrating character access by index
print(quote[0]) # I
print(quote[2]) # l
# quote[2] = 'x' # uncommenting this line will give an error as immutable

# string methods - using methods does not change original string
print(quote.upper()) # I LOVE PYTHON
print(quote) # I love python

# string methods (manipulation)
msg = "Hi, all"
print(msg.upper()) # HI, ALL <- capitalises each letter
print(msg.lower()) # hi, all <- lowers each letter
print(msg.title()) # Hi, All <- capitalises the first letter of each word
print(msg.capitalize()) # Hi, all <- capitalises only the first letter of the string

# trimming whitespace
quote1 = "     Dream... you sleep"
trimmed_quote = quote.strip()
print(trimmed_quote) # Dream... you sleep <- just removes space from left

# striping specific characters
quote2 = "---Dream... sleep---"
print(quote2.strip("-")) # Dream... you sleep <- takes dashes out from both sides
print(quote2.lstrip("-"))  # Dream... you sleep--- <- takes dashes out from left
print(quote2.rstrip("-"))  # ---Dream... you sleep <- takes dashes out from right

# finding substrings
quote3 = "Dream... you sleep"
print(quote3.find('something')) # 20 <- index 20
print(quote3.find('Dream')) # 0 <- takes first 1 if more than one, in this case pos 0
print(quote3.find('**')) # -1 <- none found

# immutable strings and replacement 
new_quote = quote3.replace("Dream","🛌")
print(new_quote) # 🛌... you sleep
print(quote3) # Dream... you sleep <- unchanged

# counting, validating and length
print(quote3.count("Dream")) # 2
print(quote3.startswith("Dream")) # True
print(quote3.endswith("sleep")) # True
bage_no = "45445"
print(bage_no.isdigit()) # True
name = "ark" 
print(name.islower()) # True
print(len(name)) # 3