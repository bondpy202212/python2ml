import random
import asyncio


#@asyncio.coroutine
#def produce():
async def produce():
    while True:
        await asyncio.sleep(0.5)
        #yield from asyncio.sleep(0.5)
        data = random.randint(1, 100)
        return data


#@asyncio.coroutine
#def consume():
async def consume():
    sum_ = 0
    count = 0

    while True:
        ##data = yield
        #data = yield from produce()
        data = await produce()
        print('Got data:', data)

        sum_ += data
        count += 1

        print('Sum:', sum_)
        print('Average:', sum_ / count)
        print()

# another task for example paralel potok
@asyncio.coroutine
def another_task():
    while True:
        print()
        print('Hello from another task!')
        print()
        yield from asyncio.sleep(2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [consume(), another_task()]
    loop.run_until_complete(asyncio.wait(tasks))