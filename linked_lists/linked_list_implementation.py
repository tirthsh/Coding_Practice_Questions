class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

linked_list_obj = LinkedList()
node1 = Node(1)
node2 = Node(2)