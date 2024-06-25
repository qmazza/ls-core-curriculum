Notes for Lesson 2 for PY101 course.
- Pass by Reference vs Pass by Value

```
1. Python passes references to object, not objects themselves. (Python exhibits combination of behaviors from both pass-by-reference and pass-by-value.)

2. The distinction between mutable and immutable types in Python then dictates whether you can modify the original object through that reference.
```

# Contents
- [Contents](#contents)
  - [Introduction](#introduction)
  - [What does pass by "value" mean?](#what-does-pass-by-value-mean)
  - [What does pass by "reference" mean?](#what-does-pass-by-reference-mean)
  - [What Python does](#what-python-does)


## Introduction

- It's important to know what happens to function arguments. Different languages have different strategies for this.
- The terms **pass-by-reference** and **pass-by-value** describe the two main strategies.
- Important to understand how to invoke functions with the behavior you expect.

What those terms mean and how they relate to Python's behavior:

## What does pass by "value" mean?

- -- C. In C, when you have "**pass by value**", the function only has a *copy* of the original object.
  - Operations performed on the oject within the function have no effect on the orginal object outside of the function.
- This can lead you to believe that Python is pass-by-value since reassigning a parameter variable within a function doesn't affect the variable outside the function. For example: 
  
```python
def change_name(name):
    name = 'bob'

name = 'jim'
change_name(name)
print(name)  # Output: jim
```
- example above has two different variables called `name`. One locally scoped, one global scope.
- We **passed in the value**. Since reassigning the variable only affected the function-level variable, and not the global scope variable.


## What does pass by "reference" mean?

- Python is not pure "**pass by value"**. Operations within a functin can change the original object plainly in Python. Example:

```python
def add_element(my_list):
    my_list.append([4])

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)        # => [1, 2, 3, [4]]
```
- This implies Python is "**pass by reference**", since operations within the function affected the original object.
- However, not all operations affect the original obejct. Example with modified version of previous code:
```python
def add_element(my_list):
    my_list = my_list + [4]

my_list = [1, 2, 3]
add_element(my_list)
print(my_list)        # => [1, 2, 3]
```
- This is back to "**pass by value**"


## What Python does
- Python exhibits combination of behaviors from both "**pass-by-reference**" and "**pass-by-value**"
- Its behavior is described as **"pass by object reference"** as you are passing a reference to the object (value) rather than a copy of the object itself.
  - Whether the function can modify the object depends on whether object is mutable or immutable.
>- **Important to remember:** Python passes references to object, not objects themselves. 
>- The distinction between mutable and immutable types in Python then dictates whether you can modify the original object through that reference.