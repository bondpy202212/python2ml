
def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        #print(second)
        yield second
        first, second = second, first + second

#f = fibonacci(5)
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))

count = int(input('How many Fibonacci numbers to pritn:'))   
for fib in fibonacci(count):
    #pass
    print(fib)