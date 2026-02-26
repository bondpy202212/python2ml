import os.path

dic1 = {'1': '123123',
        '2': '232323',
        '3': '00000'}




#print(len(dic1.keys()))
#print(dic1.items())
#for lines in dic1.items():
#    print(lines[0])

file_path = os.path.join('data', 'hw_24_examp_dict.txt')
with open(file_path, 'w+') as my_dict:
    for lines in dic1.items():
        my_dict.write('{} {}\n'.format(lines[0], lines[1]))

dict0 = {}
try:
    with open(file_path, 'r+') as my_dict0:
        for tems in my_dict0:
            key1 = tems[: tems.index(' ')]
            value1 = tems[tems.index(' '):-1]
            #print(key1)
            #print(value1)
            dict0[key1] = value1
except ValueError as error:
    print('File not found!!!')

print(dict0)