# -*- coding: utf-8 -*-
"""
Get information published in the Refurbished and Clearance section of
the Apple Store http://www.apple.com/us/shop/browse/home/specialdeals
"""

from typing import List

import requests

from . import parser
from .model import Product

REFURBISHED_BASE_URL = (
    "http://www.apple.com/%(country)s/shop/refurbished/%(product)s"
)


class ProductNotFoundError(Exception):
    pass


class Store:
    """
    Get data from the Apple Certified Refurbished stores
    (the store is different for each country where Apple operates).
    """

    def __init__(self, country):
        self.country = country
        # TODO: Check the /shop/refurbished page to determine which
        #   product families are available.

    def get_iphones(self, **kwargs) -> List[Product]:
        """
        Fetch data for the iPhone product family.
        """
        return self._get_products("iphone", **kwargs)

    def get_ipads(self, **kwargs) -> List[Product]:
        """
        Fetch data for the iPad product family.
        """
        return self._get_products("ipad", **kwargs)

    def get_macs(self, **kwargs) -> List[Product]:
        """
        Fetch data for the Mac product family.
        """
        return self._get_products("mac", **kwargs)

    def get_appletvs(self, **kwargs) -> List[Product]:
        """
        Fetch data for the Apple TV product family.
        """
        return self._get_products("appletv", **kwargs)

    def get_watches(self, **kwargs) -> List[Product]:
        """
        Fetch data for the Apple Watch product family.
        """
        return self._get_products("watch", **kwargs)

    def get_accessories(self, **kwargs) -> List[Product]:
        """
        Fetch data for the accessories.
        """
        return self._get_products("accessories", **kwargs)

    def get_clearance(self, **kwargs) -> List[Product]:
        """
        Fetch data for the accessories.
        """
        return self._get_products("clearance", **kwargs)

    def _get_products(
        self,
        product_family,
        min_saving=0.0,
        min_saving_percentage=0.0,
        max_price=None,
        max_previous_price=None,
        name=None,
    ):
        """
        Fetch product information from the Apple refurbished page.
        """
        products_url = REFURBISHED_BASE_URL % dict(
            country=self.country, product=product_family
        )

        with requests.Session() as session:
            resp = session.get(products_url)

            if resp.status_code == 404:
                raise ProductNotFoundError(
                    "Ooops, it looks like your store doesn't carry "
                    f"those products: {product_family}"
                )
            elif not resp.ok:
                raise Exception("Ooops, cannot fetch the product page.")

            # Parse HTML response from Apple website
            products = parser.parse_products(product_family, resp.text)

            # set up the criteria to filter the products
            criteria = (
                lambda p: p.savings_price >= min_saving
                and p.saving_percentage * 100 >= min_saving_percentage
                and (max_price is None or p.price <= max_price)
                and (
                    max_previous_price is None
                    or p.previous_price <= max_previous_price
                )
                and (name is None or name in p.name)
            )

            # Filter products
            products = list(filter(criteria, products))

            return products
