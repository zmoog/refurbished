import csv
import decimal
import io
import json
from dataclasses import asdict

import click


def _custom_json_encoder(obj):
    """
    Custom JSON encoder for types that require special handling.

    Replaces deprecated pydantic.json.pydantic_encoder in Pydantic v2.
    """
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(
        f"Object of type {type(obj).__name__} is not JSON serializable"
    )


class Feedback:
    def __init__(self, format):
        self.format = format

    def echo(self, text, nl=True, err=False):
        click.echo(text, nl=nl, err=err)

    def result(self, result) -> None:
        if self.format == "text":
            click.echo(
                result.str(),
                # delegate newlines to the result class
                nl=False,
            )
        elif self.format == "json":
            # assumption: entries are all pydantic dataclasses
            data = [asdict(entry) for entry in result.data()]
            click.echo(
                json.dumps(data, indent=2, default=_custom_json_encoder),
                # delegate newline to json.dumps
                nl=False,
            )
        elif self.format == "ndjson":
            # assumption: entries are all pydantic dataclasses
            for entry in result.data():
                click.echo(
                    json.dumps(asdict(entry), default=_custom_json_encoder),
                    # The newline is required by the format to separate the
                    # JSON objects
                    nl=True,
                )
        elif self.format == "csv":
            entries = result.data()

            # we need at least one entry to get the fieldnames from
            # the pydantic dataclass and write the csv header
            if not entries:
                return

            out = io.StringIO()
            writer = csv.DictWriter(out, fieldnames=result.fieldnames())
            writer.writeheader()
            for entry in entries:
                writer.writerow(asdict(entry))

            # delegate newline to the csv writer
            click.echo(out.getvalue(), nl=False)


_current_feedback = Feedback("text")


def set_format(format):
    _current_feedback.format = format


def echo(value, nl=True, err=False):
    _current_feedback.echo(value, nl=nl, err=err)


def result(values):
    _current_feedback.result(values)
