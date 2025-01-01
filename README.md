# Refurbished

Refurbished is a CLI tool (and a Python [library on PyPI](https://pypi.org/project/refurbished/)) to access the product information available on the [Apple Certified Refurbished](https://www.apple.com/shop/refurbished) section of the Apple Store.

## Usage

### As a CLI Tool

A quick search for Macs with a min saving of 300 EUR on the Italian store:

```shell
$ rfrb it macs --min-saving=300
                                                             Refurbished Products                                                             
                                                                                                                                              
  Model    Current   Previous   Saving       Name                                                                                                
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  FGN63T   869       1,229      29% (-360)   MacBook Air 13,3" ricondizionato con chip Apple M1, CPU 8‐core e GPU 7‐core - Grigio siderale       
  FGN93T   869       1,229      29% (-360)   MacBook Air 13,3" ricondizionato con chip Apple M1, CPU 8‐core e GPU 7‐core - Argento               
  FGND3T   869       1,229      29% (-360)   MacBook Air 13,3" ricondizionato con chip Apple M1, CPU 8‐core e GPU 7‐core - Oro                   
  FGN73T   1,049     1,429      27% (-380)   MacBook Air 13,3" ricondizionato con chip Apple M1, CPU 8‐core e GPU 8‐core - Grigio siderale       
  FGNA3T   1,049     1,429      27% (-380)   MacBook Air 13,3" ricondizionato con chip Apple M1, CPU 8‐core e GPU 8‐core - Argento               
  FQKR3T   1,209     1,519      20% (-310)   MacBook Air 15" ricondizionato con chip Apple M2, CPU 8‐core e GPU 10‐core - Argento                
  FQKU3T   1,209     1,519      20% (-310)   MacBook Air 15" ricondizionato con chip Apple M2, CPU 8‐core e GPU 10‐core - Galassia               
  FQKW3T   1,209     1,519      20% (-310)   MacBook Air 15" ricondizionato con chip Apple M2, CPU 8‐core e GPU 10‐core - Mezzanotte             
  FRX63T   2,019     2,379      15% (-360)   MacBook Pro 14" ricondizionato con chip Apple M3 Pro, CPU 11‐core e GPU 14‐core - Argento           
  FRX33T   2,019     2,379      15% (-360)   MacBook Pro 14" ricondizionato con chip Apple M3 Pro, CPU 11‐core e GPU 14‐core - Nero siderale     
  FRX43T   2,449     2,879      15% (-430)   MacBook Pro 14" ricondizionato con chip Apple M3 Pro, CPU 12-core e GPU 18-core - Nero siderale     
  FRX73T   2,449     2,879      15% (-430)   MacBook Pro 14" ricondizionato con chip Apple M3 Pro, CPU 12-core e GPU 18-core - Argento           
  FRX53T   3,209     3,779      15% (-570)   MacBook Pro 14" ricondizionato con chip Apple M3 Max con CPU 14‐core e GPU 30‐core - Nero siderale  
  FRX83T   3,209     3,779      15% (-570)   MacBook Pro 14" ricondizionato con chip Apple M3 Max con CPU 14‐core e GPU 30‐core - Argento        
  FNWA3T   3,349     4,219      21% (-870)   MacBook Pro 16" ricondizionato con chip Apple M2 Max, CPU 12‐core e GPU 38‐core - Grigio siderale   
  FNWE3T   3,349     4,219      21% (-870)   MacBook Pro 16" ricondizionato con chip Apple M2 Max, CPU 12‐core e GPU 38‐core - Argento           
  FUW63T   3,979     4,679      15% (-700)   MacBook Pro 16" ricondizionato con chip Apple M3 Max, CPU 16‐core e GPU 40‐core - Nero siderale                   
```

#### Products

Refurbished supports the following products from the refurbished section of the Apple Store:

- `accessories`
- `airpods`
- `appletvs`
- `homepods`
- `macs`
- `iphones`
- `ipads`
- `watches`
- `clearance`

#### Output formats

Refurbished supports several output formats:

- `text`
- `json`
- `ndjson`
- `csv`

Here are a few examples.

##### Text

```shell
$ rfrb it ipads --max-price 539
                                             Refurbished Products                                              
                                                                                                               
  Model     Current   Previous   Saving      Name                                                       
 ────────────────────────────────────────────────────────────────────────────────────────────────────── 
  FUWA3ZM   79        89         11% (-10)   Apple Pencil (USB‐C) ricondizionata                        
  FCM84TY   339       409        17% (-70)   iPad Wi-Fi 64GB ricondizionato - Blu (decima generazione)  
```

##### JSON

```shell
$ rfrb it ipads --max-price 539 --format json
[
  {
    "name": "Apple Pencil (USB\u2010C) ricondizionata",
    "family": "ipad",
    "store": "it",
    "url": "https://www.apple.com/it/shop/product/FUWA3ZM/A/apple-pencil-usb%E2%80%91c-ricondizionata",
    "price": 79.0,
    "previous_price": 89.0,
    "savings_price": 10.0,
    "saving_percentage": 0.11235955056179775,
    "model": "FUWA3ZM"
  },
  {
    "name": "iPad Wi-Fi 64GB ricondizionato - Blu (decima generazione)",
    "family": "ipad",
    "store": "it",
    "url": "https://www.apple.com/it/shop/product/FCM84TY/A/ipad-wi-fi-64gb-ricondizionato-blu-decima-generazione",
    "price": 339.0,
    "previous_price": 409.0,
    "savings_price": 70.0,
    "saving_percentage": 0.17114914425427874,
    "model": "FCM84TY"
  }
]
```

##### NDJSON

```shell
$ rfrb it ipads --max-price 539 --format ndjson
{"name": "Apple Pencil (USB\u2010C) ricondizionata", "family": "ipad", "store": "it", "url": "https://www.apple.com/it/shop/product/FUWA3ZM/A/apple-pencil-usb%E2%80%91c-ricondizionata", "price": 79.0, "previous_price": 89.0, "savings_price": 10.0, "saving_percentage": 0.11235955056179775, "model": "FUWA3ZM"}
{"name": "iPad Wi-Fi 64GB ricondizionato - Blu (decima generazione)", "family": "ipad", "store": "it", "url": "https://www.apple.com/it/shop/product/FCM84TY/A/ipad-wi-fi-64gb-ricondizionato-blu-decima-generazione", "price": 339.0, "previous_price": 409.0, "savings_price": 70.0, "saving_percentage": 0.17114914425427874, "model": "FCM84TY"}

```

##### CSV

```shell
$ rfrb it ipads --name 'iPad Air Wi-Fi 64GB' --format csv
name,family,store,url,price,previous_price,savings_price,saving_percentage,model
iPad Air Wi-Fi 64GB ricondizionato - Oro (terza generazione),ipad,it,https://www.apple.com/it/shop/product/FUUL2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Oro-terza-generazione,479.00,559.00,80.00,0.14,FUUL2TY
iPad Air Wi-Fi 64GB ricondizionato - Celeste (quarta generazione),ipad,it,https://www.apple.com/it/shop/product/FYFQ2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Celeste-quarta-generazione,539.00,639.00,100.00,0.16,FYFQ2TY
iPad Air Wi-Fi 64GB ricondizionato - Grigio siderale (quarta generazione),ipad,it,https://www.apple.com/it/shop/product/FYFM2TY/A/iPad-Air-Wi-Fi-64GB-ricondizionato-Grigio-siderale-quarta-generazione,539.00,639.00,100.00,0.16,FYFM2TY
```

### As a Python Library

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

- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
- [price-parser](https://github.com/scrapinghub/price-parser)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [requests](https://requests.readthedocs.io/en/master/)
- [rich](https://github.com/Textualize/rich)

## Development

If you want make some changes or contributed, please check the [development.md](docs/development.md) guide in the `docs` folder.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/zmoog/76aef48ad9d9faa096c41c7b16f2fc7c) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

- **Maurizio Branca** - *Initial work* - [zmoog](https://github.com/zmoog)
- **Yizhou "Andi" Cui** - *Improved parser* - [AndiCui](https://github.com/AndiCui)
- **Grant** - *Dockerfile* - [Firefishy](https://github.com/Firefishy)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
