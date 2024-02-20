stock1="vanilla"
stock2="lime"
stock3="chocolate"
answer=input('enter flavour: ')
if (answer==stock1):
  print(f'yes, we do have the flavour {stock1} you want')
elif (answer==stock2):
  print(f'yes, we do have the flavour {stock2} you want')
elif (answer==stock3):
  print(f'yes, we do have the flavour {stock3} you want')
else: 
  print('sorry! we ran out of stock')