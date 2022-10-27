from typing import List

from .model import Product


class ProductsResult:
    def __init__(self, values: List[Product]):
        self.values = values

    def str(self) -> str:
        if len(self.values) == 0:
            return "No products found"
        out = ""
        for p in self.values:
            out += (
                f"{p.previous_price} "
                f"{p.price} "
                f"{p.savings_price} "
                f"({p.saving_percentage * 100}%) {p.name}\n"
            )
        return out

    def data(self) -> List[Product]:
        return self.values

    def fieldnames(self) -> List[str]:
        if self.values:
            return (
                self.values[0].__pydantic_model__.schema()["properties"].keys()
            )
        return []
