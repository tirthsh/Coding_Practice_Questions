import logging as logger
import json

#create node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#create linked list class    
class LinkedList:
    def __init__(self):
        self.head = None
    
    #give a key, and value, add to linked list
    def add(self, key, value):
        data = {key: value}
        new_node = Node(data)
        #if linked list is empty, means its the first element, make it head
        if self.head == None:
            self.head = new_node
            return
        
        #if linked list is not empty, iterate till end, and append it to add
        last_val = self.head
        while last_val.next != None:
            last_val = last_val.next
        
        #make last node new node
        last_val.next = new_node
        return
    
    #helper for print
    def helper_retrieve_data(self):
        temp = self.head
        data = []

        while temp:
            data.append(temp.data)
            temp = temp.next

        return data
    
    #give a value, find it exists in a linked list or not
    def find(self, value_to_find):
        tmp = self.head
        #iterate till end of linked list
        while tmp != None:
            #find data of the current node
            data = tmp.data
            curr_val = list(data.values())[0]
            #if values match, you've found your match
            if curr_val == value_to_find:
                return True
            #go to next node if you didn't find it
            tmp = tmp.next
        
        #value not in the linked list as we've gone through all nodes in the LL
        return False
    
    #delete value in the linked list
    def delete(self, value_to_delete):
        #previous node - will be needed to change linkage
        prev = Node()
        curr = self.head

        #iterate through all nodes in the LL
        while curr != None:
            data = curr.data
            curr_value = list(data.values())[0]
            #check if current node's value is what we want to delete
            if curr_value == value_to_delete:
                #if our value to delete is the head, make the next node the new head
                if curr == self.head:
                    self.head = curr.next
                #re-assemble linkage - previous node should point to next node (i.e. dropping any linkage to current node)
                else:
                    prev.next = curr.next
                return
            #make previous node current node, and current node to next node
            prev = curr
            curr = curr.next

        #value to delete did not exist in our LL
        return

#create hash table class
class HashTable:
    #constructor
    def __init__(self):
        self.MAX = 3 #size of list
        self.list = [[] for i in range(self.MAX)] #create empty list of size self.MAX
    
    #write hash function
    #h(x) = x % len(table) - can be any hash function
    # the "better" the hash function, the less the collisions = better complexity for adding, searching, deleting
    def hash_function(self, value):
        return value % self.MAX
        
    #add value given a key
    #create linked list
    def add(self, key, value):
        index = self.hash_function(key)

        if len(self.get_list(index)) == 0:
            #list at that index is empty, create a linked list and insert {key:value} as a Node in the list at the index 'index'
            new_linked_list = LinkedList()
            new_linked_list.add(key, value)
            self.list[index].append(new_linked_list)
        else:
            current_linked_list = self.list[index][0]
            current_linked_list.add(key, value)
            self.list[index] = [current_linked_list]
    
    def print_hash_table(self):
        for each_list in self.list:
            if len(each_list) == 0:
                print([], end="")
            else:
                linked_list = each_list[0]
                data = linked_list.helper_retrieve_data()
                print(data, end="")
        print()

    #function finds value given a key
    def get_list(self, key):
        return self.list[key]
    
    def is_present(self, find_value):
        for each_list in self.list:
            linked_list = each_list[0]
            if linked_list.find(find_value):
                return True
        return False
    
    #function deletes value at a given key
    def delete(self, value_to_delete):
        for each_list in self.list:
            linked_list = each_list[0]
            linked_list.delete(value_to_delete)


#create hash table obj
hash_table_obj = HashTable()

hash_table_obj.add(0, 000)

hash_table_obj.add(1, 111)
hash_table_obj.add(1, 222)
hash_table_obj.add(1, 333)

hash_table_obj.add(2, 444)

hash_table_obj.print_hash_table()

print(hash_table_obj.is_present(444))

hash_table_obj.delete(333)
hash_table_obj.print_hash_table()

