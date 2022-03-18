# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        #add 1 to signify current level
        return max(left, right) + 1

node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)

solution = Solution()
print(solution.maxDepth(node1))