import logging as logger
import math
from random import random

class HashTable:
    #constructor
    def __init__(self):
        self.MAX = 5 #size of list
        self.list = [None for i in range(self.MAX)] #create empty list of size self.MAX
        self.element_count = 0
    
    #write hash function
    #hash function which adds ascii value of all characters and returns mod of size of that
    def hash_function(self, value):
        total_ascii_value = 0
        for each_char in value:
            total_ascii_value += ord(each_char)

        return total_ascii_value % self.MAX
    
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
    
    #function deletes value at a given key
    def delete(self, key):
        index = self.hash_function(key)
        self.list[index] = None


#create hash table obj
hash_table_obj = HashTable()

hash_table_obj.add('march 6', 000)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add('march 6', 111)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add('march 6', 222)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add('march 6', 333)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add('march 6', 444)
print(hash_table_obj.list)

