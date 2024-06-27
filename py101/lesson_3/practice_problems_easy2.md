Notes for Lesson 3 for PY101 course.
- Practice Problems: Easy 2
  
# Contents
- [Contents](#contents)
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)
- [Question 4](#question-4)
- [Question 5](#question-5)
- [Question 6](#question-6)
- [Question 7](#question-7)
- [Question 8](#question-8)
- [Question 9](#question-9)


# Question 1

Write two distinct ways of reversing the list without mutating the original list.

```python
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
```

```python
numbers = [1, 2, 3, 4, 5]
reverse_num = list(reversed(numbers))
print(reverse_num)

# reversed creates a lazer iterator.
You will have to convert that iterator to a list.

# OR

# Use slicing to reverse

numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1] # using step
print(reversed_numbers)

```

reverse with reversed, then convert to list
slice to reverse

# Question 2

Given a number and a list, determine whether the number is included in the list.

```python
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
```

My answer:
```python
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
number1 = 8
number2 = 95
number1 in numbers
number2 in numbers

```

# Question 3

Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.


My Answer
```python

42 in range(10,100)
100 in range(10,100)
101 in range(10,100)
```

# Question 4

Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number at index 2, so that the list becomes [1, 2, 4, 5].

My answer:
```python
numbers = [1, 2, 3, 4, 5]

del numbers[2]
print(numbers)
```

# Question 5

How would you verify whether the data structures assigned to the variables numbers and table are of type list?

my answer:
```python
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

type(numbers) is list
type(table) is list
```

Preferred answer is using isinstance:
```python
isinstance(numbers, list)  # True
isinstance(table, list)    # False
```


# Question 6

Back in the stone age (before CSS), we used spaces to align things on the screen. If we have a 40-character wide table of Flintstone family members, how can we center the following title above the table with spaces?

```python
title = "Flintstone Family Members"
centered_title = title.center(40)
print(centered_title)
```
Python's str.center function lets you center a string in a given width (40 is used). can be padded.


# Question 7

Write a one-liner to count the number of lower-case t characters in each of the following strings:

my answer:
```python
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(statement1.count('t') + statement2.count('t'))
```

quiz answer:
```python
statement1.count('t')
statement2.count('t')
```

# Question 8

Determine whether the following dictionary of people and their age contains an entry for 'Spot':

```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
```

My answer:
```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
'spot' in ages
```

# Question 9

We have most of the Munster family in our ages dictionary:

```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
```
Add entries for Marilyn and Spot to the dictionary:
```python
additional_ages = {'Marilyn': 22, 'Spot': 237}
```

My answer:
```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update({'Marilyn': 22, 'Spot': 237})

print(ages)


```
