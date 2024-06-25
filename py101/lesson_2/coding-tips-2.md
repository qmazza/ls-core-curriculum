Notes for Lesson 2 for PY101 course.
- Coding tips 2
  
# Contents
- [Contents](#contents)
  - [Using blank lines to organize code](#using-blank-lines-to-organize-code)
  - [Name functions appropriately](#name-functions-appropriately)
  - [Don't mutate the collection during iteration](#dont-mutate-the-collection-during-iteration)
  - [Variable shadowing](#variable-shadowing)
  - [Use underscore for unused identifiers](#use-underscore-for-unused-identifiers)
  - [Gain experience through struggling](#gain-experience-through-struggling)


## Using blank lines to organize code

- Blank lines help programmers organize chunks of code to make it easier to read.
  
```python
# better code spacing

name = input("Enter your name: ").strip()

while not name:
    print("That's an invalid name. Try again:")
    name = input().strip()

print(f"Welcome {name}!")
print("What would you like to do?")
```

- Easier to visually see where it's divided into 3 parts. initial user input, input validation, using the variable.

## Name functions appropriately

- Choose descriptive function names such as `display_` or `print_` (`print_` would expect to print a total rather than return anything)
  -  A function named `total `should return a value, while `print_total` should display something and likely return `None`.

```python
def total(a, b):
    return a + b

# Example usage:
result = total(5, 3)
print(result)  # Output: 8
```

```python
def print_total(a, b):
    print(f"The total is: {a + b}")

# Example usage:
print_total(5, 3)  # Output: The total is: 8
result = print_total(5, 3)
print(result)  # Output: None
```
## Don't mutate the collection during iteration

- Don't mutate a collection while iterating through it. Behavior may not be expected.
  - using words.remove(word) instead of pair.pop(0) below would not do what's expected.
```python
# Proper to mutate the individual elements within that collection, just not the collection itself.
pairs = [[6, 'scooby'], [2, 'do'], [2, 'on'], [7, 'channel'], [3, 'two']]

for pair in pairs:
    pair.pop(0)

print(pairs)  # prints [['scooby'], ['do'], ['on'], ['channel'], ['two']]
```

## Variable shadowing

- Variable shadowing occurs when local variable in an inner scope shares the same name as a variable in an outer scope.
- Can lead to bugs and confusion since it prevents access to the outer scope variable from within the inner scope.

```python
name = 'johnson'

def print_full_name():
    for first_name in ['kim', 'joe', 'sam']:
        print(f"{first_name} {name}")

print_full_name()
# Prints:
# kim johnson
# joe johnson
# sam johnson
print(name) # johnson
```

if `first_name` was `name`, the last print would be sam

- Select appropriate varaibale names when using loops or nested functions. A variable name that matches an outer scope variable risks shadowing the outer variable.

## Use underscore for unused identifiers

Suppose you have a list of names, and you want to print out a string for every name in the list, but you don't care about the actual names.

In those situations, use an underscore to signify that we don't care about this particular loop variable.
```python
names = ['kim', 'joe', 'sam']
for _ in names:
    print('Got a name!')
```

Another example is when you need the first item (typically the index) of a sequence in a loop but don't need the second item (the value).

You can use `_` to indicate that the second item is not being used in the loop:


```python
names = ['kim', 'joe', 'sam']
for index, _ in enumerate(names):
    print(f"{index}: Got a name!")

# prints
# 0: Got a name!
# 1: Got a name!
# 2: Got a name!
```
Note: The `enumerate` function is used to iterate over a sequence in a way that makes both the index and the value available to the loop body. 

Thus, the above loop iterates over `names`, with each iteration passing the index to the `index` variable, and the element value to the `_` variable.


## Gain experience through struggling
- Becoming a good developer means experiencing and solving a lot of weird issues.
- Don't memorize "best practices," but spend time programming to the point where you understand the context for those practices.
  - You'll be able to lean on your experience rather than try to retrieve a bullet list from something you read months or years ago.
- Don't fear violating rules or be afraid to make mistake.
- Coding is like writing -- there are syntactical rules, but there are also creative ways of expression.

>Spend time programming. Learn to debug problems, struggle with them, search for the right terms, play around with the code, and you'll be able to transform into a professional developer. That's what professional developers do every day.

