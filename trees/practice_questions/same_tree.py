# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        #if both are null, we can assume its same 
        if p == None and q == None:
            return True
        #if one of them is null, its a problem
        elif p == None or q == None:
            return False
        #if none are null but their values dont match, its a problem
        elif p.val != q.val:
            return False
        else:
            #both are non-null and their values match, recurse on each left and right tree respectively
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

node2 = TreeNode(2)
node3 = TreeNode(3)
#root t1
node1 = TreeNode(1, node2, node3)

#root t2
node4 = TreeNode(1, node2, node3)

#--------------

node8 = TreeNode(2)
#root t1
node7 = TreeNode(1, node8, None)

#root t2
node9 = TreeNode(1, None, node8)

solution = Solution()
print(solution.isSameTree(node1, node4))
print(solution.isSameTree(node7, node9))
