from operator import neg, add, sub, mul, truediv


values = [5, 2, 1, 3, 8, -3]
print( list(map(neg, values)) )
# it's == next
print()
print( list(map(lambda x: -x, values)) )
print()


# for a2_example
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
    }

try:
    first = float(input('First number: '))
    operation = input('Operation: ')
    second = float(input('Second number:'))
    result = operations[operation](first, second)
except ValueError:
    print('Incorrect input')
except KeyError:
    print('Usupported operation')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Result:', result)


# for a12_func
from functools import reduce 

values = [4, 5, 2]
product = reduce(mul, values)
print(product)