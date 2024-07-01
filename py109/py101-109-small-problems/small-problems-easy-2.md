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

```python

```

My Answer:
```python

```

# Question 8 - Odd Lists

```python

```

My Answer:
```python

```

# Question 9 - How Old is Teddy?

```python

```

My Answer:
```python

```

# Question 10 - When Will I Retire?

```python

```

My Answer:
```python

```

# Question 11 - Get Middle Character

```python

```

My Answer:
```python

```

# Question 12 - Always Return Negative

```python

```

My Answer:
```python

```