import logging as logger

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
        length_of_ll = self.helper_length_of_linked_list()

        if index > self.helper_length_of_linked_list():
            logger.error("Cannot add at index " + str(index) + " as length of linked list is " + str(length_of_ll))

        #inserting at the front and LL is empty
        if tmp == None and index == 0:
            self.head = node_obj
            return
        
        #inserting at the front but LL is not empty
        if tmp != None and index == 0:
            self.head = node_obj
            self.head.next = tmp
            return
        
        #keep track of previous and current, starting at index 1
        prev_node = tmp
        curr_node = prev_node.next

        curr_index = 1
        while curr_node != None:
            if curr_index == index:
                prev_node.next = node_obj
                node_obj.next = curr_node
                return
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
        
        #insert at the end
        if curr_index == index:
            prev_node.next = node_obj

        return

        
    def search_value(self, value_to_find):
        tmp = self.head
        while tmp != None:
            if tmp.data == value_to_find:
                return True
            tmp = tmp.next
        
        return False
    
    def delete_first_node(self):
        tmp = self.head

        if tmp == None or tmp.next == None:
            self.head = None
            return
        
        self.head = tmp.next
    
    def delete_last_node(self):
        tmp = self.head 

        if tmp == None or tmp.next == None:
            self.head = None
            return
        
        while tmp.next != None:
            prev = tmp
            tmp = tmp.next
        
        prev.next = None

    def delete_node_at_index(self, index):
        tmp = self.head
        length_of_ll = self.helper_length_of_linked_list()
        if index > length_of_ll - 1:
            logger.error("Cannot delete at index " + str(index) + " as length of linked list is " + str(length_of_ll))
            return
        
        if index == 0:
            self.head = tmp.next
            return

        curr_index = 1
        prev_node = tmp
        curr_node = tmp.next

        while curr_node != None:
            if curr_index == index:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
            
    def helper_length_of_linked_list(self):
        length = 0
        tmp = self.head

        while tmp != None:
            length += 1
            tmp = tmp.next
        
        return length

    def print_linked_list(self):
        tmp = self.head
        while tmp != None:
            print(str(tmp.data) + " -> ", end = "")
            tmp = tmp.next
        print("None")
        print()
        
linked_list_obj = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node6 = Node(0)
node7 = Node(6)

print("Adding a few nodes to the end...")
linked_list_obj.add_node_to_end(node1)
linked_list_obj.add_node_to_end(node2)
linked_list_obj.add_node_to_end(node3)
linked_list_obj.add_node_to_end(node4)
linked_list_obj.add_node_to_end(node5)

linked_list_obj.print_linked_list()

print("Adding a node to the front ...")
linked_list_obj.add_node_to_front(node6)
linked_list_obj.print_linked_list()

print("Adding node at index 6 ...")
linked_list_obj.add_node_at_index(node7, 6)
linked_list_obj.print_linked_list()

print("Deleting the first node ...")
linked_list_obj.delete_first_node()
linked_list_obj.print_linked_list()

print("Deleting the last node ... ")
linked_list_obj.delete_last_node()
linked_list_obj.print_linked_list()

print("Deleting at index 1 ... ")
linked_list_obj.delete_node_at_index(1)
linked_list_obj.print_linked_list()

print("Checking if value 1 exists ... ", end = "")
find_val = linked_list_obj.search_value(1)
print(find_val)
print()

print("Checking if value 10 exists ... ", end = "")
find_val = linked_list_obj.search_value(2)
print(find_val)
print()

print("Length of linked list is ... ")
curr_length = linked_list_obj.helper_length_of_linked_list()
print(curr_length)