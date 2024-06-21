Notes for Lesson 2 for PY101 course.
- Python Virtual Environments
# Contents <!-- omit in toc -->
- [Overview of Virtual Environments](#overview-of-virtual-environments)
  - [How I entered my mac Development Environment](#how-i-entered-my-mac-development-environment)
  - [Using an Environment](#using-an-environment)





# Overview of Virtual Environments

Different programs may need different python versions.

- Program a.py requires version 3.8 of Python:
```python
import sys

print(f"This is program {__file__}")
print(f"The Python version is {sys.version}")
```

- Program b.py requires version 3.10 of Python and version 2.3.1 of Flask:
```python
import sys
import flask

print(f"This is program {__file__}")
print(f"The Python version is {sys.version}")
print(f"The Flask version is {flask.__version__}")
```
- Program c.py requires version 3.10 of Python and version 2.1.2 of Flask:
```python
import sys
import flask

print(f"This is program {__file__}")
print(f"The Python version is {sys.version}")
print(f"The Flask version is {flask.__version__}")
```

**^To avoid doing the above `PATH` edits ^ use virtual environment:**
- Virtual environments let you set up multiple environments, each providing a specific version of Python and any required packages. 

- When you run your program, you activate the virtual environment the program requires. That takes care of the necessary `PATH` changes.


## How I entered my mac Development Environment

```python
python3.8 -m venv ~/.venv/env_a
source ~/.venv/env_a/bin/activate
python --version            # Should show version 3.8.something

python3.10 -m venv ~/.venv/env_b
source ~/.venv/env_b/bin/activate
python --version            # Should show version 3.10.something
pip install flask==2.3.1

python3.10 -m venv ~/.venv/env_c
source ~/.venv/env_c/bin/activate
python --version            # Should show version 3.10.something
pip install werkzeug==2.2.2 flask==2.1.2

deactivate #to exit
```

## Using an Environment

Our environments are set up and applications are ready to run.

```python
source ~/.venv/env_a/bin/activate

source ~/.venv/env_b/bin/activate

source ~/.venv/env_c/bin/activate 

Deactivate
```