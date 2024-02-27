# Shortcuts
# ctrl + shift + p --> command
# ctrl + p --> find file

# # Lexical Scope - Inheritance
# # Closure - Own scope + lexical scope
# def market():
#     price = 100
#     def get_price():
#         print("The price is: ", price)
#     get_price()
# print(market())

# # Scope - Lifetime of a variable
# def cool():
#     x = 10 
# cool()
# print("The value of x is: ", x)    

# code_word = "Hulk"
# def space_ship():
#     question = "Please provide code word"
    
#     def code_word_check():
#         password = "Hulk"
#         print(question)

#         if(password == code_word):
#             print(f"Welcome, {password} the strongest avenger ")
#         else:
#             print("Acces denied")
#     code_word_check()

# space_ship()  

# currying
# def add(x):
#     def add1(y):
#         return x + y
#     return add1
# print(add(10)(5))

# def fun(nums=[]):
#     nums.append(10)
#     print(nums)
   
# fun() # [10]
# fun() # [10, 10]
# fun() # [10, 10, 10]
# fun() # [10, 10, 10, 10]  
 
# def fun(nums):
#     pass
 
# # Expectation
# fun() # [10]
# fun() # [10]
# fun() # [10]
# fun() # [10]  

def fun(nums=None):
    if nums is None:
        nums = [10]
    print(nums)

# Test cases
fun() # [10]
fun() # [10]
fun() # [10]
fun() # [10]

