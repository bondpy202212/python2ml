
import array
import os.path

filename = 'data\example7.bin'
# lenght file
filesize = os.path.getsize(filename)
# quately elements
count = filesize // array.array('i').itemsize
# array for numbers
numbers = array.array('i', (0 for _ in range(count)))

with open(filename, 'rb') as binary_file:
    binary_file.readinto(numbers)

#print(numbers)
print(numbers.tolist())