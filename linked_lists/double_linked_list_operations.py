class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_first(self, new_node):
        tmp = self.head

        if tmp == None:
            self.head = new_node
            return
        
        new_node.next = tmp
        tmp.prev = new_node
        self.head = new_node
    
    def delete_first(self):
        tmp = self.head 

        if tmp == None or tmp.next == None:
            self.head = None
            return

        self.head = tmp.next
        self.head.prev = None

    def insert_last(self, new_node):
        tmp = self.head

        if tmp == None:
            self.head = new_node
            return
        
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = new_node
        new_node.prev = tmp
    
    def delete_last(self):
        tmp = self.head

        if tmp == None or tmp.next == None:
            self.head = None
            return
        
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.prev.next = None
        
    def insert_at_k(self, index, new_node):
        tmp = self.head

        if index > self.length_of_list() or index < 0:
            print("ERROR: Index must be less or equal to length of the list")
            return
        
        if index == 0:
            return self.add_first(new_node)

        curr_index = 0
        while tmp != None:
            if curr_index == index:
                tmp.prev = new_node
                tmp.prev.next = new_node

                new_node.next = tmp
                new_node.prev = tmp.prev
                return
            tmp = tmp.next

    
    def delete_at_k(self):
        pass
    
    def print_forward(self):
        tmp = self.head

        while tmp != None:
            print(str(tmp.data) + " <-> ", end="")
            tmp = tmp.next

        print("None")
        print()

    def print_backward(self):
        pass
    
    def length_of_list(self):
        length = 0
        tmp = self.head

        while tmp != None:
            length += 1
            tmp = tmp.next

        return length 
    

doubly_linked_list_obj = DoublyLinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

doubly_linked_list_obj.add_first(node1)
doubly_linked_list_obj.add_first(node2)
doubly_linked_list_obj.add_first(node3)

doubly_linked_list_obj.print_forward()

# doubly_linked_list_obj.delete_first()
# doubly_linked_list_obj.print_forward()

# doubly_linked_list_obj.insert_last(node4)
# doubly_linked_list_obj.print_forward()

# doubly_linked_list_obj.delete_last()
# doubly_linked_list_obj.print_forward()

doubly_linked_list_obj.insert_at_k(1, node5)
doubly_linked_list_obj.print_forward()
