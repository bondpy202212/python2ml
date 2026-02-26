
#def generator():
#    yield from range(10)
#    yield 'end'


#for value in generator():
#    print(value)


#def generator():
#    yield from (x * 3 for x in range(5))
#    yield 'end'

#for value in generator():
#    print(value)



def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield '[generator]   start'
    yield from subgenerator()
    yield '[generator]   end'

for value in generator():
    print(value)