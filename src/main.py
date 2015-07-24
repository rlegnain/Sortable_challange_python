from myPackage import functions
from collections import defaultdict
import json


Products_file = "products.txt"
Listings_file = "listings.txt"




        
products_dic = functions.read_prducts_file(Products_file)# {['KEY=MANUFACTURER': [Val0='PRODUCT_NAME',Val1='FAMILY' , Val2='MODEL']] , ....}
manufactur_list = products_dic.keys()

listings_dic = functions.read_listings_file(Listings_file, manufactur_list)# {['KEY=MANUFACTURER': Val=TITLE] , .............}
# listings_dic only contains the matched manufacturer from the Product list. In other words, it ignores the manufacturer that is not in the product list. this way we can reduce the search time.

count_matching_product = 0
Result = defaultdict(list)
for m in manufactur_list:
    title = listings_dic[m]
    product = products_dic[m]
    for L in title:
        for P in product:
            if functions.test_match(P,L):
                #Result["".join(P[0])].append(L)
                Result[P[0]].append(L)
                count_matching_product += 1 

print count_matching_product


with open("Results.txt", "w") as f:
    for prod, title in Result.iteritems():
        x = {"product_name": prod , "listing":title}
        json.dump(x, f)
        f.write('\n')
        #xx = json.dumps(x, ensure_ascii=False, encoding='utf8')
        #f.write(xx)