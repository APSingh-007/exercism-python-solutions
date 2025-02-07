class Node:
    def __init__(self, value, next):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self.simple_ll = []
        for value in values:
            self.push(value)

    def __len__(self):
        return len(self.simple_ll)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index == len(self) - 1:
            raise StopIteration
        self.index += 1
        return self.simple_ll[len(self) - 1 - self.index].value()

    def head(self):
        if not self.simple_ll:
            raise EmptyListException("The list is empty.")
        return self.simple_ll[-1]

    def push(self, value):
        next = self.simple_ll[-1] if self.simple_ll else None
        self.simple_ll.append(Node(value, next))

    def pop(self):
        if not self.simple_ll:
            raise EmptyListException("The list is empty.")
        return self.simple_ll.pop(-1).value()

    def reversed(self):
        return LinkedList([node.value() for node in self.simple_ll[::-1]])

    def tail(self):
        if not self.simple_ll:
            raise EmptyListException("The list is empty.")
        return self.simple_ll[0]


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
