
print([0] * 5)
print('*' * 20)
print('*+ '.join(['a', 'b', 'c']))
print([[1] * 3] * 4)
print('-1-')
print()

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))

#print_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix = [[0] * 5] * 5
print_matrix(matrix)
print('-2-')
print()

matrix[1][3] = 1
print_matrix(matrix)
print('-3-')
print()

print(matrix[0] is matrix[1])
print(id(matrix[0]))
print(id(matrix[1]))
print('-4-')
print()

matrix = [[0] * 5 for _ in range(5)]
print_matrix(matrix)
print('-5-')
print()

matrix[1][3] = 1
print_matrix(matrix)
print('-6-')
print()