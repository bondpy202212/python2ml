import os.path


current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
print("--1) Start path --")
print()

parent_path1 = os.path.dirname(current_path)
print(parent_path1)
print("--2) Parent path1 --")
print()

parent_path2 = os.path.dirname(parent_path1)
print(parent_path2)
print("--3) Parent path2 --")
print()

#parent_path3 = os.path.dirname(parent_path2)
#print(parent_path3)
#print()

modify_path1 = os.path.join(parent_path2, 'PythonBase_lesson6')
modify_path2 = os.path.join(modify_path1, 'PythonBase_lesson6')
print(modify_path2)
print("--4) Parent path2 + 'PythonBase_lesson6' +'PythonBase_lesson6' --")
print()

import sys
sys.path.append(modify_path2)
#print(sys.path)
#print()

from a17_homework_program_servis import my_func1 as func11
#my_funct11() 


    


num_eser = None

while True:
    print("""
    Servis usage users:
    1. Enter number user
    2. Start servis saved 'Name link'
    3. Print number user
    4. Quit
    ---------------------------------
    """)
    

    choice = None
    try:
        choice = int(input('Enter your choice (first -> 1): '))
    except ValueError as error:
        print('Inccorect entered!!!\n', error)
    
    

    if choice in range(1,5) and num_eser or choice== 1 or choice== 4:
        if choice == 1:
            num_eser = input('Enter number user: ')

        elif choice ==2:
            print()
            print('Started servis "Saved Nane link"...')
            print()
            
            #from a17_homework_program_servis import my_func1 as func11
            func11()                      

        elif choice == 3:
            print('Your numbeer is:', num_eser)

        elif choice == 4:
            break
        else:
            print('?????')

    else:
        print('Inccorect choise!!!')
