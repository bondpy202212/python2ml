
def decorator(fn):
    def decorated_fn(*args, **kwargs):
        print('Starting decorated function')
        fn(*args, **kwargs)
        print('End of decorated function')
    return decorated_fn



def print_hello():
    print('Hello!')

print_hello()
print()


print_hello = decorator(print_hello) # == @ decorator
print_hello()
print()



@decorator
def print_hello():
    print('Hello!')

print_hello()