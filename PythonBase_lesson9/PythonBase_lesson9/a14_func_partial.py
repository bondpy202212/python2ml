from functools import partial

# partial for position arguments
def add(x, y):
    return x + y

add_to_five = partial(add, 5)
print(add_to_five(3))
print(add_to_five(10))


# partial for named arguments
print_with_comma = partial(print, sep=', ')
print(1, 2, 3)
print_with_comma(1, 2, 3)