import json
from collections import defaultdict
from myPackage import classes


# This function decodes products list from JSON object to Python object
def Product_json_reader(x):
    return classes.Product(x["product_name"], x["manufacturer"], x.get("family", ""), x["model"], x["announced-date"])

# This function decodes listing  from JSON object to Python object
def Listing_json_reader(x):
    return classes.Listing(x["title"], x["manufacturer"],  x["currency"], x["price"])


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


def read_listings_file(file_name):
    listings_dic = defaultdict(list)     # {'KEY=MANUFACTURER': Val=TITLE }
    with open(file_name, "r") as f:
        for row in f:
            x = json.loads(row, object_hook = Listing_json_reader)
            listings_dic[x.manufacturer].append(x.title) 
    return listings_dic

def match(family_model_list, title_list):
    matched_list = defaultdict(list)
    for m  in family_model_list:
        product_name = m[0]
        family = m[1]
        model  = m[2]
        for k in title_list:
            #print m , '====='
            if (family in k and model in k):
                #print 'pass xxxxxxxxx'
                matched_list[product_name].append(k)
    return matched_list