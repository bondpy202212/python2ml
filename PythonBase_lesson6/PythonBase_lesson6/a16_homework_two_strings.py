
string01 = 'asdfdsagdsagadsf'
string02 = 'asddwwergerhrg'

string1 = set(string01)
string2 = set(string02)

#print(string1 & string2)

# intersection
str_intsect = string1 & string2

print('str first:', string01)
print('str second:', string02)
print('this string has next simbol:')
for i in str_intsect:
    print(i)