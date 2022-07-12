'''
This code may work in theory. You can't run it, since not all
functions are implemented. XOR linked lists are still a little
confusing to me, but theoretically the logic is there, would
just need to be written in a languge that actually has pointers
or with some magical implementation of the pointers in Python.
'''
def get_pointer(element):
    '''Implementation would get Node at element pointer'''
    return None
def dereference_pointer(element):
    '''Implementation would get pointer of element Node'''
    return None

class Node:
    '''Basic structure of a node'''
    def __init__(self, val, both):
        self.val = val
        self.both = both

class XOR_List:
    def __init__(self, head):
        self.head = head

    def add(self, element):
        '''Add node element to end'''
        self.last().both = get_pointer( \
            dereference_pointer(self.last().both) \
            ^ dereference_pointer(element) \
        )

    def get(self, index):
        '''Get element at index'''
        left = 0
        current = dereference_pointer(self.head.both)
        for i in range(index):
            right = left ^ current
            left = current
            current = dereference_pointer(get_pointer(right).both)
        return get_pointer(right)

    def last(self):
        '''Implementation would return pointer to last element'''
        pass