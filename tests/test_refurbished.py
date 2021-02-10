import pkgutil
import io
from unittest import mock
from unittest.mock import patch


class ResponseBuilder(object):

    def __init__(self, response_filename):
        self.response_filename = response_filename

    def __call__(self, _):
        return self._build_response()

    def _build_response(self):
        """
        Build a response object with a subset of the response object from the requests API.
        """
        resource = pkgutil.get_data('tests', self.response_filename)
        text = io.BytesIO(resource).read().decode()

        mock_response = mock.Mock()
        mock_response.text = text
        mock_response.ok = True

        return mock_response


class TestStore:
    """
    Test the Refutbished Store API.
    """

    @patch('requests.Session.get', side_effect=ResponseBuilder('it_ipad.html'))
    def test_product_ipad(self, _):

        from refurbished import Store

        store = Store('it')
        products = store.get_ipads()

        assert len(products) == 34

    @patch('requests.Session.get', side_effect=ResponseBuilder('it_mac.html'))
    def test_product_macs(self, _):

        from refurbished import Store

        store = Store('it')
        products = store.get_macs()

        assert len(products) == 82

    @patch('requests.Session.get', side_effect=ResponseBuilder('it_accessories.html'))
    def test_product_accessories(self, _):

        from refurbished import Store

        store = Store('it')
        products = store.get_accessories()

        assert len(products) == 0
