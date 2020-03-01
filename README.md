# Refurbished

Python library to access the products information available on the Apple Certified Refurbished section of the Apple Store.

# Usage

```python
>>> from refurbished import Store
>>> store = Store('it')
>>> macs = store.get_macs()
>>> [mac for mac in macs if mac.savings_price > 400]
[Product(name='MacBook\xa0Pro 15,4" ricondizionato con Intel Core i9 8-core a 2,3GHz e display Retina - Grigio siderale', price=Decimal('2619.00'), previous_price=Decimal('3079.00'), savings_price=Decimal('460.00'))]
```

### Prerequisites

You need to install the following tools:

* [Git](https://git-scm.com)
* [Python](https://www.python.org) 3.7, the language used to write all the application code. You should evaluate [pyenv](https://github.com/pyenv/pyenv#installation) as tool to manage Python versions.
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/) — tested with version 2018.11.26, it's used to streamline development in Python projects.


### Installing

A step by step series of steps that tell you how to get a development env running.

First, you need to get the project source code:

```bash
$ git clone https://github.com/zmoog/refurbished.git

$ cd refurbished
```

Create/activate the virtual environment for this project:

```bash
$ pipenv shell
```


Install the project dependencies:

```bash
# installs the Python deps
$ pipenv install -dev
```


Set some environment variables and aliases:

```bash
$ export PYTHONPATH=`pwd`:$PYTHONPATH 
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

```bash
$ pipenv run pytest tests
```

### And coding style tests

Coding style is enforced using `flake8`.

```bash
$ pipenv run flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
```



## Built With

* [requests](https://requests.readthedocs.io/en/master/)
* [lxml](https://lxml.de)
* [price-parser](https://github.com/scrapinghub/price-parser)


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/zmoog/76aef48ad9d9faa096c41c7b16f2fc7c) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Maurizio Branca** - *Initial work* - [zmoog](https://github.com/zmoog)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
