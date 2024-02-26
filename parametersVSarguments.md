# Parameters vs. Arguments

## Parameters:

Parameters are variables listed in the function definition. They act as placeholders for the values that will be passed into the function when it is called.

### Characteristics of Parameters:
- *Defined in Function Signature:* Parameters are declared within the parentheses of a function definition.
- *Serve as Placeholders:* They represent the data that the function will work with.
- *Defined by the Function Creator:* Parameters are determined by the function creator and are used to define the function's behavior.
- *Descriptive Names:* Parameter names should ideally describe the data they expect.

Example:
```python
def greet(name):
  print("Hello,", name)
```
In the above Python function, `name` is a parameter. It serves as a placeholder for the value that will be provided when the function is called.

## Arguments:

Arguments are the actual values that are passed to a function when it is called. These values are substituted into the parameters of the function.

### Characteristics of Arguments:
- *Provided during Function Call:* Arguments are passed to a function when calling it.
- *Concrete Values:* They are specific data values that are supplied to fulfill the function's parameter requirements.
- *Supplied by the Function Caller:* Arguments are provided by the code that calls the function.
- *Positional or Keyword:* Arguments can be passed by their position or explicitly using keyword assignment.

Example:
```python
greet("Ragav")
```
In the function call above, `"Ragav"` is an argument. It is the actual value passed to the `greet` function to be used as the `name` parameter.