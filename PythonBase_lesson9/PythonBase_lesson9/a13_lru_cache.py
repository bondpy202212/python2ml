from functools import lru_cache

#def fibonacci(n):
#    if n == 1 or n == 2:
#        return 1
#    else:
#        return fibonacci(n - 1) + fibonacci(n - 2)

#print(fibonacci(10))

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(1, 40):
    print(fibonacci(i))