import decimal
import re
from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class Product:
    """
    Data Class representing a store product
    """

    name: str
    family: str
    store: str
    url: str
    price: decimal.Decimal
    previous_price: decimal.Decimal
    savings_price: decimal.Decimal
    saving_percentage: float = 0
    model: Optional[str] = None

    def __post_init__(self):
        """
        Populate fields that are derivable by other values.

        Note: In Pydantic v2, __post_init__ is called AFTER validation,
        which is the desired behavior for computed fields.
        """
        self.saving_percentage = float(
            self.savings_price / self.previous_price
        )
        self.model = re.search("/shop/product/(.[^/]*)/", self.url).group(1)

    def __repr__(self):
        """
        A readable version for prints.
        """
        return (
            f"{self.price} ({'-{:.0%}'.format(self.saving_percentage)}) "
            "- [{self.model}] {self.name} {self.url}"
        )
