## Content


# Draft Code before start of Bonus features
"""
In this assignment, we'll build a Rock Paper Scissors game. 
Rock Paper Scissors is a simple game played between two opponents. 
Both opponents choose an item from rock, paper, or scissors. 
The winner is decided according to the following rules:

If player a chooses rock and player b chooses scissors, player a wins.
If player a chooses paper and player b chooses rock, player a wins.
If player a chooses scissors and player b chooses paper, player a wins.
If both players choose the same item, neither player wins. It's a tie.
Our version of the game lets the user play against the computer. The game flow should go like this:

The user makes a choice.
The computer makes a choice.
The winner is displayed.
"""
```python
import random

#CONSTANTS
VALID_CHOICES = ['rock','paper','scissors']

# Prompt message start helper funciton
def prompt(message):
    print(f'==> {message}')

# Helper function to display winner
def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        prompt('You win!')
    elif ((player == 'rock' and computer == 'spaper') or
        (player == 'paper' and computer == 'scissors') or
        (player == 'scissors' and computer == 'rock')):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")    



while True:
    #use .lower? . 
    # Can interpolate valid_choce with f string
    # ', ' with join to concatenate into a string.
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    # Validate user input
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    # Computers choice
    computer_choice = random.choice(VALID_CHOICES)

    # Display choices
    prompt(f'You chose {choice}, computer chose {computer_choice}')

    # function to check display the winner while being more readable and easier to change.
    display_winner(choice, computer_choice)
    
    # Player Wins:
    # rock beats scissors
    # paper beats rock
    # scissors beats paper

    # choice = computer_choice tie

    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):# Checks for a valid input. Wont let user enter empty string.
            break
        
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    # After validating input that there is at least an index of 0, break loop.
    if answer[0] == 'n':
        break

```

# Bonus draft
"""
Rock paper scissors lizard spock

1. Lizard Spock This game is a variation on the Rock Paper Scissors game that adds two more options - Lizard and Spock. The full explanation and rules are here. There's also a hilarious Big Bang Theory video about it here.

The goal of this bonus is to add Lizard and Spock to your game.

2. Shortened Input Typing the full word "rock" or "lizard" is tiring. Update the program so the user can type "r" for "rock," "p" for "paper," and so on. Note that if you do bonus #1, you'll have two words that start with "s." How do you resolve that?

3. Best of Five Keep score of the player's and computer's wins. When either the player or computer reaches three wins, the match is over, and the winning player becomes the grand winner. Don't add your incrementing logic to display_winner. Keep your functions simple; they should perform one logical task -- no more, no less.

4. Pylint complaints Run your program through Pylint to see what problems it identifies, and try to fix them.
"""

```python
import random

# CONSTANTs
'''

'''
VALID_CHOICES = ['Rock','Paper','Scissors','Lizard','Spock','r','p','s','l','sp']
SHORT_CHOICES = ['r','p','s','l','sp']
COMPUTER_CHOICES = ['Rock','Paper','Scissors','Lizard','Spock']

def convert_choice(user_choice):
    match user_choice:
        case 'r':
            user_choice = 'Rock'
        case 'p':
            user_choice = 'Paper'
        case 's':
            user_choice = 'Scissors'
        case 'l':
            user_choice = 'Lizard'
        case 'sp':
            user_choice = 'Spock'
    return user_choice



# Prompt message start helper funciton
def prompt(message):
    print(f'==> {message}')

# Helper function to display winner
def display_winner(player, computer):
    if ((player == 'rock' and (computer == 'scissors' or computer == 'lizard')) or
        (player == 'paper' and (computer == 'rock' or computer == 'spock')) or
        (player == 'scissors' and (computer == 'paper' or computer == 'lizard')) or
        (player == 'lizard' and (computer == 'spock' or computer == 'paper')) or
        (player == 'spock' and (computer == 'scissors' or computer == 'rock'))):
        prompt('You win!')
    elif ((player == 'rock' and (computer == 'paper' or computer == 'spock')) or
        (player == 'paper' and (computer == 'scissors' or computer == 'lizard')) or
        (player == 'scissors' and (computer == 'rock' or computer == 'spock')) or
        (player == 'lizard' and (computer == 'rock' or computer == 'scissors')) or
        (player == 'spock' and (computer == 'paper' or computer == 'lizard'))):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")


while True:
    #use .lower? . 
    # Can interpolate valid_choce with f string
    # ', ' with join to concatenate into a string.
    
    prompt(f'Choose one: {', '.join(COMPUTER_CHOICES)}')
    user_choice = input().lower()

    # Validate user input. if short choice, convert and pass to choice
    while user_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        user_choice = input()
    
    if user_choice in SHORT_CHOICES:
        player_choice = convert_choice(user_choice)

    # Computers choice
    computer_choice = random.choice(COMPUTER_CHOICES)

    # Display choices
    prompt(f'You chose {player_choice}, Computer chose {computer_choice}')

    # function to check display the winner while being more readable and easier to change.
    display_winner(user_choice, computer_choice)
    
    # Player Wins:
    # rock beats scissors
    # paper beats rock
    # scissors beats paper

    # choice = computer_choice tie

    prompt('Do you want to play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):# Checks for a valid input. Wont let user enter empty string.
            break
        
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    # After validating input that there is at least an index of 0, break loop.
    if answer[0] == 'n':
        print("Thanks for playing! Goodbye!")
        break

```

