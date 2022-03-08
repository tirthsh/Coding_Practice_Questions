class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node_obj):
        tmp = self.head 

        if tmp == None:
            self.head = node_obj
            return
        
        while tmp.next != None:
            tmp = tmp.next

        tmp.next = node_obj
    
    '''
    None -> 3 -> 2 -> 1 -> None
    

    '''
    def sort_linked_list(self):
        pass

    def print_linked_list(self):
        tmp = self.head

        while tmp != None:
            print(str(tmp.data) + " -> ", end = "")
            tmp = tmp.next
        print("None")
        print()
    
linked_list_obj = LinkedList()
node1 = Node(3)
node2 = Node(2)

linked_list_obj.add_node(node1)
linked_list_obj.print_linked_list()

linked_list_obj.add_node(node2)
linked_list_obj.print_linked_list()

linked_list_obj.sort_linked_list()
linked_list_obj.print_linked_list()
