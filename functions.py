# a=8
# b=10
# print("The sum is: ", a+b)

# a=40
# b=70
# print("The sum is: ", a+b)

# functions to pack knowledge - avoid logic being repeated (definition/declaration)
def sum(a,b): # function name, # arguments/parameters
  return a+b # body of function

# abstracted logic - no need to know how it works, hiding implementation
print(sum(30,50)) # calling function
print(sum(50,40))

# default values (argument) should come at last
def driving_test(name,age=15,car="Toyota tazz"): # function name, # arguments/parameters
  if age>=18:
    return f"{name} You're eligible for driving. You will be tested with {car}."
  else:
    return "Try again after a few years 👶🍼"

# print(driving_test(20),"GR Corrolla")
# print(driving_test(20))
# print(driving_test(21,"dhara")) # type error
# print(driving_test(age=21,name="dhara")) # no error --> keyword arguments
# [9,3,8].sort(reverse=true)
# print(driving_test("dhara")) # order matters