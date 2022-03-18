#Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal_iterative(self, root):
        if root == None:
            return None
        
        stack = []
        output = []
        
        curr = root
        
        while (curr != None or len(stack) != 0):
            #add all left nodes to stack
            while (curr != None):
                stack.append(curr)
                curr = curr.left
            
            #add the left most stack
            curr = stack.pop()
            output.append(curr.val)
            
            #
            curr = curr.right
        
        return output
    
    def inorderTraversal_recursive(self, root):
        output = []
        stack = []

        self.helper(root, output)
        return output

    def helper(self,elem, output):
        if elem != None:
            if (elem.left != None):
                self.helper(elem.left, output)
            
            output.append(elem.val)

            if (elem.right != None):
                self.helper(elem.right, output)
    

            
                
node5 = Node(5)                
node6 = Node(6)       
node3 = Node(3, node5, node6)                
node4 = Node(4) 
node1 = Node(1, node3, node4)

solution = Solution()
print(solution.inorderTraversal_iterative(node1))

print(solution.inorderTraversal_recursive(node1))
               


        
        