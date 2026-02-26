
# first - emumerationg dictionaty keys

my_dict0 = dict(one = 1, two = 2, three = 3)
my_dict1 = {'one_a' : 0.1, 'two_b' : 0.2, 'three_c' : 0.3 }
my_dict2 = [('one_01', 0.01), ('two_02', 0.02), ('three_03', 0.03)]
my_dict2 = dict(my_dict2)

print(my_dict0)
print(my_dict1)
print(my_dict2)
print('-- 1 --')
print()


# iteration dictionaries element (my_dict0, my_dict1, my_dict2)
# -----------------------------------
for key in my_dict0:
    print(key, '->', my_dict0[key])
print('-- 2 --')
print()

for key in my_dict1.keys():
    print(key, '->', my_dict1[key])
print('-- 3 --')
print()

for key, value in my_dict2.items():
    print(key, '->', value)
print('-----------------------------------')
print('-- 4 --')
print()

keys = ['one10', 'two20', 'three30']
dict1 = dict.fromkeys(keys,0)
print(dict1)
print(my_dict0)
my_dict0.update(one='1.0')
print(my_dict0)
print('-----------------------------------')
print('-- 5 --')
print()

for key, value in reversed(my_dict0.items()):
    print(key, '->', value)
print('-----------------------------------')
print('dict.move_to_end -> not found this metod for dict')
print('--6 --')
print()
# -----------------------------------
# -----------------------------------
print('-----------------------------------')
print()


from collections import OrderedDict
dict_ordered1 = OrderedDict()
dict_ordered1['one_1'] = 0.001
dict_ordered1['two_2'] = 0.002
dict_ordered1['three_3'] = 0.003
print(dict_ordered1)
dict_ordered1.update(one_1=1.0)
print(dict_ordered1)
print('-----------------------------------')
print('-- 7 --')
print()

dict_ordered1.move_to_end('one_1')
print(dict_ordered1)
print('-----------------------------------')
print('-- 8 --')
print()
dict_ordered1.move_to_end('one_1', last=False)
print(dict_ordered1)
print('-----------------------------------')
print('-- 9 --')
print()

print(dict_ordered1.popitem())
print(dict_ordered1)
print('-- 10 --')
print()

dict_ordered1.update(three_3=3)
print(dict_ordered1)
print('-----------------------------------')
print('-- 11 --')
print()

print(dict_ordered1.popitem(last=False))
print(dict_ordered1)
print('-----------------------------------')
print('-----------------------------------')
print('-- 12 --')
print()


let_1 = dict(a = 1, b = 2, c = 3)
let_2 = dict(b = 2, a = 1, c = 3)
print(let_1 == let_2)


let_01 = OrderedDict(a = 1, b = 2, c = 3)
let_02 = OrderedDict(b = 2, a = 1, c = 3)
print(let_01 == let_02)
