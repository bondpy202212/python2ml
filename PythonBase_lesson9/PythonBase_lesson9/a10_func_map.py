
values = [2, 3, 4, 5, 10, 7]
for square in map(lambda x: x ** 2, values):
    print(square)
print()

print('for Python 2.0')
print(map(lambda x: x + 1, values)) # for python 2.0
print()

print('for Python 3.0')
print(list(map(lambda x: x + 1, values))) # for python 3.0
