Notes for Lesson 2 for PY101 course.
- Debugging techniques. Alongside debugging_pracice.py and debug.py
  
# Contents
- [Contents](#contents)
- [Line by Line Debugging](#line-by-line-debugging)
- [Rubber Duck Debugging](#rubber-duck-debugging)
- [Debugging by Walking Away](#debugging-by-walking-away)
- [Debugging with print](#debugging-with-print)
- [Inspecting with a Debugger](#inspecting-with-a-debugger)
- [Advanced Debugging](#advanced-debugging)
- [Summary](#summary)


# Line by Line Debugging
- Best tool is patience.
- Most bugs from overlooking a detail.
- Be careful, patient and read code line-by-line, word-by-word, character-by-character.

# Rubber Duck Debugging
- Uses an object as a sounding broard when faced with a hard problem.
- Explaining to a duck forces yourself to articulate the problem detail by detail.
- Forces your midn to walk through the code which may reveal a small detail revealing a deeper problem.

# Debugging by Walking Away
- This is only effective if you first spend time loading the problem in your brain.
- Once loaded, you may walk away while it's being processed in the backgroudn or when when you're sleeping.


# Debugging with print
- overlooked technique is to use `print` at points to inspect state of data.

# Inspecting with a Debugger
- `pdb` is a built in debugger - `pdb.set_trace()`
- Let's you pause the program during execution and inspect values at runtime.
- Multuple breakpoints can be used.
- access value of any variable in scope using `p` command followed by variable name. 
- Example - p counter
```python
1
> /Users/xyzzy/ls_test/test.py(10)<module>()
-> counter += 1
(Pdb) p counter # Our command
1               # The output, the current value of `counter'
```

-  `c` command using the to pause at the breakpoint for each iteration in loop.
-  `n` command to move on to next line of code
-  `q` and Enter to exit debugger
# Advanced Debugging
**`pdb` has a lot of other helpful features**
- Example: Has mechanisms to print all arguments with their values in the current function etc. 

# Summary
- Develop a patient, systematic temperament; carefully read error messages; use all the resources.
- Approach debugging in sequential steps.
- Use the techniques covered above -- especially the debugger.
