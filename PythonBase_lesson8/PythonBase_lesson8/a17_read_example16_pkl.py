
import pickle

with open('data/example16.pkl', 'rb') as data:
    people = pickle.load(data)

print(people)