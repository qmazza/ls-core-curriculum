"""
Rock paper scissors lizard spock
"""
import random
import json
import os

# Constants and dictionaries
VALID_CHOICES = ['rock','paper','scissors','lizard','spock',
'r','p','s','l','sp']

COMPUTER_CHOICES = ['rock','paper','scissors','lizard','spock']

DICT_CHOICES = {'r': 'rock',
                'p': 'paper', 
                's': 'scissors',
                'l': 'lizard',
                'sp': 'spock'}

WINNING_CHOICE = {
    'rock': {'scissors', 'lizard'},
    'paper': {'rock', 'spock'},
    'scissors': {'paper', 'lizard'},
    'lizard': {'spock', 'paper'},
    'spock': {'scissors', 'rock'}
}

# Game Score
player_wins = 0
computer_wins = 0
ties = 0
round_number = 1


# editing for winner of 5
def display_winner(player, computer):
    '''This function checks for the winner'''
    while True:
        if computer in WINNING_CHOICE[player]:
            print(MESSAGES['player_wins'].center(40))
            return 'player'
        elif player in WINNING_CHOICE[computer]:
            print(MESSAGES['computer_wins'].center(40))
            return 'computer'
        else:
            print(MESSAGES['no_winner'].center(40))
            return 'tie'
        break

def game_count(winner):
    '''This function increments the score count for player,
    computer, and ties'''
    global player_wins, computer_wins, ties, round_number
    if winner == 'player':
        player_wins += 1
        round_number += 1
    elif winner == 'computer':
        computer_wins += 1
        round_number += 1
    else:
        ties += 1
        round_number += 1


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


def score_check():
    '''This function checks the score. If player or computer win
    3 out of 5 times, the game is over and scores are reset'''
    if player_wins == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Congratulations! You\'ve beat the computer and won the game!')
        display_current_score()
        score_reset()
        if play_again() == 'n':
            return False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    elif computer_wins == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Game over. Sorry, you\'ve lost to the computer.')
        display_current_score()
        score_reset()
        if play_again() == 'n':
            return False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    return True

def score_reset():
    '''Resets the score if user wants to continue'''
    global player_wins, computer_wins, ties, round_number
    player_wins = 0
    computer_wins = 0
    ties = 0
    round_number = 1

def play_again():
    while True:
        prompt(MESSAGES['play_again'])
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            return answer
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['invalid_answer'])

def display_current_score():
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")
    print(MESSAGES['current_round'].format(round=round_number))

os.system('cls' if os.name == 'nt' else 'clear')
print(MESSAGES['welcome'])
# Main loop to run the program
while True:

    # Prompt user for their choice.
    prompt(MESSAGES['ask_choice'] + format_choices())
    user_choice = input().lower()


    # Validate user input.
    while True:
        if user_choice not in VALID_CHOICES:
            os.system('cls' if os.name == 'nt' else 'clear')
            prompt(MESSAGES['invalid_entry'])
            user_choice = input().lower()
        else:
            break

    # If user_choice is a key DICT_CHOICES, return value
    user_choice = convert_choice(user_choice)

    # Computers choice
    computer_choice = random.choice(COMPUTER_CHOICES)

    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display choices made
    display_choice()

    # Check results and display the winner of round
    result = display_winner(user_choice, computer_choice)

    # Update score count
    game_count(result)

    # Display current scores
    display_current_score()

    # Check for game winner.
    if not score_check():
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['goodbye'])
        break


    prompt(MESSAGES['new_round_greeting'])
    
  #  answer = play_again()
    #if player_wins or computer_wins == 3:
    #     play_again()

        # Ask the user to play again
#    if player_wins or computer_wins == 3:

        # After validating input that there is at least an index of 0, break loop.
 #   if answer[0] == 'n':
  #      os.system('cls' if os.name == 'nt' else 'clear')
   #     prompt(MESSAGES['goodbye'])
   #     break
    #os.system('cls' if os.name == 'nt' else 'clear')