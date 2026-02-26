
class A:
    def method(self):
        print("Method A")


class B(A):
    pass


class C(A):
    def method(self):
        print("Method C")


class D(A):
    def method(self):
        print("Method D")

class E(B, C, D):
    pass


def main():
    obj = E()
    obj.method()
    print()

    print("Method resolution order:")
    for cls in [A, B, C, D, E]:
        print(cls.__name__ + ":", cls.mro())
        print("'object' is  in class", cls.__name__ + ":", isinstance(obj, cls))

        print(cls.__name__, "is  in class A:", issubclass(cls, A))
        print()

    print()
    

if __name__ == "__main__":
    main()
    
    
