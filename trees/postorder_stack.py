#post order -> left, right, root

#https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        if root == None:
            return []
        
        stack = []
        output = []
        
        #add root to stack
        stack.append(root)


        while len(stack) != 0:
            #insert parent at the end of the output list
            elem = stack.pop()
            output.insert(0, elem.val)
            
            #keep adding all kids in the stack
            for child in elem.children:
                stack.append(child)
        
        return output
            
                
node2 = Node(2)   
node5 = Node(5)                
node6 = Node(6)       
node3 = Node(3, [node5, node6])                
node4 = Node(4) 
node1 = Node(1, [node3, node2, node4])

solution = Solution()
print(solution.postorder(node1))

               


        
        