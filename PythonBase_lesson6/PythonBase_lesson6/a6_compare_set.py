
print({1, 2, 3} == {3, 2, 1})
print({1, 2, 3} == {3, 2, 5})
print()

print({1, 2, 3} == frozenset({3, 2, 1}) )
print({1, 2, 3} == ({3, 2, 1}) )
print()

print( {1, 2} in {frozenset([1]), frozenset([3, 2]), frozenset([1, 2])} )