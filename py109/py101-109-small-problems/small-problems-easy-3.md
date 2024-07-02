Practice Problems for Lesson 3 for PY109 course.
- Practice Problems PY109: Easy 3
  
**Table of Contents**
- [Question 1 - Repeat Yourself](#question-1---repeat-yourself)
- [Question 2 - ddaaiillyy ddoouubbllee](#question-2---ddaaiillyy-ddoouubbllee)
- [Question 3 - Bannerizer](#question-3---bannerizer)
- [Question 4 - Strings Strings](#question-4---strings-strings)
- [Question 5 - Right Triangles](#question-5---right-triangles)
- [Question 6 - Madlibs](#question-6---madlibs)
- [Question 7 - Double Doubles](#question-7---double-doubles)
- [Question 8 - Grade Book](#question-8---grade-book)
- [Question 9 - Clean up the words](#question-9---clean-up-the-words)
- [Question 10 - What Century is That?](#question-10---what-century-is-that)


# Question 1 - Repeat Yourself

Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

```python
repeat('Hello', 3)

Hello
Hello
Hello
```

my answer:
```python
def repeat(string, num):
    for number in range(num):
        print(string)


repeat('Hello', 3)
```

quiz answer:
```python
def repeat(string, number):
    for _ in range(number):
        print(string)
```

When solving exercises, it can be beneficial to progress in small increments. We started out by defining repeat with two parameters. Then, to ensure everything worked properly, we added a simple print statement inside the function.

# Question 2 - ddaaiillyy ddoouubbllee

Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

```python
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
```

```python
def crunch(text):
    index = 0
    crunched_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunched_text += text[index]

        index += 1

    return crunched_text

```
cehcking both -1 (checking if equal) or comparing +1 of the string index to itself (if not equal)

Solution builds a string named crunched_text by iterating over the characters in the text argument. While iterating, we append the character at the current index to crunched_text if the character it is not equal to the next character. If it is equal, then do nothing.

Note that we also need to determine whether we are dealing with the last character in the original string.

# Question 3 - Bannerizer

Write a function that takes a short line of text and prints it within a box.

```python

print_in_box('To boldly go where no one has gone before.')
+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+

print_in_box('')

+--+
|  |
|  |
|  |
+--+
```

My Answer:
```python
def print_in_box(msg):
    mid_width = ' ' * len(msg)
    border_width = '-' * len(msg)
    print(f'''
    +-{border_width}+
    | {mid_width}|
    | {msg}|
    | {mid_width}|
    +-{border_width}+
    ''')

```

quiz answer:

```python

def print_in_box(message):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)
```
This is a fairly straight forward solution. We use Python's built-in string multiplication to generate the horizontal rules and the spaces required for the box.

The tricky part of this solution is getting the horizontal rule and empty line formatting strings correct. With the rule, we start by constructing a string that contains `len(message) + 4 characters`, most of which are hyphens `(-)`. We bound the line with a `+` character at either end. We do something similar with the empty lines above and below the message, but this time we use spaces instead of hyphens, and `|` characters instead of + characters.

We could have written both strings a little differently:


```python
horizontal_rule = f'+{"-" * (len(message) + 2)}-+'
empty_line = f'|{" " * (len(message) + 2)}|'
```

However, we opted for what we felt were more readable strings.

In Python, the * operator is used for multiplication when working with numbers. However, when used with strings, it repeats a string a given number of times.
Let's analyze this line from our first solution:


```python
horizontal_rule = f'+-{"-" * len(message)}-+'
```

`len(message)` returns the length of the message we want to print.
`"-" * len(message)` returns a string of N hyphens, where N is the the length of the message we want to print.
We then prepend `+- `to the beginning of the hyphens.
Finally, we append `-+` to the end of the hyphens.

# Question 4 - Strings Strings

Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

```python
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
```

```python
def stringy(number):
    new_string = ''
    for index in range(number):
        if index % 2 == 0:
            new_string += '1'
        else:
            new_string += '0'
    print(new_string)
    return new_string
```

quiz answer:
```python
def stringy(size):
    result = ""
    for idx in range(size):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit

    return result
```
The solution makes use of a for loop in combination with range to loop the specified number of times. At every iteration of the loop, the solution checks whether the index position is even. If so, the solution appends a '1' to the initially empty result string. Otherwise, it appends '0'.

This ternary expression
```python
number = '1' if idx % 2 == 0 else '0'
```
is equivalent to using an if/else statement:

```python
if idx % 2 == 0:
    number = '1'
else:
    number = '0'
```

# Question 5 - Right Triangles

Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

```python
triangle(5)
triangle(9)
```

my answer:
```python
def triangle(n):
    i = n
    for num in range(n+1):
        print((' ' * i) + ('*' * num))
        i -= 1

triangle(5)
triangle(9)
```

quiz answer:
```python
def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')
```

For this problem, we use a loop with the range function to iterate from 1 to height, inclusive. This helps us determine the number of stars to print in each line.

In each iteration of the loop:

We determine the number of spaces to be printed as height - num. As num increases, the number of spaces decreases.
We determine the number of stars to be printed as num. As num increases, the number of stars increases.
As mentioned in one of the previous problems, Python's string multiplication (*) is used to create a string with a repeated sequence of characters. This lets us generate the appropriate number of spaces and stars for each line of the triangle.


# Question 6 - Madlibs

Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.

```python
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
```

my answer:
```python
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')

print(f'''
Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!
The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.
The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.
''')
```
In this exercise, we use Python's built-in input function to get various inputs from the user. Once the user has entered all of the required words, we construct the Madlibs sentences using Python's f-strings. F-strings provide a concise way to embed expressions inside string literals. They let you evaluate expressions inside the string using {}.


# Question 7 - Double Doubles

A double number is an even-length number whose left-side digits are exactly the same as its right-side digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.

```python
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
```

my answer:
```python
def twice(num):
    str_num = str(num)
    middle = len(str_num) // 2
    left_half = str_num[:middle]
    right_half = str_num[middle:]
    if len(str_num) % 2 != 0:
        return num * 2
    elif left_half == right_half:
        return num
    else:
        return num * 2
```

quiz answer:
```python
def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]

    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2
```
The logic for checking whether a number is a "double number" is maintained in the is_double_number function. Python's string slicing capabilities make it straightforward to compare the left half of the number to the right half.

We convert the number into a string using the str function.
Next, we find the midpoint (or center) of the string. We use integer division (//) to ensure we get an integer result.
We then split the string into left_number and right_number using Python's slicing syntax.
Finally, we check whether the left and right halves are equal and return the result.
The main function twice simply checks if the number is a "double number" and, depending on the result, either returns the number itself or its doubled value.


# Question 8 - Grade Book

```python

```

```python

```


# Question 9 - Clean up the words

```python

```

```python

```


# Question 10 - What Century is That?

```python

```

```python

```