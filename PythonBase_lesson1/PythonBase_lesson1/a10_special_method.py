
class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == "secret_field" and self.password == "9ea)fc":
            return "Secret value"
        else:
            return object.__getattribute__(self, item)

obj = MyObject()
print(obj.password)
### print(obj.secret_field)  - ERROR, haven't' this attribut
obj.password = "9ea)fc"
print(obj.secret_field)