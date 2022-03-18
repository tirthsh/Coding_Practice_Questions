# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root == None:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root

node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)

solution = Solution()
print(solution.invertTree(node1))