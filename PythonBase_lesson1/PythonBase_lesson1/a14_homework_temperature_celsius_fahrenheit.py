
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value ...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value ...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value
    
    # deleter
    def del_temperature(self):
        self._temperature = None

    # creating a property object
    temperature = property(get_temperature, set_temperature)


x = Celsius(-17)
print(x.temperature)
print(x.get_temperature())
print(x.to_fahrenheit())
x.set_temperature(50)
print(x.get_temperature())
x.del_temperature()
print(x.get_temperature())
