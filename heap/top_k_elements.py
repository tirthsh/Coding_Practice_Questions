'''
Create max heap to keep track of max k elements
'''

class Max_Heap:
    def __init__(self, k):
        self.max_heap = []
        self.size = 0
        self.MAX_LENGTH = k 

    def insert(self, elem):
        key = elem[0]
        freq = elem[1]
        if self.size < self.MAX_LENGTH:
            self.max_heap.append(elem)
            self.size += 1
            self.heapify(self.size - 1)
        else:
            if freq > self.peek()[1]:
                self.max_heap[0] = elem
                self.heapify(self.size - 1)
    
    def peek(self):
        return self.max_heap[0]
    
    def get_parent(self, child_index):
        return child_index // 2
    
    def has_parent(self, child_index):
        return self.get_parent(child_index) >= 0
    
    def swap(self, index1, index2):
        self.max_heap[index1], self.max_heap[index2] = self.max_heap[index2], self.max_heap[index1]
    
    def heapify(self, child_index):
        parent_index = self.get_parent(child_index)
        
        child_freq = self.max_heap[child_index][1]
        parent_freq = self.max_heap[parent_index][1]

        while (self.has_parent(child_index) and  child_freq > parent_freq):
            self.swap(child_index, parent_index)
            child_index = parent_index
    
    def print_max_heap(self):
        print(self.max_heap)
    
    #used to get only keys of each (key, frequency) pair
    def get_result(self):
        res = []

        for each_elem in self.max_heap:
            res.append(each_elem[0])
        
        return res
        

class Solution:
    def topKFrequent(self, nums, k):
        if not nums or k == 0:
            return []
        
        #create a mapping of each character to its frequency
        mapping = {}
        
        for each_num in nums:
            if each_num in mapping:
                mapping[each_num] += 1
            else:
                mapping[each_num] = 1
        
        max_heap = Max_Heap(k)
        for key,freq in mapping.items():
            max_heap.insert((key,freq))
        
        return max_heap.get_result()
        
        
        
            
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k))
        
nums = [1]
k = 1
print(solution.topKFrequent(nums, k))