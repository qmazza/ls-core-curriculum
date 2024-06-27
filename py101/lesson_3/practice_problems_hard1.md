Notes for Lesson 3 for PY101 course.
- Practice Problems: Hard 1
  
# Contents

# Questions 1

Will the following functions return the same results?

```python
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())
```

Try to answer without running the code or looking at the solution.

My Answer:
>NO - nothing after return statement in def second(). It will return None. Indented block is unreachable

>These functions do not return the same thing. The function first() returns the expected value of { prop1: "hi there" }, but second() returns None without throwing any errors.

>In Python, if there's nothing after a return statement, the function will return None. The indented block after the return statement in second function is unreachable and doesn't affect the return value.


# Questions 2

What does the last line in the following code output?

```python
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
```

Answer:
```python
[1, 2]
{'first': [1, 2]}
```
Since num_list is a reference to the original list in dictionary, appending to num_list modifies the list. Thus, the original dictionary is also updated.

If, instead of modifying the original dictionary, we want to modify num_list but not dictionary, we have a couple of options:

We can initialize num_list with a reference to a copy of the original list:
```python
dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)
```
We can use list slicing which returns a new list:
```python
dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)
```

# Questions 3

Given the following similar sets of code, what will each code snippet print?

A
```python
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

B
```python
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

C
```python
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

# Questions 4

```python

```

My Answer:
```python

```

# Questions 5

```python

```

My Answer:
```python

```