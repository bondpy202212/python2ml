
print({1, 2} < {1, 2, 3})
print({1, 2} <= {1, 2, 3})
print()

print({1, 2, 3} <= {1, 2, 3})
print({1, 2, 3}.issubset({1, 2, 3}))
print({1, 2, 3} < {1, 2, 3})
print()

print({1, 2, 3} >= {1, 2})
print({1, 2, 3} >= {1, 2, 3})
print({1, 2, 3}.issuperset({1, 2, 3}))
print({1, 2, 3} > {1, 2})
print({1, 2, 3} > {1, 2, 3})
print()

print({1, 2, 3}.isdisjoint({1, 2}))
print({1, 2, 3}.isdisjoint({4, 5, 6}))
print()