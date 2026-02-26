from functools import lru_cache

fib_n = 20

@lru_cache(maxsize = None)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#        print(fibonacci(i))
list_fib = []
def fib_numb(n):
    for i in range(1, n):
        list_fib.append(fibonacci(i))
    return list_fib
print(fib_numb(fib_n))



def decorator_even_numbers(generator):
    def decorated_sequence(*args):
        seq = generator(*args)
        return filter(lambda x: x % 2 == 0, seq)
    return decorated_sequence

list_fib = []
@decorator_even_numbers
def fib_numb(n):
    for i in range(1, n):
        list_fib.append(fibonacci(i))
    return list_fib
print(list(fib_numb(fib_n)))