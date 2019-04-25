class Node:
    def __init__(self, item, next=None):
        self.item = item  # data item
        self.next = next  # point to successor


class StackIterator:
    def __init__(self, first):
        self.current = first

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            x = self.current.item
            self.current = self.current.next
            return x


class Stack:
    """
    Implementation of a LIFO stack abstract data type.
    """

    def __init__(self):
        self.first = None  # top of stack
        self.n = 0  # number of stack elements

    def push(self, x):
        self.first = Node(x, self.first)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack underflow')
        else:
            x = self.first.item
            self.first = self.first.next
            self.n -= 1
            return x

    def is_empty(self):
        return self.n == 0

    def __iter__(self):
        return StackIterator(self.first)

    def print(self):
        for x in self:
            print(x, end=' '),
        print()
