
def generator():
    yield 'helo'
    yield 'world'

print(generator)
print(generator())
print('--------------')

g = generator()
print(g)
print(g.__iter__)
print()
print(next(g))
print(next(g))