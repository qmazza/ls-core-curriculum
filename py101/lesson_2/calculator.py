#First program in course will be a command line calculator program

#Ask the user for two numbers.
#Ask the user for the type of operation to perform.
# - add, subtract, multiply or divide.
#Perform the calculation and display the result

#default language
import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(messages('welcome'))
while True:
    # Language selection prompt
    prompt("Choose your language (en/es): ")
    language_choice = input().strip().lower()

    # Validate language choice
    if language_choice not in ['en', 'es']:
        prompt("Invalid choice. Please enter 'en' or 'es'.")
        continue


    while True:
        prompt(messages('number_prompt_1', lang=language_choice))
        number1 = input()

        if not invalid_number(number1):
            break

        prompt(messages('invalid_number', lang=language_choice))

    while True:
        prompt(messages('number_prompt_2', lang=language_choice))
        number2 = input()

        if not invalid_number(number2):
            break

        prompt(messages('invalid_number', lang=language_choice))

    while True:
        prompt(messages('operation_prompt', lang=language_choice))
        operation = input()

        if operation in ["1", "2", "3", "4"]:
            break

        prompt(messages('invalid_operation', lang=language_choice))

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            if float(number2) == 0:
                prompt(messages('division_by_zero', lang=language_choice))
                exit(1)
            output = float(number1) / float(number2)

    output = round(output, 2)  # Round the result to two decimals

    prompt(messages('result', lang=language_choice).format(output=output))

    prompt(messages('another_operation', lang=language_choice))
    answer = input()
    if answer[0].lower() != 'y':
        break