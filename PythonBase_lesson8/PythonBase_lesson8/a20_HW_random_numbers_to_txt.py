import random
import os.path


x_numb = random.sample(range(0, 100000), 10000)

file_path = os.path.join('data', 'hw_20.txt')

str1=''
with open(file_path, 'w') as data:
    data.write(str1)

with open(file_path, 'a') as data:    
    for xi in x_numb:        
        data.write(str(xi))
        data.write('\n')
print()

print((x_numb))

