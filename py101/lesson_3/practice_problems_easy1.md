Notes for Lesson 3 for PY101 course.
- Practice Problems: Easy 1
  
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
- [Question 10](#question-10)


# Question 1

Will the code below raise an error?

```python
numbers = [1, 2, 3]
numbers[6] = 5
```
Yes, we receieve `IndexErrorlist assignment index out of range.`

>It will raise an error. This error is a result of 6 being an out of range index: the only indexes currently defined for the numbers list are 0, 1, and 2. Any attempt to access or modify an element at an index that does not exist will result in an IndexError exception.

# Question 2

How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

my answer:
```python
str1 = "Come over here!"
str2 = "What's up, Doc?"

def str_check(string):
    if '!' in string:
        return True
    return 'False'


print(str_check(str1))
print(str_check(str2))
```

quiz answer:
>print(str1.endswith("!"))  # True

>print(str2.endswith("!"))  # False


# Question 3

Starting with the string:

```python
famous_words = "seven years ago..."
appended_famous = ''.join('Four score and ', famous_words)
#appended_operate = "Four score and " + "seven years ago..."
```

Show two different ways to create a new string with "Four score and " prepended to the front of the string.



my answer:
strings not iterable. cannot use .join


```python
famous_words = "seven years ago..."
appended_famous = (f'Four score and {famous_words}')
appended_operate = "Four score and " + "seven years ago..."
```


# Question 4

Using the following string, print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.

```python
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
```

my answer:
```python
munsters_description = "the Munsters are CREEPY and Spooky."
munsters = munsters_description.lower().capitalize()
print(munsters)
```

quiz answer:
```python
print(munsters_description.capitalize())
```


# Question 5

Starting with the string:

```python
munsters_description = "The Munsters are creepy and spooky."
```

print the string with the case of all letters swapped:

```python
"tHE mUNSTERS ARE CREEPY AND SPOOKY."
```
That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase"


My answer:
```python
munsters_description = "The Munsters are creepy and spooky."
munsters = munsters_description.swapcase()
print(munsters)
```

# Question 6

Determine whether the name Dino appears in the strings below -- check each string separately:

```python
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
```

My answer:
```python
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print("dino" in str1)
print("dino" in str2)
```

quiz answer:
```python
'Dino' in str1  # False
'Dino' in str2  # True
```


# Question 7

How can we add the family pet, "Dino", to the following list?

```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
```

My Answer:
```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)
```

# Question 8

In the previous problem, our first answer added 'Dino' to the list like this:

```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
```
How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? Replace the call to append with another method invocation.

```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino","Hoppy"])
print(flintstones)
```
.extend to add or insert multiple items to a list.

# Question 9

Print a new version of the sentence given by advice that ends just before the word house. Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

```python
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
```

My answer:
```python
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.split("house")[0])
```

advice.split("house") splits advice where "house" appears and creates a list of substrings.

[0] retrieves the first substring from that list.

advice.split("house")[0] prints the 1st element(substring) of advice that appears before the first occurrence of "house". If "house" not found, entire string advice is returned.


# Question 10

Print the following string with the word important replaced by urgent:

```python
advice = "Few things in life are as important as house training your pet dinosaur."
```


My answer"
```python

advice = advice = "Few things in life are as important as house training your pet dinosaur."
advice.replace('important', 'urgent')
```