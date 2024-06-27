Notes for Lesson 3 for PY101 course.
- Practice Problems: Easy 3
  
# Contents
- [Contents](#contents)
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)
- [Question 4](#question-4)
- [Question 5](#question-5)


# Question 1

Write two different ways to remove all of the elements from the following list:

```python
numbers = [1, 2, 3, 4]
```

```python
numbers = [1, 2, 3, 4]
del numbers[0:] #remove elements from 0 til the end
print(numbers)



numbers = [1, 2, 3, 4]
numbers.clear() # clears list
print(numbers)
```

quiz answer:

```python

while numbers:
   numbers.pop()
#Note that this solution will set numbers to an empty list, but it doesn't clear the original list. That's fine if you know there are no other references to the list.
numbers = []
```

# Question 2

What will the following code output?

```python
print([1, 2, 3] + [4, 5])
```
answer without running

```python
[1, 2, 3, 4, 5]

```
Using the + operator to concatenate two lists. This operation merges the second list into the first one, producing a new combined list.

# Question 3

What will the following code output?

```python
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
```
answer without running

My Answer:
```python
"hello there"
```
In python, strings are immutatble. no way to change value of str1 unless reassignment.

# Question 4

What will the following code output?

```python
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
```
answer without running


My Answer:
```python
[{"first": "42"}, {"second": "value2"}, 3, 4, 5]
```

>For simplicity, we're showing the integer values stored directly in the list. Since everything in Python is an object, those integers are actually stored elsewhere and accessed through pointers, just like the dictionaries.

# Question 5

The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?

```python
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
```
Try to come up with two different solutions.

My Answer:
```python
def is_color_valid(color):
    return color == "blue" or color == "green"

# Can also use the in operator to check if the color exists in a list:
def is_color_valid(color):
    return color in ["blue", "green"]
```