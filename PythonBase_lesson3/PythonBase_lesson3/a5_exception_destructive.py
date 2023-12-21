
class MyObject:
    def __del__(self):
        print(self, "is about to be deleted")


obj = MyObject()
ref = obj
print(id(obj))
del obj         # nathing
print(id(ref))
del ref         # process delet object - ref(obj)
print('----------------------------------------')
print()



class ObjectWithDestructor:
    def __del__(self):
        print('destructor invoked')
        raise Exception


print('Creating object...')
obj = ObjectWithDestructor()

print('Deleting reference...')
del obj

print('Done')