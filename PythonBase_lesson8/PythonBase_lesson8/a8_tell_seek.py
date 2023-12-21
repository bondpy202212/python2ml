
#import os
import io
print(io.open is open)
print()

data = io.StringIO('asdf in memory')
print(data.getvalue())
print()

print('--index_start "tell"-- (position)')
print(data.tell())
print()

print('--length_data--')
print(len(data.getvalue()) )
print()

print('--read_date--')
print(data.read())
print('--(position)--')
print(data.tell())
print()

print('--next_read--')
print(data.read())
print()


print('--get_start_position_file')
print(data.seek(0))
print()

print('--write_word--')
print(data.write('data'))
print('--position--')
print(data.tell())
print()

print('--change_in_potok--')
print(data.read())
print()

print('--all_file--')
print(data.getvalue())
print()
