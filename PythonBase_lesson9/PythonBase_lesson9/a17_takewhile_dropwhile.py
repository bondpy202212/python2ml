from itertools import takewhile, dropwhile

values =[1, 4, 3, 5, 3, 2, 8]
predicate = lambda x: x < 5

for elem in takewhile(predicate, values):
    print(elem)
print()


for elem in dropwhile(predicate, values):
    print(elem)