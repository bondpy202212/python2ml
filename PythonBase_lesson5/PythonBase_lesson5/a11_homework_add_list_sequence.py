

# add only one number
my_list = []
while True:
    print("""Enter numbers and print sort list:
    1. enter sequence
    2. print list
    3. quit
    """)
    try:
        change = str(input("Enter your change: "))
    except ValueError as error:
        print(error)

    if change == '3':
        break


    elif change == '1':
        try:
            print()
            x = str(input("Enter sequence (used only 0 <= number and space, comma):\n "))
            print()             
        except ValueError as error:
            print(error)  
            
        for i in x:
           
            if i != ' ':
                my_list.append(i)
     

    elif change == '2':
        print()
        my_list.sort()
        print('Your numbers list:\n', my_list)
        print()

    else:
        print()
        print('You need enter change!!!')
        print()
#print(my_list)
