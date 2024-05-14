import pymongo
import pandas as pd
from pymongo import MongoClient
from faker import Faker
import random
import time
import json
from operator import itemgetter


# Start connection
conn_str = 'mongodb+srv://root:root@cluster0.ij81hqc.mongodb.net/test'
client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

# Get mongodb data
myDB = client['Amazone']
Prod_rating_col = myDB["Product_rating"]
customer_col = myDB['Customer']
product_col = myDB['Products']

myDB.Product_rating.create_index('Customer_ID')

product_rating = myDB.Product_rating

    

customer_d = {}

count= 0
for i in range(1,20+1): # For each customer
    prod_data = Prod_rating_col.find({'Customer_ID':i})
    current_cus_l = []
    product_d = {}
    for document in prod_data:
        current_cus_rating = document['Product_rating']
        current_prod_id = document['Product_ID']
        if current_prod_id not in product_d:
            product_d[current_prod_id] = [current_cus_rating]
            continue

        else:
            product_d[current_prod_id].append(current_cus_rating) 

    prods = {}
    ratings = {}
    for key in product_d:
        sum_rating = int(sum(product_d[key])/len(product_d[key]))
        prods[key] = sum_rating

    chose_p = dict(sorted(prods.items(), key = itemgetter(1), reverse = True)[:2])
    
    customer_d[i] = list(chose_p.keys())

    customer_data = customer_col.find({'Customer_ID': i})
    product_id_1 = customer_d[i][0]
    product_id_2 = customer_d[i][1]
    product_data1 = product_col.find({'Product_id': product_id_1})
    for m in product_data1:
        recommended_product_1 = {
            "Product_ID": product_id_1,
            "Name": m["Detail"]["Name"],
            "Average_customer_rating": prods[product_id_1],
            "Price": m['Detail']['Price']
        }
    
    product_data2 = product_col.find({'Product_id': product_id_2})
    for b in product_data2:
        recommended_product_2 = {
            "Product_ID": product_id_2,
            "Name": b["Detail"]["Name"],
            "Average_customer_rating": prods[product_id_2],
            "Price": b['Detail']['Price']
        }
    print(myDB["Customer"].update_one({
        "Customer_ID": i
    }, {
        "$set": {
            "Recommended_Products":[ 
                recommended_product_1,
                recommended_product_2
                ]
        }
    }))
    