# Development

## Prerequisites

You need to install the following tools:

* [Git](https://git-scm.com)
* [Python](https://www.python.org) 3.10 or later, the language used to write all the application code.

## Checkout

A step by step series of steps that tell you how to get a development env running.

First, you need to get the project source code:

```shell
git clone https://github.com/zmoog/refurbished.git

cd refurbished
```

Create/activate the virtual environment for this project:

```shell
python -m venv venv

source ./venv/bin/activate
```

Install the project dependencies:

```shell
# installs the Python deps
$ pip install -r requirements-*
```

Set some environment variables and aliases:

```shell
export PYTHONPATH=`pwd`:$PYTHONPATH 
```

Let's run the lambda function locally to see if it's all working!

```python
>>> from refurbished import Store
>>> store = Store('it')
>>> tvs = store.get_appletvs()
>>> 
>>> print(tvs)

```

## Running the tests

The library uses pytest to run all its tests.

### Unit and integration tests

You can run the test suite with a single command:

```shell
$ pytest tests
======================================================================================================= test session starts ========================================================================================================
platform darwin -- Python 3.9.10, pytest-7.0.1, pluggy-1.0.0
rootdir: /Users/mbranca/code/projects/zmoog/refurbished
collected 11 items

tests/test_parser.py .....                                                                                                                                                                                                   [ 45%]
tests/test_refurbished.py ......                                                                                                                                                                                             [100%]

======================================================================================================== 11 passed in 0.76s ========================================================================================================
(
```
