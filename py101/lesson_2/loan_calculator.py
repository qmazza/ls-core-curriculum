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

# Clear before starting Calculator
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