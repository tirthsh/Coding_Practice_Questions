class MinHeap:

    def __init__(self):
        self.heap = []
    
    def get_parent_index(self, index):
        return index // 2
    
    def get_left_child_index(self, index):
        return (2 * index) + 1

    def get_right_child_index(self, index):
        return (2 * index) + 2
    
    def has_parent(self, index):
        return self.get_parent_index(index) >= 0
    
    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)
    
    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def insert_item(self, value):
        self.heap.append(value)
        self.heapify(len(self.heap) - 1)
    
    def delete_item(self, index):
        self.swap(index, len(self.heap) - 1)
        self.heap.pop()
        self.heapify(index)
    
    def heapify(self, index):
        while (self.has_parent(index) and self.heap[index] < self.heap[self.get_parent_index(index)]):
            self.swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)
    
    def print_min_heap(self):
        print(self.heap)

min_heap = MinHeap()
arr = [45, 99, 63, 27, 29, 57, 42, 35, 12, 24]

for elem in arr:
    min_heap.insert_item(elem)

min_heap.print_min_heap()

min_heap.delete_item(9)
min_heap.print_min_heap()
