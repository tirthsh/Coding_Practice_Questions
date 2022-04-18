# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromFront(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
            
        if n == 0:
            return head.next
        
        prev = head
        curr = head.next
        index = 1
        
        
        while curr != None:
            if index == n:
                prev.next = curr.next
                return head
            
            index += 1
            prev = curr
            curr = curr.next
        
        
        
            
        