from unittest.mock import patch

from click.testing import CliRunner

from . import ResponseBuilder, import_module

rfrb = import_module("rfrb", "cli/rfrb")


class TestCLI:
    """
    Test the Refurbished Command Line Interface (CLI).
    """

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("page_not_found.html", status_code=404),
    )
    def test_product_ipad_it(self, _, cli_runner: CliRunner):
        runner = CliRunner()

        result = runner.invoke(rfrb.get_products, ["be", "macs"])

        assert result.exit_code == 0, result.output
        assert (
            "Product 'macs' is not available in the 'be' store"
            in result.output
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_max_price(self, _, cli_runner: CliRunner):
        runner = CliRunner()

        result = runner.invoke(
            rfrb.get_products, ["it", "ipads", "--max-price", "400"]
        )

        assert result.exit_code == 0
        assert (
            # this is the only product that matches the max price
            "449.00 389.00 60.00 (13.3630289532294%) iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)"  # noqa
            in result.output
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_max_previous_price(self, _, cli_runner: CliRunner):
        runner = CliRunner()

        result = runner.invoke(
            rfrb.get_products, ["it", "ipads", "--max-previous-price", "500"]
        )

        assert result.exit_code == 0
        assert (
            # this is the only product that matches the max previous price
            "449.00 389.00 60.00 (13.3630289532294%) iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)"  # noqa
            in result.output
        )
