class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
Implementing a stack = LIFO
pop() -> first item is removed
push() -> item added to the front
'''
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_node):
        tmp = self.head

        if tmp == None:
            self.head = new_node
            return
        
        self.head = new_node
        self.head.next = tmp
            
    def pop(self):
        tmp = self.head

        if tmp == None or tmp.next == None:
            self.head = None
            return
        
        self.head = tmp.next
    
    def print_linked_list(self):
        tmp = self.head
        
        while tmp != None:
            print(str(tmp.data) + " -> ", end="")
            tmp = tmp.next
        
        print("None")
        print()

linked_list_obj = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

linked_list_obj.push(node1)
linked_list_obj.push(node2)
linked_list_obj.push(node3)

linked_list_obj.print_linked_list()

linked_list_obj.pop()

linked_list_obj.print_linked_list()
