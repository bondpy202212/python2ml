
import array
import random

numbers = [random.randint(-1000000000, 1000000000)
          for _ in range(1000)]
print(len(numbers))
print(numbers)

with open('data\example7.txt', 'w') as text_file:
    for number in numbers:
        text_file.write('{}\n'.format(number))



numbers_array = array.array('i', numbers)

with open('data/example7.bin', 'wb') as binary_file:
    binary_file.write(numbers_array)