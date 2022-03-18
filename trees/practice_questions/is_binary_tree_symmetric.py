# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    
    def isMirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        
        if node1 == None or node2 == None:
            return False
        
        if node1.val == node2.val:
            return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

node4 = TreeNode(4)
node3 = TreeNode(3)
node2_1 = TreeNode(2, node3, node4)
node2_2 = TreeNode(2, node4, node3)
node1 = TreeNode(1,node2_1,node2_2)

solution = Solution()
print(solution.isSymmetric(node1))