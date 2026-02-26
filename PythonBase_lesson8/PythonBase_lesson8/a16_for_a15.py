import pickle
from a15_module_pickle_for_binary_data import Person

john = Person('John', 29)
melissa = Person('Melissa', 24)
Person.make_siblings(john, melissa)

#print(john, melissa)

with open('data/example16.pkl', 'wb') as data:
    pickle.dump((john, melissa), data)
