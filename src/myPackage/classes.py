

class Product:
    def __init__(self, product_name, manufacturer, family, model, announced_date):
        self.product_name = product_name 
        self.manufacturer = manufacturer    #.replace(' ','')
        self.family = family
        self.model = model
        self.announced_date = announced_date        
        
class Listing:
    def __init__(self, title, manufacturer, currency, price):
        self.title = title    # This line is used to replace symbols '-' or '_' with whitespace #String// description of product for sale
        self.manufacturer = manufacturer
        self.currency = currency         
        self.price = price              

class Result:
#A file full of Result objects is what your solution will be generating. 
#A Result simply associates a Product with a list of matching Listing objects.
    def __init__(self, product_name, listings):
        self.product_name = product_name     #String   
        self.listings = listings             #Array[Listing]
