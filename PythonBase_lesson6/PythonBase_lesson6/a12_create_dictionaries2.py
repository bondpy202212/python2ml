
first_way = {'one':1, 'two':2, 'three':3}
print(first_way)
print()

second_way = dict(one=1, two=2, three=3)
print(second_way)
print()

third_way = [('one', 1), ('two', 2), ('three', 3)]
print(dict(third_way))
print()

#@ classmethod
#fourth_way
dict1 = {}
dict1.fromkeys(range(10))
print(dict1)
print(len(dict1.items()))

