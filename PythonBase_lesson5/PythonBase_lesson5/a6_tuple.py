
print(type(()))
print(type( (1,) ))
print( tuple(range(5)) )
x = 1, 2, 'xgdsf'
print(type(x))
print('-1-')
print()

print( (1, 2) * 5 )
print('-2-')
print()

cities = ('K1', 'London', 'Kvibek')
populations = (10000, 12400, 17500)
x1 = zip(cities, populations)
print(type(x1))
x1 = list(x1)
print(x1)
print('-3-')
print()

z1 = enumerate(cities)
z2 = list(z1)
print(z2)
print('-4-')
print()

z3 = enumerate(cities, 1)
z4 = list(z3)
print(z4)
print('-5-')
print()

a, b, c = 1, 2, 3
print('a, b, c = 1, 2, 3')
print(a)
print(b)
print(c)
print('-6-')
print()

a, b, c = 'fgh'
print('a, b, c = "fgh" ')
print(a)
print(b)
print(c)
print('-7-')
print()

head, *tail = range(10)
print(head)
print(tail)
print('-8-')
print()

*head, tail = range(10)
print(head)
print(tail)
print('-9-')
print()

first, second, *midle, tail = range(10)
print(first)
print(second)
print(midle)
print(tail)
print('-10-')
print()

x = 5
y = 2
x, y = y, x
print(x, y)
print('-11-')
print()

values = [5, 2, 1, 4, 8]
for index, value in enumerate(values):
    print('values[{}] = {}'.format(index, value))
print()

for city_number, city in enumerate(cities, 1):
    print('City', city_number, 'is', city)
print()
    