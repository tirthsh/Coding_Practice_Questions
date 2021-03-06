import logging as logger
import math
from random import random

class HashTable:
    #constructor
    def __init__(self):
        self.MAX = 3 #size of list
        self.list = [None for i in range(self.MAX)] #create empty list of size self.MAX
        self.element_count = 0
    
    #write hash function
    #h(x) = x % len(table)
    def hash_function(self, value):
        return value % self.MAX
    
    def is_table_full(self):
        return self.element_count == self.MAX
        
    #add value given a key
    #use quadratic probing if collision found
    def add(self, key, value):
        index = self.hash_function(key)

        #collision - linear probing 
        if self.list[index] != None:
            count = 1
            #find the next empty slot and add it there
            while not self.is_table_full():
                #need to random number in the case index never fills a certain spot, adding a random number will ensure every spot will be taken up 
                random_num = random()
                if self.list[(index + int(math.pow(count, 2) + random_num)) % self.MAX] == None:
                    self.list[(index + int(math.pow(count, 2) + random_num)) % self.MAX] = value
                    self.element_count += 1
                    return
                count += 1
            #if you come back to where you started, means you've maxed out -> hash table is full
            logger.error("Hash table is full, cannot add anymore ...")
            return
        else:
            #no collision - happy case
            self.list[index] = value
            self.element_count += 1

    #function finds value given a key
    def get(self, key):
        index = self.hash_function(key)
        value = self.list[index]
        return value
    
    def is_present(self, find_value):
        value_at_key = self.hash_function(find_value)

        if value_at_key != find_value:
            count = 1
            possible_index = (value_at_key + count) % self.MAX

            while possible_index != value_at_key:
                if self.list[possible_index] == find_value:
                    return True
                count += 1
                possible_index = (value_at_key + count) % self.MAX
            return False
        else:
            return True
    
    #function deletes value at a given key
    def delete(self, key):
        index = self.hash_function(key)
        self.list[index] = None


#create hash table obj
hash_table_obj = HashTable()

hash_table_obj.add(0, 130)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add(0, 111)
print(hash_table_obj.list)

#will add it to next available index since index 1 is taken from above collision
hash_table_obj.add(1, 222)
print(hash_table_obj.list)

#hash table is full since size is 3
hash_table_obj.add(2, 333) #ERROR - table is full
print(hash_table_obj.list)

value_found = hash_table_obj.is_present(222)
#found the element
print(value_found)

value_found = hash_table_obj.is_present(333)
#did not find the element
print(value_found)

print(hash_table_obj.get(0))

hash_table_obj.delete(1)
print(hash_table_obj.list)