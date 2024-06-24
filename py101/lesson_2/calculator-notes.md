Notes for Lesson 2 for PY101 course.
- Calculator notes for calculator.py & loan_calculator.py

# contents
- [contents](#contents)
  - [Bonus Calculator](#bonus-calculator)
    - [1. Asking the user for another calculation](#1-asking-the-user-for-another-calculation)
    - [2. Extracting messages in the program to a configuration file.](#2-extracting-messages-in-the-program-to-a-configuration-file)
    - [3. Internationalization](#3-internationalization)
- [Loan Calculator notes and code](#loan-calculator-notes-and-code)
- [Second to last](#second-to-last)
- [Final](#final)


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


# Check answer is not an empty string 
    # Trying to access an index of the empty string would raise an IndexError
    # `if answer and answer[0]` is a common Python idiom for dealing with empty 
    # strings that you don't want to try indexing

 # if answer and answer[0].lower() != 'y'
```
## Bonus Calculator 
### 1. Asking the user for another calculation
```python
# Our calculator asks the user for two numbers and an operation and then 
# exits after displaying the result. 
# Wouldn't it be nice if we could ask the user if they wanted to 
# perform another calculation and start a new calculation when they 
# respond with yes?

# answer = wrapped in while True
# check for empty string, then convert to lower case. if not match, then break.
# if anwer and answer[0].lower() != 'y'
```
### 2. Extracting messages in the program to a configuration file.
```python
# There are several messages sprinkled throughout the program. 
#Can we move them into some configuration file and access them by key? 
#That would let us manage the messages more easily, and we could even internationaliz
# the messages.

# What is JSON https://developers.squarespace.com/what-is-json
# import JSON # to store message in calculator_messages.json 
#   #open JSOn file for reading
# Now 'data' contains the contents of the JSON file as a Python dictionary or list
# Access the messages from that object with object property access syntax.

Step 1:

Created calculator_messages.json

Step 2:
import json
# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
     MESSAGES = json.load(file)
# Now 'MESSAGES' contains the loaded messages as a Python dictionary

# This line will load the contents of the calculator_messages.json file in the form of a dictionary and assign it to the MESSAGES constant. 

# Since it's a regular dictionary, we don't have to do anything before we use it. 


Step 3:
moved messages into a JSON object which is this:
 {
    "welcome_message": "Welcome to Calculator!",
    "invalid_number_message": "Hmm... that doesn't look like a valid number.",
 }

Step 4:
# replace this:
prompt('Welcome to Calculator!')

# with this:
prompt(MESSAGES['welcome_message'])
```
### 3. Internationalization
- Your calculator program is a hit, and it's being used all over the world! 
- The problem is, not everyone speaks English. 
- You now need to internationalize the messages in your calculator.
- You've already done the hard work of extracting all the messages to a configuration file. 
- Now, all you have to do is send that configuration file to translators and call the right translation in your code.

JSON templating - https://developers.squarespace.com/templating-basics

Step 1:
- Created a function to load json messages. 
- Added a fallback to English is the specific language is not found.
- syntax for fallback `dictionary.get(key, default_value)`
```python 
def message(language):
    with open('calculator_messages.json', 'r') as file:
        MESSAGES = json.load(file)
    return MESSAGES.get(language, MESSAGES["en"])  # Fallback to English if the specified language is not found
```
Step 2:
- changed json to include es.
```json
  {
    "en": {
        "welcome_message": "Welcome to Calculator!",
    },
    "es": {
        "welcome_message": "¡Bienvenido al Calculadora!",
       "invalid_number_message": "Hmm... eso no parece un número
    }
}
```
Step 4.
- Just before the calculator while loop, set prompt for choosing language. 
- open calculator_messages.json to 'load language_prompt' in 'en'
```python
with open('calculator_messages.json', 'r') as file:
    ALL_MESSAGES = json.load(file)

# Using English as the default language for the ask_language prompt
ask_language = (ALL_MESSAGES['en']['language_prompt'])
prompt(ask_language)
language = input().strip().lower()
```

**Note:**
In Python, when you use the open() function to open a file, the second argument specifies the mode in which you want to open the file. 

- 'r': Opens the file for reading. The file pointer is placed at the beginning of the file. This is the default mode when you don't specify one explicitly.
- 'w': Opens the file for writing. Truncates the file to zero length or creates a new file if it doesn't exist.
- 'a': Opens the file for appending. The file pointer is at the end of the file if the file exists. Otherwise, it creates a new file.
- 'r+': Opens the file for both reading and writing. The file pointer is placed at the beginning of the file.
- 'w+': Opens the file for both reading and writing. Truncates the file to zero length or creates a new file if it doesn't exist.
- 'a+': Opens the file for both reading and appending. The file pointer is at the end of the file if the file exists. Otherwise, it creates a new file.


# Loan Calculator notes and code

```python
#Build  a car loan/payment calculator.

"""
You'll need three pieces of information:

- the loan amount
- the Annual Percentage Rate (APR)
- the loan duration

From the above, you'll need to calculate the following two things:

- monthly interest rate (APR / 12)
- loan duration in months

------------
You can use the following formula:
m = p * (j / (1 - (1 + j) ** (-n)))

m = monthly payment
p = loan amount
j = monthly interest rate
n = loan duration in months

------------
-Don't use single letter variables.
-Print amount as dollar and cents amount.
-Run through pylint
-Code Review 
------------
Hints:

Decide what input formats your program expects. 
For example, should the user enter an interest rate of 5% as 5 or .05?
If you're working with an Annual Percentage Rate (APR), you need to convert it to a monthly interest rate for use in the formula.
Be careful about the loan duration -- are you working with months or years? 
Choose variable names carefully to assist in remembering.
Think about edge cases. 
There are plenty of edge cases to work with in this problem, and each presents interesting challenges. For instance, consider whether you want to support no-interest loans or loans that aren't for an integer number of years.
You can use this loan calculator to check your results.


"""

"""
PseudocodeWhat I want to do:
Create a calculator that:
1. Welcomes the user
2. Takes an input for:
    loan amount
    APR (compounded monthly)
    loan duration 
    (used to calculate monthly interest rate (APR/12), and loan duration in months)
3. write functions as needed.
4. use formula to produce the result --->  m = p * (j / (1 - (1 + j) ** (-n)))
5. print the monthly payment in dollars & cents as needed.
"""


#To fix length of result, need to convert float elsewhere. i assigned denominator to use in formula

#fix no integer for years or months

# fix monthyl payment 7.5 months from 131.1 
#my answer to include 0 at end = "{:.2f}".format(monthly_payment)
#"{:2f}f.format(monthly_payment)" formats as floating point number 
# .: Separates the precision specifier from the type specifier.
# 2: Specifies the number of digits after the decimal point.
# f: Indicates that the value should be formatted as a fixed-point number (i.e., a floating-point number). If 123.4 is given. 123.40 would be displayed to preserve 0


def prompt(message):
    print(f'==> {message}')

def invalid_number(number_input):
    try:
        float(number_input)
    except ValueError:
        return True
    return False

print('Welcome to the Monthly Car Payment Calculator!')

#loop to run calculator
while True:
    # Prompt for user to provide information.
    #Initializing loan_amount for user input. Stripping input of '$' and removing ',' if included
    while True:
        prompt('What is the loan amount in US Dollars?')
        loan_amount = input().strip('$').replace(',','')

    # Invalid to check if user input is a float or integer
        if not invalid_number(loan_amount):
            break
        print('Please enter a valid number.')

    # Prompt for user to provide.
    # Initializing loan_length for loan term.
    while True:
        prompt('Enter the number of months for the loan term')
        loan_length = input()

    # Invalid to check if user input is a float or integer
        if not invalid_number(loan_length):
            break
        print('Please enter a valid number.')

    # Prompt for user to provide.
    # Initializing apr variable for user input. stripping input of %.
    while True:
        prompt('What is the Annual Percentage Rate(APR)?')
        apr = input().strip('%')

    # Invalid to check if user input is a float or integer
    #intializing monthly_interest variable. Assigning monthly percentage.
        if not invalid_number(apr):
            break
        print('Please enter a valid Percentage, e.g., 8% or 10%')

    # Initializing monthly_interest. Convert apr to decimal, then into monthly.
    monthly_interest = (float(apr) / 100) / 12

    # Using formula to calculate results after converting string to float.
    # Split the formula to satisfy pylint into numerator/denominator
    # m = p * (j / (1 - (1 + j) ** (-n)))
    loan_denominator = 1 - (1 + monthly_interest) ** (-float(loan_length))
    result = float(loan_amount) * (monthly_interest / loan_denominator )

    # Round the result to two decimals
    monthly_payment = round(result, 2)

    # formatting for payment
    formatted_monthly_payment = "{:.2f}".format(monthly_payment)

    # Prompt monthly payment
    prompt(f'Your monthly payment is: ${formatted_monthly_payment}')

    # Prompt to ask user to try again
    # if answer doesn't equal 'y', loop continues.
    prompt('Would you like to calculate another Monthly Car Payment? (y/n)')
    answer = input()
    if answer[0].lower() != 'y':
        break

```


NEWEST ATTEMPT:

```python

import os


def prompt(message):
    print(f'==> {message}')

def invalid_number(number_input):
    if number_input is None:
        return True
    try:
        float(number_input)
        if number_input == float('inf') or number_input == float('-inf') or number_input != number_input:
            return True
    except ValueError:
            return True
    return False

def strip_input(input_string):
    return input_string.replace('$', '').replace('%', '').replace(',', '')

def formatted_results(result):
    if result = float(result):
        return "${:.2f}".format(round(result, 2))

os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to the Monthly Car Payment Calculator!')

#loop to run calculator
while True:
    # Prompt for user to provide information.
    #Initializing loan_amount for user input. Stripping input of '$' and removing ',' if included
    while True:
        prompt('Enter the loan amount (e.g,"50000.50"):')
        get_loan_amount = input().strip('"')
        #remove unwantedcharacters and convert to float)
        try:
            calc_loan_amount = float(get_loan_amount.replace('$','').replace(',',''))
        except ValueError:
            calc_loan_amount = float('nan') #To catch nan input then c
        #os.system('cls' if os.name == 'nt' else 'clear')
    # Invalid to check if user input is a float or integer (has to be more than 0)
        if not invalid_number(calc_loan_amount) and calc_loan_amount > 0:
            break
        print('Please enter a positive loan amount.')

    # Prompt for user to provide.
    # Initializing loan_length for loan term.
    while True:
        prompt('Enter the number of months for the loan term (e.g., "72"):')
        get_loan_length = input().strip('"')

        try:
            calc_loan_length = float(get_loan_length)
        except ValueError:
            calc_loan_length = float('nan')
        os.system('cls' if os.name == 'nt' else 'clear')

    # Invalid to check if user input is a float or integer
        if not invalid_number(calc_loan_length) and calc_loan_length > 0:
            break
        print('Please enter a positive loan term number.')

    # Prompt for user to provide.
    # Initializing apr variable for user input. stripping input of %.
    while True:
        prompt('Enter the Annual Percentage Rate(APR) (e.g., "7%"):')
        get_apr = input().strip('"')
        
        try:
            calc_apr = float(get_apr.strip('%'))
        except ValueError:
            calc_apr = float('nan')
        os.system('cls' if os.name == 'nt' else 'clear')

    # Invalid to check if user input is a float or integer
    #intializing monthly_interest variable. Assigning monthly percentage.
        if not invalid_number(calc_apr) and calc_apr >= 0:
            break
        print('Please enter a positive interest rate.')

    # Initializing monthly_interest. Convert apr to decimal, then into monthly.
    calc_monthly_interest = (calc_apr / 100) / 12

    # Using formula to calculate results after converting string to float.
    # Split the formula to satisfy pylint into numerator/denominator
    # m = p * (j / (1 - (1 + j) ** (-n)))
    #    loan_denominator = 1 - (1 + monthly_interest) ** (-float(loan_length))
    #result = float(loan_amount) * (monthly_interest / loan_denominator )
    loan_denominator = 1 - (1 + calc_monthly_interest) ** (-calc_loan_length)
    loan_monthly_payment = calc_loan_amount * (calc_monthly_interest / loan_denominator )


    # Formatting for payment
    # Round the result to two decimals
    display_loan_amount = "${:.2f}".format(round(calc_loan_amount, 2))
    display_apr = f"{calc_apr}% (compounded monthly)"
    display_loan_length = f"{calc_loan_length} months"
    display_monthly_payment = "${:.2f}".format(round(loan_monthly_payment, 2)).center(20)


    os.system('cls' if os.name == 'nt' else 'clear')
    # Prompt monthly payment
    print(f'''Based on the details you\'ve provided:
    - Loan Amount: {display_loan_amount}
    - Loan Term: {display_loan_length}
    - Annual Percentage Rate(APR): {display_apr}

    Your monthly payment would be:
     ~> {display_monthly_payment} <~
    ''')

    # Prompt to ask user to try again
    # if answer doesn't equal 'y', loop continues.
    prompt('Would you like to calculate another Monthly Car Payment? (y/n)')
    answer = input()
    if answer[0].lower() != 'y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
```

# Second to last
```python
#To fix length of result, need to convert float elsewhere. i assigned denominator to use in formula

# fix monthly payment 7.5 months from 131.1 
#my answer to include 0 at end = "{:.2f}".format(monthly_payment)
#"{:2f}f.format(monthly_payment)" formats as floating point number 
# .: Separates the precision specifier from the type specifier.
# 2: Specifies the number of digits after the decimal point.
# f: Indicates that the value should be formatted as a fixed-point number (i.e., a floating-point number). If 123.4 is given. 123.40 would be displayed to preserve 0

#clear screen - import os, function to clear 
# os.system('cls' if os.name == 'nt' else 'clear')  . if os is 'nt'(windows), use cls to clear. else 'clear'
# some others - loan no space, more descriptive variables done


# others 0, NaN, ah 
# fixed with:    
#    if number_input is None:
#        return True
#    try:
#        float_value = float(number_input) #need to assign to varaible to check 
#        # Check for infinity and NaN
#        if float_value == float('inf') or float_value == float('-inf') or float_value != float_value:
#            return True

# number with - handled

#"7%" quotes. done

# if they enter % more than once. %%%% done

#FIX  .00 ISSUE?!


import os


def prompt(message):
    print(f'==> {message}')

def invalid_number(number_input):
    if number_input is None:
        return True
    try:
        float_value = float(number_input) #need to assign to varaible to check 
        # Check for infinity and NaN
        if float_value == float('inf') or float_value == float('-inf') or float_value != float_value:
            return True
    except ValueError:
            return True
    return False

def strip_input(input_string):
    return input_string.replace('$', '').replace('%', '').replace(',', '').replace('"', '')

def formatted_results(result):
    formatted_result = "{:.2f}".format(result)
    if formatted_result[-2:] == '00':
        return "{:.0f}".format(result)
    else:
        return formatted_result


os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to the Monthly Car Payment Calculator!')

#loop to run calculator
while True:
    # Prompt for user to provide information.
    #Initializing loan_amount for user input. Stripping input of '$' and removing ',' if included
    while True:
        prompt('Enter the loan amount (e.g,"50000.50"):')
        get_loan_amount = input().strip('"')
        get_loan_amount = strip_input(get_loan_amount)
        os.system('cls' if os.name == 'nt' else 'clear')
        if not invalid_number(get_loan_amount):
            calc_loan_amount = float(get_loan_amount)
            if calc_loan_amount > 0:
                break
        print('Please enter a positive loan amount.')      


#        calc_loan_amount = float(get_loan_amount)
        #remove unwantedcharacters and convert to float)
#        try:
#            calc_loan_amount = float(get_loan_amount.replace('$','').replace(',',''))
#        except ValueError:
#            calc_loan_amount = float('nan') #To catch nan input then c

    # Invalid to check if user input is a float or integer (has to be more than 0)
#        if not invalid_number(calc_loan_amount) and calc_loan_amount > 0:
#            break
#        print('Please enter a positive loan amount.')


    # Prompt for user to provide.
    # Initializing loan_length for loan term.
    while True:
        prompt('Enter the number of months for the loan term (e.g., "72"):')
        get_loan_length = input()
        get_loan_length = strip_input(get_loan_length)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Invalid to check if user input is a float or integer
#        if not invalid_number(calc_loan_length) and calc_loan_length > 0:
        if not invalid_number(get_loan_length):
            calc_loan_length = float(get_loan_length)
            if calc_loan_length > 0:
                break
        print('Please enter a positive loan term number.')

    # Prompt for user to provide.
    # Initializing apr variable for user input. stripping input of %.
    while True:
        prompt('Enter the Annual Percentage Rate(APR) (e.g., "7%"):')
        get_apr = input().strip('"')
        get_apr = strip_input(get_apr)
        if not invalid_number(get_apr):
            calc_apr = float(get_apr)
            if calc_apr >= 0:
                break
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Please enter a positive interest rate.')

    # Invalid to check if user input is a float or integer
    #intializing monthly_interest variable. Assigning monthly percentage.
#        if not invalid_number(calc_apr) and calc_apr >= 0:
#            break

    # Initializing monthly_interest. Convert apr to decimal, then into monthly.
    calc_monthly_interest = (calc_apr / 100) / 12

    # Using formula to calculate results after converting string to float.
    # Split the formula to satisfy pylint into numerator/denominator
    # m = p * (j / (1 - (1 + j) ** (-n)))
    #    loan_denominator = 1 - (1 + monthly_interest) ** (-float(loan_length))
    #result = float(loan_amount) * (monthly_interest / loan_denominator )
    loan_denominator = 1 - (1 + calc_monthly_interest) ** (-calc_loan_length)
    loan_monthly_payment = calc_loan_amount * (calc_monthly_interest / loan_denominator )


    # Formatted results
    display_loan_amount = f"${formatted_results(calc_loan_amount)}"
    display_apr = f"{formatted_results(calc_apr)}% (compounded monthly)"
    display_loan_length = f"{formatted_results(calc_loan_length)} months"
    display_monthly_payment = f"${formatted_results(loan_monthly_payment)}"


    os.system('cls' if os.name == 'nt' else 'clear')
    # Displayed results
    print(f'''Based on the details you\'ve provided:
    - Loan Amount: {display_loan_amount}
    - Loan Term: {display_loan_length}
    - Annual Percentage Rate(APR): {display_apr}

    Your monthly payment would be:
     ~> {display_monthly_payment} <~
    ''')

    # Prompt to ask user if they want to try again.
    prompt('Would you like to calculate another Monthly Car Payment? (y/n)')
    answer = input()
    if answer[0].lower() != 'y':
        break
    os.system('cls' if os.name == 'nt' else 'clear')
```

# Final
```python
# Monthly Car Payment Calculator

import os
import json
import math

# Function to print prompt messages
def prompt(prompt_format):
    print(f'==> {prompt_format}')

# Function to check if input is invalid
def invalid_number(number_input):
    if number_input is None:
        return True
    try:
        float_value = float(number_input)
        # Check for infinity and Not-a-Number
        if math.isinf(float_value) or math.isnan(float_value):
            return True
    except ValueError:
        return True
    return False

# Function to strip unwanted characters from input
def strip_input(input_string):
    return input_string.translate(str.maketrans('', '', "$%,\"'"))

# Function to format results to max 2 decimal format or whole numbers
def formatted_results(result):
    formatted_result = f"{result:.2f}"
    #formatted_result = "{:.2f}".format(result)
    if formatted_result[-2:] == '00':
        return f"{result:.0f}"
    return formatted_result

# Function to retrieve messages from JSON file
def message(key, lang='en'):
    return MESSAGE[lang][key]

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGE = json.load(file)

os.system('cls' if os.name == 'nt' else 'clear')

# Calculator introduction
print('Welcome to the Monthly Car Payment Calculator!')

# Language selection prompt
while True:
    prompt(message('choose_language', lang='en'))
    language_choice = input().strip().lower().replace("'", '')

    # Validate language choice
    if language_choice not in ['en', 'es']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"'{language_choice}'{message('invalid', lang='en')}")
        print(f'''{message('invalid_language', lang='en')}
        ''')
        continue
    break

#clear before running calculator
os.system('cls' if os.name == 'nt' else 'clear')

# Loop to run calculator
while True:

    # Prompt for loan amount input
    while True:
        prompt(message('ask_amount', lang=language_choice))
        get_loan_amount = input()
        get_loan_amount = strip_input(get_loan_amount)
        os.system('cls' if os.name == 'nt' else 'clear')
        if not invalid_number(get_loan_amount):
            loan_amount = float(get_loan_amount)
            if loan_amount > 0:
                break
        print(f"'{get_loan_amount}'{message('invalid', lang=language_choice)}")
        print(f'''{message('invalid_loan_amount', lang=language_choice)}
        ''')

    # Prompt for loan term input
    while True:
        prompt(message('ask_length', lang=language_choice))
        get_loan_length = input()
        get_loan_length = strip_input(get_loan_length)
        os.system('cls' if os.name == 'nt' else 'clear')
        if not invalid_number(get_loan_length):
            loan_length = float(get_loan_length)
            if loan_length > 0:
                break
        print(f"'{get_loan_length}'{message('invalid', lang=language_choice)}")
        print(f'''{message('invalid_loan_length', lang=language_choice)}
        ''')

    # Prompt for APR input
    while True:
        prompt(message('ask_apr', lang=language_choice))
        get_apr = input()
        get_apr = strip_input(get_apr)
        if not invalid_number(get_apr):
            calc_apr = float(get_apr)
            if calc_apr >= 0:
                break
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"'{get_apr}'{message('invalid', lang=language_choice)}")
        print(f'''{message('invalid_apr', lang=language_choice)}
        ''')

    # Function to check zero apr for display message.
    def check_zero_apr(apr_value):
        if apr_value != 0:
            apr_message = f"{formatted_results(calc_apr)}%(compounded monthly)"
        else:
            apr_message = "0% interest"
        return apr_message

    # Calculate monthly interest, then calculate monthly payment
    def payment(apr_value):
        if apr_value != 0:
            monthly_interest = (calc_apr / 100) / 12
            calc_devisor = 1 - (1 + monthly_interest) ** (-loan_length)
            monthly_payment = loan_amount * (monthly_interest / calc_devisor)
        else:
            monthly_interest = 0
            monthly_payment = loan_amount / loan_length
        return monthly_payment


    # Formatted results
    display_apr = check_zero_apr(calc_apr)
    display_loan_amount = f"${formatted_results(loan_amount)}"
    display_loan_length = f"{formatted_results(loan_length)} month(s)"
    display_monthly_payment = f"${formatted_results(payment(calc_apr))}"

    # Clear screen before displaying results
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display results
    print(f'''{message('details_provided', lang=language_choice)}
    {message('amount_provided', lang=language_choice)}{display_loan_amount}
    {message('term_provided', lang=language_choice)}{display_loan_length}
    {message('apr_provided', lang=language_choice)}{display_apr}

    {message('conclude', lang=language_choice)}
    ~> {display_monthly_payment} <~

    ''')

    # Prompt to ask user if they want to perform another calculation
    prompt(message('another_calculation', lang=language_choice))
    answer = input()
    if answer[0].lower() != 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(message('goodbye_message', lang=language_choice))
        break
    os.system('cls' if os.name == 'nt' else 'clear')
```