Notes for Lesson 2 for PY101 course.
- Python Package Index
# Contents <!-- omit in toc -->
- [Now](#now)


# Introductioon
Python Package index (PyPI) is a repository of amny software tools and libraries you use with or in Python.

**Pip Installs Packages (PyPI)**
- PyPI provides a package manager called pip.
- Pip provides interface to install and manage packages

**to install/uninstall packages**
- `pip3` for some systems or `pip` 
```python
pip3 install example2
pip3 uninstall example2
```
pip installed on:
source ~/.venv/env_b/bin/activate
source ~/.venv/env_c/bin/activate

# Installing Jupyter

JupyterLab and Jupyter Notebook are alternative Python REPLs. 
- The most significant benefit provided by these programs is that you can write and try out code, copy and paste code with blank lines and indentation, and much more.

**It's better to install Jupyter in a virtual environment so you can use it with different versions of Python:**

- To install JupyterLab in virtual environments, first activate one:
```python
# VENVNAME is your virtual environment's name
source ~/.venv/VENVNAME/bin/activate
```
- pip (or pip3) to install jupyterlab:
 ```python
 pip install jupyterlab
 ```
- can then run it:
```python
jupyter lab
```

- JupyterLab opens in default browser. 
- use interface to create a new notebook and write some code. 
- To execute -> {Shift}{Enter}. You can go back, edit it, and run again.
