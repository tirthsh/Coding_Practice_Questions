#https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root):
        if root == None:
            return None

        if root.left != None:
            root.left = self.pruneTree(root.left)
        
        if root.right != None:
            root.right = self.pruneTree(root.right)
        
        if root.val == 0 and (root.left == None and root.right == None):
            return None
        
        return root
    
    def print_tree(self, root):
        output = []
        stack = []

        if root == None:
            return output
        
        stack.append(root)

        while stack:
            curr = stack.pop()
            output.append(curr.val)

            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)

        return output
    
node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(0)
node4 = TreeNode(0)

node5 = TreeNode(0, node2, node3)
node6 = TreeNode(1, node4, node1)

node7 = TreeNode(1, node5, node6)

solution = Solution()
print(solution.print_tree(solution.pruneTree(node7)))
