# Lesson 2 notes	

Here's a short list of guidelines that we recommend. 
They will help you write readable code, and smooth the process of asking for code reviews at Launch School.

## Style Guide
	Set your text editor to use space characters -- not tabs -- for indentation. The editor should also insert spaces if you press the Tab key on your keyboard.
Set your text editor to use 4 spaces for indentation and when converting tab characters to spaces.

Try to limit lines to 79 characters. This limit isn't a universal preference, but it helps readability. Not all developers have massive screens or good eyesight.

Python uses the character # to mark the beginning of a comment. The comment runs through the end of the line. Programmers use comments to leave notes for other programmers or themselves at a later point in time; however, don't overdo your comments. Let your code do the talking instead.

Use snake_case formatting for variable and function names. Such names begin with a lowercase letter. 
If the name contains multiple words, they should be separated with the underscore (_):


### initializing a variable
```python
	my_variable = 'Hello, World'
```
	
### defining a function
```python
	def four_score_and_seven_years_ago():
	    # do something
	


	Class names use PascalCase in Python.
```

### defining a class
```python
	class DomesticCat:
	    # do something
	
	cat = DomesticCat('Fluffy')
```

### Constants
Use uppercase names with underscores to represent constants: values that don't change.

```python
INTEREST_RATE = 0.0525
	FOUR = 'four'
```

	


This naming style is called SCREAMING_SNAKE_CASE.
All names -- variables and constants as well as functions -- should use alphabetic (a-z, A-Z without umlauts, accents, and so on) and numeric characters only. The first character must be alphabetic. Variable, constant, and function names may include underscores, subject to the underscore limitations.
Use spaces between operators and operands to make your code less cluttered and easier to read:


### bad
	sum=x+5
	
### good
	sum = x + 5
	


For more comprehensive guidelines on Python styling, you can refer to PEP 8, the official Python style guide. Adhering to PEP 8 will help your code align with the broader Python community's conventions and make it easier for others to understand and collaborate on your projects.


## git init
git init
Can echo ‘# README #’ > README.md
echo ‘# LICENSE #’ > LICENSE.md
The > character on lines 3 and 4 above is the redirection operator. This operator takes the output of the command and places it in the file whose name appears to the right. These two commands, thus, create 2 files, README.md and LICENSE.md, each of which starts with a simple comment (# README #, # LICENSE #).


https://launchschool.com/books/git/read/creating_repositories#createanexampleproject



## Truthinesss
Ability to express true or false is vital.
Helps build conditional logic and understand the state of an object or expression.

```python
print(True)  # True
print(False)  # False

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string

print(make_longer("abc", True))  # 'abcabc'
print(make_longer("xyz", False))  # 'xyz'

def is_digit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False

print(is_digit("5"))  # True
print(is_digit("a"))  # False

value = True  # or False

if value is True:
    print("It's true!")
elif value is False:
    print("It's false!")
else:
    print("It's not true or false!")
```

## Expressions & conditionals
In real code you wouldn’t use a conditional expression like value == true. You would evaluate an expression act should evaluate as either True or False


```python
If num < 10:
    print(“small number”)
else:
    print(“large number”)
"(Evaluated in REPL)>>> num = 5
>>> num < 10
True"
```




a function doesn't usually return True or False explicitly. Instead, it returns the result of a conditional expression

```python
"def is_small(number):
    return number < 10

num = 15

if is_small(num):
    print("small number")
else:
    print("large number")"
```
code prints large number since is_small(num) evaluates as False when num is greater than or equal to 10.
———————————————————————

## Logical operators
 evaluate an expression that involves two subexpressions, then return a value that evaluates as True or False

## The `and` operator 
evaluates as true only when both sub-expressions evaluate as true

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

num = 5
print(num < 10 and num > 3)  # True
print(num < 10 and num > 6)  # False
print(num > 10 and num < 6)  # False
print(num > 10 and num < 3)  # False
```

Precedence rule handles comparison operators like < and > with higher precedence than logical operators like and. (So no parenthesis for num < 10). But its good to make it clear if needed. 

You can chain sub expressions with and. Evaluated from left to right. If any sub-expression is false, the entire and chain evaluates as False. The whole expression evaluates as true only when all sub expressions true.

```python
num = 5

print((num < 10) and (num > 0) and ((num % 2) == 1))  # True
print((num < 10) and (num > 0) and ((num % 2) == 1) and False)  # False
```

## The `or` operator 
evaluates as true when either of the two sub-expressions evaluate as true; evaluates as False when both expressions evaluate as False

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

num = 5
print(num < 10 or num > 3)  # True
print(num < 10 or num > 6)  # True
print(num > 10 or num < 6)  # True
print(num > 10 or num < 3)  # False
```



## `not` operator
Inverts the truth value of a condition it’s applied to.
It’s a logical negation to check the opposite.

```python
print(not True)  # False
print(not False) # True

value = 3
is_even = (value % 2 == 0)

print(is_even)       # False
print(not is_even)   # True
```

## Short-Circuit operators - `and`, `or` 
exhibit a behavior called short-circuiting (Python stops evaluating sub-expressions once it can determine the final value)

`And` Short Circuits when it realizes the entire expression can’t be True (encounters False)

```python
print(False and len(None))  # False
```

`Or` Short Circuits when it realizes that the expression can’t be False. (One is True)

`and`: short-circuits when it encounters the first sub-expression (from left-to-right) that evaluates as False. By itself, len(none) would raise a TypeError. However, left side of the and guarantees entire expression can’t be true. So right never executes.
Conversely - Exception ->
```python
print(True and len(None))
# TypeError: object of type 'NoneType' has no len()
```

`or`: short-circuits when it encounters the first True sub-expression, again based on left-to-right evaluation:

This code doesn't raise a TypeError since or didn't evaluate the second sub-expression; it short-circuited when True evaluated as True.

Dangerous but can be handy. 
For instance, suppose you have a `name` variable that usually contains a string, but may sometimes be `None`.  Before you can use the string’s `isupper()` method, you must confirm that it isn’t `None`

```python
print(True or len(None))  # True
```

## Truthiness
"Truthiness differs from boolean values in that Python evaluates almost all values as true. There are some exceptions, however:

```python
False
None
0
0.0
0j
"" (an empty string)
[] (an empty list)
{} (an empty dictionary)
() (an empty tuple)
set() (an empty set)
frozenset() (an empty frozenset)
range(0) (an empty range)
```

All of these values evaluate as false."
The terms True and False refer to the Boolean values True and False; the other phrases refer to truthiness, that is, a truthy or falsy value. Can use “evaluated as True/False”

Truthiness can use any condition or logical expression
Output is “valid number”. Any non-zero number is truth.
```python
num = 5
if num:
    print("valid number")
else:
    print("error!")
```

get_name_from_user solicits and returns the user's name and returns an empty string "" if the user doesn't enter a name.

- proper usage of truthy falsy if statement checking
```python
name = get_name_from_user()
if name == "":
    print("you must enter your name!")
else:
    print(f"Hi {name}")
    ```
