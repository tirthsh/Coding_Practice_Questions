class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, new_node):
        tmp = self.head

        if tmp == None:
            self.head = new_node
            return
        
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = new_node
    
    #reverse LL
    def reverse_linked_list(self):
        '''
        Input -> single linked list
        Output -> reversed linked list
        Assumptions -> data type is of LL, and fullfill all of LL properties 
        Edge Cases -> empty LL
        Examples -> 
            LL = [1], RLL = [1]
            LL = None, RLL = None
            LL = [1] -> [2] -> [3], RLL = [3] -> [2] -> [1]
        Algo ->
        Complexity ->
        '''
        tmp = self.head

        if tmp == None or tmp.next == None:
            return tmp
        
        prev = None
        while tmp != None:
            #save next node so it can be tmp node after this iteration
            next_node = tmp.next
            # [1] -> [2] ---- [1] <- [2]
            #flip pointer
            tmp.next = prev
            #update previous node
            prev = tmp
            tmp = next_node

        self.head = prev
    
    def print_linked_list(self):
        tmp = self.head

        while tmp != None:
            print(str(tmp.data) + " -> ", end = "")
            tmp = tmp.next
        
        print("None")
        print()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

linked_list = LinkedList()
linked_list.add(node1)
linked_list.add(node2)
linked_list.add(node3)

linked_list.print_linked_list()

#reverse
linked_list.reverse_linked_list()

linked_list.print_linked_list()
