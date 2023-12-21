
print(list())
print([])
print([1, 2, 3, 4,])
print([x ** 2 for x in range(5)])
print(list(range(10)))
print('-1-')
print()

x = [6, 8, 5, 7, 2]
y = x.copy()
print(x)
x.sort()
print(x)
y.reverse()
print(y)
x.sort(reverse = True)
print(x)
print('-2-')
print()


z = ['jhklsdf', 'asd', 'bfdfs']
print(z)
z.sort()
print(z)
print('-3-')
print()

z = ['jhklsdf', 'asd', 'bfdfs','.', 'Bsd', 'Adsdsd', ',']
z1 = z.copy()
print(z)
z.sort()
print(z)
print('-4-')
print()

print(ord('A'))
print(ord('a'))
print('-5-')
print()

numbers = [5, 3, -2, 0, -1]
numbers.sort()
print(numbers)
numbers.sort(key=abs)
print(numbers)
print('-6-')
print()

print(z1)
print(z)
z1.sort(key=str.lower)
print(z1)
print('-7-')
print()