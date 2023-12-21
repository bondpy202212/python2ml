
def check_instance(obj, cls):
    return cls in type(obj).mro()

def check_subclass(child, base):
    return base in child.mro()


print(check_instance(8, int))
print(check_instance(8, str))
print(check_instance(True, int))
print(check_instance("", object))
print('-------------------------- 1)')

print(check_subclass(bool, int))
print(check_subclass(bool, object))
print(check_subclass(bool, str))
print(check_subclass(bool, bool))
print('-------------------------- 2)')




def check_instance2(obj, cls):
    return check_subclass(type(obj), cls)

print(check_instance2(8, str))
print(check_instance2(8, int))
print(check_instance2(8, object))
print('-------------------------- 3)')

def check_subclass(child, base):
    if child == base:
        return True
    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)
    return False

print(check_subclass(bool, int))
print(check_subclass(bool, str))
print(check_subclass(bool, object))
print(check_subclass(bool, bool))
print('-------------------------- 4)')



print(isinstance(8, int))
print(isinstance(8, object))
print(isinstance(8, str))
print(isinstance(True, int))
print(isinstance(True, object))
print('-------------------------- 5)')

print(issubclass(bool, bool))
print(issubclass(bool, int))
print(issubclass(bool, object))
print(issubclass(bool, str))
print('-------------------------- 6)')

print(isinstance(object, type))
print(isinstance(int, type))
