from unittest.mock import patch

from . import ResponseBuilder


class TestStore:
    """
    Test the Refutbished Store API.
    """

    @patch("requests.Session.get", side_effect=ResponseBuilder("it_ipad.html"))
    def test_product_ipad_it(self, _):

        from refurbished import Store

        store = Store("it")
        products = store.get_ipads()

        assert len(products) == 34

    @patch("requests.Session.get", side_effect=ResponseBuilder("it_mac.html"))
    def test_product_macs_it(self, _):

        from refurbished import Store

        store = Store("it")
        products = store.get_macs()

        assert len(products) == 82

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("it_accessories.html"),
    )
    def test_product_accessories_it_empty(self, _):

        from refurbished import Store

        store = Store("it")
        products = store.get_accessories()

        assert len(products) == 0

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("us_clearance.html"),
    )
    def test_product_clearance_us_empty(self, _):

        from refurbished import Store

        store = Store("us")
        products = store.get_clearance()

        assert len(products) == 0

    @patch(
        "requests.Session.get",
        side_effect=ResponseBuilder("us_accessories.html"),
    )
    def test_product_accessories_us(self, _):

        from refurbished import Store

        store = Store("us")
        products = store.get_accessories()

        assert len(products) == 2

    @patch(
        "requests.Session.get", side_effect=ResponseBuilder("cn_watch.html")
    )
    def test_product_watch_cn(self, _):
        from refurbished import Store

        store = Store("cn")
        products = store.get_watches()

        assert len(products) == 35
