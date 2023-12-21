
# encapsulation 1 (self data: acces control)
class MyObject:
    def __init__(self):
        self.__private_attribute = 42
    def get_private(self):
        return self.__private_attribute

obj = MyObject()
print(obj.get_private())
print()


print(obj._MyObject__private_attribute)
## Error, because Name private atributs
## __atribut -> __atribut + class name "Myobject"
print(obj.__private_attribute)