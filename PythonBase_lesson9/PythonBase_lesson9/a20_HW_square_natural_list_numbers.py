


start = -100
finish = 20
values = range(start, finish)

list_natural = list(filter(lambda x: x > 0, values))
even_numb = list(filter(lambda x: x % 2 == 0, list_natural))
odd_numb = list(filter(lambda x: x % 2 != 0, list_natural))
square_numb = list( map(lambda x: pow(x, 2), odd_numb) )

print('Natural numbers from {} to {}:'.format(start, finish))
print(list_natural)
print('Even numbers:')
print(even_numb)
print('Add numbers:')
print(odd_numb)
print('Squares odd numbers:')
print(square_numb)

