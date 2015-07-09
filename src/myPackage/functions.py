import json
import re     # this module is used to replace some symbols to whitespace
from collections import defaultdict
from myPackage import classes


# This function decodes products list from JSON object to Python object
def Product_json_reader(x):
    return classes.Product(x["product_name"], x["manufacturer"], x.get("family", ""), x["model"], x["announced-date"])

# This function decodes listing  from JSON object to Python object
def Listing_json_reader(x):
    return classes.Listing(x["title"], x["manufacturer"],  x["currency"], x["price"])

# ===========================================================

def read_prducts_file(file_name):
    #with open(Products_file, "r") as f:
    #    x = [ json.loads(row) for row in f ]
    #print x[0]['model']
    products_dic = defaultdict(list)     # {'KEY=MANUFACTURER': [Val0='PRODUCT_NAME', Val1='FAMILY' , Val2='MODEL'] }
    with open(file_name, "r") as f:
        for row in f:
            x = json.loads(row, object_hook = Product_json_reader)
            products_dic[x.manufacturer].append([x.product_name,x.family,x.model])
    return products_dic

# ===========================================================
def read_listings_file(file_name, manufactur_list):
    listings_dic = defaultdict(list)     # {'KEY=MANUFACTURER': Val=TITLE }
    with open(file_name, "r") as f:
        for row in f:
            x = json.loads(row, object_hook = Listing_json_reader)
            for manuP in manufactur_list:
                if match_manufactuer(manuP,x.manufacturer):
                    x.manufacturer = manuP
                    listings_dic[x.manufacturer].append(x.title) 
    return listings_dic

# ===========================================================

def match_manufactuer(Prod, Listing): 
    x = Prod.lower().split()
    y = Listing.lower().split()
    if [ m for m in y if m in x ]:
        return True
    else:
        return False
    
# ===========================================================

def test_match(P, L):  
    title = re.sub(r'[^\w]', '', L).lower()#.split()  # Remove any character that is not alphanumeric
    model = re.sub(r'[^\w]', '', P[-1]).lower() #P[-1].lower().replace('-','').split()
    #family = P[1].lower().split()   
    #if [m for m in model if title.find(m) ==0]:
    if title.find(model) ==0:
        return True
    else:
        return False        