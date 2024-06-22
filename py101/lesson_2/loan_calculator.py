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
5. print the monthly payment
"""

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
    #prompt for user to provid information. Initializing loan_amount for user input
    prompt('What is your loan amount?')
    loan_amount = input()
    #invalid to check if user input is a float or integer
    if not invalid_number(loan_amount):
        break
    print('Please enter a valid number.')