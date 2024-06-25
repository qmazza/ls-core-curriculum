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