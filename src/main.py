from myPackage import functions

Products_file = "products.txt"
Listings_file = "listings.txt"




        
products_dic = functions.read_prducts_file(Products_file)# {'KEY=MANUFACTURER': [Val0='PRODUCT_NAME',Val1='FAMILY' , Val2='MODEL'] }
listings_dic = functions.read_listings_file(Listings_file)

for m in products_dic:
    for n in listings_dic:
        if n in m:          # test if manufacturer of listings matches manufacturer of product
            xx = functions.match(products_dic[m],listings_dic[n])
            print xx
            #print n
            #print listings_dic[n][0]
            #print '\n'           