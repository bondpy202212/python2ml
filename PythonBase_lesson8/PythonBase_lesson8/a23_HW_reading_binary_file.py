import array
import os.path

###################################
# reading bynary file

file_path = os.path.join('data', 'hw_22.bin')

file_size = os.path.getsize(file_path) 
count_file = file_size // array.array('i').itemsize
numbers_array = array.array('i', (0 for _ in range(count_file)) )
#print(file_size)
#print(file_size // array.array( 'i').itemsize )
#print(numbers_array)
#print(len(numbers_array))


with open(file_path, 'rb') as binary_file2:
    binary_file2.readinto(numbers_array)

    list_bin = numbers_array.tolist()
    #print(list_bin)
    print('Count random numbers (bin): {}'.format(len(list_bin)))
    print('Sum random numbers   (bin): {}'.format(sum(list_bin)))