from functools import reduce 

#values = [4, -3, 2, 5, -5, -6, -0.3, 0.2, 0.5]
values = [1, 2, -3]
product = reduce(lambda x, y: x * y, values)
print(product)
