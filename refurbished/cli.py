import io
from typing import List

from rich.console import Console
from rich.table import Table

from .model import Product


class ProductsResult:
    def __init__(self, values: List[Product]):
        self.values = values

    def str(self) -> str:
        if not self.values:
            return "No products found\n"

        table = Table(title="Refurbished Products", width=200)

        table.add_column("Previous Price")
        table.add_column("Price")
        table.add_column("Saving Price")
        table.add_column("Saving Percentage")
        table.add_column("Name")

        for p in self.values:
            table.add_row(
                f"{p.previous_price}",
                f"{p.price}",
                f"{p.savings_price}",
                f"{p.saving_percentage}",
                p.name,
            )

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
