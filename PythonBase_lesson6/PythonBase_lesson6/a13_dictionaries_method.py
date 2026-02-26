
phonebook = { 'Guido': '832-43-18', 'Mary': '123-80-24'}

print(len(phonebook))

print('Guido' in phonebook)
print(phonebook['Guido'])
print('Ron' in phonebook)
print('----- 1 ---------')
print()

print(phonebook.get('Ron'))
print(phonebook.get('Ron', '000-00-00'))
print(phonebook.get('Guido', '000-00-00'))
print('----- 2 ---------')
print()

print(phonebook)
print(phonebook.setdefault('Mary', '000-00-00'))
print(phonebook.setdefault('Ron', '000-00-00'))
print(phonebook)
print('----- 3 ---------')
print()

phonebook['Ron'] = '123-45-02'
print(phonebook)
phonebook['Jack'] = '342-26-78'
print(phonebook)
print('----- 4 ---------')
print()

del phonebook['Jack']
print(phonebook)
print('----- 5 ---------')
print()

copybook = phonebook.copy()
print(copybook)
print('----- 6 ---------')
print()

newbook = dict.fromkeys(['Mary', 'Jack', 'Linda'], '123-45-98')
print(newbook)
print('----- 7 ---------')
print()

print(phonebook)
ron = phonebook.pop('Ron')
print(ron)
print(phonebook)
print('----- 8 ---------')
print()

delitem = phonebook.popitem()
print(delitem)
print(phonebook)
print('----- 9 ---------')
print()

phonebook.update(Mary='125-89-74', Jack='854-64-35')
print(phonebook)
print('----- 10 ---------')
print()

phonebook.update({'A1': '145-08-09', 'G2': '159-86-45'})
print(phonebook)
print('----- 11 ---------')
print()

phonebook.update([('Michael', '234-20-48'), ('Linda', '156-09-56')] )
print(phonebook)
print('----- 12 ---------')
print()

phonebook.clear()
print(phonebook)
print('----- 13 ---------')
print()

print(newbook)
