import json
from typing import List

import click
from pydantic.json import pydantic_encoder

from .model import Product


class Feedback:
    def __init__(self, format):
        self.format = format

    def echo(self, text, nl=True, err=False):
        click.echo(text, nl=nl, err=err)

    def result(self, result):
        if self.format == "text":
            click.echo(
                result.str(),
                # delefate newlines to the result class
                nl=False,
            )
        elif self.format == "json":
            click.echo(
                json.dumps(result.data(), indent=2, default=pydantic_encoder),
                # delegate newline to json.dumps
                nl=False,
            )
        elif self.format == "ndjson":
            for product in result.data():
                click.echo(
                    json.dumps(product, default=pydantic_encoder),
                    # The newline is required by the format to separate the
                    # JSON objects
                    nl=True,
                )


_current_feedback = Feedback("text")


def set_format(format):
    _current_feedback.format = format


def echo(value, nl=True, err=False):
    _current_feedback.echo(value, nl=nl, err=err)


def result(values):
    _current_feedback.result(values)


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

    def data(self):
        return self.values
