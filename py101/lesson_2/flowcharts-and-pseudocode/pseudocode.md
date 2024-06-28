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
Given a list of strings

Create an empty string called result

For each string in the list
    Add the current string to result

Return result

- - Formal Pseudocode

START

# Given a list of strings called "string_list"

SET result to an empty string

FOR index FROM 0 TO length of string_list - 1
    SET current_string to element at position "index" in string_list
    CONCATENATE current_string to result

RETURN result


END
```
3. a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance: every_other([1,4,7,2,5]) # => [1,7,5]
```
- - Pseudocode
Given a list of integers

Create an empty list called new_list

For each element in the original list, starting with the first element
    If the position of the element is even (0, 2, 4, ...)
        Add the element to new_list

Return new_list


- - Formal Pseudocode

START

# Given a list of integers called "original_list"

SET new_list to an empty list

FOR index FROM 0 TO length of original_list - 1
    IF index MOD 2 is equal to 0
        ADD element at position "index" in original_list to new_list

RETURN new_list

END


```


4. a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.
```

- - Pseudocode

Given a string and a character

Set count to 0
Set index to 0

Go through each character in the string one by one
    If the current character matches the given character
        Increase the count by 1
        If the count is 3
            Return the current position (index)
    Move to the next character (increase index by 1)

If the character is found less than 3 times in the string
    Return None

 Given a string called "input_string" and a character called "target_char"


- - Formal Pseudocode

START
SET count = 0
SET iterator = 0

WHILE iterator < length of input_string
    SET current_char = character at position "iterator" in input_string

    IF current_char is equal to target_char
        count = count + 1

        IF count is equal to 3
            PRINT iterator
            EXIT

    iterator = iterator + 1

PRINT None

END
```

5. a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance: merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
   
```
- - Pseudocode
Given two lists of numbers, list1 and list2

Create an empty list called merged_list

Set index1 to 0
Set index2 to 0

While there are elements left in either list1 or list2
    If index1 is less than the length of list1
        Add element at position index1 of list1 to merged_list
        Increase index1 by 1
    If index2 is less than the length of list2
        Add element at position index2 of list2 to merged_list
        Increase index2 by 1

Return merged_list


- - Formal Pseudocode

START

# Given two lists of numbers called "list1" and "list2"

SET merged_list to an empty list
SET index1 to 0
SET index2 to 0

WHILE index1 < length of list1 OR index2 < length of list2
    IF index1 < length of list1
        ADD element at position "index1" in list1 to merged_list
        SET index1 to index1 + 1
    IF index2 < length of list2
        ADD element at position "index2" in list2 to merged_list
        SET index2 to index2 + 1

RETURN merged_list

END
```
