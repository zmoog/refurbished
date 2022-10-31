import io
from typing import List

from rich import box
from rich.console import Console
from rich.table import Table

from .model import Product


class ProductsResult:
    def __init__(self, values: List[Product]):
        self.values = values

    def str(self) -> str:
        if not self.values:
            return "No products found\n"

        table = Table(title="Refurbished Products", box=box.SIMPLE)
        table.add_column("Current")
        table.add_column("Previous")
        table.add_column("Saving")
        table.add_column("Name")

        for v in self.values:
            table.add_row(
                f"{v.price:,.0f}",
                f"{v.previous_price:,.0f}",
                f"{v.saving_percentage:.0%} (-{v.savings_price:,.0f})",
                v.name,
            )

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        return console.file.getvalue()

    def data(self) -> List[Product]:
        return self.values

    def fieldnames(self) -> List[str]:
        if self.values:
            return (
                self.values[0].__pydantic_model__.schema()["properties"].keys()
            )
        return []
