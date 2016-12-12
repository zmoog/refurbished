import unittest
import pkgutil
import io
import pprint
from unittest import mock
from unittest.mock import patch


pp = pprint.PrettyPrinter(indent=4)


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
        text = io.BytesIO(resource).read()

        mock_response = mock.Mock()
        mock_response.text = text
        mock_response.ok = True

        return mock_response


class StoreTest(unittest.TestCase):
    """
    Test the Refutbished Store API.
    """

    def setUp(self):
        pass

    @patch('requests.Session.get', side_effect=ResponseBuilder('it__ipad__ipad_pro_97__wi_fi.html'))
    def test_product_ipad__ipad_pro_97__wifi(self, _):

        from refurbished import Store

        store = Store('it')
        products = store.get_ipads(model='ipad_pro_97', connectivity='wi_fi')

        self.assertEqual(len(products), 3)
