from data import products, people, list_1_to_10


# new_list =list(map(lambda x: x*2,list_1_to_10)) map

# new_list =[x*2 for x in list_1_to_10] list compression

# prices=list(map(lambda p:p['price'],products)) find prices of products

""" Rising prices from dictionary
def raise_price(prices):
    prices['price'] = round(prices['price'] * 1.05,2)
    return prices

new_prices = (map(raise_price, products))
for price in new_prices:
    print(price)
"""

"""Iterating names
names = map(lambda n: n['name'], people)
for name in names:
    print(name)
"""
