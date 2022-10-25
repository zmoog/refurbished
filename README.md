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

#### Output formats

Refurbished supports several output formats:

- `text`
- `json`
- `ndjson`
- `csv`

Here are a few examples.

##### text

```shell
$ rfrb it ipads --max-price 539
559.00 479.00 80.00 (14.311270125223613%) iPad Air Wi-Fi 64GB ricondizionato - Oro (terza generazione)
639.00 539.00 100.00 (15.64945226917058%) iPad Air Wi-Fi 64GB ricondizionato - Celeste (quarta generazione)
```

##### json

```shell
$ rfrb it ipads --max-price 539 --format json
[
  {
    "name": "iPad Air Wi-Fi 64GB ricondizionato - Oro (terza generazione)",
    "family": "ipad",
    "url": "https://www.apple.com/it/shop/product/FUUL2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Oro-terza-generazione",
    "price": 479.0,
    "previous_price": 559.0,
    "savings_price": 80.0,
    "saving_percentage": 0.14311270125223613,
    "model": "FUUL2TY"
  },
  {
    "name": "iPad Air Wi-Fi 64GB ricondizionato - Celeste (quarta generazione)",
    "family": "ipad",
    "url": "https://www.apple.com/it/shop/product/FYFQ2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Celeste-quarta-generazione",
    "price": 539.0,
    "previous_price": 639.0,
    "savings_price": 100.0,
    "saving_percentage": 0.1564945226917058,
    "model": "FYFQ2TY"
  }
]
```

##### ndjson

```shell
$ rfrb it ipads --max-price 539 --format ndjson
{"name": "iPad Air Wi-Fi 64GB ricondizionato - Oro (terza generazione)", "family": "ipad", "url": "https://www.apple.com/it/shop/product/FUUL2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Oro-terza-generazione", "price": 479.0, "previous_price": 559.0, "savings_price": 80.0, "saving_percentage": 0.14311270125223613, "model": "FUUL2TY"}
{"name": "iPad Air Wi-Fi 64GB ricondizionato - Celeste (quarta generazione)", "family": "ipad", "url": "https://www.apple.com/it/shop/product/FYFQ2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Celeste-quarta-generazione", "price": 539.0, "previous_price": 639.0, "savings_price": 100.0, "saving_percentage": 0.1564945226917058, "model": "FYFQ2TY"}
```

##### CSV

```shell
$ rfrb it ipads --name 'iPad Air Wi-Fi 64GB' --format csv                                                    zmoog/csv-output-option  ✭ ✱
name,family,store,url,price,previous_price,savings_price,saving_percentage,model
iPad Air Wi-Fi 64GB ricondizionato - Oro (terza generazione),ipad,it,https://www.apple.com/it/shop/product/FUUL2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Oro-terza-generazione,479.00,559.00,80.00,0.14,FUUL2TY
iPad Air Wi-Fi 64GB ricondizionato - Celeste (quarta generazione),ipad,it,https://www.apple.com/it/shop/product/FYFQ2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Celeste-quarta-generazione,539.00,639.00,100.00,0.16,FYFQ2TY
iPad Air Wi-Fi 64GB ricondizionato - Grigio siderale (quarta generazione),ipad,it,https://www.apple.com/it/shop/product/FYFM2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Grigio-siderale-quarta-generazione,539.00,639.00,100.00,0.16,FYFM2TY
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

## Built With

* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
* [price-parser](https://github.com/scrapinghub/price-parser)
* [pydantic](https://pydantic-docs.helpmanual.io/)
* [requests](https://requests.readthedocs.io/en/master/)

## Development

If you want make some changes or contributed, please check the [development.md](docs/development.md) guide in the `docs` folder.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/zmoog/76aef48ad9d9faa096c41c7b16f2fc7c) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Maurizio Branca** - *Initial work* - [zmoog](https://github.com/zmoog)
* **Yizhou "Andi" Cui** - *Improved parser* - [AndiCui](https://github.com/AndiCui)
* **Grant** - *Dockerfile* - [Firefishy](https://github.com/Firefishy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
