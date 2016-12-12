"""
Parser the Apple Refurbished pages to build useful product data.
"""

from collections import namedtuple
import decimal
import re

from lxml import html


Product = namedtuple('Product', 'name price')


def parse_products(page_text):
    """
    Parse the HTML page source to extract product data.
    """

    page = html.fromstring(page_text)

    products = page.xpath('//tr[@class="product"]')

    return [Product(
        _parse_name(product),
        _parse_price(product))
            for product in products]


def _parse_price(product):
    price_as_text = product.xpath(
        'td[@class="purchase-info"]/p[@class="price"]/span/span/span')[0].text.strip()
    price_components = re.search(r'(?P<a>\d+)[.,](?P<b>\d{1,})', price_as_text)
    return decimal.Decimal('%s.%s' % (price_components.group(1), price_components.group(2)))

def _parse_name(product):
    return product.xpath('td[@class="specs"]/h3/a')[0].text.strip()
