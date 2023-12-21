from itertools import product, chain

#for i in range(1, 5):
#    for j in range(1, 5):
#        print('{} x {} = {}'.format(i, j, i * j))

for i, j in product(range(1, 5), range(1, 5)):
    print('{} x {} = {}'.format(i, j, i * j))
print()

for i in chain(range(1, 5), range(1, 5)):
    print(i)