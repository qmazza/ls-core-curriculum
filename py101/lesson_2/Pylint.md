Notes for Lesson 2 for PY101 course.
- Pylint
  
# Contents
- [Contents](#contents)
- [Introduction](#introduction)
- [Style Format](#style-format)
- [Code Linting](#code-linting)
- [Installation \& Usage](#installation--usage)
- [Quick tutorial](#quick-tutorial)
  - [Configuring Pylint](#configuring-pylint)


# Introduction
- Pylint is  astac code analyzer for Python.
- Analyzes code, offers advice about style & logical errors
- pluggable architecture with enforcement rules for standards/best practice: "checkers"

# Style Format
- Many Pylint checkers enforce guidelines provided by PEP 8 (outlines used and commonly adhered to coding conventions)
- Example: without proper indentation (4 spaces), the "checker will raise concern.

# Code Linting
- Pylint offers this to identify potentical logical errors (or code smells)
- Examines your code for common mistakes to catch early.
- Example: unused variables will cause checker to raise "unused-variable" alert
  
# Installation & Usage
- `pip install pylint` for any virtual environment I set up (Current: env_a, env_b, env_c, env_d)

# Quick tutorial
- new hello.py
```python
print("hello world")
```
- Pylint generates reports about the analyzed Python file.
- Each assigned a type, represented by letter followed by four digits.
- Letter denotes the severity level.
  - C: (Convention) for programming standard violation
  - R: (Refactor) for bad code smell
  - W: (Warning) for Python specific problems
  - E: (Error) for semantic errors that cause broken code
  - F: (Fatal) for errors which prevented further processing

`pylint hello.py` to check
```python
************* Module hello #name of file
hello.py:1:0: C0304: Final newline missing (missing-final-newline) #name:line 1 column 0(first character). Error code `c0304` represents error type. Description in parenthesis for context. note message might not be displayed on some systems
hello.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 0.00/10 #overall rating for code based on detected issues. Notation for previous run indicates previous rating if any, and the change from previous run.
```

**Module Docstring**
- A module doctring is a special type of comment or string serving as documentation for a Python module.
- Module is a file containing code.
- docstring at beginning of module provides conscise/informative description - purpose, contents, and usage without going through the code.
  
```python
"""
Module Name

A brief description of what this module does.

Module contents (functions, classes, variables, etc.) can be briefly introduced here.
"""
# Rest of your code goes here
```
## Configuring Pylint
- Pylint searches for .pylintrc in current working directory.
- file is hidden starting with a dot(.)
- If none found, it will search up hierarchy of Python modules until it finds .pylintrc.
- if none in hierarchy, it will check home directory, then system wide directory.
- if none, will rever to using default configuration settings.

**Create .pylintrc**
- .pylintrc should noramlly be in project directory.
- if Pylint ignores, make sure i am in where the .pylintrc file is.
- You must create .pylintrc file manually in the project directory; not be created automatically.

The easiest way to create a .pylintrc file is to use the command line:

```python
# PROJECT_DIRECTORY is the name of your project directory.
cd PROJECT_DIRECTORY
touch .pylintrc

#Once created, can open in text editor.

#IF HIDDEN BY DEFAULT, ASK IT TO SHOW ALLF FILES.
```

- nested .pylintrc is confusing. Best to use one in project root directory.

> After installing pylint & .pylintrc (manually), no longer have an error.
> 
```python
$ pylint hello.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 0.00/10, +10.00)
```