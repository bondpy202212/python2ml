
# 1)
## for Python3 this is ERROR except
#try:
#    raise ValueError
#except ValueError:
#    raise ZeroDivisionError


# 2)
#print('------------------------')
#print('atribute -  .__context__')
#value_error = ValueError()
#value_error.__context__ = ZeroDivisionError()
#raise value_error


# 3)
#print('------------------------')
#print('atribute -  .__cause__ (operator: raise exceptNew from exceptOld )')
#print('------------------------')
#print()
#value_error = ValueError()
#value_error.__cause__ = ZeroDivisionError()
#raise value_error


# 4)
#print('------------------------')
#print('(operator: raise exceptNew from exceptOld ')
#print('------------------------')
#print()
#raise ValueError from ZeroDivisionError


# 5)
print('exapmle - Python 3')
a = 5
b = 0

try:
    result = a / b
except ZeroDivisionError as error:
    raise ValueError('variable b is incorrect') from error
print()



## 6)
#print('exapmle - Python 2')
#a = 5
#b = 0

#try:
#    result = a / b
#except ZeroDivisionError as error:
#    raise ValueError('variable b is incorrect') from None
