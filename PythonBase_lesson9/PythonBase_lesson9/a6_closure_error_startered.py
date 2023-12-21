#1)
# this's error i = 4
print("1) this's error i = 4")
def make_powers(coung):
    powers = []
    for i in range(coung):
        powers.append(lambda x: x ** i)
    return powers

powers = make_powers(5)
for power in powers:
    print(power(2))
print()

#2)
print('2) function lambda in func lambda (+ value p)')
print('for all program language')
def make_powers(coung):
    powers = []
    for i in range(coung):
        powers.append( (lambda p: lambda x: x ** p)(i) )
    return powers

powers = make_powers(5)
for power in powers:
    print(power(2))
print()


#3)
print('3) for Python')
def make_powers(coung):
    powers = []
    for i in range(coung):
        powers.append( (lambda x, p=i: x ** p) )
    return powers

powers = make_powers(5)
for power in powers:
    print(power(2))
print()


#4)
print('4) for Python(hack Python)')
def make_powers(coung):
    powers = []
    for i in range(coung):
        powers.append( (lambda x, i=i: x ** i) )
    return powers

powers = make_powers(5)
for power in powers:
    print(power(2))
print()
