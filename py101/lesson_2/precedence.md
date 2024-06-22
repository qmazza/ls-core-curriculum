Notes for Lesson 2 for PY101 course.
- Precedence
  
# Contents
- [Contents](#contents)
- [Introduction](#introduction)
- [Evaluation Order](#evaluation-order)
- [Use Parenthesis](#use-parenthesis)


# Introduction

- **Operator precedence** determines the meaning of an expression.
- It's a set of rules to dicate how Python determs what operands each operator takes
- **Operands** are simply values -- the results of evaluating exprssions -- that are used by the operator.
   - For most Operators, there are two Operands.
   - There is also a "Unary" operator that takes one operand.
```python
2 + 5             # Two operands (2 and 5)
not True          # Unary: One operand (True)
```

Each operand can be the result of evaluating some other operator and its operands. Consider this expression:

```python
3 + 5 * 7  # Result: 38
```

- In this example, 2 operators  (`+` and `*`)
- Precedence determines the *meaning* of an expression.
- Operations involving operators with high precedence get evaluated before operations involving low precedence.
- using parenthess to explicitly define the intended order is recommended.
- An operator that has higher precedence than another is said to bind more tightly to its operands. 
    - In the expression 3 + 5 * 7, the * operator binds more tightly to its operands, 5 and 7, than does the + operator.
  
# Evaluation Order
- Precedence is only part of the story. Other parts are  `left-to-right evaluation`, `right-to-left evaluation` and `short-circuiting`.

```python
def value(n):
    print(n)
    return n

print(value(3) + value(5) * value(7))

3
5
7
38
```
-  The issue here is that operators like + and * need values that they can work with. 
   -  Function invocations like value(5) and value(7) are not values.
-  In an arithmetic expression, Python first goes through an expression left-to-right and evaluates everything it can without calling any operators
- Here it evaluates value(3), value(5), and value(7) first, in that order.
- Python re-evaluates the result with the precedence rules only after it has those values

Right-to-left evaluation occurs when you do multiple assignments or multiple ** operators:

```python
a = b = c = 3
5 ** 3 ** 2  # 1953125 (same as 5 ** (3 ** 2) = 5 ** 9 = 5 * 5 * 5 * 5 * 5 * 5 * 5 * 5 * 5)
```
Neither of these are good practice in Python though.

Short-circuit operators and and or can lead to unexpected behavior regarding precedence. Consider these expressions:

```python
5 and 1 / 0           # ZeroDivisionError
None or 1 / 0         # ZeroDivisionError
```
if we modify things so that 1 / 0 isn't needed:
```python
None and 1 / 0           # None
5 or 1 / 0               # 5
```
- In both cases, 1 / 0 **never gets executed**, even though operator precedence would suggest that it should be evaluated first.
- However, these two expressions don't evaluate 1 / 0 due to `short-circuiting`.
- This is simply the way Python works 
  - it treats `and`, and `or` differently from other operators and *doesn't evaluate subexpressions unless it needs them*.

# Use Parenthesis
- Don't rely on the precedence rules when you're mixing operators
  - Use parentheses whenever you mix operators in an expression
-  You'll eventually decide to work from memory. Sooner or later you'll misremember the rule, and introduce bugs.
   - Someone reading your code may not be as familiar with the precedence rules as you.
   - They will either have to look up the rules, or assume that you knew what you were doing when you wrote the code. 
   - If they assume that you knew what you were doing, they will miss the bug.  