

class Xerror:
    def __init__(self, x1 = 0):
        self.x1 = x1
        #if x1 == '01':
        #    print()
        #    print("It's my except: x_error 1")
        #    print()


    def get_atr(self):
        return  "It's my except: x_error 2"



def main():
    while True:
        x = (input('Enter "01": '))
        if type(x) == str:
            if x == '01':                
                obj = Xerror(x)
                message = obj.get_atr()
                ### Exception
                if message == "It's my except: x_error 2":
                    print()
                    print("{It's his messsage: ", message, '}', sep='')
                    print('->')
                    print("this only bad latter...")
                    print()
                    break
                ### 

                print(message)
                break            
            else:
                print("You don't enter str'01'")
 
               
def main2():
    try:
        obj = Xerror()
        raise Xerror()
    except BaseException as error:
        print(error)



if __name__ == '__main__':
    main()