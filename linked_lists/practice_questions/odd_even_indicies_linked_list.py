class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def oddEvenList(self, head):
        if head == None:
            return None
        
        #if there is only 1 or 2 nodes, then we just return head
        if head.next == None or head.next.next == None:
            return head

        odd_tmp = head
        even_tmp = head.next

        odd_head = head
        even_head = head.next

        while odd_tmp.next != None and even_tmp.next != None:
            odd_tmp.next = even_tmp.next
            even_tmp.next = odd_tmp.next.next

            odd_tmp = odd_tmp.next
            even_tmp = even_tmp.next
        
        odd_tmp.next = even_head
        return odd_head