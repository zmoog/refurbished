import decimal
import pkgutil
import io
import pprint

from refurbished.parser import parse_products


pp = pprint.PrettyPrinter(indent=4)


class TestParser:

    def test_product_ipad_it(self):
        resource = pkgutil.get_data(
            'tests',
            'it_ipad.html'
        )

        page = io.BytesIO(resource).read().decode('UTF-8')

        products = parse_products(page)
        assert len(products) == 34

        product = products[0]
        assert product.name == 'iPad Wi-Fi 128GB ricondizionato - Argento (sesta generazione)'
        assert product.url == 'https://www.apple.com/it/shop/product/FR7K2TY/A/Refurbished-iPad-Wi-Fi-128GB-Silver-6th-Generation'
        assert product.price == decimal.Decimal('389.00')
        assert product.previous_price == decimal.Decimal('449.00')
        assert product.savings_price == decimal.Decimal('60.00')

    def test_product_mac_it(self):
        resource = pkgutil.get_data(
            'tests',
            'it_mac.html'
        )

        page = io.BytesIO(resource).read().decode('UTF-8')

        products = parse_products(page)
        assert len(products) == 82

        product = products[0]
        print(product)
        assert product.name == 'iMac 21,5" ricondizionato con Intel Core i5 dual-core a 2,3GHz'
        assert product.price == decimal.Decimal('1139.00')
        assert product.previous_price == decimal.Decimal('1349.00')
        assert product.savings_price == decimal.Decimal('210.00')

    def test_product_watch_cn(self):
        resource = pkgutil.get_data(
            'tests',
            'cn_watch.html'
        )

        html = io.BytesIO(resource).read().decode()

        products = parse_products(html)
        assert len(products) == 35

        product = products[0]
        print(product)
        assert product.name == '翻新 Apple Watch Series 3 (GPS),38 毫米深空灰色铝金属表壳搭配黑色运动型表带'
        assert product.price == decimal.Decimal('1269')
        # assert product.previous_price == decimal.Decimal('0')
        # assert product.savings_price == decimal.Decimal('0')

    def test_product_accessories_us(self):
        resource = pkgutil.get_data(
            'tests',
            'us_accessories.html'
        )

        html = io.BytesIO(resource).read().decode()

        products = parse_products(html)
        assert len(products) == 2

        product = products[0]
        print(product)
        assert product.name == 'Refurbished Apple Pencil'
        assert product.price == decimal.Decimal('85.00')
        assert product.previous_price == decimal.Decimal('99.00')
        assert product.savings_price == decimal.Decimal('14.00')
