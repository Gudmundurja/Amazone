import pandas as pd

from faker import Faker
import random
import time
import json
import math
from datetime import datetime
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

#data = json.loads('Bakey_json.txt')
#df = pd.json_normalize()
#bakery_df = pd.read_json('Bakey_json.txt')

with open("Books_json.txt", "r") as book, open("drink_json.txt", "r") as drink, open("Bakey_json.txt", "r") as bakery, open("CD_json.txt", "r") as CD_d, open("Fruits_veg_json.txt", "r") as FV_d, open("Home_appliance_json.txt", "r") as HA_d, open("Mobile_phones_json.txt", "r") as MP_d:
     drink_df = json.load(drink)
     books_df = json.load(book)
     bakery_df = json.load(bakery)
     cd_df = json.load(CD_d)
     fv_df = json.load(FV_d)
     ha_df = json.load(HA_d)
     mp_df = json.load(MP_d)
     

B=2

current_order_storage = []
customer_count = 1
order_count = 1
#order_date = #random_date("1/1/2022", "31/12/2022", random.random())

def create_ordered_items():
    other_prod_types = {"CD":cd_df, "Book":books_df, "Home Appliance":ha_df, "Mobile phones":mp_df}
    fresh_prod_types = {"Fruits and vegetables": fv_df, "Drinks":drink_df, "Bakery":bakery_df}


    other_prods = ["CD", "Book", "Home Appliance", "Mobile phones"]
    fresh_prods = ["Fruits and vegetables", "Drinks", "Bakery"]
    n_items = random.randint(1,7)

    quantity = random.randint(1,10)
    current_cust_list = []
    order_price = 0
    order_cost = 0
    for m in range(n_items):
        prod_types = random.choice(["Fresh", "Other"])

        
        fresh_product_sel = random.randint(0,4)
        other_product_sel = random.randint(0,9)
        quantity = random.randint(1,10)
        if prod_types == "Fresh":
            choice = random.randint(0,2)
            current_prod_type = fresh_prods[choice]
            current_prod_l = fresh_prod_types[current_prod_type]
            current_product = current_prod_l[fresh_product_sel]

            store_id = random.randint(1,5)
        else:
            choice = random.randint(0,3)
            current_prod_type = other_prods[choice]

            current_prod_l = other_prod_types[current_prod_type]
            current_product = current_prod_l[other_product_sel]
            store_id = 6
        if current_prod_type == 'Home Appliance' or current_prod_type == 'Mobile phones':
            price = current_product['Price']
            cost = current_product['Cost']
        else:
            price = current_product['Details']['Price']
            cost = current_product['Details']['Cost']


        ordered_items = {
                "Product_ID": current_product['Product_id'],
                "Type": current_product['Details']['Type'],
                "Price": price,
                "Quantity": quantity,
                "From_store_or_warehouse": store_id
            }
        order_price += price*quantity
        order_cost += cost*quantity
        current_cust_list.append(ordered_items)
    return current_cust_list, order_price, order_cost 


customer_count = 1
order_count = 1

