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

print('Welcome to Calculator!')

# Ask the user for the numbers
print("What's the first number?")
number1 = input()
print("What's the second number?")
number2 = input()

print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':   # '1' represents addition
                       # Inputs are strings, so we must compare operation variable with string '1'. Number version won't evaluate as True
    output = int(number1) + int(number2) # Need to convert inputs into integer before adding.
elif operation == '2': # '2' represents subtraction
    output = int(number1) - int(number2)
elif operation == '3': # '3' represents multiplication
    output = int(number1) * int(number2)
elif operation == '4': # '4' represents division
    output = int(number1) / int(number2)
print(f"The result is: {output}")

#Issues - negative numbers aren't being kept when converting from string to integer?

