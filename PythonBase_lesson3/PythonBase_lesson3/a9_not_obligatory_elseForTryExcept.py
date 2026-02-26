# from a3
Max_Stars = 30
Width = 80


def print_result(number):
    if number ==0:
        stars_count = Max_Stars
    else:
        stars_count = round(Max_Stars / number)
        if stars_count > Max_Stars:
            star_count = Max_Stars

    number_field_width = Width - 2 * stars_count
    stars = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'
    
    print(fmt.format(stars, number))

def main():
    while True:
        try:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))
            result = first_number / second_number
            #print_result(result)
            #break
        except (ValueError, ZeroDivisionError) as error:
            print('Error', error)
            print('Please try again')
        else:
            print_result(result)
            break

if __name__ == '__main__':
    main()
