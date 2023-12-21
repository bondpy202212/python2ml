
import random
import time

def sleep(seconds):
    start = time.time()
    while time.time() - start < seconds:
        yield



#def produce(consume):
#    while True:
#        yield from sleep(0.5)
#        data = random.randint(1, 100)
#        consume.send(data)

def produce():
    while True:
        yield from sleep(0.5)
        data = random.randint(1, 100)
        return data

def consume():
    sum_ = 0
    count = 0

    while True:
        #data = yield
        data = yield from produce()
        print('Got data:', data)

        sum_ += data
        count += 1

        print('Sum:', sum_)
        print('Average:', sum_ / count)
        print()

# another task for example paralel potok
def another_task():
    while True:
        print()
        print('Hello from another task!')
        print()
        yield from sleep(2)


if __name__ == '__main__':
    consumer = consume()
    #next(consumer)
    #producer = produce(consumer)

    task = another_task()

    while True:
        ###print("next iteration")
        #next(producer)

        next(consumer)
        next(task)