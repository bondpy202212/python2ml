def main():
    try:
        raise ValueError('value is incorrect 1')
    except ValueError as error:
        print("Exception:", error)
        raise



try:
    main()
except ValueError:
    print('ValueError detected')

print('-----------------------')
#def main():
#    try:
#        raise ValueError('value is incorrect 2')
#    except ValueError as error:
#        print("Exception:", error)
#        raise
#main()