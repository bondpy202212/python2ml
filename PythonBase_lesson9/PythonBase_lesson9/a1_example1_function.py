# addition
def add(x, y):
    return x + y

# subtraction
def sub(x, y):
    return x - y

# multiplication
def mul(x, y):
    return x * y

# division
def div(x, y):
    return x / y

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
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