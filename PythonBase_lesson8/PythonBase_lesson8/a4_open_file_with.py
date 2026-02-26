
import os.path

file_name = os.path.join('data', 'example1.txt')

with open(file_name) as file:
    print(file.read())
    print()

#example_file = open(file_name)
#print(example_file.read())
