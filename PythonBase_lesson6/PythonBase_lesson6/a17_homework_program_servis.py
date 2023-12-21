def my_func1():

    #file_path = os.path.join('data', 'hw_data_base_links.txt')
    file_path = 'hw_data_base_links.txt'
    dict1= {}
    try:
        with open(file_path, 'r') as my_dict0:
            for tems in my_dict0:
                key1 = tems[: tems.index(' ')]
                value1 = tems[tems.index(' '):-1]
                #print(key1)
                #print(value1)
                dict1[key1] = value1
    except FileNotFoundError as error:
        print('File not found!!!')


    #dict1 = {}

    #name1 = 'server1'
    #link1 = 'http://'

    #print(dict1)
    #dict1.update({name1:link1})
    #print(dict1)

    while True:
        print("""
        Servis saved 'Name link' and 'Link'.
        1. Enter name link and link. 
        2. Print dictionary link.
        3. Print link (by name).
        4. Delet link (by name).
        5. Exit.
        """)

        choice = None
        try:
            choice = int(input('Enter your choice: '))
        except ValueError as error:
            print('Inccorect entered!!!\n', error)
    

        if choice in range(1,6):
            if choice == 1:
                try:
                    name_link = str(input('Enter "Name link": '))
                    link = 'http:\\' + str(input('Enter "link" (http:\\): '))
                except ValueError as error:
                    print(error)
                dict1.update({name_link : link})

            elif choice == 2:
                print('Name link : Link\n'
                      '----------------')
                for name_link, in_link in dict1.items():
                    print('{}\t : {}'.format(name_link, in_link))

            elif choice == 3:
                name1 = str(input('Enter name link for print: '))
                if name1:
                    if dict1.get(name1):
                        print()
                        print('Link for name "{}" is:\n {}'.format(name1, dict1.get(name1)))
                        print()
                    else:
                        print()
                        print("Link's list haven't link for name {}".format(name1))
                        print()

            elif choice == 4:
                name2 = str(input('Enter name link for delete: '))
                if name2:
                    if dict1.get(name2):
                        print()
                        choice2 = str(input('Delete link {1} for name "{0}"\n'
                              'enter "y/n" '.format(name2, dict1.get(name2))))
                    
                        if choice2 == 'y' or choice2 == 'n':
                            if choice2 == 'y':                           
                                #dict1.update({name2 : None})
                                dict1.pop(name2)

                            elif choice2 == 'n':
                                pass
                        else:
                            print('Inccorect enter "y/n')
                        print()
                    else:
                        print()
                        print("Link's list haven't link for name {}".format(name2))
                        print()

            elif choice == 5:
                break

            else:
                print("- Inccorect entered!!!! -")
            

        else:
            print()
            print("-- Inccorect entered!!!! --")
            print()
    #######################################
    #print(dict1)
    with open(file_path, 'w') as my_dict:
        for lines in dict1.items():
            my_dict.write('{} {}\n'.format(lines[0], lines[1]))
    #######################################

if __name__ == '__main__':
    my_func1()



########################################
#file_path = os.path.join('data', 'hw_24_examp_dict.txt')
#with open(file_path, 'w+') as my_dict:
#    for lines in dic1.items():
#        my_dict.write('{} {}\n'.format(lines[0], lines[1]))

#dict0 = {}
#try:
#    with open(file_path, '+') as my_dict0:
#        for tems in my_dict0:
#            key1 = tems[: tems.index(' ')]
#            value1 = tems[tems.index(' '):-1]
#            #print(key1)
#            #print(value1)
#            dict0[key1] = value1
#except ValueError as error:
#    print('File not found!!!')
########################################