'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = None
        self.tail = None
    
    def get(self, key):
        if key in cache:
            get_node = cache[key]
            get_val = get_node.value
            
            #make new tail
            if self.tail == get_node:
                self.tail = get_node.prev

            #update order
            get_node.prev.next = get_node.next
            get_node.next.prev = get_node.prev

            old_head = self.head
            get_node.next = old_head
            get_node.prev = None
            old_head.prev = get_node

            #make this node the new head (since it was the most recently used)
            self.head = get_node

            return get_val
        else:
            return -1
        
    def put(self, key, value):
        if key not in cache:
            new_node = Node(value)

            if self.count < self.capacity:
                old_head = self.head
                old_head.prev = new_node

                new_node.next = old_head

                #size of cache increased by 1
                self.count += 1
            else:
                #remove last node in LL
                self.tail.prev.next = None

                old_head = self.head
                old_head.prev = new_node

                new_node.next = old_head

            #new head 
            self.head = new_node
            #update cache
            cache[key] = new_node

        else:
            existing_node = cache[key]
            existing_node.value = value

            #move updated node to front
            existing_node.prev.next = existing_node.next
            existing_node.next.prev = existing_node.prev

            old_head = self.head
            old_head.prev = existing_node

            existing_node.next = old_head
            existing_node.prev = None
            self.head = existing_node

            #update hashtable
            cache[key] = existing_node







