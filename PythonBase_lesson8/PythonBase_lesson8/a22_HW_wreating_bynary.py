import os.path
import random
import array

file_path = os.path.join('data', 'hw_22.bin')

numbers = [random.randint(-100000, 100000) for _ in range(10)]
print(numbers)

numbers_array = array.array('i', numbers)
#print(numbers_array)

with open(file_path, 'wb') as binary_file:
    binary_file.write(numbers_array)

