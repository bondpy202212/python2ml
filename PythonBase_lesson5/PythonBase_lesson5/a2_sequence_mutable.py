
values = [5, 8, 2, 1, 9, 2, 7, 4]
values[3] = 42
print(values)
values.__setitem__(2, 41)
print(values)
print('1) .__setitem__')
print()

values[:4] = range(4)
print(values)
print('2) values[:4] = range(4)')
print()

values[-1:] = [5, 5, 5, 5]
print(values)
print('3) values[-1:] = [5, 5, 5, 5]')
print()

values[4:7] = []
print(values)
print('4) values[4:7] = []')
print()

values[4:4] = [0] * 5
print(values)
print(values[4:9])
print('5) values[4:4] = [0] * 5')
print()

values[4:9] = [5, 1, 2]
print(values)
print('6) values[4:9] = [5, 1, 2]')
print()

del values[0]
print(values)
print('7) del values[0]')
print()

del values[:3]
print(values)
print('7) del values[:3]')
print()

values[4:] = [3, 4, 5, 6]
print(values)
print('8) values[4:] = [3, 4, 5, 6]')
print()

del values[::2]
print(values)
print('9) del values[::2]')
print()

values.__delitem__(2)
print(values)
print('10) values.__delitem__(2)')
print()

values.append(2)
print(values)
print('11) values.append(2)')
print()

values.extend(range(3))
print(values)
print('12) values.extend(range(3))')
print()

list_ = values
print(list_ is values)
print(id(list_))
print(id(values))
print('13) copy list(id)')
print()

list_.append('marker')
print(values)
print('14) list_.append("marker")')
print()

del list_[-1]
print(values)
print('15) del list_[-1]')
print()

list_ = values.copy()
print(list_ is values)
print(id(list_))
print(id(values))
print('16) list_ = values.copy()')
print()

print(values)
values.insert(2, -1)
print(values)
print('17) values.insert(2, -1)')
print()

print(values)
values.insert(100, 12)
print(values)
print('17) values.insert(100, 12)')
print()

print(values)
values.insert(-100, -10)
print(values)
print('18) values.insert(-100, -10)')
print()

print(values)
x = values.pop()
print(x)
print(values)
print('19) values.pop()')
print()

print(values)
x = values.pop(3)
print(x)
print(values)
print('20) values.pop(3)')
print()

print(values)
values.remove(1)
print(values)
print('21) values.remove(1)')
print()

print(values)
values.remove(1)
print(values)
print('22) values.remove(1)')
print()

print(list_)
list_.clear()
print(list_)
print('23) list_.clear()')
print()

print(values)
values.reverse()
print(values)
print('24) values.reverse()')
print()