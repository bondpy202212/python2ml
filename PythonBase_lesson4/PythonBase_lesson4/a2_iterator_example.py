
class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


iterable = SimpleIterable()
for value in iterable:
    print(value)


iterator = iter(iterable)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration as error:
    print(error)

