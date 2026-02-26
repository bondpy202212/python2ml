
print("Calculator")

#a = 10
#b  = 0

# 1)
try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
except Exception as error:
    print(error)
    print(type(error))
except ZeroDivisionError:
    print("---division by zero--- 1)")
print()


# 2)
try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
except ZeroDivisionError:
    print("---division by zero--- 2)")
except Exception as error:
    print(error)
    print(type(error))
print()

 


## 3)
try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
except ZeroDivisionError:
    print("---division by zero--- 3)")
except ValueError as error:
    print(error)
    print(type(error))
print()



# 4)
try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
except (ZeroDivisionError, ValueError) as error:
    print(error)
    print(type(error))

print('Stopping the calculator.  4)')
