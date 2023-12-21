
def function(x, *args):
    print(x)
    print(type(args))
    print(args)

function(2, 3, 5)
print()



def mean(first, *numbers):
    sum_ = first + sum(numbers)
    return sum_ / (len(numbers) + 1)
print(mean(2, 3, 4, 4, 15))
print(mean(2))
print(mean(0))
print(mean(-3, -2))
print()



values = [2, 3, 4, 5, 5, 6]
print(values)
print(*values)
print(*values, sep=', ')