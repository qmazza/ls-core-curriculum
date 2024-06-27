Notes for Lesson 3 for PY101 course.
- Practice Problems: Medium 1
  
# Contents
- [Contents](#contents)
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)
- [Question](#question)
- [Question 5](#question-5)
- [Question 6](#question-6)
- [Question 7](#question-7)
- [Question 8](#question-8)
- [Question 9](#question-9)
- [Question 10](#question-10)


# Question 1

Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:

```python
-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
...
```

My answer:

# Question 2

Alan wrote the following function, which was intended to return all of the factors of number:

```python
def factors(number):
    divisor = number
    result = []
    print(number, divisor)
    while divisor != 0:
        print(number, divisor)
        if number % divisor == 0:
            result.append(divisor)
        if number < 0:
            divisor += 1
        else:
            divisor -=1
        print(number, divisor)
    return result

number = 10

factors(number)
```python
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
```

Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

Bonus Question: What is the purpose of number % divisor == 0 in that code?

It checks if number has no remainder if divided by diviser.

My answer:
```python
def factors(number):
    divisor = number
    result = []
    print(number, divisor)
    while divisor != 0:
        print(number, divisor)
        if number % divisor == 0:
            result.append(divisor)
        if number < 0:
            divisor += 1
        else:
            divisor -=1
        print(number, divisor)
    return result

number = 10

factors(number)

Bonus Question: What is the purpose of number % divisor == 0 in that code?

It checks if number has no remainder if divided by diviser.
```
# Question 3

Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:

```python
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
```

Is there a difference between these implementations, other than the way she is adding an element to the buffer?

Answer:
Yes, there is a difference. 
The first function (add_to_rolling_buffer1) mutates the original list represented by buffer. 
The second function (add_to_rolling_buffer2) does not mutate the original list, but instead creates a new list and assigns it to buffer, whose value ultimately gets returned by the function.


# Question

What will the following two lines of code output?

```python
print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)
```

float Output is
```python
0.8999999999999999
False
```
Python uses floating point numbers for all numeric operations. Most floating point representations used on computers lack a certain amount of precision, and that can yield unexpected results like these.

One way around the problem is to use the math.isclose function:

```python
import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))
```


# Question 5

What do you think the following code will output?

```python
nan_value = float("nan")

print(nan_value == float("nan"))
```


The output is False. 

nan -- not a number -- is a special numeric value that indicates that an operation that was intended to return a number failed. Python doesn't let you use == to determine whether a value is nan.

To test whether the value is nan, you can use the math.isnan() function


# Question 6

What is the output of the following code?

```python
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)
```


34

# Question 7

One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

```python
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
```
After writing this function, he typed the following code:


```python
mess_with_demographics(munsters)
```

Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?


Answer:

Spot will find himself in the "dog house" for this one. The family's data is in shambles now.

Why? In Python, dictionaries are mutable, and when passed to a function, a reference to the dictionary is passed, not a copy. Thus, Spot's demo_dict starts off pointing to the munsters object. As a result, the changes made within the function directly affect the munsters dictionary. The key aspect here is that the nested dictionaries (the individual family members' data) are the ones being mutated. Each family member's dictionary ({"age": x, "gender": y}) is accessed and modified. Since these nested dictionaries are part of the larger munsters dictionary, the changes are reflected in the original data structure.

His program could replace that with some other object, and the family's data would be safe. However, in this case, the program doesn't reassign demo_dict; it just uses it, as-is. Thus, the object that gets changed by the function is the munsters object.

# Question 8

Function and method calls can take expressions as arguments. Suppose we define a function named rps as follows, which follows the classic rules of the rock-paper-scissors game, but with a slight twist: in the event of a tie, it just returns the choice made by both players.



```python
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
```

What does the following code output?

```python
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
```

paper


The outermost call determines the result of comparing rps(rps("rock", "paper"), rps("rock", "scissors")) against rock. 

That means that we must evaluate the two separate calls, rps("rock", "paper") and rps("rock", "scissors"), and combine them by calling rps on their results. 

Those innermost expressions return "paper" and "rock", respectively. 

Calling rps on those two values returns "paper", which, when evaluated against "rock", returns "paper".


# Question 9

Consider these two simple functions:

```python
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"
```

What will the following function invocation return?


```python
bar(foo())
```

no.

When bar(foo()) is called, the foo function is executed first, returning "yes". This return value ("yes") is then passed as the argument to the bar function. In bar, the parameter param is now "yes". The expression param == "no" and foo() or "no" is evaluated as follows:

param == "no" evaluates to False since param is "yes".
**Due to the and operator**, foo() is not executed because the first part of the and expression is already False.

Since the left side of the or (the result of the and expression) is False, Python evaluates and returns the right side of the or, which is "no".

Therefore, bar(foo()) ultimately returns "no".

This is because the value returned from the foo function will always be "yes" , and "yes" == "no" will be False.

# Question 10

In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".

Given the following code, predict the output:

```python
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
```

My answer:
True

Here, a and c reference the same object in memory, so their ids are the same. b will, in this case, have the same id as a and c due to interning. Therefore, the code will output True.

In Python, there's a predefined range of integers, specifically from -5 to 256, for which memory locations are pre-assigned. When you reference an integer within this span, Python consistently points to the same memory spot. This strategy enhances efficiency since these particular numbers are commonly utilized in many programming scenarios.

However, when you work with integers outside of this specific range, Python doesn't assure that it will consistently point to the same memory address for identical values across different variables.