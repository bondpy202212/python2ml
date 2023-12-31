



class MyList(object):
    

    class _ListNode(object):
        
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        
        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        
        self._length = 0
        
        self._head = None
        
        self._tail = None

        
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        

        
        node = MyList._ListNode(element)

        if self._tail is None:
           
            self._head = self._tail = node
        else:
            
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        return self._get_node_by_index(index).value

    def __iter__(self):
        return MyList._Iterator(self)

    def clear(self):
        

        node = self._head
        while node is not None:
            next_node = node.next
            del node
            node = next_node

        self._head = self._tail = None
        self._length = 0

    def insert(self, index, value):
        

        if index < 0:
            index += len(self)

        if index < 0:
            index = 0
        if index > len(self):
            index = len(self)

        if index == len(self):
            self.append(value)
        else:
            node = MyList._ListNode(value)

            place = self._get_node_by_index(index)

            left = place.prev

            if left is not None:
                left.next = node
            else:
                self._head = node

            place.prev = node

            node.prev = left
            node.next = place

            self._length += 1

    def _get_node_by_index(self, index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node

    def pop(self, index=None):
        

        if index is None:
            index = len(self) - 1

        node = self._get_node_by_index(index)

        value = node.value

        left = node.prev
        right = node.next

        if left is not None:
            left.next = right
        else:
            self._head = right

        if right is not None:
            right.prev = left
        else:
            self._tail = left

        del node 

        self._length -= 1

        return value


def main():
    my_list = MyList([1, 2, 5])
    print(my_list)    

    my_list.clear()
    print(my_list)

    my_list.append(3)
    my_list.insert(0, 2)
    my_list.insert(1, 5)
    print(my_list)

    my_list.pop(1)
    print(my_list)

    my_list.pop()
    print(my_list)

    #my_list.pop()
    #print(my_list)


if __name__ == '__main__':
    main()
