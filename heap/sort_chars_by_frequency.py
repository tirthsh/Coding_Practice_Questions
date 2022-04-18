class Solution:
    def frequencySort(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""
        
        mapping = {}
        sorted_str = ""
        max_heap = []
        
        for each_char in s:
            if each_char not in mapping:
                mapping[each_char] = 1
            else:
                mapping[each_char] += 1
            
        print(mapping)
        
        max_heap = MaxHeap()
        values = []
        for char,freq in mapping.items():
            values = max_heap.insert({char:freq})
        print(values)
        

        # for each_pair in values:
        #     for char, freq in each_pair.items():
        #         print(char, freq)
        #         sorted_str += char*freq
        
        return sorted_str
    
    def frequencySort2(self, s):
        mapping = {}
        
        for each_char in s:
            if each_char not in mapping:
                mapping[each_char] = 1
            else:
                mapping[each_char] += 1
                
        temp = sorted(mapping.items(), key = lambda elem: elem[1], reverse=True)
        print(temp)
        s = ''
        for elem in temp:
            s += elem[0] * elem[1]
        
        return s
        

class MaxHeap:
    def __init__(self):
        self.max_heap = []
    
    def insert(self, dictionary):
        self.max_heap.append(dictionary)
        print(self.max_heap)
        self.heapify(len(self.max_heap) - 1)
        return self.max_heap
    
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
        
        child_val = list(self.max_heap[child_index].values())[0]
        parent_val = list(self.max_heap[parent_index].values())[0]
        print(child_val)
        print(parent_val)

        while (self.has_parent(child_index) and child_val > parent_val):
            self.swap(child_index, parent_index)
            child_index = parent_index

solution = Solution()
s = "tree" 

print(solution.frequencySort(s))