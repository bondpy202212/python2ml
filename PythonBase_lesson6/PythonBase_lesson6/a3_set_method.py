
first_set = {5, 2, 1, 8, 3, 10}
second_set = {1, 2, 3, 4, 5, 6, 10}

print(first_set)
print(second_set)
print('-------')

print(first_set & second_set)
print(second_set & first_set)

print(first_set.intersection(second_set))
print(second_set.intersection(first_set))
print('--- 1 ---')

print(first_set | second_set)
print(first_set.union(second_set))
print('--- 2 ---')

print(first_set - second_set)
print(second_set - first_set)
print(first_set.difference(second_set))
print(second_set.difference(first_set))
print('--- 3 ---')


print(first_set ^ second_set)
print(first_set.symmetric_difference(second_set))
print('--- 4 ---')
