Notes for Lesson 2 for PY101 course.
- Type Conversions
  
# Contents

# Introduction

**Type Coercion** is the process of converting a value of type to another.


# Explicit type coercion

- Occurs when a programmer intentionally employs various built-in function to convert a value of tiype to another.
- Such as using `int` and `float` functions

## Coercing values to Integers
- The `int()` function is used to convert values to integers. 
  - It takes a value as input and attempts to convert it to an integer.
  - Attempting to convert a non-numeric string to an integer using int()will raise a ValueError.
```python
non_numeric_str = "abc"
try:
    non_numeric_integer = int(non_numeric_str)
except ValueError:
    print("Cannot convert to int")
```

- It can also accept a real number(floating-point numbers), bytes-like object, and, surprisingly, it won't raise an error if we pass a boolean to it.
- Passing any other data type, like a list for example will result in a TypeError. 

## Coercing values to Floats

- The `float()` function is used to convert values to floating-point numbers.
  - Attempting to convert a non-numeric string to a float using float() will raise a ValueError.
  - Just like int(), passing any other data type, other than string, a real number, bytes-type object, and a boolean to it, it will raise a TypeError.
  - Floats have a speal **"Not-a-Number"** value `nan` Not-a-Number is one of the common ways to represent the missing value in data.
  
```python
#we subtract positive infinity from positive infinity, which results in a nan value.
result = float('inf') - float('inf')
print(result) # nan
```

- attempting to convert "NaN" to float, output: nan

## Coercing values to Strings

- The `str()` function is used to convert values to strings. 
  - Works with all built-in Python data types and most non-built-in types.
- When using `print()`, python automatically convers teh value of a string using the str() function.
  
```python
number = 42
print("The answer is:", number)  # Output: The answer is: 42
```

-String interpolation is a common technique for including values within a string. 
  - When you use interpolation, Python automatically coerces the values to strings using the str() function.
  
```python
name = "Karl"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # Output: Hello, my name is Karl and I am 30 years old.
```

## Coercing values to Booleans

- The `bool()` function is used to convert values to booleans. 
  - It works with all built-in Python values and most non-built-in values. 
  - When using the `bool()` function, it returns True if the value is truthy (evaluates to True in a boolean context), and False if the value is falsy (evaluates to False in a boolean context)

```python
truthy_value = "Hello"
falsy_value = None

is_truthy = bool(truthy_value)
is_falsy = bool(falsy_value)

print(is_truthy)  # Output: True
print(is_falsy)   # Output: False
```

## repr() vs str()

In Python, the `repr()` function returns a string representation of an object, which can be used to recreate the object using Python code.

```python
x = [1, 2, 3]
repr_x = repr(x)
print(repr_x)  # Output: '[1, 2, 3]'
```

Difference between `str()` and r`epr()`:
- `str()`: This function is used to create a string representation of an object that is meant to be human-readable. It focuses on providing a concise and user-friendly representation of the object's value. It is often used for display purposes, such as in print() and string interpolation.
- `repr()`: This function is used to create an unambiguous string representation of an object that can be used to recreate the object. It is often used for debugging and development purposes. The repr() representation should ideally be a valid Python expression that, when evaluated, would recreate the original object.

Example:

```python
import datetime

today = datetime.datetime.now()
print(str(today)) # 2023-08-10 10:18:05.535262
print(repr(today)) # datetime.datetime(2023, 8, 10, 10, 18, 5, 535262)
```

# Implicit type coercion
**Implicit type conversion**, often known as *automatic data type conversion*, is when Python automatically transforms one data type into another without the programmer's direct instruction.
- typically occurs during calculations or when mixing distinct data types.

## Combining Integer with Float

When you conduct a calculation involving both integer and a float, system automatically adjusts the integer to a float, ensuring outcome is a float as well.

```python
x = 3          # Integer
y = 2.0        # Float

result = x + y # Presence of float y in arithmetic expression
print(result)  # Outputs: 5.0
print(type(result))  # Outputs: <class 'float'>
```

## Combining String with Non-string

- Combining a string with a non-string using the `+` operator raises a TypeError in Python.
- However, when using commas inside the `print()` function, Python implicitly converts any non-string arguments to a string.

```python
name = "Clare"
age = 35

# This would raise a TypeError: print(name + age)

# But this works:
print(name, age)  # Outputs: Clare 35
```