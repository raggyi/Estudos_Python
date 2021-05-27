from functools import reduce
from data import products, people, list_1_to_10


"""Accumulator with For
accumulator=0
for numbers in list_1_to_10:
    accumulator += numbers
print(accumulator)

"""
"""Accumulator with Reduce
sum_list=reduce(lambda ac, i: i+ac, list_1_to_10, 0)
print(sum_list)

"""
"""Dictionary's Accumulator with Reduce
sum_prices=reduce(lambda ac, p: p['price'] + ac, products, 0)
print(sum_prices) sum
print(sum_prices/len(products)) media

"""