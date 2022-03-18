# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
        if root == None:
            return []
        
        stack = []
        output = []
        
        stack.append(root)
        
        while stack:
            elem = stack.pop()
            output.append(elem.val)
            
            #add all children backwards so the left most always gets popped first
            for child in elem.children[::-1]:
                stack.append(child)
        
        return output

node2 = Node(2)   
node5 = Node(5)                
node6 = Node(6)       
node3 = Node(3, [node5, node6])                
node4 = Node(4) 
node1 = Node(1, [node3, node2, node4])

solution = Solution()
print(solution.preorder(node1))