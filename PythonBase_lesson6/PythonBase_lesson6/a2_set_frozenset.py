
print(set())
print(type(frozenset()))
print()

x = [1, 2, 3, 5, 4]
print(set(x))
print(frozenset(x))
print({1, 2, 3, 4, 5})
print({1, 2, 3, 3, 3})
print()


print( {x ** 2 for x in range(1, 11)} )