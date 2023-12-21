import pickle
from a18_HW_classStore import Store

AndroidTv1 = Store('BOX x98', 1655)
AndroidTv2 = Store('BOX x96', 1111)
AndroidTv3 = Store('BOX x94', 1285)
AndroidTv4 = Store('BOX x95', 1005)
AndroidTv5 = Store('BOX x91', 1105)

#print(AndroidTv1)
#print()

# writing file.pkl (binary)
with open('data\hw_18.pkl', 'wb') as data1:
    pickle.dump((AndroidTv1, AndroidTv2, AndroidTv3,
                 AndroidTv4, AndroidTv5), data1)


# read file.pkl (binaty)
with open('data/hw_18.pkl', 'rb') as data2:
    products = pickle.load(data2)

print('From pickle file:')
print(products)
print('--------------------------------')
for iprod0 in products:
    print(iprod0)
print()




import json
# writing file.json 
with open('data/hw_18_2.json', 'w') as file1:
    json.dump(products, file1, indent=2, default=Store.to_json1)

# reading file.json
with open('data\hw_18_2.json') as file2:
    products2 = json.load(file2, object_hook=Store.from_json1)

print('From JSON:')
print(products2)
print('--------------------------------')
for iprod in products2:
    print(iprod)
