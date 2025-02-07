class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def __iter__(self):
        for i in range(self.length):
            if i == 0:
                next_node = self.head
            else:
                next_node = next_node.succeeding
            yield next_node

    def push(self, data: int) -> None:
        if self.length == 0:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data, None, self.tail)
            self.tail.succeeding = new_node

        self.tail = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            raise IndexError("List is empty")

        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        self.length -= 1
        return value

    def delete(self, value: int) -> None:
        for curr_node in self:
            if curr_node.value == value:
                if curr_node != self.head:
                    curr_node.previous.succeeding = curr_node.succeeding
                else:
                    self.head = curr_node.succeeding
                if curr_node != self.tail:
                    curr_node.succeeding.previous = curr_node.previous
                else:
                    self.tail = curr_node.previous
                self.length -= 1
                break
        else:
            raise ValueError("Value not found")

    def shift(self) -> int:
        if self.length == 0:
            raise IndexError("List is empty")
        try:
            value = self.head.value
        except ValueError:
            raise ValueError("Value not found")
        self.delete(value)
        return value

    def unshift(self, value) -> None:
        new_node = Node(value, self.head, None)
        if self.length == 0:
            new_node.succeeding = None
            self.head = self.tail = new_node
        else:
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
