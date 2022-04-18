# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head):
        if head == None:
            return None
        
        arr = []
        tmp = head
        
        #all numbers to an array
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        
        total = 0
        start = 0
        end = 0
        
        
        while start <= len(arr)-1:
            total += arr[end]
            
            #if total is 0, remove the subarray arr[start:end+1]
            if total == 0:
                arr = arr[:start] + arr[end+1:]
                
                #start again in case there are in any other subarrays which total=0
                start = 0
                end = 0
                total = 0
            else:
                #if total is not 0, increment end pointer
                end += 1
            
            #boundry check
            #if end is reached, start again, but this time with start += 1
            if end > len(arr)-1:
                start += 1
                end = start
                total = 0
        
        #convert list to LL from arr
        if len(arr) != 0:
            #store the head so you return it
            head = Node(arr[0])
            tmp = head

            #go through all nodes and make LL
            #start at 1
            for i in range(1,len(arr)):
                new_node = Node(arr[i])
                tmp.next = new_node
                tmp = new_node
            
            return head
        else:
            return None

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)

solution = Solution()
node = solution.removeZeroSumSublists(node)

while node:
  print(node.val)
  node = node.next