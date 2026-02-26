
phonebook = { 'Guido': '832-43-18', 'Mary': '123-80-24'}
print(phonebook)
phonebook['Key'] = '123-89-89'
phonebook['Ron'] = '156-88-71'
print(phonebook)
print('------- 1 -----------')
print()

print(phonebook.keys())
print(phonebook.values())
print(phonebook.items())
print('------- 2 -----------')
print()

print(list(phonebook.keys()))
print(list(phonebook.values()))
print(list(phonebook.items()))
print('------- 3 -----------')
print()

for name, number in phonebook.items():
    print(name + "'s number is", number)
print('------- 4 -----------')
print()


people = phonebook.keys()
print(people)
phonebook['Linda'] = '234-99-56'
print(phonebook)
print(people)

del phonebook['Linda']
print(people)
print('------- 5 -----------')
print()

print(people & {'Key', 'Ron', 'ale', 'ollive'})
print('------- 6 -----------')
print()


first_phonebook = phonebook
second_phonebook = { 'Guido': '832-43-18', 'Mary': '123-80-24'}
print(first_phonebook)
print(second_phonebook)
print()

print(first_phonebook.keys() & second_phonebook.keys())