
class MethodContainer:
    def __init__(self, data):
        self.data = data

    def method(self):
        print('method invode')
        print("data =", self.data)


instance = MethodContainer(8)
print(type(MethodContainer.method))
print(type(instance.method))
print()

print(MethodContainer.method(instance))
instance.method()


