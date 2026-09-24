class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, position):

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for i in range(position - 1):
            if current is None:
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


students = LinkedList()

students.append("Ali")
students.append("Sara")
students.append("Zara")
students.append("Ahmed")

students.insert_at_position("Hina", 2)

students.display()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 def delete_at_position(self, position):

    # Delete the head
    if position == 0:
        if self.head is not None:
            self.head = self.head.next
        return

    current = self.head

    # Move to the node before the target
    for i in range(position - 1):
        if current is None:
            return
        current = current.next

    # Check that target exists
    if current is None or current.next is None:
        return

    # Skip the target node
    current.next = current.next.next