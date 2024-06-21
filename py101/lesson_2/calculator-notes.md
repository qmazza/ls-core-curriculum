```python
#Our first program in this course will be a command line calculator program that will:

#Ask the user for two numbers.
#Ask the user for the type of operation to perform: add, subtract, multiply or divide.
#Perform the calculation and display the result


# === >

# Write pseudosteps before starting. Example below

# === >
# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.


def prompt(message): #prepends marker to fron to fstring that it prints.
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError: #Accept valueError to keep integer. But don't want others.
        return True
    return False

prompt('Welcome to Calculator!')
# Ask the user for the numbers
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide') # hacve 2 options. Line continuation backslash at end of line, or triple qotes. I changed this to triple quote to define multi-line string and shorten for pylint
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output= int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)
prompt(f"The result is: {output}")

#       Below if elif else logic is the use-case that matches the match case statement was designed to use.

#if operation == '1':   # '1' represents addition
#                       # Inputs are strings, so we must compare operation variable with string '1'. Number version won't evaluate as True
#    output = int(number1) + int(number2) # Need to convert inputs into integer before adding.
#elif operation == '2': # '2' represents subtraction
#    output = int(number1) - int(number2)
#elif operation == '3': # '3' represents multiplication
#    output = int(number1) * int(number2)
#elif operation == '4': # '4' represents division
#    output = int(number1) / int(number2)


#negative multiplied by negative = a positive.
#positive multiple by negative = a negative.

#divide gives float
```