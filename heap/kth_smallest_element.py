#when finidng smallest elemenet, have max heap 

'''
Input -> list of numbers
Output -> int, kth smallest number
Assumptions -> list can be unsorted, can have negative numbers, length of list is at least k
Edge cases -> empty list, one element
Examples ->
    n = [9,2,3,7,-1], k = 2, output = 2
    n = [1], k = 1, output = 1
    n = [1,2,3,4,5], k=4 output = 2
Algo -> 
    Approach 1)
        - sort the list in descending order (nlogn)
        - return kth-1 element O(1)
    Approach 2)
        - insert element in max heap O(log(n-k)
        - heap length of max k
        - if new element to insert is bigger than largest element (use peek()), dont add, else switch with largest element
        - return the largest element (first element)
Complexity ->
'''

class MaxHeap:
    def __init__(self, k):
        self.max_heap = []
        #your length of heap should only be of length k, i.e. if you need to find 2nd smallest, you only need to store smallest and 2nd smallest in min heap
        self.MAX_LENGTH = k
        #keep track of how many elements have been added - can also be done by just len(min_heap)
        self.count = 0

    #insert element to heap
    def insert(self, num):
        #if number of element so far is less than length the max length (k), insert
        if self.count < self.MAX_LENGTH:
            #insert element to the end
            self.max_heap.append(num)
            self.count += 1
            #make sure properties of heap is maintained after insertion
            self.heapify(self.count - 1)
        else:
            #if max numbers are added (i.e. k), 
            #check if number you want to add is smaller than the largest number in the heap (ie. at the top)
            #if it is, make number to add at the top of the heap
            if num < self.peek():
                self.max_heap[0] = num
                #make sure properties of heap is maintained after insertion
                self.heapify(self.count - 1)

    
    def peek(self):
        return self.max_heap[0]
    
    def get_parent_index(self, index):
        return index // 2
    
    def has_parent(self, child_index):
        return self.get_parent_index(child_index) >= 0

    #swapping is as simple as switching the two values
    def swap(self, index1, index2):
        self.max_heap[index1], self.max_heap[index2] = self.max_heap[index2], self.max_heap[index1]

    #switch value at index with value at parent, if index has parent AND value at index is greater than value at parent (bc max heap)
    def heapify(self, index):
        parent_index = self.get_parent_index(index)

        while (self.has_parent(index) and self.max_heap[index] > self.max_heap[parent_index]):
            self.swap(index, parent_index)
            #switch index
            index = parent_index
    
    def print_heap(self):
        print(self.max_heap)

n = [9,2,3,7,-1]
k = 2

heap = MaxHeap(k)

for each_elem in n:
    heap.insert(each_elem)

heap.print_heap()

kth_smallest_element = heap.peek()
print(kth_smallest_element)
