filename = 'data\example5.txt'

with open(filename) as data:
    lines = data.readlines()

lines.insert(1, '+ inserted_line\n')


with open(filename, 'w') as date:
    date.writelines(lines)


