Notes for Lesson 2 for PY101 course.
- Variables and Functions
  
# Contents
- [Contents](#contents)
  - [Example 1](#example-1)
  - [Example 2](#example-2)
  - [Example 3](#example-3)
  - [Example 4](#example-4)
  - [Example 5](#example-5)
  - [Example 6](#example-6)
  - [Example 7](#example-7)
  - [Example 8](#example-8)
  - [Example 9](#example-9)
  - [Summary](#summary)


## Example 1

```python
my_var = 1

def my_func():
    print(my_var) # Output: 1

my_func()
```
- `my_var` on line 4 is the same variable as `my_var` on line 1.

## Example 2

```python
my_var = 1

def my_func():
    my_var = 2

my_func()
print(my_var)  # Output: 1
```
- By default, assigning a variable inside a function, as we do on line 4, creates a new local variable inside that function. 
- Thus, `my_var` on line 4 is a different variable than the one on lines 1 and 7.
  
## Example 3

```python
my_var = [1]

def my_func():
    my_var[0] = 2

my_func()
print(my_var)  # Output: [2]
```
- In this code, we're reassigning an element of the list referenced by `my_var`. 
- Unlike example 2, this does not create a new variable -- reassigning an element in a collection **mutates** the collection.

## Example 4

```python
def my_func():
    my_var = 1

my_func()
print(my_var)  # NameError: name 'my_var' is not defined
```
- As seen in example 2, assigning a variable inside a function creates a new local variable inside the function. 
- Since a local variable is only visible in the function in which it is defined, trying to print `my_var` on line 5 produces an error.

## Example 5

```python
my_var = [1]

def my_func(my_var):
    my_var.append(2)

my_func(my_var)
print(my_var)  # Output: [1, 2]
```
- In this code, `my_var` on lines 3 and 4 are different variables `from my_var` on lines 1, 6, and 7. 
- However, since we pass `my_var` as an argument to `my_func` on line 6, `my_var` inside the function is a reference to the object that is referenced by `my_var` on line 6. 
- Thus, the mutating method append mutates that object, which means that the final output is [1, 2].

## Example 6

```python
my_var = [1]

def my_func(my_var):
    my_var = [2]

my_func(my_var)
print(my_var)  # Output: [1]
```
- Unlike example 6, the assignment on line 4 creates a new local variable that is only known to `my_func`. 
- This assignment breaks the connection between `my_var` on line 3 amd the value of `my_var` on line 6.

## Example 7

```python
my_var = "Hello"

def my_func():
    print(my_var + " world")  # Output: "Hello world"

my_func()
```
- In this code, `my_var` on line 4 is the same variable as `my_var` on line 1. 
- We are not assigning `my_var` inside the function, so we can access the `global` variable.

## Example 8

```python
my_var = "Hello"

def my_func():
    return my_var + " world"

my_func()
print(my_var) # Output: "Hello"
```
- In this example, `my_func` concatenates `my_var` and `" world"` in the same way as example 7. 
- Rather that printing it immediately, it instead *returns the result* to the calling code on line 6. 
- However, the code on line 6 does not capture the return value. T
- herefore, `my_var` has its original value when we print it on line 8.

## Example 9

```python
my_var = "Hello"

def my_func():
    my_var = my_var + " world"
    # UnboundLocalError: local variable 'my_var' referenced before assignment
    return my_var

my_func()
print(my_var)
```
- In this example, the assignment to `my_var` creates a new local variable inside `my_var`.
- That new variable is initially undefined, so when the code attempts to append `my_var` and `" world"`, an error occurs.

## Summary

- Differences in outcome and output can be significant.
- Need to understand exactly why the differences in the code lead to different outcome.
- Requires understanding different concepts and how they work together.
  - Variable Scope
  - Mutability
  - Variables as References
  - Passing Arguments to Functions