class HashTable:
    def __init__(self):
        self.MAX = 100 #size of list
        self.list = [None for i in range(self.MAX)] #create empty list of size self.MAX
    
    #write hash function
    def hash_function(self, value):
        total_ascii_value = 0
        for each_char in value:
            total_ascii_value += ord(each_char)
        
        return total_ascii_value % self.MAX
    
    def add(self, key, value):
        index = self.hash_function(key)
        self.list[index] = value
    
    def get(self, key):
        index = self.hash_function(key)
        value = self.list[index]
        return value
    
    def delete(self, key):
        index = self.hash_function(key)
        self.list[index] = None

hash_table_obj = HashTable()
hash_table_obj.add('march 6', 130)
hash_table_obj.add('apr 12', 9)
hash_table_obj.add('dec 13', 222)

print(hash_table_obj.get('march 6'))
hash_table_obj.delete('march 6')
print(hash_table_obj.get('march 6'))

