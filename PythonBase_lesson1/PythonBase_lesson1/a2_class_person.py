
#class Person:
#    pass


#john = Person()
#john.name = "John"
#john.age = 22

#lucy = Person()
#lucy.name = "Lucy"
#lucy.age = 21

#print(john.name, "is", john.age)
#print(lucy.name, "is", lucy.age)
#print()







#class Person:
#    def print_info(self):
#        print(self.name, "is", self.age)


#john = Person()
#john.name = "John"
#john.age = 22

#lucy = Person()
#lucy.name = "Lucy"
#lucy.age = 21

##Person.print_info(john)
##Person.print_info(lucy)
##print()

#john.print_info()
#lucy.print_info()
#print()






class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


john = Person("John", 22)
lucy = Person("Lucy", 21)

john.print_info()
lucy.print_info()
print()