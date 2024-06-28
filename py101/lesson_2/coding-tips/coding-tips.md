Notes for Lesson 2 for PY101 course.
- Coding Tips
  
# Contents
- [Contents](#contents)
  - [Dramatic Experience and Retaining Knowledge](#dramatic-experience-and-retaining-knowledge)
  - [Naming Things](#naming-things)
  - [Naming Conventions](#naming-conventions)
  - [Valid but Non-Idiomatic Names](#valid-but-non-idiomatic-names)
  - [Invalid Names](#invalid-names)
  - [Avoid Magic Numbers](#avoid-magic-numbers)
  - [Formatting](#formatting)
  - [Mutating Constants](#mutating-constants)
  - [Function Guidelines](#function-guidelines)
  - [Functions should be at the same level of abstraction](#functions-should-be-at-the-same-level-of-abstraction)
  - [Function Names Should Reflect What They Do](#function-names-should-reflect-what-they-do)
  - [Displaying Output](#displaying-output)
  - [Miscellaneous Tips](#miscellaneous-tips)
  - [Approach to Learning](#approach-to-learning)


## Dramatic Experience and Retaining Knowledge

- Programming requires repetition.
- Taking a couple hours to debut a small problem is your **burn**
- Burn keeps helps you retain for the long haul.
- Embrace burns and remember their lessons.


## Naming Things

- Choose descriptive names.
- Variable names should describe content of the variable.


## Naming Conventions
- Names that follow naming conventions in the Python style guide are **idomatic names**
- Idiomatic or not depends on what kind of name we're describing.
- examples that are and aren't **idiomatic** in various ategories and when.

| Category                                       | Name            | Notes                              |
|------------------------------------------------|-----------------|------------------------------------|
| Non-constant variables and object properties   | employee        |                                    |
|                                                | number          |                                    |
|                                                | fizz_buzz       |                                    |
|                                                | speed_of_light  |                                    |
|                                                | destination_url | url is an acronym                  |
|                                                | _var            | meant for internal use             |
|                                                | var_            | used to avoid conflicts with keywords |
| Classes                                        | Cat             |                                    |
|                                                | BoxTurtle       |                                    |
|                                                | FlightlessBird  |                                    |
| Functions and methods                          | parse_url       | url is an acronym                  |
|                                                | go_faster       |                                    |
| Constant Names                                 | DEFAULT_TIMEOUT | SCREAMING_SNAKE_CASE               |
|                                                | MIN_AGE         |                                    |


## Valid but Non-Idiomatic Names

| Category                                     | Name            | Notes                           |
|----------------------------------------------|-----------------|---------------------------------|
| Universally non-idiomatic                    | π               | Non ASCII characters            |
|                                              | __var __         | except as defined by Python     |
|                                              | user_Profile    | should be all lowercase         |
|                                              | userProfile     | camelCase is not idiomatic      |
|                                              | milesperhour    | Undifferentiated words          |
| Non-constant variables and dictionary keys   | FIZZ_BUZZ       | SCREAMING_SNAKE_CASE            |
|                                              | fizzBUZZ        | camelCase (sorta); non-idiomatic|
| Classes                                      | cat             | Begins with lowercase letter    |
|                                              | make_turtle     | snake_case                      |

## Invalid Names
| Category   | Name         | Notes                                |
|------------|--------------|--------------------------------------|
| 42ndStreet | Begins with a digit                                 |
| fizz buzz  | contains space                                      |
| fizz-buzz  | contains special character except underscore        |
| for        | Python keyword                                      |


## Avoid Magic Numbers

- A **magic number** is a number (or other simple value) that appears in your program without any information that describes what that number represents.
- Such as 'in range(5)'  - Why 5 in particular?
- The way to avoid magic numbers is to use constants.

```python
NUMBER_CARDS_IN_HAND = 5

def deal_hand():
    hand = []
    for card_number in range(NUMBER_CARDS_IN_HAND):
        hand.append(deal_card())

    return hand
```

- Sometimes you may need the unicode. So something like this example works:

```python
FIRST_CHARACTER_CODE = ord('a')
LAST_CHARACTER_CODE = ord('z')
```
- Reason being that te numbers are explain in context instead of 'FIRST_CHARACTER_CODE = 97'
- 


## Formatting

- Always use 4 space haracters, not tab characters.
- Mind length. Make sure stays easy to read.
- Use spaces.

## Mutating Constants

- Constants are values that remain unchanged through the program's execution.
- In Python, avoid mutating(changing) constants.
- use SCREAMING_SNAKE_CASE, and treat as read-only values.

## Function Guidelines

- Functions should do one thing, and that responsibility is limited.
- SHould be short (10 lines). Consider splitting if 15 or longer.
- Function has **side effects** if it:
  - Reassigns any non-local variables. Reassigning a variable in outer scope is a side effect.
  - Modifies value of any data structure passed as an argument or accessed directly from outer scope. Mutating an object such as appending an element to a list argument is a side effect.
  - Reads from or writes to a file, network connection, browser, or the systme hardware. **Side effects like this include printing and reading input from the terminal.**
  - Raises an exception without handling it.
  - calls another function that has side effects.
```python
# Examples of side effects
# add_to_list returns and has side effect. this shouldn't both be done:

# side effect: prints output
# returns: None

def display_total(num1, num2):
    print(num1 + num2)

# side effect: mutates the passed-in list
# returns: updated list

def add_to_list(target_list, value_to_append):
    target_list.append(value_to_append)
    return target_list
```

```python
# Example with no side effect

# side effect: none
# returns: a new number

def compute_total(num1, num2):
    return num1 + num2
```

- Most functions should return a useful value or should have side effect, not both.
- Avoid doing the example given as `add_to_list` does both. You may have trouble remembering.
- `Useful value` means function returns a value that has meaning to the calling code.
- functions returning arbitrary value or the same value (such as `None`) is not a useful value
- exceptions: 
  - read from database that displays on console.
  - display prompt for input from users keyboard, read input from terminal, then return value.
  - accessing a database and reading and writing from the terminal are side effects, but you may still need a return value.
- function names should reflect whether side effects may occur. Such as `display_total`
- funciton that computes the total for it would be `compute_total`
  
## Functions should be at the same level of abstraction

- When working with a function, mentally extract the function from the progrma and work with it in isolation. Should be able to feed it inputs and expect outputs.
- Can use it without thinking about the implementation.
- Compartmentalizes focus when working on large code bases.
- programming becomes much simpler due to the functions all on the same layer of abstraction.
  -  `deal()` and `iterate_through_cards()` are not at same abstraction level.
     - deal is a verb used for the game. iterate_through_cards is implementation details which you shouldn't care about. 
- Should be able to look at function later and understand how to use without studying their implementation.

## Function Names Should Reflect What They Do

- Functions shold reflet whether side effects occur:

```python
def updated_total(total, cards):
    # ... some code here
```

- Seeing `updated_total`, we assume it mutates something.
- Use naming conventions to signify functions that mutate vs return
- Avoid - `get_and_display_total` (displays and returns)
  - There are exceptions. one is: function requests input then returns that input. (input funciton lets you read user input from terminal)
- Build small functions like LEGO blocks. Stand-alone pieces used to piece together larger structures.
- when functions become convoluted due to complex logic(meaning you don't understand problem well enough to break it into well-compartmentalized pieces), refactor code to reflect increased clarity.

## Displaying Output

- If i'm printing a welcome mesage. `def print_welcome():` is the clear option for  function name.

## Miscellaneous Tips

- Watch indentation. 4 spaces, not tabs.
- Name functions from perspective of using them later.
  - think about how you want to invoke. implementation later.
  - For example, if you have a list of cards, and you want to write a function to find the ace, your function should be called find_ace, and you can use it like this: ace = find_ace(cards). 
- Know when to use regular **while** loop vs generic **while True** loop.

Examples:
```python

while answer.lower() != 'n':
    print('Continue? (y/n)')
    answer = input()
```
With this code: Python throws an exception of "NameError: name 'answer' is not defined". To correct it, we must initialize answer before the while statement, like this:

```python
answer = ''
while answer.lower() != 'n':
    print('Continue? (y/n)')
    answer = input()
```

This would work, but another implementation would be to use a generic loop with a break statement:

```python
while True:
    print('Continue? (y/n)')
    answer = input()
    if answer.lower() == 'n':
        break
```

Here, all the code is contained in the loop, and it's slightly easier to reason about it. 

You could even do without the answer variable and use the user's input (i.e. input()) in the if condition directly, but using answer is fine -- 

Clarity over terseness.

## Approach to Learning

- Learning takes attention and focus.
- Need plenty of repetition.
- You'll re-visit topics over and over, and, through experience, the most important information will get burned into your long-term memory
