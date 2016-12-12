import decimal
import unittest
import pkgutil
import io
import pprint

import parser


pp = pprint.PrettyPrinter(indent=4)


class ParserTest(unittest.TestCase):

    def setUp(self):

        resource = pkgutil.get_data('tests', 'ipad__ipad_pro_97__wi_fi.html')

        self.page_text = io.BytesIO(resource).read()


    def test_product_ipad__ipad_pro_97__wi_fi(self):
        """
        Tests the specific product page.
        """

        products = parser.parse_products(self.page_text)

        pp.pprint(products)

        self.assertEqual(len(products), 3)

        # for spec in [
        #     'iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Grigio siderale',
        #     'iPad Pro 9, 7" Wi-Fi 32GB ricondizionato - Argento',
        #     'iPad Pro 9,7" Wi-Fi 128GB ricondizionato - Oro rosa'
        #     ], x in products:

        #     self.assertEqual(products[0].specs, spec)

        product = products[0]

        self.assertEqual(product.name, 'iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Grigio siderale')
        self.assertEqual(product.price, decimal.Decimal('589.00'))
