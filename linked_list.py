class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_beginning(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        return None

    def remove_at_end(self):
        if not self.head:
            return None
        current = self.head
        if not current.next:
            removed_data = current.data
            self.head = None
            return removed_data
        while current.next:
            prev = current
            current = current.next
        removed_data = current.data
        prev.next = None
        return removed_data

    def remove_at(self, data):
        if not self.head:
            return None
        current = self.head
        if current.data == data:
            removed_data = current.data
            self.head = current.next
            return removed_data
        while current:
            if current.data == data:
                removed_data = current.data
                prev.next = current.next
                return removed_data
            prev = current
            current = current.next
        return None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "List is empty"
