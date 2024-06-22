Notes for Lesson 2 for PY101 course.
- Preventing Errors
  
# Contents
- [Contents](#contents)
- [Introduction](#introduction)
- [LBYL: Look Before You Leap](#lbyl-look-before-you-leap)
  - [Guard Clauses](#guard-clauses)
  - [When To Use Guard Clauses](#when-to-use-guard-clauses)
- [EAFP: It's Easier to Ask Forgiveness than Permission](#eafp-its-easier-to-ask-forgiveness-than-permission)
- [Detecting Edge Cases](#detecting-edge-cases)
- [Planning Your Code](#planning-your-code)


# Introduction
- Preventing errors and handlign exceptions is crucial for writing reliable code.
- Two main approaches to error prevention:
  - `"Look Before You Leap (LBYL)"`
  - `"It's Easier to Ask Forgiveness than Permission (EAFP)"`

# LBYL: Look Before You Leap
- **LBYL** approach involves checking for potential errors before executing code
  
    Example of **LBYL** code:
```python
def lower_first(word):
    # Ensure word is a string
    if type(word) != str:
        return word

    # Ensure word contains at least one character
    if len(word) == 0:
        return word

    # We now know that word is a string that contains
    # at least one character. That means the following
    # code will run without generating an error.
    return word[0].lower() + word[1:]

print(lower_first("FOO"))  # Output: "fOO"
print(lower_first(32))     # Output: 32
```

## Guard Clauses
- **LBYL** uses one or more guard clauses to ensure data meets the specific preconditions a function expects.
- `lower_first` function above has two guard clauses:
  
  1. The guard clause on lines 3 and 4 ensures that `word` is a string. If it is not, we just return the string as-is.
  2. The guard clause on lines 7 and 8 ensures that `word` has at least one character. If it does not, we just return the string as-is (it's empty).

## When To Use Guard Clauses
- Best used when a function cannot assume that it's arguments are valid.
- Invalid arguments can have incorrect types, structures, values, or properties.
- If you can trust your program always calls `lower_first` with non-empty string, you might not need the guard clause.

# EAFP: It's Easier to Ask Forgiveness than Permission
- **EAFP** approach involves trying an operation and handling any exceptions that arise.
- Assumes that the code executes successfully and handles execeptions only if something goes wrong.

    Example of EAFP code:
```python
def lower_first(word):
    try:
        return word[0].lower() + word[1:]
    except (TypeError, IndexError):
        return word  # Handle exceptions by returning `word` as-is

print(lower_first("FOO"))  # Output: "fOO"
print(lower_first(32))     # Output: "32"
```
- EAFP approach is generally preferred for its readability and concise code.
- More examples in errors.md
  
# Detecting Edge Cases
- In `lower_first`, the shortest possible string `('')` is an edge case.
- To identify edge cases, analyze inputs. In most functions, they are typically arguments.
- Each argument may have certain values that can lead to unexpected behavior.
- In `lower_first`, we observed that empty strings can cause issues when the function isn't prepared for them.
- Other types of strings can also pose challenges, such as those beginning or ending with spaces, consisting solely of spaces, or containing special characters.
- Specific  combinations of values can lead to unforeseen conditions.

# Planning Your Code

- Plan ahead by writing out common use cases of a function, then check how the function handles it.
- It's a great way to identify edge cases.
  
Example: Writing a function that inserts new element to a list in its proper alphabetically sorted position:
```python
countries = ['Australia', 'Cuba', 'Senegal']

alpha_insert(countries, 'Brazil')

print(', '.join(countries))  # Outputs "Australia, Brazil, Cuba, Senegal"
```

Some uses cases we want to ensure `alpha_insert` can handle:
```python
alpha_insert([], 'Brazil')             # Inserting into an empty list
alpha_insert(['Brazil'], 'Australia')  # At the beginning of a list
alpha_insert(['Brazil'], 'Cuba')       # At the end of a list
alpha_insert(['Brazil'], 'Brazil')     # Duplicate entry
```

- Focus on happy path. Most basic use-cases.
- Afterward, revisit your comprehensive list of use cases and ensure your implementation functions effectively in each scenario.
- If a specific case fails, address it and then reevaluate the use cases.

>Note: our list of use cases ignores the problem of invalid data types passed as arguments (for instance, passing a Number when a function expects a String). You can check argument types when this is a real possibility, but doing so in every function is unneeded and difficult to maintain.