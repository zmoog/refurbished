import decimal
import re

# from dataclasses import dataclass
from pydantic.dataclasses import dataclass


@dataclass
class Product:
    """
    Data Class representing a store product
    """

    name: str
    family: str
    url: str
    price: decimal.Decimal
    previous_price: decimal.Decimal
    savings_price: decimal.Decimal
    saving_percentage: float = 0
    model: str = None

    def __post_init__(self):
        """
        Populate fields that are derivable by other values
        """
        self.saving_percentage = float(
            self.savings_price / self.previous_price
        )
        self.model = re.search("/shop/product/(.[^/]*)/", self.url).group(1)

    def __repr__(self):
        """
        A readable version for prints.
        """
        return f"{self.price} ({'-{:.0%}'.format(self.saving_percentage)}) "
        "- [{self.model}] {self.name} {self.url}"
