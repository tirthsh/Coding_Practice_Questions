#when finidng largest elemenet, have min heap 

'''
Input -> list of numbers
Output -> int, kth largeset number
Assumptions -> list can be unsorted, can have negative numbers, length of list is at least k
Edge cases -> empty list, one element
Examples ->
    n = [9,2,3,7,-1], k = 2, output = 7
    n = [1], k = 1, output = 1
    n = [1,2,3,4,5], output = 4
Algo -> 
    Approach 1)
        - sort the list in ascending order (nlogn)
        - return kth-1 element O(1)
    Approach 2)
        - insert element in min heap O(log(n-k))
        - heap length of max k
        - if new element to insert is smaller than smallest element (use peek()), dont add, else switch with smallest element
        - return the smallest element
Complexity ->
'''

class MinHeap:
    def __init__(self, k):
        self.min_heap = []
        #your length of heap should only be of length k, i.e. if you need to find 2nd largest, you only need to store largst and 2nd largest in min heap
        self.MAX_LENGTH = k 
        #keep track of how many elements have been added - can also be done by just len(min_heap)
        self.count = 0
    
    #insert element to heap
    def insert(self, num):
        #if number of element so far is less length the max length (k), insert
        if self.count < self.MAX_LENGTH:
            #insert element to the end
            self.min_heap.append(num)
            self.count += 1
            #make sure properties of heap is maintained after insertion
            self.heapify(self.count - 1)
        else:
            #if max numbers are added (i.e. k), 
            #check if number you want to add is bigger than the smallest number in the heap (ie. at the top)
            #if it is, make number to add at the top of the heap
            if num > self.peek():
                self.min_heap[0] = num
                #make sure properties of heap is maintained after insertion
                self.heapify(self.count - 1)

    def peek(self):
        return self.min_heap[0]

    def get_parents_index(self, child_index):
        return child_index // 2
    
    def has_parent(self, child_index):
        return self.get_parents_index(child_index) >= 0
    
    #swapping is as simple as switching the two values
    def swap(self, index1, index2):
        self.min_heap[index1], self.min_heap[index2] = self.min_heap[index2], self.min_heap[index1]
    
    #switch value at index with value at parent, if index has parent AND value at index is less than value at parent (bc min heap)
    def heapify(self, index):
        parent_index = self.get_parents_index(index)

        while (self.has_parent(index) and self.min_heap[index] < self.min_heap[parent_index]):
            self.swap(child_index, parent_index)
            #switch index
            index = parent_index
    
    def print_heap(self):
        print(self.min_heap)

my_list = [3,2,3,1,2,4,5,5,6] #1,2,2,3,3,4,5,5,6
k = 4
heap = MinHeap(k)

for each_elem in my_list:
    heap.insert(each_elem)
    heap.print_heap()


#heap.print_heap()
kth_largest = heap.peek()

print(kth_largest)