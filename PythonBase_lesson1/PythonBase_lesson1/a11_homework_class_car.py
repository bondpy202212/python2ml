
''''
class Car1 for create car's in list CarShop
'''''
class Car1:
    def __init__(self, name_car='', year_car='', price_car=''):
        self.name_car = name_car
        self.year_car = year_car
        self.price_car = price_car

    def print_car(self):
        print('|', self.name_car, '|', self.year_car, '|', self.price_car)        
        print()

    def take_car(self):
        return self.name_car, self.year_car, self.price_car




class CarShop:
    
    def __init__(self, list1):
        self.list1 = list1

    def print_list(self): 
        list_new = []
        for i in self.list1:
            if i == 'BMW':
                #list_1 = ['1. BMW', 2015, 10000]
                #print(list_1)
                bmw = Car1('BMW', 2015, 10000)
                bmw1 = (bmw.take_car())
                #print(bmw1)
                list_new.append(bmw1)
            elif i == 'OPEL':
                #list_2 = ["2. OPEL", 2020, 8000]
                #print(list_2)
                opel = Car1("OPEL", 2020, 8000)
                opel1 = (opel.take_car())
                #print(opel1)
                list_new.append(opel1)
            elif i == 'BMW2':
                #list_3 = ['3. BMW2', 2015, 10000]
                #print(list_3)
                bmw2 = Car1('BMW2', 2015, 12000)
                bmw21 = (bmw2.take_car())
                #print(bmw21)
                list_new.append(bmw21)
            #print(i)
        
        #print(list_new)
        
        exit = ''
        while exit != 'y':
            print("Last cars in the shop:")
            count0 = 1
            if list_new != []:
                for first, second, third in list_new:                
                    print(count0, first, second, third)
                    count0 += 1
            else:
                print('-0-')

            change = int(input("""change : 
            1. to bye the car
            2. quit
            -> """))
            if change == 1:
                enter1 = int(input("Enter number car: "))
                list_new1 = []
                count1 = 0
                for first, second, third in list_new:
                    if enter1 - 1 != count1:
                        list_new1.append((first, second, third))
                    count1 += 1
                #print(list_new1)
                list_new = list_new1
            if change == 2:
                exit = 'y'
               



#bmw = Car1('bmw', 2015, 10000)
#opel = Car1("opel", 2020, 8000)
#bmw2 = Car1('bmw2', 2015, 10000)
#print(bmw.print_car())

list_car = ['BMW', 'OPEL', 'BMW2']
list2 = CarShop(list_car)
list2.print_list()


