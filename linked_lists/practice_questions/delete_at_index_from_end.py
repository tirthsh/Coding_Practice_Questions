# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
        
        index_to_remove = length - n
        
        if index_to_remove == 0:
            return head.next

        prev = head
        curr = head.next
        index = 1
        
        while curr != None:
            if index == index_to_remove:
                prev.next = curr.next
                return head
            
            index += 1
            prev = curr
            curr = curr.next