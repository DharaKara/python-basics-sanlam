p1= input('please give your name')
h1= int(input('please provide height in cm'))
p2= input('please give your name')
h2= int(input('please provide height in cm'))

if (h1>h2):
  print(f"{p1} is taller")
elif (h1==h2):
  print(f"{p1} and {p2} is of the same height")
else:
  print(f"{p2} is taller")