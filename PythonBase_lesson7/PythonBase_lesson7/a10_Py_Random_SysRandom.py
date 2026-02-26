import random

print(random.Random)

obj = random.Random()
print(obj.randint(1, 100))
print()

rnd = random.SystemRandom()
print(rnd.random())
print()

