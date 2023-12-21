
class Reversed1(object):    

    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.sequence[self.index]
        self.index -= 1
        #yield value
        
        return value



def main():
    my_list1 = [1, 2, 3, 4, 9, 8]
    for i in Reversed1(my_list1):
        print(i)


if __name__ == '__main__':
    main()





#class Reversed(object):

#    def __init__(self, sequence):
#        self.sequence = sequence
#        self.index = len(sequence) - 1

#    def __iter__(self):
#        return self

#    def __next__(self):
#        if self.index < 0:
#            raise StopIteration

#        value = self.sequence[self.index]
#        self.index -= 1

#        return value


#def main():
#    my_list = [1, 2, 5, 7, 9]
#    for i in Reversed(my_list):
#        print(i)


#if __name__ == '__main__':
#    main()
