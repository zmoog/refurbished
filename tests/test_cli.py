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
    def test_product_ipad_it(self, _):
        runner = CliRunner()

        result = runner.invoke(rfrb.get_products, ["be", "macs"])

        assert result.exit_code == 0
        assert (
            "Product 'macs' is not available in the 'be' store"
            in result.output
        )
