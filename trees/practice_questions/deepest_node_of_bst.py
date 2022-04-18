class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    
class Solution:
    def deepest_node(self, root):
        if root == None:
            return None
        
        queue = []
        queue.append(root)

        while queue:
            curr = queue.pop(0)

            #if there's a left, add left node
            if curr.left:
                queue.append(curr.left)
            
            #if there's a right, add right node
            if curr.right:
                queue.append(curr.right)

        #this has be the deepest node since it was the last one from queue
        return curr.val

node1 = Node(60)
node2 = Node(50, None, node1)
node3 = Node(40, None, node2)

node4 = Node(20)
node5 = Node(10, None, node4)

node6 = Node(30, node5, node3)

solution = Solution()
print(solution.deepest_node(node6))