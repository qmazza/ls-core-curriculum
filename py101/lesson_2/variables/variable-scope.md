Notes for Lesson 2 for PY101 course.
- Variable scope
  
# Contents
- [Contents](#contents)
  - [Introduction](#introduction)
  - [Scope from book:](#scope-from-book)
  - [Global \& non local statements from book:](#global--non-local-statements-from-book)
  - [Global scope](#global-scope)
  - [Local scope](#local-scope)
    - [Function scope](#function-scope)
      - [Rule 1:](#rule-1)
      - [Rule 2:](#rule-2)
      - [Rule 3:](#rule-3)
      - [Rule 4:](#rule-4)
      - [Rule 5:](#rule-5)
    - [Block scope](#block-scope)
  - [Exercises](#exercises)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3)
    - [Question 4](#question-4)
    - [Question 5](#question-5)
    - [Question 6](#question-6)
  - [Summary](#summary)


## Introduction
- A variable's scope is the part of the program that can access that variably by name.
- Variable scoping rules describe how and where the language finds previously defined variables.

## Scope from book:
https://launchschool.com/books/python/read/functions_methods#scope

- Scope of an identifier determines where you can use it.
- In Python, identifiers have **function scope**. (meaning anything initialized inside a function is only available within the body of that function and any nested functions. No outside access to that identifier.)
- when no assignment inside a function, python looks in the **lexical scope**. (means it searches outer scopes for nearest definition.)
  
## Global & non local statements from book:
https://launchschool.com/books/python/read/more_stuff#globalnonlocalstatements

- Functions add complexity to the concept of scope.
- Python lets you access variable that is defined in outer scope.
- Cariables inside a function are by default local variables.
- `global` and `nonlocal` statements allow programmers to override this behavior.
  - `global` - Python is told to look to the outermost scope (global scope) for variable to be used.
  - `nonlocal` statement only works in nested functions. Functions defined inside an outer function. When Python processes a nonlocal statement, it looks for the associated variable in one of the outer functions.

global example:
```python
greeting = 'Salutations'

def well_howdy(who):
    global greeting
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
# Howdy, Angie
# Howdy
```


nonlocal example:

we may want some of these functions to use one of the variables defined in the surrounding scope. For instance, assume we want foo in inner2 to reference the foo variable in inner1

attempt with global
```python
def outer():
    def inner1():
        def inner2():
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()
# inner2 -> 3 with id 4339312328
# inner1 -> 2 with id 4339312296
# outer -> 1 with id 4339312264
```

Answer to this problem is to use the nonlocal statement:

```python
def outer():
    def inner1():
        def inner2():
            nonlocal foo
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()
# print(f"global -> {foo} with id {id(foo)}")  # statement removed

# inner2 -> 3 with id 4339312328
# inner1 -> 2 with id 4339312296
# outer -> 1 with id 4339312264
# global -> 3 with id 4339312328     # Note: same as `inner2`
```
managed to change foo from inner1. However, it did not change foo in outer. We can address that readily by adding a nonlocal statement in inner1:

```python
def outer():
    def inner1():
        def inner2():
            nonlocal foo
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()
# print(f"global -> {foo} with id {id(foo)}")  # statement removed

# inner2 -> 3 with id 4339312328
# inner1 -> 3 with id 4339312328       # Same as inner2
# outer -> 1 with id 4339312264
```
This time, we got 3's across the board. Effectively, the assignment in inner2 changed the value of foo in inner2, inner1, and outer.

- Don't use global and nonlocal haphazardly.
- It's not usually good practice to reassign variables outside the local scope.
- Mkes the program harder to read, understand, and maintain. 
- In some circumstances, you must use the nonlocal statement, but the global statement is rarely required. 
- Global variables often indicate poor design choices.

## Global scope
- In Python, variables initialized outside of any function have a global scope.

Example:
```python
name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()  # Output: Hello, John!
```


## Local scope


### Function scope

- Functions define a new scope for local variables. 
- Think of the scope defined by a function as an inner scope. 
- Nested functions define nested scopes. 
- A variable's scope is determined by where it is initialized or declared.

#### Rule 1:

Variables defined in a function are local to that function and cannot be accessed in the outer scope

```python
def my_func():
    local_var = 10
    print(local_var)

my_func()  # Output: 10
print(local_var)  # Raises NameError: name 'local_var' is not defined
```

#### Rule 2:

Variables that are defined within a function are local unless explicitly marked as `global` or `nonlocal`

```python
def my_func():
    global global_var
    global_var = 20

my_func()
print(global_var) # Output: 20
```

In this example, the `global` keyword is used inside the `my_func` function to indicate that the `global_var` being modified is the global variable, not a local one. 

As a result, it is **accessible outside of the function**.

The nonlocal statement's use and behavior is similar to that of global. However it only applies in nested functions.

#### Rule 3:

Variables used but not reassigned in a function may be in the outer scope

```python
outer_var = 15

def my_func():
    print(outer_var)

my_func()  # Output: 15
```

`outer_var` is used but not reassigned in the `my_func` function, so Python looks for it in the outer scope and finds the value 15.

Lets functions access variables from their containing scope unless those variables are redefined within the function. Only applies to reading the variable's value; if you attempt to reassign the variable within the function without using the `global` keyword, a new local variable will be created instead.

#### Rule 4:

Peer scopes do not conflict

```python
def func_a():
    a = 'hello'
    print(a)

def func_b():
    print(a)  # NameError: name 'a' is not defined

func_a()
func_b()
```
Executing `print(a)` on line 6 raises an error since `a` is not in scope in `func_b`. 

The assignment on line 2 does define a variable named `a`, but that variable's scope is confined to `func_a`. 

`func_b` cannot access the variable defined in `func_a`. 

We could define a separate a variable in `func_b` if we wanted. Would have different local scopes and would be independent of each other.

#### Rule 5:

Nested functions have their own scope.

```python
a = 1  # first level variable

def foo():  # second level
    b = 2

    def bar():  # third level
        c = 3
        print(a)  # => 1
        print(b)  # => 2
        print(c)  # => 3

    bar()

    print(a)  # => 1
    print(b)  # => 2
    print(c)  # => NameError: name 'c' is not defined

foo()
```
Make sure to understand the rules around inner scope versus outer scope.

### Block scope

- Unlike some programming languages, Python does not have a block scope.
- Variables defined within blocks (if statements or loops), are accessible outside of those blocks


```python
if True:
    block_var = 'Hello'

print(block_var)  # Output: Hello
```
`block_var` is initialized within the `if` block but can still be accessed outside of it.

## Exercises

### Question 1
What will the following code print and why? Don't run it until you have tried to answer.

```python
num = 5

def my_func():
    print(num)

my_func()

# my answer: 5


# This prints 5. The variable num initialized to 5 on line 1 is accessible within the scope of the my_func function. When that function is invoked, 5 is printed.

```

### Question 2

What will the following code print and why? Don't run it until you have tried to answer.

```python
num = 5

def my_func():
    num = 10

my_func()
print(num)

# my answer: 5

# This prints 5. The variable num initialized to 5 on line 1 and the variable num initialized on line 4 within the function my_func are two different variables. We can't reassign variable num initialized on line 1 within the function

```

### Question 3

What will the following code print and why? Don't run it until you have tried to answer.

```python
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# my answer: 10
# This prints 10. The variable num is initialized to 5 on line 1. On line 4 we use global keyword inside the function to reference the global variable num initialized on line 1. For that reason, on line 5 we are reassigning global variable num to 10 and on line 8 printing that value.
```

### Question 4

What will the following code print and why? Don't run it until you have tried to answer.

```python
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# my answer: Hello World
# This prints Hello World. The outer() function defines a local variable outer_var with the value 'Hello'. Inside it, the inner() function is defined, which has its own local variable inner_var with the value 'World'. When inner() is called within outer(), both outer_var and inner_var are printed using print(outer_var, inner_var), which outputs Hello World.
```

### Question 5

What will the following code print and why? Don't run it until you have tried to answer.

```python
def my_func():
    num = 10

my_func()
print(num)

# my answer: NameError - variable num is defined wihtint he function. Not accessible outside of its scope.
# This code raises a NameError since the variable num is defined within the function my_func and is not accessible outside of its scope.
```

### Question 6

```python
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# my answer: 
# Inner 1:25
# Inner 2:15 
# Inside my_func, a local variable x is initialized to 15. When inner_func1 is called, it defines its own local variable x with a value of 25 and prints "Inner 1: 25". However, when inner_func2 is called, it doesn't have access to the variable x from the inner_func1 as it is in its peer scope but accesses variable x defined in the scope of my_func.
```

## Summary
- Use Python REPL or editor to refresh memory on rules and how to use.
- Make sure to know how variable scope works with regard to functions
