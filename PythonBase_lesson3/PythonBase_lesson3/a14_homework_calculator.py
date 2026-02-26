
class Calculator(object):
    def __init__(self, x=0.0, y =0.0):
        self.x = x
        self.y = y


    def get_plus(self):
        return self.x + self.y


    def get_minus(self):
        return self.x - self.y


    def get_devision(self):        
        return self.x / self.y


    def get_miltiplication(self):
        return self.x * self.y

    def get_exponential(self):
        return self.x ** self.y



def main():
    while True:
        operation = input("Enter perations(+,-,*,/,**): ")        
        if operation in ['+', '-', '*', '/', '**']:
            break
        else:
            print("You enter incorrect operation, repeat enter.")


    while True:        
        first_n = (input("Enter first number(int or float): "))
        second_n = (input("Enter second number(int or float): "))
        

        try:
            first_n = float(first_n)
            second_n = float(second_n)
        except ValueError as error:
            print()
            print('-> ' + str(error))
            print()

        if type(first_n) in [float, int] and type(second_n) in [float, int]:
            break
        else:
            print("You need enter numbers - first and second, repeat.")


    obj = Calculator(first_n, second_n)
    if operation == '+':
        result = obj.get_plus()
    elif operation == '-':
        result = obj.get_minus()
    elif operation == '*':
        result = obj.get_miltiplication()
    elif operation == '/':
        try:
            result = obj.get_devision()
        except ZeroDivisionError as error:        
            result = None
            print("---", error, "---")
    elif operation == '**':        
        try:
            result = obj.get_exponential()
        except ZeroDivisionError as error:
            result = None
            print("---", error, "---")
    else:
        print("it's incorrect operation!!!")
    
    return result


if __name__ == '__main__':
    res = main()
    print()
    print("You result:\n", res)
    print() 