# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        
        currentA = headA
        currentB = headB
        
        some_set = set()
        
        while currentA:
            #add the node, not the value
            some_set.add(currentA)
            currentA = currentA.next
        
        while currentB:
            #check if that node exists in the set
            #ie. value and next node all are the same
            if currentB in some_set:
                print(currentB.val)
                return currentB
            currentB = currentB.next
        
        return None

node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node6 = ListNode(5)
node7 = ListNode(6)

node6.next = node7
node7.next = node2

solution = Solution()
print(solution.getIntersectionNode(node1, node6))