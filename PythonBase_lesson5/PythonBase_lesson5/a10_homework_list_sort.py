
# add only one number
my_list = []
while True:
    print("""Enter numbers and print sort list:
    1. enter number
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
            x = float(input("Enter number: "))
            print()            
        except ValueError as error:
            print(error)
        my_list.append(x)

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