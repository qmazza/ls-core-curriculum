Notes for Lesson 2 for PY101 course.
- Errors
  
# Contents
- [Contents](#contents)
- [Introduction](#introduction)
- [Terminology](#terminology)
  - [NameError](#nameerror)
  - [TypeError](#typeerror)
  - [SyntaxError](#syntaxerror)
  - [ValueError](#valueerror)
  - [IndexError](#indexerror)
  - [KeyError](#keyerror)
  - [ZeroDivisionError](#zerodivisionerror)
  - [Exception Handling](#exception-handling)


# Introduction
- Many situations where Python Interpreter cannot continue executiing a program.
- Instead, it creates an **Exception object** that describes the problem and stops the program.

# Terminology
>When an error occurs in a python, we say it **raises** an Exception
- Some programming languages use **errors** to denote exception; others refer to throwing exception.
- **Exception** and **error** are interchangeable, just as **raise** and **throw** are.
## NameError
Arises when you attempt to use a variable or function that hasn't been defined.
```python
a        # Referencing an undefined variable results in a NameError.
a()      # The same applies when trying to call an undefined function.
```
## TypeError
A TypeError occurs when a value of the wrong type is used in an expression.

Example: The following situations should raise a TypeError exception:

- using an argument of the wrong type as a function argument
```python
>>> my_str = "abc"
>>> my_str.find(42)  # TypeError: must be str, not int
```

- trying to call an object that isn't callable:
```python
>>> my_int = 42
>>> my_int()        # TypeError: 'int' object is not callable
```

## SyntaxError

A SyntaxError is unique in that it typically arises immediately after loading a Python program but before it starts running. 

Unlike NameError and TypeError, which hinge on specific variables and values encountered during runtime, ***Python detects SyntaxErrors solely from the program's text***.

```python
def (     # SyntaxError: unexpected EOF while parsing
```
Several cases can lead to a SyntaxError while a Python program is running. 

For example, this code would result in a SyntaxError at runtime:

```python
expression = "2 * (3 + 4"
result = eval(expression)
```
The code uses Python's eval function to evaluate a Python expression that has been written as a string. 

Thus, the above code is effectively the same as:
```python
result 2 * (3 + 4
```
The key difference is that the eval function raises a SyntaxError when the code is executed, but the second code fragment raises a SyntaxError during the parsing phase.

- Don't worry about remembering `eval`. It's best avoided by most developers. Slow and potentially dangerous from security standpoint.
  
## ValueError
A ValueError is raised when a function receives an argument of the correct data type, but the value of the argument is inappropriate for the operation.

```python
number = int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'
# A float would be invalid as well, since it's not an integer.
```

## IndexError

An IndexError occurs when trying to access an index of a sequence (like a list or string) that is outside the range of valid indexes.

```python
nums = [1,2]
num = nums[2] # IndexError: list index out of range
```

## KeyError

A KeyError is raised when trying to access a dictionary key that doesn't exist.

```python
my_dict = {"a": 1, "b": 2}
value = my_dict["c"] # KeyError: 'c'
```
## ZeroDivisionError

A ZeroDivisionError occurs when attempting to divide by zero or when trying to use 0 on the right side of the modulus (%) operator:

```python
result1 = 10 / 0 # ZeroDivisionError: division by zero
result2 = 42 % 0 # ZeroDivisionError: integer modulo by zero
```

## Exception Handling

- Lets you manage errors that might occur during program execution.

- Python provides a structured way to handle exceptions using the `try`, `except`, `else`, and `finally` statements.

Here's how the exception handling process works:

1. ***Try Block:*** The code that might raise when ana exception is placed within the `try block`. Python will monitor this block for any exceptions that may occur during its execution.

2. ***Except Block***: If an exception is raised in the `try block`, Python will look for a matching `except block` that can handle that specific type of exception. If a match is found, the code within the corresponding `except block` is executed.

3. ***Else Block (Optional):*** The `else block` is executed only if no exceptions occurred in the `try block`. It's used for code that should run when no errors were encountered.

4. ***Finally Block (Optional):*** The `finally block` is always executed, regardless of whether an exception was raised or not. It is used for cleanup operations or tasks that must be performed, such as releasing resources.

Example that demonstrates the different aspects of exception handling in Python:

```python
try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")
```

In this example:

- If the user enters a non-integer value, a `ValueError` is caught, and the program displays an error message.
- If the user enters zero, a `ZeroDivisionError` is caught, and the program warns about division by zero.
- If no exceptions occur, the division result is printed.
Regardless of whether an exception was caught or not, the `finally block` ensures that the final message is displayed.