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


# Create Linked List
students = LinkedList()

students.append("Ali")
students.append("Sara")
students.append("Zara")
students.append("Ahmed")


# Display the list
current = students.head

while current is not None:
    print(current.data)
    current = current.next
    