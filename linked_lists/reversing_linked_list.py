class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, new_node):
        tmp = self.head

        if tmp == None:
            self.head = new_node
            return
        
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = new_node

    '''
    None -> 1 -> 2 -> 3 -> None
    None <- 1 -> 2 -> 3 -> None
    None <- 1 <- 2 -> 3 -> None
    None <- 1 <- 2 <- 3 -> None
    None <- 1 <- 2 <- 3 <- None

    '''
    
    #NOTE: you're NOT changing the data, you're changing the pointers!!
    #point pointers opposite way
    def reversing_linked_list(self):
        curr = self.head

        #if LL is empty or only containers 1 node, nothing to reverse
        if curr == None or curr.next == None:
            return
        
        prev = None
        #change link to going backwards 
        while curr != None:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev
    
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

linked_list_obj.add_node(node1)
linked_list_obj.add_node(node2)
linked_list_obj.add_node(node3)

linked_list_obj.print_linked_list()

linked_list_obj.reversing_linked_list()
linked_list_obj.print_linked_list()
