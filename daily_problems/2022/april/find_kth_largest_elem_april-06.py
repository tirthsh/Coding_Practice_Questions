class MinHeap:
    def __init__(self, k):
        self.min_heap = []
        self.count = 0
        self.max_count = k
    
    def insert(self, val):
        if self.count < self.max_count:
            self.min_heap.append(val)
            self.count += 1
        else:
            if self.peek() > val:
                self.min_heap[0] = val
                
        self.heapify(self.count-1)

    def peek(self):
        return self.min_heap[0]

    def get_parent_index(self, child_index):
        return child_index // 2 
    
    def has_parent(self, child_index):
        return self.get_parent_index(child_index) >= 0
    
    def swap(self, index1, index2):
        self.min_heap[index1], self.min_heap[index2] = self.min_heap[index2], self.min_heap[index1]
    
    def heapify(self, child_index):
        parent_index = self.get_parent_index(child_index)

        while self.has_parent(child_index) and self.min_heap[child_index] > self.min_heap[parent_index]:
            self.swap(child_index, parent_index)
            child_index = parent_index


    def print_heap(self):
        print(self.min_heap)

list_of_nums = [3, 5, 2, 4, 6, 8]
k = 3

min_heap = MinHeap(k)
for each_num in list_of_nums:
    min_heap.insert(each_num)

min_heap.print_heap()
print(min_heap.peek())