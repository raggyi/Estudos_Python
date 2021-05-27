from data import products, people, list_1_to_10

# new_list = list(filter(lambda x: x > 5, list_1_to_10)) with filter

# new_list = [x for x in list_1_to_10 if x>5] with List Comprehension

""" Selecting products over 50 with filter and lambdas

products_over50 = filter(lambda p:p['price'] > 50, products)
for product in products_over50:
    print(product)
"""

"""Selecting products over 50 with functions and filter

def filter_over50(product) :
    if product['price'] > 50 :
        return True
        
products_over50=filter( filter_over50, products )
for product in products_over50 :
    print( product )

"""


