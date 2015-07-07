import re     # this module is used to replace some symbols to whitespace


class Product:
    def __init__(self, product_name, manufacturer, family, model, announced_date):
        self.product_name = product_name.lower() 
        self.manufacturer = manufacturer.lower()    #.replace(' ','')
        self.family = family.lower()
        self.model = model.lower()
        self.announced_date = announced_date
        #self.model = re.sub('[_|-]', ' ' , self.model)    # This line is used to replace symbols '-' or '_' with whitespace
        
        
class Listing:
    def __init__(self, title, manufacturer, currency, price):
        self.title = re.sub('[_|-]', ' ' , title.lower())    # This line is used to replace symbols '-' or '_' with whitespace #String// description of product for sale
        self.manufacturer = manufacturer.lower() 
        self.currency = currency.lower()         
        self.price = price              

class Result:
#A file full of Result objects is what your solution will be generating. 
#A Result simply associates a Product with a list of matching Listing objects.
    def __init__(self, product_name, listings):
        self.product_name = product_name     #String   
        self.listings = listings             #Array[Listing]
