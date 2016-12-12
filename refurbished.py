"""
Get information published in the Refurbished and Clearance section of
the Apple Store http://www.apple.com/us/shop/browse/home/specialdeals

iPad products

- ipad
- ipad_pro_97
- wi_fi

"""
# -*- coding: utf-8 -*-

import requests

import parser

REFURBISHED_BASE_URL = 'http://www.apple.com/%(country)s/shop/browse/home/specialdeals'


class UrlBuilder(object):
    pass


class Store(object):
    """
    Get data from the Apple Certified Refurbished stores (the store is different for each country where Apple operates).
    """

    def __init__(self, country):
        self.country = country
        self.store_url = REFURBISHED_BASE_URL % dict(country=self.country)

    def get_ipads(self, model=None, connectivity=None):
        """
        Fetch data for the iPad product family.
        """
        return self._get_products('ipad', model, connectivity)


    def _get_products(self, family, model=None, connectivity=None):
        """
        Fetch product information from the Apple refurbished page.
        """

        products_url = self.store_url + '/%(family)s' % dict(family=family)

        if model is not None:
            products_url += '/%(model)s' % dict(model=model)

            if connectivity is not None:
                products_url += '/%(connectivity)s' % dict(connectivity=connectivity)

        with requests.Session() as session:

            resp = session.get(products_url)

            if not resp.ok:
                raise Exception('Ooops, cannot fetch the product page.')

            return parser.parse_products(resp.text)
