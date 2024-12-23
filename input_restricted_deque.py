# input_restricted_deque.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class InputRestrictedDeque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None

    def enqueue_at_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue_at_beginning(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def dequeue_at_end(self):
        if self.is_empty():
            return None
        else:
            if self.head.next is None:
                value = self.head.data
                self.head = None
                self.tail = None
                return value

            temp = self.head
            while temp.next.next:  
                temp = temp.next
            value = temp.next.data 
            self.tail = temp  
            self.tail.next = None  
            return value

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next