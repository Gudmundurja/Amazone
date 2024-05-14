import pymongo
import pandas as pd
from pymongo import MongoClient
from faker import Faker
import random
import time
import json
from operator import itemgetter
import datetime

# Start connection
conn_str = 'mongodb+srv://root:root@cluster0.ij81hqc.mongodb.net/test'
client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)

# Get mongodb data
myDB = client['Amazone']
Carts_col = myDB["Carts"]
Daily_inventory_col = myDB['Daily_Inventory_Level']
fresh_prod_availability = myDB['Fresh_Product_Availability_Tracker']
other_prod_availability = myDB['Other_Product_Warehouse_Storage']

product_col = myDB['Products']
other_prods = ["CD", "Books", "Home Appliances", "Mobile phones"]
fresh_prods = ["Fruits and Vegetables", "Drinks", "Bakery"]

for cart in Carts_col.find():

    status = cart['Status']
    items = cart['items'][0]
    items_in_cart = cart['items'][0]['items_in_cart']
    items = {}
    if status == 'expired':
        for item in items_in_cart:
            if item['Category'] in other_prods:
                cart_quantity = item['Quantity']
                product_id = item['Product_id']
                warehouse_data = other_prod_availability.find({"Product_ID": product_id})
                for p in warehouse_data:
                    current_quant = p['Inventory_in_warehouse']['Quantity']
                myDB['Other_Product_Warehouse_Storage'].update_one({
                    'Product_ID': product_id
                }, {
                    '$set': {
                        'Inventory_in_warehouse': {
                        'Warehouse_ID': 6,
                        'Quantity': current_quant+cart_quantity
                    }}
                })
                Daily_inventory_data = Daily_inventory_col.find({'Product_ID':product_id})
                for k in Daily_inventory_data:
                    daily_inv_q = k['Inventory_measurement ']['Quantity']
                    daily_inv_id = k['Daily_inventory_ID']
                myDB['Daily_Inventory_Level'].update_one({
                    'Daily_inventory_ID': daily_inv_id
                }, {
                    "$set": {
                    "Inventory_measurement ": {
                        'Date': datetime.datetime.now().isoformat(),
                        'Quantity': daily_inv_q + cart_quantity
                    }
        }
    })
            
            else:
                for items in cart['items']:
                    for cart_item in items['items_in_cart']:
                        product_id = cart_item['Product_id']
                        store_data = fresh_prod_availability.find({"Product_ID": product_id})
                        cart_quantity = cart_item['Quantity']
                        for m in store_data:
                            store_quantity = m['Total quantity across stores']
                            Inventory = m['Inventory in store']
                            chosen_store_q = 0
                            count = 0
                            for inventory_item in Inventory:
                                if count == 0:
                                    chosen_store_q = inventory_item['Quantity']
                                count += 1    
                                
                                inventory_quantity = inventory_item['Quantity']
                                
                                if inventory_quantity < chosen_store_q :
                                    chosen_store_q = inventory_quantity
                                    chosen_store_id = inventory_item['Store_ID']
                                else:
                                    continue
                            myDB['Fresh_Product_Availability_Tracker'].update_one({
                                'Product_ID': product_id
                            }, {
                                '$set': {
                                    'Total quantity across stores': store_quantity +cart_quantity
                                }
                            })
                            myDB['Fresh_Product_Availability_Tracker'].update_one({
                                'Product_ID': product_id, 'Inventory in store': {'$elemMatch': {'Store_ID':2}}
                            }, {
                                '$set': {
                                    'Inventory in store.$.Quantity': chosen_store_q + cart_quantity
                                }
                            })


        print(myDB['Carts'].delete_one({'Customer_ID': cart['Customer_ID'],'Status':'expired'}))
            




