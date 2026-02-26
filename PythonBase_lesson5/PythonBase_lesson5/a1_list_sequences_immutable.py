
values = [5, 8, 2, 1, 9, 2, 7, 4]
print(values)

print(values[1])
print(values.__getitem__(1))

print(slice(2, 5))
print(values[2:5])
print(values.__getitem__(slice(2, 5)))
print('-------------------')
print()

print('1) x in [....]')
print('-------------------')
values1 = [1, 2, 5]
print(2 in values1)
print(values.__contains__(2))
print(2 not in values1)
print(not values.__contains__(2))
print('-------------------')
print()

print('2) str1 + str2')
print('-------------------')
print('Hello, ' + 'world')
print([1, 2] + [4, 5])
print('-------------------')
print()

print('3) [...] * n')
print('-------------------')
print([1, 0] * 5)
print('* ' * 10)
print('-------------------')
print()

print('4) s[i]')
print('-------------------')
values = [5, 8, 2, 1, 9, 2]
print(values[1])
print(values.__getitem__(1))
print('-------------------')
print()

print('5) s[i:j]')
print('-------------------')
print(slice(2, 5))
print(values[2:5])
print(values.__getitem__(slice(2, 5)))
print('-------------------')
print()

print('6)len[i:j]')
print('-------------------')
print(values)
print(len(values))
print('-------------------')
print()

print('7) s.index(x[,i[,j]])')
print('-------------------')
values = [5, 8, 2, 1, 9, 2, 7, 4]
print(values)
print(values.index(2))
print(values.index(2, 3))
#print(values.index(2, 6))
print(values.index(8, 0, 4))
print('-------------------')
print()

print('8) s.count(x)')
print('-------------------')
print(values)
print(values.count(2))
print(values.count(10))
print('-------------------')
print()