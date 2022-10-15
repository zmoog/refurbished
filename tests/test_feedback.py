from unittest.mock import patch

from click.testing import CliRunner

from . import ResponseBuilder, import_module

rfrb = import_module("rfrb", "cli/rfrb")


class TestFeedback(object):
    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_default_format(self, _, cli_runner: CliRunner):
        result = cli_runner.invoke(
            rfrb.get_products, ["it", "ipads", "--max-price", "389"]
        )

        assert result.exit_code == 0
        assert (
            result.output
            == "449.00 389.00 60.00 (13.3630289532294%) iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)\n"  # noqa: E501
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_text_format(self, _, cli_runner: CliRunner):
        result = cli_runner.invoke(
            rfrb.get_products,
            ["it", "ipads", "--max-price", "389", "--format", "text"],
        )

        assert result.exit_code == 0
        assert (
            result.output
            == "449.00 389.00 60.00 (13.3630289532294%) iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)\n"  # noqa: E501
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_json_format(self, _, cli_runner: CliRunner):
        result = cli_runner.invoke(
            rfrb.get_products,
            ["it", "ipads", "--max-price", "389", "--format", "json"],
        )

        assert result.exit_code == 0
        # Output is pretty printed with two spaces indentation
        assert (
            result.output
            == """[
  {
    "name": "iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)",
    "family": "ipad",
    "url": "https://www.apple.com/it/shop/product/FR7K2TY/A/Refurbished-iPad-Wi-Fi-128GB-Silver-6th-Generation",
    "price": 389.0,
    "previous_price": 449.0,
    "savings_price": 60.0,
    "saving_percentage": 0.133630289532294,
    "model": "FR7K2TY"
  }
]"""  # noqa: E501
        )