name_dict = {1: "Tracey Medina", 2: "Diana Hall", 3: "Lisa Navarro", 4: "Scott Taylor",
5: "Philip Davies", 6: "Edgar Brown", 7: "Jason Davilla", 8: "Michele Lopez",
9: "Brandon Jenkins", 10: "Jennifer Esparaza", 11: "Anna Smith", 12: "Jeffrey Neal",
13: "Jessica Snow", 14: "Stephanie Cooper", 15: "Debra Burke", 16: "Shannon Harrison",
17: "Shaun Stone", 18: "Travis Collier", 19: "Richard Rhodes", 20: "Patricia Thomas"
}
address_dict = {1: {
			"House_Number": 80,
			"Street": "Lincoln Square",
			"City": "Manchester",
			"Postcode": "M7Z 5HU"
		}, 2:{
			"House_Number": 40,
			"Street": "Copson Street",
			"City": "Manchester",
			"Postcode": "M6U 2IF"
		}, 3: {
			"House_Number": 52,
			"Street": "Spring Gardens",
			"City": "Manchester",
			"Postcode": "M8H 2WS"
		}, 4: {
			"House_Number": 25,
			"Street": "Hulme Street",
			"City": "Manchester",
			"Postcode": "M60 5CB"
		}, 5: {
			"House_Number": 57,
			"Street": "Portland Street",
			"City": "Manchester",
			"Postcode": "M5V 3RR"
		}, 6: {
			"House_Number": 46,
			"Street": "Copson Street",
			"City": "Manchester",
			"Postcode": "M6U 2IF"
		}, 7: {
			"House_Number": 39,
			"Street": "George Street",
			"City": "Manchester",
			"Postcode": "M8P 4EQ"
		}, 8: {
			"House_Number": 46,
			"Street": "Copson Street",
			"City": "Manchester",
			"Postcode": "M6U 2IF"
		}, 9: {
			"House_Number": 80,
			"Street": "Lincoln Square",
			"City": "Manchester",
			"Postcode": "M2 5LN"
		}, 10: {
			"House_Number": 46,
			"Street": "Copson Street",
			"City": "Manchester",
			"Postcode": "M6U 2IF"
		}, 11: {
			"House_Number": 95,
			"Street": "King Street",
			"City": "Manchester",
			"Postcode": "M4R 1BM"
		}, 12: {
			"House_Number": 39,
			"Street": "Geroge Street",
			"City": "Manchester",
			"Postcode": "M8P 4EQ"
		}, 13: {
			"House_Number": 80,
			"Street": "Oxford Road",
			"City": "Manchester",
			"Postcode": "M2E 2DL"
		}, 14: {
			"House_Number": 25,
			"Street": "Hulme Street",
			"City": "Manchester",
			"Postcode": "M60 5CB"
		}, 15: {
			"House_Number": 52,
			"Street": "George Street",
			"City": "Manchester",
			"Postcode": "M7B 3NX"
		}, 16: {
			"House_Number": 67,
			"Street": "Fountain Street",
			"City": "Manchester",
			"Postcode": "M5P 5HX"
		}, 17: {
			"House_Number": 95,
			"Street": "King Street",
			"City": "Manchester",
			"Postcode": "M4R 1BM"
		}, 18: {
			"House_Number": 40,
			"Street": "Cheetham Hill Road",
			"City": "Manchester",
			"Postcode": "M4U 5ZG"
		}, 19: {
			"House_Number": 95,
			"Street": "King Street",
			"City": "Manchester",
			"Postcode": "M4R 1BM"
		}, 20: {
			"House_Number": 15,
			"Street": "Portland Street",
			"City": "Manchester",
			"Postcode": "M4H 3QF"
		}
}
for i in range(20):
    
    Eta = random.randint(1, 15)
    #order_date = random_date("15/1/2022", "31/12/2022", random.random())
    order_date = datetime.strptime(random_date("15/12/2020", "31/12/2022", random.random()),'%d/%m/%Y')
    order_date = order_date.isoformat()

    for n in range(2):
        current_cust_list, order_price, order_cost = create_ordered_items()
        partner_id = random.randint(1,5)
        Json_past_order = {
            "Order_ID": order_count,
            "Customer_ID": customer_count,
            "Customer_name": name_dict[customer_count],
            "Shipping_address": address_dict[customer_count],
            "Order_date": order_date,
            "Tracking": {
                "Tracking_number": order_count,
                "Status": "Undelivered",
                "Estimated_delivery_time": Eta,
                "Partner_ID": partner_id
            },
            "Ordered_items": current_cust_list,
            "Total_Order_Price": round(order_price, 2),
            "Partner_ID": partner_id,
            "Total_Order_Cost": round(order_cost, 2)
        }
        
        if customer_count == 20:
            customer_count = 0
        customer_count += 1
        order_count += 1
        current_order_storage.append(Json_past_order)
print(current_order_storage)

with open('current_order_new_6.txt', 'w') as f:
  json.dump(current_order_storage, f, ensure_ascii=False)