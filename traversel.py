class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


coach1 = Node("Coach 1")
coach2 = Node("Coach 2")
coach3 = Node("Coach 3")

coach1.next = coach2
coach2.next = coach3


current = coach1

while current is not None:
    print(current.data)
    current = current.next