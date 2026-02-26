from functools import partial
from operator import mul


# use part function
def add_my(x, y):
    return x * y

# use part function
print('--partial function--')
add_to_ten = partial(add_my, 3)
print(add_to_ten(10))
print()
#print()
#print(add_my(3, 2))




# use currying function
def add_my2(x):
    def add_two(y):
        return mul(x, y)
    return add_two

# use currying functioncurrying
print('--currying--')
add_to_five = add_my2(5)
print(add_to_five(4))
