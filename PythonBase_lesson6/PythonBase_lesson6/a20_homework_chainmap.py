
from collections import ChainMap
first_dict = {'a23': 22, 'a35': 33}
second_dict = {'a11': 12, 'a12': 15}

d = ChainMap(first_dict, second_dict)
print(d)
print()

first_dict['a23'] = 5
print(d)
print()

print(list(d))

print(d)
d.maps.reverse()
print(d)
print()
print(d.maps[0])
print(d.maps[1])
print()

d.maps[0]['a12'] = 27
print(d)
print(first_dict)
print(second_dict)

