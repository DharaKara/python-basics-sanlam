quote="I love python"
# use slicing to extract parts of the string
slice1 = quote[2:6] # love
slice2 = quote[7:] # python
print(slice1)
print(slice2)

print(quote[-1]) # n
print(quote[-6]) # python, so -1 is last letter of string
print(quote[::3]) # Ilphn, start:end:skip
# remember in slice it's -1 so skips every second letter

# exploring advance slicing features
reverse_first_char = quote[-1]
substring = quote[-6:]
skip_characters = quote[::3]
print(reverse_first_char)
print(substring)
print(skip_characters)

# reversing the whole string using slicing, -1 means skipping none
print(quote[::-1]) # nohtyp evol I

