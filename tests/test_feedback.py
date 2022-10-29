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

        with open("sample.txt", "w") as f:
            f.write(result.output)

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
                                                                                
  Previous   Current   Saving      Name                                         
 ────────────────────────────────────────────────────────────────────────────── 
  449        389       13% (-60)   iPad Wi-Fi 128GB ricondizionato - Argento    
                                   (sesta generazione)                          
                                                                                
"""  # noqanoqa: W291 W293
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
                                                                                
  Previous   Current   Saving      Name                                         
 ────────────────────────────────────────────────────────────────────────────── 
  449        389       13% (-60)   iPad Wi-Fi 128GB ricondizionato - Argento    
                                   (sesta generazione)                          
                                                                                
"""  # noqa: W291 W293
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
    "store": "it",
    "url": "https://www.apple.com/it/shop/product/FR7K2TY/A/Refurbished-iPad-Wi-Fi-128GB-Silver-6th-Generation",
    "price": 389.0,
    "previous_price": 449.0,
    "savings_price": 60.0,
    "saving_percentage": 0.133630289532294,
    "model": "FR7K2TY"
  }
]"""  # noqa: E501
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_ndjson_format(self, _, cli_runner: CliRunner):
        result = cli_runner.invoke(
            rfrb.get_products,
            ["it", "ipads", "--max-price", "389", "--format", "ndjson"],
        )

        assert result.exit_code == 0
        assert (
            result.output
            == '{"name": "iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)", "family": "ipad", "store": "it", "url": "https://www.apple.com/it/shop/product/FR7K2TY/A/Refurbished-iPad-Wi-Fi-128GB-Silver-6th-Generation", "price": 389.0, "previous_price": 449.0, "savings_price": 60.0, "saving_percentage": 0.133630289532294, "model": "FR7K2TY"}\n'  # noqa: E501
        )

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_ipad.html"),
    )
    def test_csv_format(self, _, cli_runner: CliRunner):
        result = cli_runner.invoke(
            rfrb.get_products,
            ["it", "ipads", "--max-price", "389", "--format", "csv"],
        )

        assert result.exit_code == 0
        assert (
            result.output
            == """name,family,store,url,price,previous_price,savings_price,saving_percentage,model
iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione),ipad,it,https://www.apple.com/it/shop/product/FR7K2TY/A/Refurbished-iPad-Wi-Fi-128GB-Silver-6th-Generation,389.00,449.00,60.00,0.133630289532294,FR7K2TY
"""  # noqa: E501
        )
