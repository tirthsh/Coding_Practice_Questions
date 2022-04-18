# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        #get inorder of all the nodes
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node)
                inorder(node.right)
        
        inorder(root)
        
        #sort the inoder array into bst order
        def bst(start, end):
            if start < end:
                #calculate mid
                mid = start+(end-start)//2
                
                root = res[mid]
                #recurse
                root.left = bst(start, mid-1)
                #recurse
                root.right = bst(mid+1, end)
            elif start == end: #leaf node
                mid = start+(end-start)//2
                root = res[mid]
                
                #leaf has no left and right
                root.left = None
                root.right = None
            else:
                return None
        
            return root
        
        return bst(0, len(res)-1)