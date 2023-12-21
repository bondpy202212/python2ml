from collections import deque, namedtuple

## deque - extract fomr iterable[number, -1]
## namedtuple - return subtuple with name "..."

def Getback(iterable, number):
    
    return deque(iterable, number)



Text = 'asdfsadfsdgsadgf'
Text = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Getback(Text, 5))
print('--------------------------------')
print()


Point = namedtuple('point_000', ['x', 'y'])
print(Point.__name__)
#print(type(Point))
p = Point(10, y = 20)
#print(type(p))
print(p[0])
print(p[1])
print('---1---')

x1, y1 = p
print(x1)
print(y1)
print('---2---')
print()

print(x1 - y1)
print(p)
print(p.x)
print(p.y)
