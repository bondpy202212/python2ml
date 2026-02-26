
def my_generator(sequence):

    index = len(sequence) - 1

    while index >= 0:
        yield sequence[index]
        index -= 1


def main():
    list1 = [0, -1, -2, -3, -5, -6]
    for i in my_generator(list1):
        print(i)


if __name__ == '__main__':
    main()