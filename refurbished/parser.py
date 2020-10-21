"""
Parser the Apple Refurbished pages to build useful product data.
"""
import decimal

from dataclasses import dataclass

import bs4
import unicodedata
from price_parser import Price


@dataclass
class Product:
    """
    Data Class representing a store product
    """

    name: str
    url: str
    price: decimal.Decimal
    previous_price: decimal.Decimal
    savings_price: decimal.Decimal


def parse_products(page: str):
    """
    Parse the HTML page source to extract product data.
    """

    page = unicodedata.normalize("NFKD", page)
    page = bs4.BeautifulSoup(page, 'html.parser')
    products = page.find("div", class_="refurbished-category-grid-no-js").ul.findAll("li")
    return [Product(
        _parse_name(product),
        _parse_url(product),
        _parse_current_price(product),
        _parse_previous_price(product),
        _parse_savings_price(product),
    )
        for product in products
    ]


def _parse_name(product: bs4.element.Tag) -> str:
    """Parse the fragment with the product name."""
    return product.h3.a.get_text().strip()


def _parse_current_price(product: bs4.element.Tag) -> decimal.Decimal:
    """Parse the fragment with the current product price."""
    return _extract_price(product.div.get_text())


def _parse_previous_price(product: bs4.element.Tag) -> decimal.Decimal:
    """Parse the fragment with the previous product price."""
    return _extract_price(product.find("span", class_="as-price-previousprice").get_text())


def _parse_savings_price(product: bs4.element.Tag) -> decimal.Decimal:
    """Parse the fragment with the savings price.

    Its value should be equal to `previous` - `current` prices.
    """
    return _extract_price(product.find("span", class_="as-producttile-savingsprice").get_text())


def _parse_url(product: bs4.element.Tag) -> str:
    """Parse the fragment with product URL."""
    href = product.h3.a.attrs["href"]
    return f'https://www.apple.com{href}'


def _extract_price(price_as_text: str) -> decimal.Decimal:
    """Parse the text and extract the price as a `Decimal`."""
    price = Price.fromstring(price_as_text)
    if price.amount:
        return price.amount
    return decimal.Decimal(0)
