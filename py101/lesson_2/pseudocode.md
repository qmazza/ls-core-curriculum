Notes for Lesson 2 for PY101 course.
- Pseudocode
  
# Contents
- [Contents](#contents)
- [Follow a rigid format when programming.](#follow-a-rigid-format-when-programming)
- [Formal Pseudocode](#formal-pseudocode)
  - [Translating Pseudocode to Program Code](#translating-pseudocode-to-program-code)
  - [Exercises](#exercises)




# Follow a rigid format when programming.
**example:**
pseudocode for a function that determines which number in a collection has the greatest value.

```Given a collection of numbers.

- Iterate through the collection one by one.
  - save the first value as the starting value.
  - for each iteration, compare the saved value with the current value.
    - if the current number is greater
      - reassign the saved value as the current value
    - otherwise, if the current value smaller or equal
      - move to the next value in the collection
  - After iterating through the collection, return the saved value.
  ```
 
Load the problem into our brain first

**There are two layers to solving any problem:**
- The logical problem domain layer.
- The syntactical programming language layer.

Doing both when not fluent is difficult.

To verify the logic, we translate the pseudocode into programming code, which is where you can focus on programming language syntax issues without having it interrupt your flow.

# Formal Pseudocode
Before translating pseudocode to program code, formalize it.

- Keywords to help us break down the program logic into concrete commands, which makes translating to code more natural.

**Keyword and meanings we will use**
- START	start of the program
- SET	set a variable that we can use for later
- GET	retrieve input from user
- PRINT	display output to user
- READ	retrieve a value from a variable
- IF/ELSE IF/ELSE	show conditional branches in logic
- WHILE	show looping logic
- END	end of the program

Example of translating to formal pseudocode:
```python
START

# Given a collection of integers called "numbers"

SET iterator = 1
SET savedNumber = value within numbers collection at space 1

WHILE iterator <= length of numbers
    SET currentNumber = value within numbers collection at space "iterator"
    IF currentNumber > savedNumber
        savedNumber = currentNumber
    ELSE
        skip to the next iteration

    iterator = iterator + 1

PRINT savedNumber
```

## Translating Pseudocode to Program Code

```python
def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number

        iterator += 1

    return saved_number
```


- Pseudocode is a guess at the solution; there's no verification that the logic is correct. 

- You can't do that until you translate it to program code.

For sophisticated problems, take it piece by piece.
Once we verify that the logic is correct, we can move to the next piece of the problem

## Exercises
Write out pseudocode (both casual and formal) that does the following:

1. A function that returns the sum of two numbers
```
- - Pseudocode
create a function `the_sum` to call with 2 parameters
    return the sum of the first input and second input

- - Formal Pseudocode
START
# given 2 separate inputs

SET input1, input2
RETURN result of input1 + input2

SET result
END
```
2. A function that takes a list of strings, and returns a string that is all those strings concatenated together
```
- - Pseudocode
create a function that takes list of strings
join the strings

- - Formal Pseudocode
START
SET list of strings
SET joined strings

IF list of strings
    return joinedstrings.join(list)

PRINT joined strings
END
```
3. a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance: every_other([1,4,7,2,5]) # => [1,7,5]
   ```
- - Pseudocode


SET new list
GET list of integers
WHILE lis in list 

- - Formal Pseudocode
START

END
```