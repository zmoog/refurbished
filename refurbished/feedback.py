import csv
import io
import json
from dataclasses import asdict

import click
from pydantic.json import pydantic_encoder


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
            click.echo(
                json.dumps(result.data(), indent=2, default=pydantic_encoder),
                # delegate newline to json.dumps
                nl=False,
            )
        elif self.format == "ndjson":
            # assumption: entries are all pydantic dataclasses
            for entry in result.data():
                click.echo(
                    json.dumps(entry, default=pydantic_encoder),
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
