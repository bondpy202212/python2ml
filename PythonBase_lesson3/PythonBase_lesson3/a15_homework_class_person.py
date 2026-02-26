
class Person:
    
    def __init__(self, name_p=None, secondname_p=None, company_p=None, year_p=None):
        self.name_p         = name_p
        self.secondname_p   = secondname_p
        self.company_p      = company_p
        self.year_p         = year_p

        #if name_p.count(' ') != 1:
        #    warnings.warn('Name format may be incorrect')
        #    print()
        if ' ' in self.name_p:
            print('----------------------------')
            print("Name format may be incorrect!")
            print()
        if ' ' in self.secondname_p:
            print('----------------------------')
            print("Secondname format may be incorrect!")
            print()
        if ' ' in self.company_p:
            print('----------------------------')
            print("Name company format may be incorrect!")
            print()
        if ' ' in self.year_p:
            print('----------------------------')
            print("Year format may be incorrect!")
            print()
      


    ## getter
    def get_person(self):
        return self.name_p, self.secondname_p, self.company_p, self.year_p


    ### setter
    #def set_person(self, new_name, new_secondname, new_company, new_year):
    #    self.name_p         = new_name
    #    self.secondname_p   = new_secondname
    #    self.company_p      = new_company
    #    self.year_p         = new_year
      

def main1():
    year_from       = None    
    company_list    = []
    company_list.append(('name', 'secname', 'company', 0))
    print(company_list)

    while True:
        choise1 = input("Enter your choise:\n\
        1. Add person\n\
        2. Enter year from print person\n\
        3. Print list person\n\
        4. Quit\n\
        -> ")
        
        try:
            choise1 = int(choise1)
        except ValueError as error:
            print()
            print(error)
            print()
            choise1 = None

        if choise1:
            if choise1 == 1:
                while True:
                    name_per    = input("Enter name person: ")
                    secname_per = input("Enter secondname person: ")
                    comp_per    = input("Enter name company: ")
                    year_1      = input("Enter year: ")
        
                    try:
                        year_1 = int(year_1)
                    except ValueError as error:
                        print()
                        print("Enter intiger year!")
                        print()
                        year_1 = None
                        
                    if name_per and secname_per and comp_per and year_1:
                        break
                    else:
                        print("Enter correct data!")
                        print()
                #person_in = Person('name', 'secondname', 'company', 'year')
                year_2 = str(year_1)
                person_in = Person(name_per, secname_per, comp_per, year_2)
                z = person_in.get_person()               
                company_list.append(z)
                #print(company_list)

            elif choise1 ==2:
                year_from = input("Enter year: ")
                try:
                    year_from = int(year_from)
                except ValueError as error:
                    print()
                    print(error)
                    print()
                    choise1 = None


            elif choise1 == 3:
                if year_from:
                    for first, second, third, fourth in company_list:   
                        if  fourth == 0:
                            fourth1 = 'year'
                            print('|', first, '\t', '\t|', second, '\t', '\t|',
                            third, '\t', '\t|', fourth1, '\t', '\t|', sep='')
                            print()

                        if int(fourth) >= year_from:
                            if fourth == 0:
                                fourth = 'year'
                            print('|', first, '\t', '\t|', second, '\t', '\t|',
                             third, '\t', '\t|', fourth, '\t', '\t|', sep='')
                            print()
                else:
                    for first, second, third, fourth in company_list:
                        if fourth == 0:
                                fourth = 'year'
                        print('|', first, '\t', '\t|', second, '\t', '\t|',
                                third, '\t', '\t|', fourth, '\t', '\t|', sep='')
                        print()


            elif choise1 == 4:
                break
            else:
                print("Inccorect choise!!!")

    #print(name_per, secname_per, comp_per, year_1)



if __name__ == '__main__':
    main1()


#person_in = Person('name', 'secondname', 'company', 'year')
#print(person_in.get_person())
#person_1 = Person('alex', 'bright', 'samsung', '2001')
#print(person_1.get_person())


    #    def print_list(self): 
    #    list_new = []
    #    for i in self.list1:
    #        if i == 'BMW':
    #            #list_1 = ['1. BMW', 2015, 10000]
    #            #print(list_1)
    #            bmw = Car1('BMW', 2015, 10000)
    #            bmw1 = (bmw.take_car())
    #            #print(bmw1)
    #            list_new.append(bmw1)


    #      # getter
    #def get_temperature(self):
    #    print("Getting value ...")
    #    return self._temperature

    ## setter
    #def set_temperature(self, value):
    #    print("Setting value ...")
    #    if value < -273.15:
    #        raise ValueError("Temperature below -273.15 is not possible")
    #    self._temperature = value
    
    ## deleter
    #def del_temperature(self):
    #    self._temperature = None

    ## creating a property object
    #temperature = property(get_temperature, set_temperature)