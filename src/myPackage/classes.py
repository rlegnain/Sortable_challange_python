

class Product:
    def __init__(self, product_name, manufacturer, family, model, announced_date):
        """
        Parameter:
        ----------
            title:          String, A unique id for the product
            manufacturer:   String
            family:         String. optional grouping of products
            model:          String
            announced-date: String. ISO-8601 formatted date string, e.g. 2011-04-28T19:00:00.000-05:00
        """
        self.product_name = product_name
        self.manufacturer = manufacturer
        self.family = family
        self.announced_date = announced_date
        self.model = model


class Listing:
    def __init__(self, title, manufacturer, currency, price):
        """
        Parameters:
        -----------
            title:        String. Description of product for sale
            manufacturer: String. who manufactures the product for sale
            currency:     String. currency code, e.g. USD, CAD, GBP, etc.
            price:        String. price, e.g. 19.99, 100.00
        """
        self.title = title
        self.manufacturer = manufacturer
        self.currency = currency         
        self.price = price              


class Result:
    """
    A file full of Result objects is what your solution will be generating.
    A Result simply associates a Product with a list of matching Listing objects.
    """
    def __init__(self, product_name, listings):
        self.product_name = product_name
        self.listings = listings
