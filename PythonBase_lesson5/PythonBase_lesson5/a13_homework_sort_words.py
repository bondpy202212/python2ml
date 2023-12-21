
list_x = []
x = str()

while True:

    print(''''Sort text!
    1. Enter text.
    2. print word.
    3. clear text.
    4. quit.
    ''')
    choice1 = input('Enter your choice: ')

    if choice1 == '1':
        x = input('Enter text for sorting: ')

    elif choice1 == '2':
        if x:
            list_x = (x.split())

            #for i in list_x:
            #    print(i)

            list_x2 = enumerate(list_x, 1)
            print()
            for first, word2 in list_x2:
                print('You {} word: {}'.format(first, word2))
            print()
        else:
            print(list_x)

    elif choice1 == '3':
        list_x.clear()
        x = str()

    elif choice1 == '4':
        break

    else:
        print('you need enter choce!')

