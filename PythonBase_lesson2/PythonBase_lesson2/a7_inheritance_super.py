
class Base:
    def method(self):
        print("Base method invoked on", type(self).__name__, 'instance')


class Child(Base):
    def method(self):
        #Base.method(self)
        #super(Child, self).method()
        super().method()
        print("Child method invoked on", type(self).__name__, 'instance')



#base_instance = Base()
#base_instance.method()


child_instance = Child()
child_instance.method()

Base.method(child_instance)