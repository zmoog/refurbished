# Refurbished

Refurbished is a Python library and CLI tool to access the products information available on the [Apple Certified Refurbished](https://www.apple.com/shop/refurbished) section of the Apple Store.

## Usage

Refurbished can be used as a library or as a handly CLI tool to search for refurbished products from the terminal.

### CLI

A quick search for Macs with a min saving or 300 EUR on the Italian store:

```shell
$ rfrb it macs --min-saving=300

1979.00 1679.00 300.00 (15.159171298635673%) MacBook Pro 13,3" ricondizionato con Intel Core i5 quad‐core a 2,4GHz e display Retina - Grigio siderale
2229.00 1889.00 340.00 (15.25347689546882%) MacBook Pro 13,3" ricondizionato con Intel Core i5 quad-core a 2,0GHz e display Retina - Argento
2229.00 1889.00 340.00 (15.25347689546882%) MacBook Pro 13,3" ricondizionato con Intel Core i5 quad‐core a 2,0GHz e display Retina - Grigio siderale
2459.00 2109.00 350.00 (14.233428222854819%) MacBook Pro 13,3" ricondizionato con Intel Core i5 quad-core a 2,0GHz e display Retina - Argento
```

### Library

The same search using the `refurbished` package in your own project:

```shell
>>>
>>> from refurbished import Store
>>> store = Store('it')
>>>
>>> for mac in store.get_macs(min_saving=300):
...   print(mac.name, mac.price)
...
MacBook Pro 13,3" ricondizionato con Intel Core i5 quad‐core a 2,4GHz e display Retina - Grigio siderale 1679.00
MacBook Pro 13,3" ricondizionato con Intel Core i5 quad-core a 2,0GHz e display Retina - Argento 1889.00
MacBook Pro 13,3" ricondizionato con Intel Core i5 quad‐core a 2,0GHz e display Retina - Grigio siderale 1889.00
MacBook Pro 13,3" ricondizionato con Intel Core i5 quad-core a 2,0GHz e display Retina - Argento 2109.00
```

## Development

### Prerequisites

You need to install the following tools:

* [Git](https://git-scm.com)
* [Python](https://www.python.org) 3.7 or later, the language used to write all the application code.

### Checkout

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

## Built With

* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
* [price-parser](https://github.com/scrapinghub/price-parser)
* [requests](https://requests.readthedocs.io/en/master/)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/zmoog/76aef48ad9d9faa096c41c7b16f2fc7c) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Maurizio Branca** - *Initial work* - [zmoog](https://github.com/zmoog)
* **Yizhou "Andi" Cui** - *Improved parser* - [AndiCui](https://github.com/AndiCui)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
