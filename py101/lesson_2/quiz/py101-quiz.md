Notes for Lesson 2 for PY101 course.
- Programming Foundations with Python: Basics
  
# Contents
- [Contents](#contents)
- [MyClass is an example of](#myclass-is-an-example-of)
- [Identify the valid Python comment style.](#identify-the-valid-python-comment-style)
- [Examine the following code](#examine-the-following-code)
- [What is Pseudocode?](#what-is-pseudocode)
- [Examine the code below:](#examine-the-code-below)
- [Given the following pseudocode, which code implementation most closely matches it?](#given-the-following-pseudocode-which-code-implementation-most-closely-matches-it)
- [Which of the following values are considered falsy in Python? Choose all that apply:](#which-of-the-following-values-are-considered-falsy-in-python-choose-all-that-apply)
- [What specifically do we mean when we refer to a variable's scope?](#what-specifically-do-we-mean-when-we-refer-to-a-variables-scope)
- [Select all of the statements which are true regarding local variable scope in Python.](#select-all-of-the-statements-which-are-true-regarding-local-variable-scope-in-python)
- [Which statement most accurately describes why the last line of the code below outputs "hi"?](#which-statement-most-accurately-describes-why-the-last-line-of-the-code-below-outputs-hi)
- [Looking again at the code from the previous question:](#looking-again-at-the-code-from-the-previous-question)
- [Given the following code, which names are in scope when line 12 is reached?](#given-the-following-code-which-names-are-in-scope-when-line-12-is-reached)
- [In Python, what do we mean when we talk about variables as references? Select all answers that apply.](#in-python-what-do-we-mean-when-we-talk-about-variables-as-references-select-all-answers-that-apply)
- [The following Python code doesn't raise an exception. Why is that?](#the-following-python-code-doesnt-raise-an-exception-why-is-that)


# MyClass is an example of
PascalCase

# Identify the valid Python comment style.
```python
# example here
```

# Examine the following code
There is an error in the code which means that it will raise an exception before execution. Identify the line responsible for the error.

```python
import random
a = 2
b = random.randint(0,1)
a *= b

if a = 2:
    print('Two')
else:
    print('Not Two')
```

if a = 2: will raise an exception.
(every syntax error is an exception.)

# What is Pseudocode?

Pseudocode is a human-readable, high-level description of a program or algorithm which helps us formulate a solution at the logical problem domain level.

# Examine the code below:

```python
num = 8

if #omitted code:
    print('Goodbye')
```
Which of the following code snippets can replace #omitted code so the code outputs Goodbye? Select all that apply.
num > 5 and num < 10
num < 4 or num == 8 and num > 6
num < 7 or num > 7
num >= 8 and num < 6 or num > 4

# Given the following pseudocode, which code implementation most closely matches it?

```
Given a sentence made up of several words, write a function to do the following.

Iterate through the words one by one.
save the first word as the starting value.
starting with the next word iterate through all the remaining words in the sentence
for each iteration, compare the saved value with the current word.
if the word is longer or the same length as the saved value:
reassign the saved value as the current word
move on to the next word
After iterating through the sentence, return the saved value.
```
```python
def longest_word(sentence):
    words = sentence.split()
    saved_word = words.pop(0)

    for word in words:
        if len(word) >= len(saved_word):
            saved_word = word

    return saved_word
```
 These solutions are all fairly similar and some only have subtle differences, but solution 'C' most closely matches what is specified in the pseudocode.
 ( using words[0] iterates the sentence at first word rather than the next one. shouldn't affect outcome but not strictly what was specified)


# Which of the following values are considered falsy in Python? Choose all that apply:

[]

"" (an empty string)

False

{}

0

( [None] is truthy. list containing single element None)

# What specifically do we mean when we refer to a variable's scope?

Where the variable is available for use.

# Select all of the statements which are true regarding local variable scope in Python.

Variables initialized inside a function can only be accessed inside that function.

Variables from the outer scope of a function can't be reassigned inside that function unless explicitly declared as global or nonlocal.

# Which statement most accurately describes why the last line of the code below outputs "hi"?

```python
def extend_greeting(greeting):
    return greeting + " there"

greeting = "hi"
extend_greeting(greeting)

print(greeting)
```

The extend_greeting function does not mutate the value of the greeting argument. Thus, the global greeting variable is not modified in any way.

# Looking again at the code from the previous question:

Select all the ways in which we could change this code in order for the last line to output "hi there".

# Given the following code, which names are in scope when line 12 is reached?

```python
foo = 1

def bar():
    xyz = 3
    qux = 5
    return qux

def yam():
    pass

bar()
print("Done")
```

foo, bar and yam

Names in Python are references to objects. 

foo - in global scope
bar() - bar in the current scope. can find function object it refers to and then calls the function.
yam - referring to the function object `def yam()` (in global scope)

# In Python, what do we mean when we talk about variables as references? Select all answers that apply.

Variables in Python are references to objects in memory.

# The following Python code doesn't raise an exception. Why is that?

```python
name = "Lisa"

def name_func():
    return name

print(name_func())
```

Because Python functions can access variables defined in the global or enclosing scope.
