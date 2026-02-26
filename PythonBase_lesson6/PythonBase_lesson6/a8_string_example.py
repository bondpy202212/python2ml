## found vowels in string

vowels = {'a', 'e', 'o', 'u', 'i', 'y'}
string = input("Enter a string: ")

print('\n'.join(vowels.intersection(string)))
