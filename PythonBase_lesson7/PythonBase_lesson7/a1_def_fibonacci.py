
def fibonacci_sequence():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second

#f = fibonacci_sequence()
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))

def fibonacci(limit):
    generator = fibonacci_sequence()
    for _ in range(limit):
        yield next(generator)

def nth_fibonacci(number):
    result = None
    for current in fibonacci(number):
        result = current
    return result

#print(nth_fibonacci(1))
#print(nth_fibonacci(2))
#print(nth_fibonacci(3))
#print(nth_fibonacci(4))
#print(nth_fibonacci(5))


if __name__ == '__main__':
    print('Running Fibonacci tests...')
    assert nth_fibonacci(1) == 1
    print(nth_fibonacci(1) == 1)
    assert nth_fibonacci(2) == 1
    assert nth_fibonacci(3) == 2
    assert nth_fibonacci(4) == 3
    assert nth_fibonacci(5) == 5
    print('End fibonacci tests.')



