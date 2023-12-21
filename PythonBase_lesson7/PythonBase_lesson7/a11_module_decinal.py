
print(0.1 + 0.2)

from decimal import Decimal
print(Decimal(0.1) + Decimal(0.2))
print(Decimal('0.1') + Decimal('0.2'))
print()

print(2 ** 0.5)
print(Decimal('2') ** Decimal('0.5'))
print()

print(Decimal(1) / Decimal(3))
print('-----------------------')
print()



from fractions import Fraction

print(Fraction(1, 3))
print(Fraction(5, 8) * Fraction(1, 3) - Fraction(17, 28))
print(Fraction(1, 2) + Fraction(1, 2))
print(Fraction(4, 2) ** Fraction(1, 2))
print(Fraction(2, 3) ** Fraction(9, 3))


