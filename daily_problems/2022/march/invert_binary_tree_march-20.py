class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    
class Solution:

    def invert_binary_tree(self, root):

        if root == None:
            return root
        
        left = self.invert_binary_tree(root.left)
        right = self.invert_binary_tree(root.right)

        root.left = right
        root.right = left

        return root