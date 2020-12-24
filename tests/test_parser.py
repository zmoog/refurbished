import decimal
import pkgutil
import io
import pprint

from refurbished.parser import parse_products


pp = pprint.PrettyPrinter(indent=4)


class TestParser:

    # def test_product_ipad__ipad_pro_97__wi_fi(self):
    #     """
    #     Tests the specific product page.
    #     """
    #     resource = pkgutil.get_data(
    #         'tests',
    #         'it__ipad__ipad_pro_97__wi_fi.html')

    #     html = io.BytesIO(resource).read()

    #     products = parse_products(html)

    #     assert len(products), 3

    #     product = products[0]

    #     assert product.name, 'iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Grigio siderale'
    #     assert product.price, decimal.Decimal('589.00')

    def test_product_ipad(self):
        """
        Tests the specific product page.
        """
        resource = pkgutil.get_data(
            'tests',
            'it_ipad.html')

        page = io.BytesIO(resource).read().decode('UTF-8')

        products = parse_products(page)
        assert len(products) == 34

        product = products[0]
        assert product.name == 'iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)'
        assert product.url == 'https://www.apple.com/it/shop/product/FR7K2TY/A/Refurbished-iPad-Wi-Fi-128GB-Silver-6th-Generation?fnode=fdc6d8cf9a3a5596bf835118bf66d1c5629f169110e3c66008a511ee595b8dd45b4d55beb5e42e007c3cc2538e1432961e205bee33610351fa200165b97bfb12c52b24b5670f39ef2da2bb4482e95ada'  # noqa: E501
        assert product.price == decimal.Decimal('389.00')
        assert product.previous_price == decimal.Decimal('449.00')
        assert product.savings_price == decimal.Decimal('60.00')

    def test_product_mac(self):
        """
        Tests the specific product page.
        """
        resource = pkgutil.get_data(
            'tests',
            'it_mac.html')

        page = io.BytesIO(resource).read().decode('UTF-8')

        products = parse_products(page)
        assert len(products) == 82

        product = products[0]
        print(product)
        assert product.name == 'iMac 21,5" ricondizionato con Intel Core i5 dual-core a 2,3GHz'
        assert product.price == decimal.Decimal('1139.00')
        assert product.previous_price == decimal.Decimal('1349.00')
        assert product.savings_price == decimal.Decimal('210.00')
