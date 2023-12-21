
print(set('asdfsa'))
print({'asdf', 'asdf', 'sdg'})
print()

first = input('First string: ')
second = input('Second string: ')

## found first's leters in second string

common = set(first) & set(second)
print('Found', len(common), 'common characters: ')
#print(common)

#for chair in common:
#    print(chair)

print('\n'.join(common))
