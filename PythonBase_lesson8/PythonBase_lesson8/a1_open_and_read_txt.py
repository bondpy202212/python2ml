
# it's not correct "/"
###
#example_file = open('data/example1.txt')
#print(example_file.read())
#print()
#example_file.close()


import os.path

file_name = os.path.join('data', 'example1.txt')
example_file = open(file_name)
print(example_file.read())
print()
example_file.close()


# context manager - is the best way for open file