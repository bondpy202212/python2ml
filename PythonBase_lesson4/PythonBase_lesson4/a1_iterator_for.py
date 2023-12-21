
list1 = [1, 2, 3, 4, 5]

it = iter(list1)
while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break


print('-------------------')
def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print("Next value received:", value)


my_for(range(10), loop_body)