#implement a hash data structure 
#assume hash function is h(x) = x % size(hash_table)

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def put(self, key, value):
        data = {key: value}
        new_node = Node(data)

        if self.head == None:
            new_node = self.head
            return
        
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = new_node
    
    def get(self, key):
        tmp = self.head

        if tmp == None:
            return 
        
        while tmp != None:
            curr_data = tmp.data
            if key == list(curr_data.keys())[0]:
                return curr_data[key]
        
        return

class HashTable:
    def __init__(self):
        self.MAX = 3
        self.hash_list = [ [] for i in range(0, self.MAX) ]
    
    def hash_function(self, key):
        return key % self.MAX
    
    def add(self, key, value):
        index = self.hash_function(key)
        
        if len(hash_list[index]) == 0:
            linked_list = LinkedList()
        else:
            linked_list = hash_list[index]
        
        linked_list.put(index, value)
        self.hash_list[index] = linked_list
    
    def get(self, key):
        index = self.hash_function(key)

        if len(hash_list[index]) == 0:
            return
        else:
            linked_list = hash_list[index]
            return linked_list.get(key)