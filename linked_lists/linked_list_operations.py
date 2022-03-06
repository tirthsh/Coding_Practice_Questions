class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node_to_end(self, node_obj):
        tmp = self.head

        if tmp == None:
            self.head = node_obj
            return

        while tmp.next != None:
            tmp = tmp.next
        tmp.next = node_obj
    
    def add_node_to_front(self, node_obj):
        if self.head == None:
            self.head = node_obj
            return
        
        tmp_obj = self.head
        self.head = node_obj
        self.head.next = tmp_obj
    
    def add_node_at_index(self, node_obj, index):
        tmp = self.head
        if tmp == None and index == 0:
            self.head = node_obj
            return
        
        count = 0
        while tmp != None:
            
    
    def search_value(self, value_to_find):
        tmp = self.head
        while tmp != None:
            if tmp.data == value_to_find:
                return True
            tmp = tmp.next
        
        return False
    
    def delete_node(self, node_obj):
        pass
        

linked_list_obj = LinkedList()
node1 = Node(1)
node2 = Node(2)

linked_list_obj.add_node_to_end(node1)
linked_list_obj.add_node_to_end(node2)

find_val = linked_list_obj.search_value(2)
print(find_val)
find_val = linked_list_obj.search_value(3)
print(find_val)