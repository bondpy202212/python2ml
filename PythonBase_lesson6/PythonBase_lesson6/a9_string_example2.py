
vowels = {'a', 'e', 'o', 'u', 'i', 'y'}
words = input("Enter a string: ").split(', ')
print(words)

for word in words:
    vowels.intersection_update(word.lower())

print('\n'.join(vowels))