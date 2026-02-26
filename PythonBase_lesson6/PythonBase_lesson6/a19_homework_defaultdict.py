
from collections import defaultdict

s = [('red', 1), ('blue', 5), ('red', 6), ('blue', 8), ('red', 17)]
d1 = defaultdict(list)

for k, v in s:
    d1[k].append(v)

print(sorted(d1.items()))
print('-- 1 --')
print()


s2 = 'sdfgdsgdfsgsdgdfsg'
d2 = defaultdict(int)
for k in s2:
    d2[k] += 1

print(sorted(d2.items()))
