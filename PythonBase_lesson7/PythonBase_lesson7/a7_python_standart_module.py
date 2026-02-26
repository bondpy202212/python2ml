
import copy

class Container:
    def __init__(self):
        self.list = [1, 2, 3]
        self.number = 8

obj = Container()

print(obj.list)
print()

obj_copy = copy.copy(obj)
obj_copy.list.append(4)
print(obj.list)
print(obj_copy.list)
print()

obj2 = Container()
print(obj2.list)
print()

obj2_copy = copy.deepcopy(obj2)
obj2_copy.list.append(8)
print(obj2_copy.list)
print(obj.list)