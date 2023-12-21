
#try:
#    raise ZeroDivisionError
#finally:
#    print('finally block 1')
#    print()


#try:
#    pass
#finally:
#    print('finally block 2')
#    print()


def fn():
    try:
        return
    finally:
        print('finally block 3')


fn()