# Final draft before some last edits and pylint

```python
import random
import json
import os

# CONSTANTs
VALID_CHOICES = ['rock','paper','scissors','lizard','spock','r','p','s','l','sp']
DICT_CHOICES = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'l': 'lizard', 'sp': 'spock'}
COMPUTER_CHOICES = ['rock','paper','scissors','lizard','spock']


def message(key):
    '''Function to retrieve messages from JSON file'''
    return MESSAGES[key]

with open('rock_paper_scissors.json', 'r') as file:
    MESSAGES = json.load(file)


def format_choices(dict_choices):
    '''This function joins and formats choices for displaying.'''
    return ''.join('\n- {}) {} '.format(key, value) for key, value in DICT_CHOICES.items()).title()


def convert_choice(user_choice):
    '''This function is converts the users entry of the word into a valid choice'''
    if user_choice in DICT_CHOICES:
        return DICT_CHOICES[user_choice]
    else:
        return user_choice


def prompt(message):
    '''This function improves readability'''
    print(f'==> {message}')


def display_choice():
    '''This function formats and displays both the users and
    computers choice'''
    prompt(MESSAGES['display_choices'].format(user_choice=user_choice, 
    computer_choice=computer_choice).title())


def display_winner(player, computer):
    '''This function checks the users' choice vs computers for: the winner, the loser
    or if it's a tie. Then displays the winner.'''
    if ((player == 'rock' and (computer == 'scissors' or computer == 'lizard')) or
        (player == 'paper' and (computer == 'rock' or computer == 'spock')) or
        (player == 'scissors' and (computer == 'paper' or computer == 'lizard')) or
        (player == 'lizard' and (computer == 'spock' or computer == 'paper')) or
        (player == 'spock' and (computer == 'scissors' or computer == 'rock'))):
            print(MESSAGES['player_wins'].center(40))
    elif ((player == 'rock' and (computer == 'paper' or computer == 'spock')) or
        (player == 'paper' and (computer == 'scissors' or computer == 'lizard')) or
        (player == 'scissors' and (computer == 'rock' or computer == 'spock')) or
        (player == 'lizard' and (computer == 'rock' or computer == 'scissors')) or
        (player == 'spock' and (computer == 'paper' or computer == 'lizard'))):
            print(MESSAGES['computer_wins'].center(40))
    else:
            print(MESSAGES['no_winner'].center(40))



# Main loop to run the program
while True:
    # Clear before starting Calculator
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Prompt user for their choice.
    prompt(MESSAGES['ask_choice'] + format_choices(DICT_CHOICES))
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
        if answer.startswith('n') or answer.startswith('y'): # Checks for a valid input. Wont let user enter empty string.
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['invalid_answer'])

    # After validating input that there is at least an index of 0, break loop.
    if answer[0] == 'n':
        prompt(MESSAGES['goodbye'])
        break
```

# Final edit

```python
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


def display_winner(player, computer):
    '''This function checks for the winner'''
    while True:
        if computer in WINNING_CHOICE[player]:
            print(MESSAGES['player_wins'].center(40))
            return 'player'
        if player in WINNING_CHOICE[computer]:
            print(MESSAGES['computer_wins'].center(40))
            return 'computer'
        print(MESSAGES['no_winner'].center(40))
        return 'tie'


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
        prompt(MESSAGES['player_game_winner'])
        display_current_score()
        score_reset()
        if play_again() == 'n':
            return False
        os.system('cls' if os.name == 'nt' else 'clear')
    elif computer_wins == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['computer_game_winner'])
        display_current_score()
        score_reset()
        if play_again() == 'n':
            return False
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
    ''' This function asks the user if they want to play
    again.'''
    while True:
        prompt(MESSAGES['play_again'])
        answer = input().lower()
        if answer.startswith('n') or answer.startswith('y'):
            return answer
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['invalid_answer'])


def display_current_score():
    '''This function displays the current score and rount'''
    print(MESSAGES['display_current_score'].format(player_wins=
    player_wins, computer_wins=computer_wins, ties=ties))
    print(MESSAGES['current_round'].format(round=round_number))


# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Weclome to the game
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

    # Check for game winner. If False, end game.
    if not score_check():
        os.system('cls' if os.name == 'nt' else 'clear')
        prompt(MESSAGES['goodbye'])
        break

    # Message for game win conditions in next rounds.
    prompt(MESSAGES['new_round_rule'])
```
