import pandas as pd

from faker import Faker
import random
import time
import json
import math

product_count = 1
other_list = []
for i in range(1, 40 +1):
    Quantity = random.randint(10,100)


    other_prod_store_warehouse = {
        "Product_ID": product_count,
        "Inventory_in_warehouse":
            {"Warehouse_ID": 6,
            "Quantity": Quantity
            }
        
    }
    product_count += 1
    other_list.append(other_prod_store_warehouse)

with open('other_product_warehouse.txt', 'w') as f:
  json.dump(other_list, f, ensure_ascii=False)