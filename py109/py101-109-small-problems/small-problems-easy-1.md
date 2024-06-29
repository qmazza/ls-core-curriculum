Practice Problems for Lesson 3 for PY109 course.
- Practice Problems PY109: Easy 1
  
## Contents 

# Question 1
Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

My answer:

Function using abs:
```python
def check_if_odd(number):
    if abs(number) == 0:
        return False
    return

print(check_if_odd(5))
```

Function using modulo:
```python
def check_if_odd(number):
    if number % 2 == 0:
        return False
    return

print(check_if_odd(5))
```

Quiz answer:
```python
def is_odd(number):
    return abs(number) % 2 == 1
```
>The `abs` function returns the absolute value of the argument, ensuring it's positive. Then check whther the resulting number modulo 2 equals 1, which would indicate it's odd


# Question 2

Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?


My answer:
```python

for number in range(1, 100, 2):
    print(number)

#To print every odd number in the range of 1 to 99(inclusive), I want iterate each and print all odd numbers.

#other solution: 

for number in range(1, 100):
    if number % 2 == 1:
        print(number)
```

Further exploration  - Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

answer:
```python
def checkin():
    return [x for x in range(1, 100, 2) if str(x).startswith(str(5))]

print(checkin())

#num is for number in range 1 to 100 step 2 if str(x) startswith method starts with str (5)
```

# Question 3

Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

My Answer
```python
for num in range(2,100,2):
    print(num)

#Can also do

for number in range(1, 100):
    if number % 2 == 0:
        print(number)
```

Bonus Question: Can you solve the problem by iterating over just the even numbers?
```python
for num in range(2,100,2):
    print(num)
```


# Question 4

Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet

My answer:
```python

def ask_user():
    print("What is the length of your room in square meters?")
    ask_length = input()
    print("What is the width of your room in square meters?")
    ask_width = input()

def calculate_area():
    return ask_length * ask_width

print("Welcome to the Area Calculator")

ask_user()
area_meters = calculate_area()

print(f'The area is {area_meters}')

--------------------------------------
# Finished with extra
def ask_user_length():
    print("What is the length of your room in square meters?")
    return input()


def ask_user_width():
    print("What is the width of your room in square meters?")
    return input()

    

def calculate_area():
    return x * y

def calc_again():
    while True:
        answer = input()
        if answer.startswith('n') or answer.startswith('y'):
            return answer
        print("invalid entry. Please enter y or n")


while True:
    print("Welcome to the Area Calculator!")

    while True:
        ask_length = ask_user_length()
        if ask_length.isnumeric() is False:
            print("invalid entry. Please enter a number.")
        elif ask_length.isnumeric():
            break

    while True:
        ask_width = ask_user_width()
        if ask_width.isnumeric() is False:
            print("invalid entry. Please enter a number.")
        elif ask_length.isnumeric():
            break

    x = int(ask_length)
    y = int(ask_width)
    area_meters = int(calculate_area())
    square_meters = area_meters * 10.7639
    round_square = round(square_meters:)

    print(f'''
    With length: {x}
    With Width: {y}
    The area in meters is {area_meters}
    The area in square feet (rounded) is {round_square}
    ''')

    print(f'Would you like to perform another calculation? (y/n)')
    
    answer = calc_again()
    if answer == 'n':
        break


```

Quiz answer:
```python
length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))

area_in_meters = length * width
area_in_feet = area_in_meters * 10.7639

print(f"The area of the room is {area_in_meters:.2f} "
      f"square meters ({area_in_feet:.2f} square feet).")
```
The input function returns a string. Thus, we need to use the float function to convert this string to a floating-point number.

The format specification {:.2f} ensures that the output is formatted to two decimal places.

# Question 5

- Create a simple tip calculator. 
- The program should prompt for a bill amount and a tip rate. 
- The program must compute the tip, then print both the tip and the total amount of the bill
- You can ignore input validation and assume that the user will enter valid numbers.


What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00

Ask the user what the bill amount is
Ask the user what percentage of tip they would like.
calculate amount of tip % of the bill is
print result and total amount of the bill.


My Answer:
```python
while True:
    bill = float(input('What is your bill amount?: '))
    tip_rate = float(input('What percentage would you like to tip?: '))
    convert_tip_percent = tip_rate / 100
    tip_amount = bill * convert_tip_percent
    total = bill + tip_amount

    print(f'Your tip amount is: {tip_amount:.2f}')
    print(f'Your total bill is: {total:.2f}')
    x = input('Would you like to calculate again? (y/n):')
    if x == 'n':
        break
```

