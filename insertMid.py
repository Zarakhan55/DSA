class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


coach1 = Node("Coach 1")
coach2 = Node("Coach 2")
coach4 = Node("Coach 4")

coach1.next = coach2
coach2.next = coach4


# Create new node
coach3 = Node("Coach 3")

# Insert Coach 3 between Coach 2 and Coach 4
coach3.next = coach2.next
coach2.next = coach3


# Traverse the linked list
current = coach1

while current is not None:
    print(current.data)
    current = current.next