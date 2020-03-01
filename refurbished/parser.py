"""
Parser the Apple Refurbished pages to build useful product data.
"""
import decimal

from collections import namedtuple
from typing import List

from lxml import html
from price_parser import Price


Product = namedtuple('Product', 'name price previous_price savings_price')


def parse_products(page: str):
    """
    Parse the HTML page source to extract product data.
    """

    page = html.fromstring(page)
    products = page.xpath(
        '//div[@class="refurbished-category-grid-no-js"]/ul/li'
    )

    return [Product(
        _parse_name(product),
        _parse_current_price(product),
        _parse_previous_price(product),
        _parse_savings_price(product))
            for product in products]


def _parse_name(product: html.HtmlElement) -> str:
    """Parse the fragment with the product name."""
    return product.xpath('h3/a')[0].text.strip()


def _parse_current_price(product: html.HtmlElement) -> decimal.Decimal:
    """Parse the fragment with the current product price."""
    return _extract_price(product.xpath('div/text()'))


def _parse_previous_price(product: html.HtmlElement) -> decimal.Decimal:
    """Parse the fragment with the previous product price."""
    return _extract_price(product.xpath(
        'span[@class="as-price-previousprice"]/text()'
    ))


def _parse_savings_price(product: html.HtmlElement) -> decimal.Decimal:
    """Parse the fragment with the savings price.

    Its value should be equal to `previous` - `current` prices.
    """
    return _extract_price(product.xpath(
        'span[@class="as-producttile-savingsprice"]/text()'
    ))


def _extract_price(price_as_text: List[str]) -> decimal.Decimal:
    """Parse the text and extract the price as a `Decimal`."""
    for text in price_as_text:
        price = Price.fromstring(text)
        if price.amount:
            return price.amount
    return decimal.Decimal(0)
