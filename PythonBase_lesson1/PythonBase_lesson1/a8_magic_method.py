
string = "a string"
print(str(string))
print(repr(string))
print(string)
print() 


class Complex:
    def __init__(self, real=0.0, inaginary=0.0):
        self.real = real
        self.inaginary = inaginary

    def __repr__(self):
        return "Complex({}, {})".format(self.real, self.inaginary)

    def __str__(self):
        return "{}{:+d}i".format(self.real, self.inaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.inaginary + other.inaginary)

    def __neg__(self):
        return Complex(-self.real, - self.inaginary)

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return (self.real ** 2 + self.inaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.inaginary == other.inaginary

c = Complex(2, -5)
print('1)__str__ ()')
print(c)
print('2)__repr__ ()')
print(Complex(2, -8))
print()

print('3)__add__ (+)')
print(Complex(2, 3) + Complex(2, -1))
print()

print('4)__sub__ (-)')
print(Complex(2, 3) - Complex(1, 1))
print()

print('5)__neg__ (+ -> -)')
print(-(Complex(2, 3) - Complex(1, 1)))
print()

print('6)__abs__ (| |)')
print( abs(Complex(2, 3)) )
print()

print('7)__eq__ (==, !=)')
number1 = Complex(2, 3)
number2 = Complex(2, 3)
number3 = Complex(4, 5)
print(number1 is number2)
print(number2 is number3)
print(number1 is number3)
print(number1 == number2)
print(number1 != number2)
print(number1 == number3)
print(number1 != number3)