quiz answer:
```python
bill = float(input("What is the bill? "))
percentage = float(input("What is the tip percentage? "))

tip = bill * (percentage / 100)
total = bill + tip

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")
```

Our solution collects user input, converts it to a floating-point number, then calculates the tip and total amount. The result is formatted to two decimal places using f-strings.

However, consider a scenario where we didn't explicitly convert the inputs using float. If we attempted to compute tip without the conversion, Python would raise a TypeError, indicating that unsupported operand types were being used for the multiplication.

Since in Python, there's a clear distinction between string and number operations, always be sure to convert input strings to the appropriate numeric type before performing calculations.

# Question 6

Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

example 1:
```python
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.
```
example 2:
```python
Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
```

My Answer:
```python

#ASK the user for an integer greater than 0
#ASK the user which operation they'd like to perform
#invoke function of operation choice
#return sum or product (ooperation choice)
def calc_sum(s):
    sums = 0
    for x in range(1,s + 1):
        sums = sums + x
    return sums



def calc_product(p):
    prods = 1
    for x in range(1,p + 1):
        prods = prods * x
    return prods


print('To determine the sum or product of all numbers between 1 and a number, this amazing calculator will help you.')
while True:
    user_answer = int(input('Please enter an integer greater than 0: '))
    user_operation = (input('Enter "s" to compute the sum, or "p" to compute the product: '))
    if user_operation == 's':
        the_sum = calc_sum(user_answer)
        print(f'The sum is {the_sum}')
    elif user_operation == 'p':
        the_product = calc_product(user_answer)
        print(f'The product is {the_product}')
    else:
        print('Oops, unknown operation!')
    x = input('Would you like to calculate again? (y/n):')
    if x == 'n':
        break
```

quiz answer:
```python
def compute_sum(target_num):
    return sum(range(1, target_num+1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num+1):
        result *= num
    return result

prompt1 = "Please enter an integer greater than 0: "
prompt2 = ('Enter "s" to compute the sum, '
           'or "p" to compute the product: ')

number = int(input(prompt1))
operation = input(prompt2)
print()

if operation == "s":
    print("The sum of the integers between 1 and "
          f"{number} is {compute_sum(number)}.")
elif operation == "p":
    print("The product of the integers between 1 and "
          f"{number} is {compute_product(number)}.")
else:
    print("Oops. Unknown operation.")
```

For brevity and simplicity, our solution doesn't try too hard to validate the user input. For completeness, your solution should try to validate input and issue error messages as needed.

The solution defines two helper functions: compute_sum and compute_product. Which one the program uses depends on the input that is provided by the user ('p' or 's').

It's worth noting that, for summation, we leverage Python's built-in sum and range functions. Specifically, when using the range function, we provide target_num + 1 as the second argument, since range excludes the end value. This ensures that the target number itself is included in the computation.

There is no equivalent to sum for computing products built-in to Python, so we have to do so ourselves. Note that the NumPy package does have a prod function, but NumPy is overkill for this exercise.

### urther Exploration

Suppose the input was a list of space separated integers instead of just a single integer? How would your compute_sum and compute_product functions change?

my answer uses a comprehension to take the number in the list of numbers. and convert it to an int.
changed the sum part.
```python
    print(target_num) # list of strings ['1', '2']
    print(type(target_num)) # list of int

    print(int_numbers) # list of int [1, 2, 3]
    print(type(int_numbers)) # list

```
My answer below. BUT CAN USE :

>`return` `sum`(int_numbers)

>instead of `for` loop

```python
def compute_sum(target_num):
    sums = 0
    int_numbers = [int(num) for num in target_num]
    for num in int_numbers:
        sums += num
    return sums

def compute_product(target_num):
    result = 1
    int_numbers = [int(num) for num in target_num]
    for num in int_numbers:
        result *= num
    return result

prompt1 = "Please enter an integer greater than 0: "
prompt2 = ('Enter "s" to compute the sum, '
           'or "p" to compute the product: ')

user_answer = '1 2 3 4 5'
number = user_answer.replace(' ', '')
string_list_number = list(number)
operation = input(prompt2)
print()

if operation == "s":
    print("The sum of the integers between "
          f"'{user_answer}' is: {compute_sum(string_list_number)}.")
elif operation == "p":
    print("The product of the integers between "
          f"'{user_answer}' is: {compute_product(string_list_number)}.")
else:
    print("Oops. Unknown operation.")
```


# Question 7

# Question 8

# Question 9

# Question 10

# Question 11