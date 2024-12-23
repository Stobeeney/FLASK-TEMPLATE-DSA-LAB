# queue.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next