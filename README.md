# Refurbished

Python packace to access the products information available on the Apple Certified Refurbished section of the Apple Store.

# Example

```Python
>>> from refurbished import Store
>>> store = Store('it')
>>>
>>> store.get_ipads(model='ipad_pro_97')
>>> for ipad in ipads:
...   print(ipad.price, ipad.name)
...
589.00 iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Grigio siderale
589.00 iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Argento
679.00 iPad Pro 9,7" Wi-Fi 128GB ricondizionato - Oro rosa
809.00 iPad Pro 9,7" Wi-Fi + Cellular 128GB ricondizionato - Oro rosa
809.00 iPad Pro 9,7" Wi-Fi + Cellular 128GB ricondizionato - Grigio siderale
809.00 iPad Pro 9,7" Wi-Fi + Cellular 128GB ricondizionato - Argento
899.00 iPad Pro 9,7" Wi-Fi + Cellular 256GB ricondizionato - Oro rosa
899.00 iPad Pro 9,7" Wi-Fi + Cellular 256GB ricondizionato - Grigio siderale

>>>
>>> ipads = store.get_ipads(model='ipad_pro_97', connectivity='wi_fi')
>>> for ipad in ipads:
...   print(ipad.price, ipad.name)
...
589.00 iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Grigio siderale
589.00 iPad Pro 9,7" Wi-Fi 32GB ricondizionato - Argento
679.00 iPad Pro 9,7" Wi-Fi 128GB ricondizionato - Oro rosa

``` 