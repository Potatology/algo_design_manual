class Node:
    def __init__(self, item, next=None):
        self.item = item  # data item
        self.next = next  # point to successor


class ListIterator:
    def __init__(self, head: Node):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            x = self.current.item
            self.current = self.current.next
            return x


class List:
    """
    Linked list-based container implementation.
    """

    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def __contains__(self, x):
        return self.search(x) is not None

    def search(self, x) -> Node:
        p = self.head

        while p is not None and p.item != x:
            p = p.next

        return p

    def insert(self, x) -> None:
        self.head = Node(x, self.head)

    def delete(self, x) -> None:
        pred = None
        p = self.head

        while p is not None and p.item != x:
            pred = p
            p = p.next

        if p is not None:
            if pred is None:
                self.head = p.next
            else:
                pred.next = p.next
            p.next = None

    def __iter__(self):
        return ListIterator(self.head)

    def print(self) -> None:
        for x in self:
            print(x, end=' '),
        print()
