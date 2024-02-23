# lists are mutable (allowing dynamic modifications)
marks = [98, 75, 40, 80, 90]
print("Original list: ", marks)

# remove elements like pop demonstrates mutability
marks.pop()
print("List after .pop():", marks)

# modifying element by index
marks[2] = 85 # -> 40 to 85
print("List after modifying an element:", marks)

# adding and removing elements
subjects = ['Maths', 'Science']
subjects.append('English') # adding an element
print("After append:", subjects)

subjects.remove('Science') # removing an element
print("After remove:", subjects)

marks.insert(1, 88) # insert 88 at index 1 
print("After insert:", marks)

popped_mark = marks.pop(2)
print("After pop:", marks, " Popped element:", popped_mark)

# scrambled_message = "world the save to time no is there"
# scrambled_list=scrambled_message.split(' ')
# print(" ".join(scrambled_list[::-1]))

# num_emojis = int(input("Enter number: "))
# emoji = "😍"
# i = 0
# while i <= num_emojis:
#   print((emoji + " ") * i)
#   i += 1

# for curr in range(0,50,2):
#   print(curr)

# num_emojis = int(input("Enter number: "))
# for i in range(0, num_emojis+1):
#   print(("😍 ") * i)

# player_stats = [10, 30, 60]
# output = []
# for i in range(len(player_stats)):
#   doubled_stats = player_stats[i] * 2
#   output.append(doubled_stats)
# print(output)

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

# lengths=[]
# for heroes in avengers:
#   lengths.append(len(heroes))
# print(lengths)

# length = []
# for i in avengers:
#   if len(i) > 10:
#     length.append(i)
# print(length)

# filtered_names = [avenger.upper() for avenger in avengers if len(avenger) > 10 ]
# print(filtered_names)

# numbers = [8, 5, 7, 4, 6, 2]
# output = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
# print(output)
