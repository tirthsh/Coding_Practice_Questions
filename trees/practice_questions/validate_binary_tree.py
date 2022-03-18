# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        return self.validate(root, None, None)
    
    def validate(self, root, maxVal, minVal):
        if root == None:
            return True
        
        elif (maxVal != None and root.val >= maxVal) or (minVal != None and root.val <= minVal):
            return False
        
        else:
            #for left tree -> we don't care what the lowest val it can be, but we know it cannot be equal or greater than max value
            
            #for right tree -> we don't care what the maxmium val it can be, but we know it cannot be equal or less than the min value
            return self.validate(root.left, root.val, minVal) and self.validate(root.right, maxVal, root.val)

        
node3 = TreeNode(3)
node1 = TreeNode(1)
node2 = TreeNode(2, node1, node3)

solution = Solution()
print(solution.isValidBST(node1))

node3 = TreeNode(3)
node6 = TreeNode(6)
node4 = TreeNode(4, node3, node6)
node1 = TreeNode(1)
node5 = TreeNode(5, node1, node4)

print(solution.isValidBST(node5))
