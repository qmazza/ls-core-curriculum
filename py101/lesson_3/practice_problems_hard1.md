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
output is - 
one is: ['one']
two is: ['two']
three is: ['three']


>Since variables one, two, and three in the mess_with_vars function are local, reassigning them does not affect the original lists.


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

output is - 
one is: ['one']
two is: ['two']
three is: ['three']

>Again, the local variables in the mess_with_vars function are being reassigned, but this doesn't change the original lists. å C)


C
```python
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]two
two = ["two"]three
three = ["three"] one

mess_with_vars(one, two, three)

print(f"one is: {one}") twp
print(f"two is: {two}")three
print(f"three is: {three}") one
```
one is: ['two']
two is: ['three']
three is: ['one']

> In this case, the mess_with_vars function modifies the content of the lists directly. Since lists in Python are mutable and passed by reference, the changes are reflected outside the function.


In all three scenarios, the variables one, two, and three inside the mess_with_vars function are local to the function. 

They are not the same as the variables one, two, and three defined outside the function. 

This is known as variable shadowing, where the local variables inside the function overshadow the variables outside the function with the same names.

# Questions 4

Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.


Alyssa **supplied Ben with a function named is_an_ip_number**. *It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it*. Here's the code that Ben wrote:



```python


def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    return True


```

Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

Help Ben fix his code.

My Answer:
```python




d = '10.4.5.257'
is_an_ip_number(d)


I added -   if len(dot_separated_words) != 4:
        return False

I changed -         if not is_an_ip_number(word):
            break  --> to return False

            #Ben used a break statement to break out of the while loop, which caused control to fall through to the return True statement. 
```

# Questions 5

What do you expect to happen when the greeting variable is referenced in the last line of the code below?


```python
if False:
    greeting = "hello world"

print(greeting)
```

NameError. if block not executed

My Answer:
```python
In Python, referencing an uninitialized variable will result in a NameError being raised. This is because the if block is not executed due to the False condition, and hence, the greeting variable is never initialized.
```