# output_restricted_deque.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OutputRestrictedDeque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None

    def enqueue_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def enqueue_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue_at_beginning(self):
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