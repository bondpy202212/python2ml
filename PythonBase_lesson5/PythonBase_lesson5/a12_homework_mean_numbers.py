first = None
second = None

def mean_main(first, *numbers):

    return (first + sum(numbers)) / (len(numbers) + 1)


#print(mean_main(-100, 6))
print(mean_main(1, 2, 3, 4))


x_start = -100
x_finish = 6
print(mean_main(*range(x_start, x_finish + 1)))

