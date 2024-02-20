# mutable
# marks=[1,2,3,4,5,6, 7, 8, 9]
# copy_of_marks=marks[0:len(marks)]
# print()
# print(list)

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

lengths=[]
for heroes in avengers: 
  lengths.append(len(heroes))
print(lengths)


