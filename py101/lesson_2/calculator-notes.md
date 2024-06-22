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