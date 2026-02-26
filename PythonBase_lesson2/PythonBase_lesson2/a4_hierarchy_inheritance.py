
class Base(object):
    def method(self):
        print(("Method class:", __class__.__name__))
        print("instance class:", type(self).__name__)


class Child(Base):
    pass


if __name__ == "__main__":
    base_instance = Base()
    base_instance.method()

    child_instance = Child()
    child_instance.method()