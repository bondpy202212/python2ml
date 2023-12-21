
## 1)
#try:
#    try:
#        raise ValueError
#    except ZeroDivisionError:
#        print('divisioon by zero')
#except AttributeError:
#    print('attribute error')

#print('-------------------------')
#print('  -1) == 2)-  ')



## 2)
#def do_stuff():
#    try:
#        raise ValueError
#    except ZeroDivisionError:
#        print('divisioon by zero')


#try:
#    do_stuff()
#except AttributeError:
#    print('attribute error')


###print('-------------------------')
##print('  -3) !=  1), 2)-  ')
## 3)
#def do_stuff():
#    try:
#        raise ValueError
#    except ZeroDivisionError:
#        print('divisioon by zero')


#try:
#    do_stuff()
#except ValueError:
#    print('value error')


#print('-------------------------')
#print('  - -  ')
# 4)
def do_stuff():
    try:
        raise ZeroDivisionError
    except ZeroDivisionError:
        print('divisioon by zero')

try:
    do_stuff()
except ValueError:
    print('value error')