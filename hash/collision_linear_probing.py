import logging as logger

class HashTable:
    #constructor
    def __init__(self):
        self.MAX = 3 #size of list
        self.list = [None for i in range(self.MAX)] #create empty list of size self.MAX
    
    #write hash function
    #hash function which adds ascii value of all characters and returns mod of size of that
    def hash_function(self, value):
        total_ascii_value = 0
        for each_char in value:
            total_ascii_value += ord(each_char)

        return total_ascii_value % self.MAX
        
    #add value given a key
    #use linear probing if collision found
    def add(self, key, value):
        index = self.hash_function(key)

        #collision - linear probing 
        if self.list[index] != None:
            count = 1
            #find the next empty slot and add it there
            while (index + count) % self.MAX != index:
                if self.list[(index + count) % self.MAX] == None:
                    self.list[(index + count) % self.MAX] = value
                    return
                count += 1
            #if you come back to where you started, means you've maxed out -> hash table is full
            logger.error("Hash table is full, cannot add anymore ...")
            return
        else:
            #no collision - happy case
            self.list[index] = value

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

hash_table_obj.add('march 6', 130)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add('march 6', 111)
print(hash_table_obj.list)

#will add it to next available index
hash_table_obj.add('march 6', 222)
print(hash_table_obj.list)

#hash table is full since size is 3
hash_table_obj.add('march 6', 222)
print(hash_table_obj.list)



