"""
Rock paper scissors lizard spock
"""
import random
import json
import os

# CONSTANTs
VALID_CHOICES = ['rock','paper','scissors','lizard','spock',
'r','p','s','l','sp']

COMPUTER_CHOICES = ['rock','paper','scissors','lizard','spock']

DICT_CHOICES = {'r': 'rock',
                'p': 'paper', 
                's': 'scissors',
                'l': 'lizard',
                'sp': 'spock'}

winning_choice = {
    'rock': {'scissors', 'lizard'},
    'paper': {'rock', 'spock'},
    'scissors': {'paper', 'lizard'},
    'lizard': {'spock', 'paper'},
    'spock': {'scissors', 'rock'}
}


def display_winner(player, computer):
    '''This function checks for the winner'''
    if computer in winning_choice[player]:
        print(MESSAGES['player_wins'].center(40))
    elif player in winning_choice[computer]:
        print(MESSAGES['computer_wins'].center(40))
    else:
        print(MESSAGES['no_winner'].center(40))



def message(key):
    '''Function to retrieve messages from JSON file'''
    return MESSAGES[key]

with open('rock_paper_scissors.json', 'r') as file:
    MESSAGES = json.load(file)


def format_choices():
    '''This function joins and formats choices for displaying.'''
    return ''.join(f'\n- {key}) {value} '
    for key, value in DICT_CHOICES.items()).title()


def convert_choice(choice):
    '''This function is converts the users entry of the word into
    a valid choice'''
    if choice in DICT_CHOICES:
        return DICT_CHOICES[user_choice]
    return choice


def prompt(prompt_messages):
    '''This function improves readability'''
    print(f'==> {prompt_messages}')


def display_choice():
    '''This function formats and displays both the users and
    computers choice'''
    prompt(MESSAGES['display_choices'].format(user_choice=user_choice,
    computer_choice=computer_choice).title())


# Main loop to run the program
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Prompt user for their choice.
    print(MESSAGES['welcome'])
    prompt(MESSAGES['ask_choice'] + format_choices())
    user_choice = input().lower()


    # Validate user input.
    while True:
        if user_choice not in VALID_CHOICES:
            prompt(MESSAGES['invalid_entry'])
            user_choice = input().lower()
        else:
            break

    # If user_choice is a key DICT_CHOICES, return value
    user_choice = convert_choice(user_choice)

    # Computers choice
    computer_choice = random.choice(COMPUTER_CHOICES)

    # Clear screen then Display choices made
    os.system('cls' if os.name == 'nt' else 'clear')
    display_choice()

    # Check results and display the winner
    display_winner(user_choice, computer_choice)

    # Ask the user to play again
    while True:
        prompt(MESSAGES['play_again'])
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['invalid_answer'])

    # After validating input that there is at least an index of 0, break loop.
    if answer[0] == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['goodbye'])
        break