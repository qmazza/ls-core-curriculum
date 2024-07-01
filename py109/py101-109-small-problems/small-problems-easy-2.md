Practice Problems for Lesson 3 for PY109 course.
- Practice Problems PY109: Easy 2
  
**Table of Contents**
- [Question 1 - Welcome Stranger](#question-1---welcome-stranger)
- [Question 2 - Greeting a user](#question-2---greeting-a-user)
- [Question 3 - Multiplying Two Numbers](#question-3---multiplying-two-numbers)
- [Question 4 - Squaring an Argument](#question-4---squaring-an-argument)
- [Question 5 - Floating Point Arithmetic](#question-5---floating-point-arithmetic)
- [Question 6 - The End Is Near But Not Here](#question-6---the-end-is-near-but-not-here)
- [Question 7 - Exclusive Or](#question-7---exclusive-or)
- [Question 8 - Odd Lists](#question-8---odd-lists)
- [Question 9 - How Old is Teddy?](#question-9---how-old-is-teddy)
- [Question 10 - When Will I Retire?](#question-10---when-will-i-retire)
    - [More on datetime (further discussted in py120):](#more-on-datetime-further-discussted-in-py120)
- [Question 11 - Get Middle Character](#question-11---get-middle-character)
- [Question 12 - Always Return Negative](#question-12---always-return-negative)


# Question 1 - Welcome Stranger

Create a function that takes 2 arguments, a list and a dictionary. 

The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. 

The dictionary will contain two keys, "title" and "occupation", and the appropriate values. 

Your function should return a greeting that uses the person's full name, and mentions the person's title.

```python
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
```

My Answer:
```python
def greetings(name,job):
    joined_name = ' '.join(name)
    title = job.get("title")
    occupation = job.get("occupation")
    return (f'Hello, {joined_name}! Nice to have a {title} {occupation} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
```


Quiz Answer:
```python
def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
           f"{status['title']} {status['occupation']}"
           "around.")
```

We use the join method to change the list into a full name with appropriate spacing. For the dictionary, we access the items by their keys.

Finally, we use f-string formatting to combine everything into a single string, resulting in a concise and readable way to format the final output.

Note that the **parentheses on the return are necessary here**. Without them, Python won't deal with the continuation lines correctly.

# Question 2 - Greeting a user

Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

```python
example 1:
What is your name? Sue
Hello Sue.

example 2:
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
```

My Answer:
```python
name = input('What is your name?: ')
if '!' in name:
    print(f'HELLO {name.upper()} WHY ARE WE YELLING')
else:
    print(f'Hello {name}.')

```

quiz answer:
```python
name = input("What is your name? ")

if name.endswith("!"):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}.")
```
using str.endswith to determine if name ends with '!'

# Question 3 - Multiplying Two Numbers

Create a function that takes two arguments, multiplies them together, and returns the result.

```python
print(multiply(5, 3) == 15)  # True
```

My Answer:
```python
def multiply(num1, num2):
    return num1 * num2
```

# Question 4 - Squaring an Argument

Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

```python
print(square(5) == 25)   # True
print(square(-8) == 64)  # True
```


Quiz answer uses previous multiply function (passing 2 arguments of the name number)

```python
def square(number):
    return multiply(number, number)
```


# Question 5 - Floating Point Arithmetic

Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

```python
==> Enter the first number:
3.141529
==> Enter the second number:
2.718282
==> 3.141529 + 2.718282 = 5.859811
==> 3.141529 - 2.718282 = 0.42324699999999993
==> 3.141529 * 2.718282 = 8.539561733178
==> 3.141529 / 2.718282 = 1.1557038600115808
==> 3.141529 // 2.718282 = 1.0
==> 3.141529 % 2.718282 = 0.42324699999999993
==> 3.141529 ** 2.718282 = 22.45792517468373
```

My Answer:
```python

def calc_num(num1, num2):
    prompt(f'{num1} + {num2} = {num1 + num2}')
    prompt(f'{num1} - {num2} = {num1 - num2}')
    prompt(f'{num1} * {num2} = {num1 * num2}')
    prompt(f'{num1} // {num2} = {num1 // num2}')
    prompt(f'{num1} % {num2} = {num1 % num2}')
    prompt(f'{num1} ** {num2} = {num1 ** num2}')


def prompt(message):
    print(f'==>{message}')

prompt('Enter the first number:')
num1 = float(input())
prompt('Enter the second number:')
num2 = float(input())

calc_num(num1, num2)
```

```python
def calculate(first, second, operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")
```

First solution is straightforward, but repetitive. Such code can be very tedious and error prone, especially if you want to add a number of other mathematical operations.

The quiz solution addresses the bulk of the repetitiveness by performing the calculations in a helper function (calculate) and using a loop to perform the operations and print the results. It needs a bit more code and a bit more effort to understand, but this code will be easier to maintain in the long term.

Both solutions ignore what happens when an input value isn't a valid number, or if the second number is a zero-value. In both cases, the code will raise an exception.

# Question 6 - The End Is Near But Not Here

Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.

```python
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
```

My Answer:
```python
def penultimate(string):
    listed = string.split()
    return listed[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

```

# Question 7 - Exclusive Or

The or operator returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy. The and operator returns a truthy value if both of its operands are truthy, and a falsy value if either operand is falsy. This works great until you need only one of two conditions to be truthy, the so-called exclusive or, also known as xor (pronounced "ECKS-or").

In this exercise, you will write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

```python
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
```

My Answer:
```python
def xor(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True

    return False
```
simply returns True if exactly one of the values is truthy; otherwise, it returns False.

Shorter better version:
```python
def xor(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))
```

xor does not short circuit as it depends on its operands.

# Question 8 - Odd Lists

Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

```python
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True x
```

My Answer: (using range for start 0, stop at end, with a step 2)
```python
def oddities(inp_list):
    new_list = []
    for elem in inp_list[0::2]:
        new_list.append(elem)
        print(elem)
    return new_list
```

quiz answer:
```python
def oddities(lst):
    result = []
    for idx in range(len(lst)):
        if idx % 2 == 0:
            result.append(lst[idx])

    return result

```
This problem can be slightly confusing since we want the 1st, 3rd, 5th, and so on elements of the list, but these correspond to elements with indexes 0, 2, 4, etc. As long as you keep that in mind, there are many different ways to solve this problem correctly.

In this approach:

We loop through all indexes of the list using range(len(lst)).
In the loop, we check if the current index idx is even using the condition idx % 2 == 0. If it is even, it means we have an odd-numbered element (1st, 3rd, 5th, etc.), so we append the element to the result list.
After iterating through all indexes, we return the result list.

```python
# Bonus question usoing sclicing:

def oddities(lst):
    return lst[::2]
```
The bonus solution takes advantage of Python's list slicing, which lets us start from the first element and skip every second element to get the desired result. Python makes it relatively easy to extract every other element using the slicing mechanism, which proves to be both concise and efficient. The [::2] syntax retrieves elements from the list starting from the beginning to the end, skipping every other element.

Let's break this syntax down in more detail:

Slicing Format: list[start:stop:step]
start: The beginning index of the slice.
stop: The end index of the slice (exclusive).
step: The interval between elements.
In [::2]:
No start is provided, so it defaults to the beginning of the list.
No stop is provided, so it defaults to the end of the list.
2 is provided as the step, meaning every second element is taken.
How [::2] Works:
Starts at the beginning of the list.
Skips every second element.
Continues until the end of the list.

using step includes end of list while stop is exclusive.


# Question 9 - How Old is Teddy?

Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

```python
Teddy is 69 years old!
```

My Answer:
```python
import random

def teddy_age():
    return random.randrange(20,101)

print(f'Teddy is {teddy_age()} years old!')
```


quiz answer:
```python
import random

age = random.randint(20, 100)
print(f"Teddy is {age} years old!")
```
randint is inclusive
```python
import random

age = random.randint(20, 100)

print(f"Teddy is {age} years old!")
name = input('What is your name?:'default=Teddy)
print(f'{name} is {age} years old!')
```

further exploration - 
Modify this program to ask for a name, then print the age for that person. For an extra challenge, use "Teddy" as the name if no name is entered.

```python

import random

age = random.randint(20, 100)
default_name = 'Teddy'
print(f"Teddy is {age} years old!")
name = input("What is your name?:")
if name == '':
    name = default_name
print(f'{name} is {age} years old!')

```
# Question 10 - When Will I Retire?

Build a program that displays when the user will retire and how many years she has to work till retirement.

```python
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
```

My Answer:
```python
from datetime import datetime

def ages(x, y):
    return y - x

age = int(input(f'What is your age?: '))
retire_age = int(input(f'What age would you like to retire?: '))
years_left = ages(age, retire_age)

this_year = datetime.now().year
retire_year = datetime.now().year + years_left

print(f'It\'s {this_year}. You will retire in {retire_year}.')

print(f'You have only {years_left} years of work to go!')
```
 we use datetime.now from the datetime module to get the current date. This returns a datetime object. The datetime object has a year attribute that provides the current year.
 
 From there, we can determine the retirement year based on the two inputs and the current year.



### More on datetime (further discussted in py120):

In Python, when you use the import statement, you're essentially telling the interpreter to load a module or package, making its contents (functions, classes, and variables) available in your code. The way you import the module affects how you can access its contents.

When you do:

```python
import datetime
```
You are importing the datetime module. However, the datetime module contains a class that is also named datetime.datetime that contains methods like datetime.datetime.now. So if you were to use the above import, you would have to retrieve the current year by using:

```python
current_year = datetime.datetime.now().year
```
As you can see, the datetime.datetime syntax can be redundant and a bit confusing since you have to use datetime twice: once for the module and once for the class.

On the other hand, when you use:

```python
from datetime import datetime
```
You are specifically importing the datetime class (the second use of datetime) from the datetime module (the first use of datetime). This means you can directly use the datetime.datetime class and its methods without prefixing it with the module name:

```python
current_year = datetime.now().year
```
You can also use an alias for the datetime.datetime class:

```python
from datetime import datetime as dt
```
You are specifically importing the datetime class (the second use of datetime) from the datetime module (the first use of datetime) and giving it an alias of dt. This means you can directly use the datetime.datetime class and its methods by prefixing the method name with dt.:


```python
current_year = dt.now().year
```

# Question 11 - Get Middle Character

Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

```python
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
```

My Answer: (use floor quotient for integer. / will give float)
```python
def center_of(string):
    odd_middle = int(len(string) // 2)
    even_middle1 = int(len(string) // 2 - 1)
    even_middle2 = int(len(string) // 2)
    if len(string) % 2 == 0:
        return string[even_middle1] + string[even_middle2]
    else:
        return string[odd_middle]

```

quiz answer: (+ 2 to print 2 characters from left index which is -1)
```python
def center_of(string):
    if len(string) % 2 == 1:
        center_index = len(string) // 2
        return string[center_index]
    else:
        left_index = len(string) // 2 - 1
        return string[left_index:left_index + 2]
```


length: 6	
right index: 6 // 2 => 3	
left index: 3 - 1 => 2

Given the left index we've calculated, we can now use string slicing to extract the two characters starting at the left index as the middle characters. For our 6 character example, the syntax string[left_index:left_index + 2] will extract two characters from the string starting at left_index.


# Question 12 - Always Return Negative

Write a function that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the argument is a negative number, return it as-is.

```python
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
```

My Answer:
```python
def negative(num):
    if num > 0:
        return(-num)
    elif num == 0:
        return num
    else:
        return num

```

quiz answer:
```python
def negative(number):
    return -abs(number)
```
Python has a built-in `abs` functin which returns the absolue value of a specified number.
By preficing the result abs(number) with a negative sign , function always returns the negative representation of the given number