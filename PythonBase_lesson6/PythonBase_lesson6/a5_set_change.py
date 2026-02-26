
first_set = {5, 2, 1, 8, 3, 10}
second_set = {1, 2, 3, 4, 5, 6, 10}

print(first_set)
print(second_set)
print('-------  1  -------------------')

first_set.add(15)
print(first_set)
print('-------  2  -------------------')

first_set.remove(5)
print(first_set)
#first_set.remove(5)  - error
first_set.discard(5) # - not error
print('-------  3  -------------------')

print(first_set.copy())
print(first_set.pop())
print(first_set)
print(first_set.pop())
print(first_set)
print(first_set.pop())
print(first_set)
print(first_set.clear())
print(first_set)
print('-------  4  -------------------')

first_set.update(second_set)
print(first_set)
print(second_set)
print('-------  5  -------------------')

first_set.intersection_update(range(3, 8))
print(first_set)
print('-------  6  -------------------')

first_set.update({5, 2, 1, 10, 11, 12})
print(first_set)
print('-------  7  -------------------')

first_set.difference_update(second_set)
print(second_set)
print(first_set)
print('-------  8  -------------------')

first_set.update(range(10, 15))
print(first_set)
print(second_set)
first_set.symmetric_difference_update(second_set)
print(first_set)
print('-------  9  -------------------')