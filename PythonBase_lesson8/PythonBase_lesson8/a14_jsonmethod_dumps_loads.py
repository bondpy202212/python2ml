
import json

my_dict = {'first_field': True, 'second_field': None}

print_1 = json.dumps(my_dict)
print(print_1)
print()

print(json.loads(print_1))