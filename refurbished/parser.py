"""
Parser the Apple Refurbished pages to build useful product data.
"""
import decimal

import re
import bs4
from urllib.parse import urlparse, urljoin
import unicodedata
from price_parser import Price

from .model import Product


def parse_products(product_family: str, page: str):
    """
    Parse the HTML page source to extract product data.
    """

    page = unicodedata.normalize("NFKD", page)
    page = bs4.BeautifulSoup(page, 'html.parser')

    # Getting the domain we're on from the canonical link metadata.

    current_parsed_url = urlparse(page.find("link", rel="canonical").attrs["href"],  scheme='https')
    store_domain = f'{current_parsed_url.scheme}://{current_parsed_url.netloc}'

    products = page.find("div", class_="refurbished-category-grid-no-js").ul.findAll("li")
    return [Product(
        name=_parse_name(product),
        family=product_family,
        url=_parse_url(product, store_domain),
        price=_parse_current_price(product),
        previous_price=_parse_previous_price(product),
        savings_price=_parse_savings_price(product),
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
    """
    Parse the fragment with the previous product price.
    If such fragment doesn't exist, assume there is no price reduction.
    """
    previousprice_tag = product.find("span", class_="as-price-previousprice")
    if previousprice_tag:
        return _extract_price(previousprice_tag.get_text())
    else:
        return _parse_current_price(product)


def _parse_savings_price(product: bs4.element.Tag) -> decimal.Decimal:
    """
    Parse the fragment with the savings price.
    Its value should be equal to `previous` - `current` prices.

    If such fragment doesn't exist, assume there is no price reduction.
    FIXME: This assumption is not always correct. Some stores (e.g. cn) only displays the current prices.
        Some heuristics are perhaps needed.
    """
    savingsprice_tag = product.find("span", class_="as-producttile-savingsprice")
    if savingsprice_tag:
        return _extract_price(savingsprice_tag.get_text())
    else:
        return decimal.Decimal(0)


def _parse_url(product: bs4.element.Tag, store_domain: str) -> str:
    """
    Parse the fragment with product URL and strip away query strings and fragments.
    Just appending the relative path onto apple.com does not work for all regions.
    For example, apple.com/cn redirects to apple.com.cn.
    All links are then relative to the .cn domain.
    """
    href = product.h3.a.attrs["href"]
    return urljoin(store_domain, urlparse(href).path, allow_fragments=False)


def _extract_price(price_as_text: str) -> decimal.Decimal:
    """Parse the text and extract the price as a `Decimal`."""
    price = Price.fromstring(price_as_text)
    if price.amount:
        return price.amount
    return decimal.Decimal(0)
