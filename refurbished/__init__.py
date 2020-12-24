# -*- coding: utf-8 -*-
"""
Get information published in the Refurbished and Clearance section of
the Apple Store http://www.apple.com/us/shop/browse/home/specialdeals
"""

import requests
from . import parser

REFURBISHED_BASE_URL = 'http://www.apple.com/%(country)s/shop/refurbished/%(product)s'


class Store:
    """
    Get data from the Apple Certified Refurbished stores
    (the store is different for each country where Apple operates).
    """

    def __init__(self, country):
        self.country = country
        # TODO: Check the /shop/refurbished page to determine which
        # product families are available.

    def get_iphones(self):
        """
        Fetch data for the iPhone product family.
        """
        return self._get_products('iphone')

    def get_ipads(self):
        """
        Fetch data for the iPad product family.
        """
        return self._get_products('ipad')

    def get_macs(self):
        """
        Fetch data for the Mac product family.
        """
        return self._get_products('mac')

    def get_appletvs(self):
        """
        Fetch data for the Apple TV product family.
        """
        return self._get_products('appletv')

    def get_watches(self):
        """
        Fetch data for the Apple Watch product family.
        """
        return self._get_products('watch')

    def get_accessories(self):
        """
        Fetch data for the accessories.
        """
        return self._get_products('accessories')

    def get_clearance(self):
        """
        Fetch data for the accessories.
        """
        return self._get_products('clearance')

    def _get_products(self, family):
        """
        Fetch product information from the Apple refurbished page.
        """
        products_url = REFURBISHED_BASE_URL % dict(
            country=self.country, product=family
        )

        with requests.Session() as session:

            resp = session.get(products_url)

            if resp.status_code == 404:
                raise Exception(f'Ooops, it looks like your store doesn\'t carry those products: {family}')

            elif not resp.ok:
                raise Exception('Ooops, cannot fetch the product page.')

            return parser.parse_products(resp.text)
