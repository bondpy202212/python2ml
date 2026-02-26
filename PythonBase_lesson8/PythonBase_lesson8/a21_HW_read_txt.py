import os.path

file_path = os.path.join('data', 'hw_20.txt')
list1 = []

with open(file_path, 'r') as data0:
    for int1 in data0:
        list1.append(float(int1))
    print('Count random numbers: {}'.format(len(list1)))
    print('Sum random numbers: {}'.format(sum(list1)))
    #print(list1)
