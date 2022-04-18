class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def removeNthFromEnd(self, head, k):
        if head == None:
            return None
        
        #get length of LL
        tmp = head
        length = 0

        while tmp:
            length += 1
            tmp = tmp.next
        
        #get index to remove from front
        index_to_remove = length - k

        prev = None
        tmp = head
        index = 0

        while tmp:
            if index == index_to_remove:
                #k = 0
                if prev == None:
                    return tmp.next
                else:
                    prev.next = tmp.next
                    return head
            
            prev = tmp
            tmp = tmp.next
        
        return 
            
        



    


    
