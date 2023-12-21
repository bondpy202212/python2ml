
#def add(x, y):
#    return x + y

def add(x):
    def do_add(y):
        return x + y
    return do_add

print(add(5)(3))
print()

print('--currying--')
add_to_five = add(5)
print(add_to_five(4))
print(add_to_five(10))
