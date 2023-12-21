def main():
    while True:
        try:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))
            print("Result:", first_number / second_number)
            break
        except (ValueError, ZeroDivisionError) as error:
            print('Error', error)
            print('Please try again')


if __name__ == '__main__':
    main()