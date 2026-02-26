
print(type({}))
print('-- 1 --')

print({'name': 'John', 'occupation': 'dentist', 'age':32})
print('-- 2 --')

def function(**kwargs):
    print(kwargs)

function(a=8, b=5)
###function(3, 2) # - error
print('named argument.')
print('-- 3 --')


def function2(*args, **kwargs):
    print(args)
    print(kwargs)


function2(2, 5, 6, x=2, z=4)
print('-- 4 --')
print()

print(2, 3, 4, sep = ' --- ', end = '\n+++++\n')
print('-- 5 --')

options = {
    'sep': ' --- ',
    'end': '\n!!!!!!!!\n'
    }
print(options)
print()
print(2, 3, 4, **options)