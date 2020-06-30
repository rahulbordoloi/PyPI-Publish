# R-07 Python Package

This is an example project demonstrating how to publish a python module to PyPI.

All the classes will be imported under the package 'R07'.

## Installation

Run the following command on your terminal to install : 

```python
pip install R07
```

## Usage

```python
from R07 import say_hello

# Generate 'Hello R-07!'
say_hello()

# Generate 'Hello, Rahul!'
say_hello('Rahul')
```

# Developing R07

To install `R07`, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]
```