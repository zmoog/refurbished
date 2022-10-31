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
        result = cli_runner.invoke(rfrb.get_products, ["be", "macs"])

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
        result = cli_runner.invoke(
            rfrb.get_products, ["it", "ipads", "--max-price", "400"]
        )

        assert result.exit_code == 0
        assert (
            # Click's CliRunner uses a terminal width of 80 characters, so
            # Rich will wrap the output to fit the terminal width.
            #
            # Don't go crazy with the indentation, just save the output in a
            # file with something like:
            #
            # with open("sample.txt", "w") as f:
            #     f.write(result.output)
            #
            # And then copy the output from the file in the assert.
            result.output
            == """                              Refurbished Products                              
                                                                                
  Current   Previous   Saving      Name                                         
 ────────────────────────────────────────────────────────────────────────────── 
  389       449        13% (-60)   iPad Wi-Fi 128GB ricondizionato - Argento    
                                   (sesta generazione)                          
                                                                                
"""  # noqa: W291 W293
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_max_previous_price(self, _, cli_runner: CliRunner):
        result = cli_runner.invoke(
            rfrb.get_products,
            ["it", "ipads", "--max-previous-price", "500"],
        )

        assert result.exit_code == 0
        assert (
            # Click's CliRunner uses a terminal width of 80 characters, so
            # Rich will wrap the output to fit the terminal width.
            #
            # Don't go crazy with the indentation, just save the output in a
            # file with something like:
            #
            # with open("sample.txt", "w") as f:
            #     f.write(result.output)
            #
            # And then copy the output from the file in the assert.
            result.output
            == """                              Refurbished Products                              
                                                                                
  Current   Previous   Saving      Name                                         
 ────────────────────────────────────────────────────────────────────────────── 
  389       449        13% (-60)   iPad Wi-Fi 128GB ricondizionato - Argento    
                                   (sesta generazione)                          
                                                                                
"""  # noqa: W291 W293
        )
