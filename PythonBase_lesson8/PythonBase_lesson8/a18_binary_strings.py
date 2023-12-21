import pickle

my_dict = {'first_field': True, 'second_field': None}

print_1 = pickle.dumps(my_dict)

print(print_1)

print(pickle.loads(print_1))