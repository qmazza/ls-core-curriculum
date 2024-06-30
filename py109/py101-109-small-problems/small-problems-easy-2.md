Practice Problems for Lesson 3 for PY109 course.
- Practice Problems PY109: Easy 2
  
**Table of Contents**
- [Question 1 - Welcome Stranger](#question-1---welcome-stranger)
- [Question 2 - Greeting a user](#question-2---greeting-a-user)
- [Question 3 - Multiplying Two Numbers](#question-3---multiplying-two-numbers)
- [Question 4 - Squaring an Argument](#question-4---squaring-an-argument)
- [Question 5 - Floating Point Arithmetic](#question-5---floating-point-arithmetic)
- [Question 6 - The End Is Near But Not Here](#question-6---the-end-is-near-but-not-here)
- [Question 7 - Exclusive Or](#question-7---exclusive-or)
- [Question 8 - Odd Lists](#question-8---odd-lists)
- [Question 9 - How Old is Teddy?](#question-9---how-old-is-teddy)
- [Question 10 - When Will I Retire?](#question-10---when-will-i-retire)
- [Question 11 - Get Middle Character](#question-11---get-middle-character)
- [Question 12 - Always Return Negative](#question-12---always-return-negative)


# Question 1 - Welcome Stranger

Create a function that takes 2 arguments, a list and a dictionary. 

The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. 

The dictionary will contain two keys, "title" and "occupation", and the appropriate values. 

Your function should return a greeting that uses the person's full name, and mentions the person's title.

```python
greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
```

My Answer:
```python
def greetings(name,job):
    joined_name = ' '.join(name)
    title = job.get("title")
    occupation = job.get("occupation")
    return (f'Hello, {joined_name}! Nice to have a {title} {occupation} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
```


Quiz Answer:
```python
def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
           f"{status['title']} {status['occupation']}"
           "around.")
```

We use the join method to change the list into a full name with appropriate spacing. For the dictionary, we access the items by their keys.

Finally, we use f-string formatting to combine everything into a single string, resulting in a concise and readable way to format the final output.

Note that the **parentheses on the return are necessary here**. Without them, Python won't deal with the continuation lines correctly.

# Question 2 - Greeting a user

Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

```python
example 1:
What is your name? Sue
Hello Sue.

example 2:
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
```

My Answer:
```python

```

# Question 3 - Multiplying Two Numbers

```python

```

My Answer:
```python

```

# Question 4 - Squaring an Argument

```python

```

My Answer:
```python

```

# Question 5 - Floating Point Arithmetic

```python

```

My Answer:
```python

```

# Question 6 - The End Is Near But Not Here

```python

```

My Answer:
```python

```

# Question 7 - Exclusive Or

```python

```

My Answer:
```python

```

# Question 8 - Odd Lists

```python

```

My Answer:
```python

```

# Question 9 - How Old is Teddy?

```python

```

My Answer:
```python

```

# Question 10 - When Will I Retire?

```python

```

My Answer:
```python

```

# Question 11 - Get Middle Character

```python

```

My Answer:
```python

```

# Question 12 - Always Return Negative

```python

```

My Answer:
```python

```