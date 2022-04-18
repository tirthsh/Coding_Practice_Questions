# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1 -> 2 -> 2 -> 1

'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
    
        slowPointer = head
        fastPointer = head
        
        while (fastPointer != None and fastPointer.next != None):
            slowPointer = slowPointer.next #this will go to half
            fastPointer = fastPointer.next.next #this will go to end
        
        #reverse the 2nd half of the LL
        slowPointer = self.reverseLL(slowPointer)
        #go back to start
        fastPointer = head

        '''
        After reversing
        1 -> 2 -> 1 -> 2
       fp         sp
        '''
        
        while (slowPointer != None):
            if (slowPointer.val != fastPointer.val):
                return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        
        return True
    
    def reverseLL(self, head):
        prev = None
        while (head != None):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev