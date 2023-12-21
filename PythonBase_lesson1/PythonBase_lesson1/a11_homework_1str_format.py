
class MyObject1:
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return "string: {:4.2f} and {:4.2f}".format(self.number1, self.number2)

    def __repr__(self): # only from interactive
        return "repr: '{:4.2f}' and '{:4.2f}'".format(self.number1, self.number2)

    @classmethod
    def __bytes__(self):
        return "bytes string: {}, {}".format(self.number1, self.number2)



print("1) redefine __str__")
object1 = MyObject1()
print(object1)

print(MyObject1(1, 2))
print(MyObject1(8, -2))
print(MyObject1(3))
print()

print("2) redefine __repr__ - only from interactive")
x = 5
y = 6
z = MyObject1(x, y)
print(z)
print()


print("3) redefine __bytes__ ")
z = MyObject1.bytes(3)
print(z)
