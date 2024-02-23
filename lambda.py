# one line function, anonymous - nameless function
# implicitly/automatically returns
# functions are filtered as first class citizens
# 1. assign a function to variable
# 2. pass a function as argument
# 3. return a function
# add = lambda a, b: a + b
# print(add(6, 7))

# def fun():
#   x = 4 # 1
#   return x + y # 3
# fun(5) # 2

# map
# player_stats = [10, 30, 60]
# boosted_stats = map(lambda x: x * 2, player_stats)
# print(boosted_stats,list(boosted_stats))

# double_values = lambda x: x * 2
# boosted_stats = map(double_values, [10, 30, 60])

# def square(x):
#   return x*x
# super_boosted_stats=map(square, [10, 30, 60]) #normal function
# super_boosted_stats1=map(lambda x:x*x, [10, 30, 60]) #when you dont need to reuse
# print(list(super_boosted_stats))

# result1=map(lambda x: x * 2, [(10,6),(30,8),(5,60)])
# print(list(result1))

# def say_hello():
#   return "Hello, "
#             # function, string
# def greeting(hello_message, name):
#   print(hello_message()+name) # argument name
# greeting(say_hello, 'Caleb')

# print(say_hello) # higher order function greeting

# map_own 
# def map_own(fn, arr):
#   result = []
#   for x in arr:
#       result.append(fn(x))
#   return result

# arr = [10, 30, 60]
# result = map_own(lambda x: x * 2, arr)
# print(result)  

# # list comprehension
# def map_own(fn, arr):
#   return [fn(x) for x in arr]

# arr = [10, 30, 60]
# result = map_own(lambda x: x * 2, arr)
# print(result) 

# def sayHello1():
#   def msg():
#     return 'Hello, 🎊'
#   return msg
# print(sayHello1()())

# lambda x returns lambda y, impicit return, 
# currying, Hof part of functional prog
# paradigm (styles of programming)
# functional programming (all will have map func, F#, Haskell (no loops - recursion))
# OOP programming - inheritance
# procedural programming
# mathematical programming
# assigment --> what is currying and what is partials

# mul=lambda x: lambda y: x * y
# result=mul(3)(6)
# mul5=mul(5)
# mul10=mul(10)
# print(type(mul5))
# print(mul5(10))
# print(mul(3)(6))

# filter
# result1=map(lambda x:x*2, [10,30,60])
# result22=filter(map(lambda x:x>10, [10,50,60,100,6,8,30]))

# print(list(result1))
# print(list(result2))

# print(sum([10,30,60]))

#sequence - list
# 1. len
# 2. sum
# 3. sorted
# 4. max
# 5. min

print(max([10,80,30,60]))
print(min([10,-1,30,60]))

print(all([True,False,True]))

# falsy vals -> 0, [], none, {}, "", set(), etc.