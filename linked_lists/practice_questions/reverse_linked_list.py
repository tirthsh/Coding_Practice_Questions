'''
When doing this problem, don't think about actually reversing the LL.
Think about changing direction of each node pointing to its prev.

For example:

1 -> 2 -> 3 -> None

1 <- 2 <- 3 => switching direction of pointers is techincally reversing
'''
def reverseLinkedList(self, node):
    if node is None:
        return None

    prev = None
    curr = node

    while node:
        #store next node for next iteration
        next_node = curr.next

        #next node of current node is prev
        curr.next = prev

        #move on
        prev = curr
        curr = next_node
    
    #return prev -> it'll point to last node
    return prev